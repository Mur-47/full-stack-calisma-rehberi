"""Check links, private references and PDF text without publishing private terms."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SUFFIXES = {'.md', '.py', '.mjs', '.js', '.ts', '.json', '.cs', '.csproj', '.yml', '.yaml', '.ps1', '.sh'}
SKIP_DIRS = {'.git', '.venv', 'node_modules', 'obj', 'bin', '__pycache__'}
GENERIC_PATTERNS = [r'[A-Za-z]:[/\\]+Users[/\\]+', r'gh[pousr]_[A-Za-z0-9]{20,}']


def load_private_terms(root=ROOT, environ=None, allow_empty=False):
    env = os.environ if environ is None else environ
    raw = env.get('PUBLICATION_PRIVATE_TERMS')
    if raw is None:
        path = Path(env.get('PUBLICATION_PRIVATE_TERMS_FILE', root / '.publication-private.json')).resolve()
        if path.exists():
            if path.is_relative_to(root.resolve()):
                relative = path.relative_to(root.resolve()).as_posix()
                tracked = subprocess.run(['git', '-C', str(root), 'ls-files', '--error-unmatch', '--', relative], capture_output=True)
                ignored = subprocess.run(['git', '-C', str(root), 'check-ignore', '-q', '--', relative], capture_output=True)
                if tracked.returncode == 0 or ignored.returncode != 0:
                    raise ValueError('Private terms file must be untracked and ignored by Git.')
            raw = path.read_text(encoding='utf-8-sig')
    if raw is None:
        if allow_empty:
            return []
        raise ValueError('Set PUBLICATION_PRIVATE_TERMS, use an ignored .publication-private.json, or explicitly pass --allow-no-private-terms.')
    try:
        terms = json.loads(raw)
    except (ValueError, TypeError):
        raise ValueError('Private terms must be a JSON array of non-empty strings.')
    if not isinstance(terms, list) or not terms or any(not isinstance(term, str) or not term.strip() for term in terms):
        raise ValueError('Private terms must be a JSON array of non-empty strings.')
    return terms


def has_private_reference(text, terms):
    return any(re.search(pattern, text) for pattern in GENERIC_PATTERNS) or any(term.casefold() in text.casefold() for term in terms)


def check_source(root, terms):
    errors = []
    count = 0
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if not path.is_file() or any(p in SKIP_DIRS for p in relative.parts):
            continue
        policy_path = Path(os.environ.get('PUBLICATION_PRIVATE_TERMS_FILE', root / '.publication-private.json')).resolve()
        if path.resolve() == policy_path:
            continue
        if path.suffix not in SOURCE_SUFFIXES and path.name != 'Dockerfile':
            continue
        text = path.read_text(encoding='utf-8-sig')
        count += 1
        if has_private_reference(text, terms):
            errors.append(f'{relative}: private reference (value withheld)')
        if path.suffix == '.md':
            if text.count('```') % 2:
                errors.append(f'{relative}: unclosed code block')
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                target = unquote(target.split('#')[0].split('?')[0])
                if target and not (path.parent / target).exists():
                    errors.append(f'{relative}: missing local link')
    return errors, count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--allow-no-private-terms', action='store_true', help='Run generic checks only; explicitly skip the local private-term policy.')
    args = parser.parse_args()
    try:
        terms = load_private_terms(allow_empty=args.allow_no_private_terms)
    except (ValueError, OSError) as error:
        raise SystemExit(str(error)) from None
    errors, count = check_source(ROOT, terms)
    from pypdf import PdfReader
    reader = PdfReader(ROOT / 'pdf/full-stack-calisma-rehberi.pdf')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    if '\ufffd' in text:
        errors.append('PDF: replacement characters')
    if has_private_reference(text, terms):
        errors.append('PDF: private reference (value withheld)')
    for word in ['Docker', 'JavaScript', 'Node.js', 'ORM', 'EF Core', 'GitHub']:
        if word not in text:
            errors.append(f'PDF: missing {word}')
    if errors:
        raise SystemExit('\n'.join(errors))
    policy = 'local private policy enabled' if terms else 'generic checks only; private terms skipped'
    print(f'PASS: {count} source files, local links, PDF ({len(reader.pages)} pages); {policy}.')


if __name__ == '__main__':
    main()
