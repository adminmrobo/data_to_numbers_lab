#!/usr/bin/env python3
"""extend_data.py의 문구를 페이지에 끼운다. 여러 번 돌려도 같은 결과(표시 class로 중복 방지)."""
import re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from extend_data import INWORDS,ROWS,RECAP,REPLACE
REPO=sys.argv[1] if len(sys.argv)>1 else '.'
CSS='\n/* ai-lab-extend: 말로 먼저 */\n.inwords{background:var(--info-soft);border:1px solid #c5d5f2;border-radius:8px;padding:7px 12px;margin:8px 0 4px;font-size:15px;line-height:1.7}\n.inwords b{color:var(--info)}\n'
CSS2='\n/* ai-lab-extend: 좁은 화면 수식 */\n@media (max-width:520px){.eq{white-space:normal;overflow-wrap:anywhere;line-height:1.9}}\n'
def apply(path,name):
  s=open(path,encoding='utf-8').read();n0=len(s)
  if '.inwords{' not in s and '<style' in s: s=s.replace('</style>',CSS+'</style>',1)
  if '/* ai-lab-extend: 좁은 화면 수식 */' not in s and '<style' in s: s=s.replace('</style>',CSS2+'</style>',1)
  # 수식 상자 찾기
  parts=s.split('<div class="math">');L=INWORDS.get(name,[])
  assert len(parts)-1==len(L),(name,len(parts)-1,len(L))
  for i in range(1,len(parts)):
    p=parts[i];k=i-1
    if 'class="inwords"' not in p.split('<div class="eq">')[0]:
      p=p.replace('<div class="eq">','<div class="inwords"><b>말로 먼저</b> — '+L[k]+'</div>\n        <div class="eq">',1)
    for sym,mean in ROWS.get((name,k),[]):
      row='<tr><td>'+sym+'</td><td>'+mean+'</td></tr>'
      if row not in p:
        j=p.find('</table>');p=p[:j]+'  '+row+'\n        '+p[j:]
    parts[i]=p
  s='<div class="math">'.join(parts)
  if name in RECAP and 'class="recap first"' not in s:
    a=s.find('<section class="level" id="three"');b=s.find('</section>',a)
    s=s[:b]+'  <div class="recap first"><b>30초 복습</b> — '+RECAP[name]+'</div>\n'+s[b:]
  for a,b in REPLACE.get(name,[]):
    if a in s:s=s.replace(a,b)
  open(path,'w',encoding='utf-8').write(s);return len(s)-n0
for f in sys.argv[2:] or sorted(INWORDS):
  print(f,apply(os.path.join(REPO,f),os.path.basename(f)))
