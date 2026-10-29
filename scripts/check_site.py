"""Validate references and content before deploying. Python standard library only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, sys
ROOT = Path(__file__).resolve().parents[1]
errors=[]
class PageParser(HTMLParser):
 def __init__(self,path):super().__init__();self.path=path
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for key in ('src','href'):
   v=a.get(key,'');u=urlsplit(v)
   if not v or u.scheme or u.netloc or v.startswith('#'):continue
   if u.path and not (self.path.parent/unquote(u.path)).is_file():errors.append(f'{self.path.name}: missing {v}')
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path.name}: image missing alt')
for path in ROOT.glob('*.html'):PageParser(path).feed(path.read_text())
data=json.loads((ROOT/'content/site.json').read_text());ids=[]
for project in data['projects']:
 ids.append(project['id'])
 for field in ('title','intro','image','alt','stage'):
  if not project.get(field):errors.append(f'{project["id"]}: missing {field}')
 for name in [project['image']]+[g['image'] for g in project['gallery']]:
  if not (ROOT/f'assets/images/{name}.webp').is_file():errors.append(f'Missing image: {name}')
for group in ('development','process'):
 for image in data.get(group,[]):
  if not (ROOT/f'assets/images/{image["image"]}.webp').is_file():errors.append(f'Missing {group} image: {image["image"]}')
if len(ids)!=len(set(ids)):errors.append('Duplicate project IDs')
for page in ('index','collections','studio','journal','project','contact','process'):
 if not (ROOT/f'{page}.html').is_file():errors.append(f'Missing route: {page}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(list(ROOT.glob("*.html")))} pages, {len(ids)} projects, local file references and content checked.')
