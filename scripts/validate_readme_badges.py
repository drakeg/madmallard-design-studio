#!/usr/bin/env python3
"""Validate README badge placement, coverage and manifest-grounded claims."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
readme = (root / 'README.md').read_text()
lines = readme.splitlines()
package = json.loads((root / 'apps/desktop/package.json').read_text())
workflow = root / '.github/workflows/ci.yml'
errors = []

if not lines or lines[0] != '# Mad Mallard Design Studio':
    errors.append('Expected project title on first line')
if len(lines) < 3 or not lines[2].startswith('[!['):
    errors.append('Badges must start immediately below title (allow one blank line)')

badge_lines = []
for line in lines[2:]:
    if line.startswith('[!['):
        badge_lines.append(line)
    elif line.strip() and badge_lines:
        break
badges = '\n'.join(badge_lines)
if not 1 <= len(badge_lines) <= 3:
    errors.append('Expected one to three compact badge rows')

for name, path in [('Rust', 'Cargo.toml'), ('TypeScript', 'apps/desktop/tsconfig.json'),
                   ('Svelte', 'apps/desktop/package.json'), ('Tauri', 'apps/desktop/src-tauri/Cargo.toml'),
                   ('Vite', 'apps/desktop/package.json')]:
    if not (root / path).exists() or f'![{name}' not in badges:
        errors.append(f'Missing grounded {name} badge')

for dep, label in [('svelte', 'Svelte'), ('vite', 'Vite'), ('@tauri-apps/cli', 'Tauri')]:
    spec = package.get('dependencies', {}).get(dep) or package.get('devDependencies', {}).get(dep)
    major = re.search(r'\d+', spec or '')
    if not major or f'{label}-{major.group()}' not in badges:
        errors.append(f'{label} major badge does not match package.json')

for slug in ('actions/workflows/ci.yml/badge.svg', 'img.shields.io/github/issues/drakeg/madmallard-design-studio',
             'img.shields.io/github/issues-pr/drakeg/madmallard-design-studio'):
    if slug not in badges:
        errors.append(f'Missing dynamic badge: {slug}')
if not workflow.exists() and 'actions/workflows/ci.yml/badge.svg' in badges:
    errors.append('CI badge references a missing workflow')
if not any(root.glob('LICENSE*')) and re.search(r'img.shields.io/github/license|!\[License', badges, re.I):
    errors.append('License badge without a license file')
if not any((root / '.github/workflows').glob('*release*')) and 'img.shields.io/github/v/release' in badges:
    errors.append('Release badge requires a verified published release; check manually')
if not any(root.rglob('Dockerfile*')) and re.search(r'!\[Docker', badges):
    errors.append('Docker badge without Dockerfile')
if len(re.findall(r'\[!\[', badges)) != len(set(re.findall(r'\[!\[([^\]]+)', badges))):
    errors.append('Duplicate badge labels')

if errors:
    raise SystemExit('README badge validation failed:\n- ' + '\n- '.join(errors))
print('README badge validation passed')
