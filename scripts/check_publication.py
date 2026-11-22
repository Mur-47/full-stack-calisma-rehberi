"""Check local links, accidental private paths and basic PDF integrity."""
from pathlib import Path
import re
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
errors=[]
for path in [*ROOT.glob('*.md'),*ROOT.glob('book/*.md'),
             *ROOT.glob('examples/**/*.md')]:
    text=path.read_text(encoding='utf-8-sig')
    for pattern in [r'C:[/\\]+Users[/\\]+',r'MONSTER',r'Murat Bey',
                    r'gh[pousr]_[A-Za-z0-9]{20,}']:
        if re.search(pattern,text):
            errors.append(f'{path.relative_to(ROOT)}: private reference')
    if text.count('```')%2:
        errors.append(f'{path.relative_to(ROOT)}: unclosed code block')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
        if target.startswith(('https://','http://','#','mailto:')):
            continue
        target=target.split('#')[0].split('?')[0]
        if target and not (path.parent/target).exists():
            errors.append(f'{path.relative_to(ROOT)}: missing {target}')
pdf=ROOT/'pdf/full-stack-calisma-rehberi.pdf'
reader=PdfReader(pdf)
text='\n'.join(page.extract_text() or '' for page in reader.pages)
if '\ufffd' in text:errors.append('PDF: replacement characters')
if any(x in text for x in ['Murat Bey','MONSTER','KabinOps']):
    errors.append('PDF: personal/product reference')
for word in ['Docker','JavaScript','Node.js','ORM','EF Core','GitHub']:
    if word not in text:errors.append(f'PDF: missing {word}')
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: links, source checks and PDF ({len(reader.pages)} pages).')
