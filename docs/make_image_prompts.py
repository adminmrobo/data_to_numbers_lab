import re,os,shutil,zipfile
import sys
REPO=sys.argv[1] if len(sys.argv)>1 else '/home/claude/data_to_numbers_lab'
D=REPO+'/docs'
STYLE='16-bit RPG pixel art, bold dark outlines, 2–3 tone shading, bright sunlit white laboratory, clean white background'
NO='No text, no letters, no numbers, no logos, no speech bubbles, no night, no neon.'
CH={'doc':'the chibi scientist (thin teal square glasses, black hair with one white streak, short ponytail, white lab coat over black vest and tie)',
 'asst':'the young researcher Haru (long pink hair in two round buns with navy streaks, lavender hoodie under white lab coat, jeans)',
 'robo':'the beige boxy CRT robot (dark green screen face with mint pixel eyes, abacus-bead antenna, crawler treads)',
 'fly':'the small fruit fly researcher (black body, red compound eyes, blue helmet with gold stripe, white coat, black gloves, transparent wings)'}
KO={'doc':'박사','asst':'조수(하루)','robo':'주판봇','fly':'초파리 연구원'}
MOOD={'happy':'grinning proudly with sparkling eyes','report':'holding a clipboard and reporting earnestly','wow':'eyes wide open in amazement',
 'shock':'shocked, mouth open, hands raised','sigh':'with a big sweat drop, sheepish and deflated','magnify':'peering through a magnifying glass',
 'point':'pointing firmly with one gloved hand, confident','board':'pointing at a whiteboard like a kind teacher','spark':'with sparkling eyes, excited and proud'}
POS={'l':'on the left','r':'on the right','c':'in the center','r sm':'small on the right','c sm':'small in the center'}
SCENE={'lab':'an open laboratory floor with tidy shelves','screen':'in front of a large wall monitor','desk':'at a wooden lab desk','board':'in front of a whiteboard'}
# 컷마다 그림 속 소품·행동 (글자 없음)
PROPS={
'cm1_1':'The robot holds out a shiny red apple toward the viewer. The left half of the panel is empty.',
'cm1_2':'Haru points at a monitor filled with neat rows of green pixel blocks that look like data (no readable digits).',
'cm1_3':'A red apple and a red ball sit side by side on the desk; the fruit fly compares them.',
'cm1_4':'The whiteboard shows a red dot cluster and a green dot cluster being rearranged by arrows (no writing).',
'cm2_1':'The robot proudly holds up a single red apple as if it were a rule card (no writing).',
'cm2_2':'Haru holds up a green apple in one hand and a red ball in the other.',
'cm2_3':'The room lights are dimmed on one side; the fruit fly examines a red apple that looks almost black in the shadow.',
'cm2_4':'The whiteboard shows a simple bar gauge rising and stopping at a dashed line (no writing).',
'cm3_1':'The robot stands beside a tall stack of identical red-apple photos coming out of a copier.',
'cm3_2':'Haru holds out a green apple; the small robot looks at it with a sweat drop.',
'cm3_3':'The fruit fly fans out four cards showing the same apple painted red, green, yellow and blue.',
'cm3_4':'The whiteboard shows apple dots of different colors gathered inside one circle (no writing).',
'cm4_1':'The robot holds up a glowing trophy-shaped monitor, very proud.',
'cm4_2':'Haru holds up a picture with a few small dots on it, shocked; the small robot sweats.',
'cm4_3':'The fruit fly points with a magnifying glass at small dots on a picture that line up in one direction.',
'cm4_4':'The whiteboard shows scattered random dots on the left and one bold arrow on the right (no writing).',
'cm5_1':'The robot is about to saw a big cardboard moving box in half.',
'cm5_2':'Haru stares at important items spilling out of a box sawn in half; the small robot sweats.',
'cm5_3':'The fruit fly tosses unused items aside and squeezes clothes into a vacuum storage bag.',
'cm5_4':'The whiteboard shows a big box turning into a small box through three arrows (no writing).',
'cm6_1':'The whiteboard shows four small pictures of workstations side by side: boxes, a camera over parts, a shield, a scale (no writing).',
'cm6_2':'The robot proudly holds open a thick notebook of memorized answers.',
'cm6_3':'The fruit fly points at a control panel with green and blue knobs on a workstation.',
'cm6_4':'Haru reports from a clipboard; the small robot has put down its thick notebook and sweats.'}
src={}
for f in sorted(os.listdir(REPO)):
  if re.match(r'0[1-6]_.*\.html$',f):
    s=open(REPO+'/'+f).read()
    for m in re.finditer(r'<div class="frame" data-img="(cm\d_\d)" data-scene="(\w+)">(.*?)(?=<div class="frame"|</div>\s*</div>)',s,re.S):
      bub=re.search(r'<div class="bub"[^>]*>([^<]*)',m.group(3)).group(1)
      chars=re.findall(r'<img class="ch ([a-z ]+)" data-who="(\w+)" data-mood="(\w+)"',m.group(3))
      src[m.group(1)]=(m.group(2),bub,chars,f)
def comic(k):
  scene,bub,chars,f=src[k]
  who='; '.join(CH[w]+' '+POS[p]+', '+MOOD[md] for p,w,md in chars)
  en=f'Comic panel, 3:2 landscape (1200×800), {STYLE}. Setting: {SCENE[scene]}. Characters: {who}. {PROPS[k]} Keep the upper third of the panel empty for a speech bubble added later. Keep the same character designs as the reference images. {NO}'
  ko=', '.join(f"{KO[w]}({ {'l':'왼쪽','r':'오른쪽','c':'가운데','r sm':'오른쪽 작게','c sm':'가운데 작게'}[p]})" for p,w,md in chars)
  return en,ko,bub
COV={}
for c in ['00_index','01_why_numbers','02_rules_to_numbers','03_same_despite_looks','04_noise_and_attacks','05_lighter_models','06_hands_on']:
  t=open(f'{D}/COVER_{c}.md').read()
  en=t.split('## English prompt')[1].strip()
  key='cover_index' if c=='00_index' else 'cover_ch'+c[1]
  COV[key]=(en,c)
REQ=[('R1_style_check',['cover_index'],'16:9','먼저 이 한 장으로 그림체를 확인합니다. 마음에 들면 이 그림을 이후 모든 요청에 참고 그림으로 함께 올립니다.'),
     ('R2_covers_1to3',['cover_ch1','cover_ch2','cover_ch3'],'16:9',''),
     ('R3_covers_4to6',['cover_ch4','cover_ch5','cover_ch6'],'16:9',''),
     ('R4_comic_ch1',['cm1_1','cm1_2','cm1_3','cm1_4'],'3:2',''),('R5_comic_ch2',['cm2_1','cm2_2','cm2_3','cm2_4'],'3:2',''),
     ('R6_comic_ch3',['cm3_1','cm3_2','cm3_3','cm3_4'],'3:2',''),('R7_comic_ch4',['cm4_1','cm4_2','cm4_3','cm4_4'],'3:2',''),('R8_comic_ch5',['cm5_1','cm5_2','cm5_3','cm5_4'],'3:2',''),('R9_comic_ch6',['cm6_1','cm6_2','cm6_3','cm6_4'],'3:2','')]
def prompt(k):
  if k in COV:return COV[k][0]
  return comic(k)[0]
SIZE=lambda k:'1600×900' if k.startswith('cover') else '1200×800'
# ---- 전체 프롬프트 문서
md=['# 이미지 프롬프트 모음 — 모든 데이터는 숫자가 된다 (목차 + 1~6장)','',
'모든 그림은 **16비트 RPG 픽셀아트**, 흰 배경의 낮 연구실, 그림 안 글자·숫자·로고 없음. 말풍선은 HTML이 얹으므로 만화 컷에는 그리지 않습니다.','',
'## 그림 전체 목록','','| 구분 | 수 | 할 일 |','|---|---|---|',
'| 새로 그림: 표지 | 7 | cover_index, cover_ch1~ch6 (16:9, 1600×900) |',
'| 새로 그림: 4컷 만화 | 24 | cm1_1 ~ cm6_4 (3:2, 1200×800) |',
'| 표지에서 자름 | 7 | og_index, og_ch1~ch6 (1200×630, 표지 가운데를 기준으로) |',
'| 캐릭터 팩 재사용 | — | 말풍선·등장인물·대결·인턴·X1~X3 표정 그림 (fruitfly-lab-expressions) |','',
'## 만드는 순서 (요청 = 대화 하나)','']
for i,(r,keys,ratio,note) in enumerate(REQ,1):
  md.append(f'{i}. **{r}** — {", ".join(keys)} ({ratio})'+(f' · {note}' if note else ''))
md+=['','참고 그림: 요청마다 `refs/`의 캐릭터 기본 그림 4장을 함께 올립니다. R2부터는 R1에서 받은 cover_index도 함께 올립니다.','']
for r,keys,ratio,note in REQ:
  md.append(f'## {r} ({ratio})');md.append('')
  for k in keys:
    md.append(f'### {k} · {SIZE(k)} · 저장 이름 `{k}.png`')
    if k in COV:md.append(f'한국어 지시: `docs/COVER_{COV[k][1]}.md` 참고')
    else:
      en,ko,bub=comic(k);md.append(f'- 등장: {ko} · 이 컷의 말풍선(HTML): "{bub}"')
    md+=['','```',prompt(k),'```','']
md+=['## 표지에서 자르기 (생성하지 않음)','','| 저장 이름 | 원본 | 크기 |','|---|---|---|']
for k in ['index','ch1','ch2','ch3','ch4','ch5','ch6']:md.append(f'| og_{k}.jpg | cover_{k}.png | 1200×630 (가운데 기준, 캐릭터 얼굴이 잘리지 않게) |')
md+=['','## 반영','','받은 그림을 한 폴더에 모은 뒤:','','```','python3 build_character_pack.py --ingest ./받은그림 \\',
 '  --plates cover_index=L,cover_ch1=L,cover_ch2=L,cover_ch3=L,cover_ch4=L,cover_ch5=L,cover_ch6=L,cm1_1=E,cm1_2=E,cm1_3=E,cm1_4=E,cm2_1=E,cm2_2=E,cm2_3=E,cm2_4=E,cm3_1=E,cm3_2=E,cm3_3=E,cm3_4=E,cm4_1=E,cm4_2=E,cm4_3=E,cm4_4=E,cm5_1=E,cm5_2=E,cm5_3=E,cm5_4=E,cm6_1=E,cm6_2=E,cm6_3=E,cm6_4=E \\',
 '  --out received_all','```','','표지는 1600×900 WebP, 만화 컷은 1200×800 WebP로 줄여 각 페이지에 넣습니다(한 편 600KB 이하).']
open(f'{D}/IMAGE_PROMPTS_ALL.md','w').write('\n'.join(md)+'\n')
# ---- 요청 꾸러미
P='/home/claude/imgpack/d2n_image_request_pack';shutil.rmtree(P+'/requests',ignore_errors=True);os.makedirs(P+'/requests')
# refs/ 는 이전 꾸러미의 캐릭터 기본 그림 4장을 그대로 씀 (fruitfly-lab-expressions E13)
assert len(os.listdir(P+'/refs'))==4
for i,(r,keys,ratio,note) in enumerate(REQ,1):
  t=[f'[{r}] 비율 {ratio} · 그림 {len(keys)}장 · 한 대화에서 차례로 요청',
     '첨부: refs/ 캐릭터 기본 그림 4장'+('' if r.startswith('R1') else ' + R1에서 받은 cover_index.png'),'',
     'Use the attached character reference images to keep every character design identical. Generate the following images one by one, in this order, each as a separate image:','']
  for j,k in enumerate(keys,1):t+=[f'--- Image {j}: {k} ({SIZE(k)}) — save as {k}.png ---',prompt(k),'']
  if note:t.append('메모: '+note)
  open(f'{P}/requests/{i:02d}_{r}.txt','w').write('\n'.join(t)+'\n')
ck=['# 저장 이름 체크리스트','','받은 그림을 아래 이름으로 저장하고 확인 표시를 합니다.','']
for r,keys,ratio,note in REQ:
  ck.append(f'## {r}');ck+= [f'- [ ] {k}.png ({SIZE(k)})' for k in keys];ck.append('')
ck+=['## 자르기 (생성 안 함)']+[f'- [ ] og_{k}.jpg ← cover_{k}.png (1200×630)' for k in ['index','ch1','ch2','ch3','ch4','ch5','ch6']]
open(f'{P}/CHECKLIST.md','w').write('\n'.join(ck)+'\n')
open(f'{P}/README.md','w').write('# 이미지 요청 꾸러미 — 모든 데이터는 숫자가 된다\n\n1. requests/ 의 파일을 번호 순서대로 하나씩, 생성 도구의 새 대화에 붙여 넣습니다.\n2. 대화마다 refs/ 의 캐릭터 기본 그림 4장을 첨부합니다(R2부터는 받은 cover_index도).\n3. 받은 그림은 CHECKLIST.md 의 이름으로 저장합니다.\n4. 전체 프롬프트·한국어 설명은 저장소 docs/IMAGE_PROMPTS_ALL.md 에 있습니다.\n\n그림체: 16비트 RPG 픽셀아트, 흰 배경의 낮 연구실, 그림 안 글자·숫자·로고 없음.\n')
z=D+'/d2n_image_request_pack.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as Z:
  for root,_,fs in os.walk(P):
    for x in fs:Z.write(os.path.join(root,x),os.path.relpath(os.path.join(root,x),os.path.dirname(P)))
print(len(src),'comics', os.path.getsize(z)//1024,'KB')
