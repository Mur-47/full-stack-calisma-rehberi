"""Run locked restore and real .NET tests; reject zero/skipped/stale results."""
from pathlib import Path
import subprocess
import tempfile
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='study-validation-') as folder:
    commands = [
        ['dotnet', 'restore', 'StudyLab.sln', '--locked-mode'],
        ['dotnet', 'test', 'StudyLab.sln', '-c', 'Release', '--no-restore',
         '--logger', 'trx;LogFileName=tests.trx', '--results-directory', folder],
    ]
    for command in commands:
        result = subprocess.run(command, cwd=root, capture_output=True, encoding='utf-8', errors='replace')
        if result.returncode:
            print(result.stdout[-3000:])
            print(result.stderr[-1000:])
            raise SystemExit(result.returncode)
    report = ET.parse(Path(folder) / 'tests.trx')
    namespace = {'t': 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'}
    counters = report.find('.//t:Counters', namespace).attrib
    total = int(counters['total'])
    passed = int(counters['passed'])
    if total == 0 or total != passed:
        raise SystemExit('FAIL: zero, failed or skipped tests.')
    print(f'PASS: locked restore; .NET {passed}/{total}; failed/skipped 0.')
