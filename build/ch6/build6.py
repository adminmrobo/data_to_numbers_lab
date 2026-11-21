#!/usr/bin/env python3
"""6장 「직접 해 보기」 조립: 5장 페이지의 머리·스타일·캐릭터 팩·KGX 모듈을 그대로 쓰고 본문과 장면 스크립트를 새로 넣는다."""
import re, json, subprocess, os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
REPO=sys.argv[1] if len(sys.argv)>1 else '/home/claude/data_to_numbers_lab'
src=open(os.path.join(REPO,'05_lighter_models.html'),encoding='utf-8').read()

# ---- 머리 ----
head=src[:src.find('<style')]
head=re.sub(r'<title>.*?</title>','<title>직접 해 보기 — 모든 데이터는 숫자가 된다 6장 · 연구실 해설</title>',head)
head=re.sub(r'<meta name="description" content=".*?">','<meta name="description" content="1~5장의 결정을 직접 내려 보는 실전 연습장. 접수 창구(숫자 예산), 검수대(옮겨진 그림), 보안실(잡음과 공격), 이삿짐 센터(모델 줄이기) 네 장면과 자동 판정 미션 열두 개.">',head)
head=re.sub(r'<meta property="og:title" content=".*?">','<meta property="og:title" content="직접 해 보기 — 모든 데이터는 숫자가 된다 6장">',head)
head=re.sub(r'<meta property="og:description" content=".*?">','<meta property="og:description" content="네 개의 작업대, 미션 열두 개. 조건을 바꿔도 결론이 유지되는 선택을 직접 찾는 실전 연습장.">',head)
head=head.replace('img/og_ch5.jpg','img/og_ch6.jpg')
style=src[src.find('<style'):src.find('</style>')]
style+=open(os.path.join(HERE,'extra.css'),encoding='utf-8').read()+'\n</style>\n</head>\n'

body=open(os.path.join(HERE,'body6.html'),encoding='utf-8').read()

scripts=list(re.finditer(r'<script>(.*?)</script>',src,re.S))
sprite=scripts[0].group(0)
sim5=scripts[1].group(1)
page5=scripts[2].group(1)
kgx=scripts[3].group(0)
sim6='<script>'+sim5+open(os.path.join(HERE,'sim6_extra.js'),encoding='utf-8').read()+'</script>'

# ---- 페이지 스크립트: 5장의 공용 부분(캐릭터·만화·표지·용어·진행·퀴즈·캔버스 공용)을 쓰고 장면 부분을 바꾼다 ----
common=page5[:page5.find('/* ---------- 공용 자료 ---------- */')]
GL='''var GL={
 '필터':['필터','그림 위를 미끄러지며 작은 자리(여기서는 점 세 개)의 값을 재는 작은 창. 가로줄·세로줄처럼 정해진 모양에 크게 반응한다.'],
 '최댓값 남기기':['최댓값 남기기','필터가 그림 여러 자리에서 잰 값 중 가장 큰 것만 남기는 일. 모양이 "어디에" 있었는지는 버리고 "있었는가"만 남긴다. 사진 모델의 풀링이 하는 일.'],
 '합성곱':['합성곱','작은 창을 그림 위로 밀면서 창 안의 숫자에 가중치를 곱해 더하는 계산. 사진 모델의 기본 부품.'],
 '적대적 학습':['적대적 학습','학습하는 동안 판정기가 가장 약한 방향으로 바꾼 그림(공격받은 그림)을 함께 보여 주어, 그런 공격에 덜 흔들리게 만드는 방법.'],
 '양자화':['양자화','가중치를 정해진 눈금(2ᵇ개) 중 가장 가까운 값으로 바꿔, 숫자 하나를 적는 비트 수를 줄이는 일.'],
 '가지치기':['가지치기','판정에 덜 쓰이는(절댓값이 작은) 가중치를 0으로 만들어 지우는 일. 보통 지운 뒤 다시 학습한다.']
};'''
common=re.sub(r"var GL=\{.*?\n\};",lambda m:GL,common,flags=re.S)
QZ='''var QZ={
 q1:[{q:'예산 50,000개, 흑백 사진이면 예산 안 가장 큰 한 변은?',o:['129','223','288'],a:1,why:'√50,000 ≈ 223.6이므로 223입니다. 223 × 223 = 49,729개로 예산 안, 224면 50,176개로 넘칩니다.'},
     {q:'1초에 10장, 3초짜리 영상은 같은 크기 사진 한 장의 몇 배 숫자인가요?',o:['3배','10배','30배'],a:2,why:'장면 수 = 10 × 3 = 30장이므로 30배입니다.'}],
 q2:[{q:'필터가 점 0.4, 0.6, 0.6 위에 있을 때 필터 값은?',o:['0.40','약 0.53','0.60'],a:1,why:'(0.4 + 0.6 + 0.6) ÷ 3 = 1.6 ÷ 3 ≈ 0.53입니다.'},
     {q:'픽셀 그대로 읽는 판정기가 옮겨진 그림에 약했던 까닭은?',o:['학습 그림이 적어서','어느 자리의 점이 밝은지를 위치째로 외워서','비트가 적어서'],a:1,why:'위치째로 외웠기 때문에, 270장으로 늘려도 이동 2에서 40%였습니다.'}],
 q3:[{q:'ε = 0.05이고 가중치 차이 절댓값의 합이 40이면, 공격이 움직이는 점수 차이는 최대?',o:['0.05점','2점','40점'],a:1,why:'0.05 × 40 = 2점입니다. 정답이 2점보다 적게 앞서 있던 그림은 뒤집힐 수 있습니다.'},
     {q:'잡음 섞기로 배운 모델이 공격에 약했던 까닭은?',o:['잡음이 너무 약해서','공격은 가장 약한 방향만 골라 밀기 때문에','학습 그림이 적어서'],a:1,why:'잡음은 아무 방향으로나 흔들어, 가장 약한 방향을 따로 연습시키지 못합니다.'}],
 q4:[{q:'남은 가중치 39개를 4비트로 적고 위치 표시를 붙이면 크기는?',o:['168비트','504비트','672비트'],a:1,why:'(39 + 3) × (4 + 8) = 42 × 12 = 504비트입니다.'},
     {q:'크기 한도는 지켰는데 정확도가 72%였다. 빠뜨린 단계는?',o:['비트 늘리기','지운 뒤 다시 학습','기기 바꾸기'],a:1,why:'다시 학습하면 남은 가중치가 빈자리를 메워 97.8%로 돌아옵니다.'}]
};'''
common=re.sub(r"var QZ=\{.*?\n\};",lambda m:QZ,common,flags=re.S)
common=common.replace("study.textContent='읽은 곳 '+p+'% · 퀴즈 '+Object.keys(solved).length+'/16';",
 "var mn=0;if(typeof MIS!=='undefined')Object.keys(MIS).forEach(function(k){MIS[k].forEach(function(m){if(m.done)mn++;});});study.textContent='읽은 곳 '+p+'% · 미션 '+mn+'/12 · 퀴즈 '+Object.keys(solved).length+'/8';")
assert '미션 ' in common, 'study line not replaced'
shared='''/* ---------- 공용 자료 (4·5장과 같은 판정기) ---------- */
var TR=imgSet(60,1,0.15),TE=imgSet(90,2,0.15),M0=trainLin(TR,{});
'''
page='<script>'+common+shared+open(os.path.join(HERE,'page6_scenes.js'),encoding='utf-8').read()+'</script>'

# ---- 지식 색인 ----
kgdir=os.path.join(REPO,'kg','ch6')
kg=json.load(open(os.path.join(kgdir,'kg.json'),encoding='utf-8'))
refs=json.load(open(os.path.join(kgdir,'refs.json'),encoding='utf-8'))
meta=json.load(open(os.path.join(kgdir,'meta.json'),encoding='utf-8'))
kgxjs=re.search(r'<script>(.*?)</script>',kgx,re.S).group(1)
open('/tmp/kgx_node.js','w').write('var window={};var document={readyState:"loading",addEventListener:function(){},getElementById:function(){return null;}};\n'+kgxjs+'\nvar fs=require("fs");var a=JSON.parse(fs.readFileSync(process.argv[2]));var m=JSON.parse(fs.readFileSync(process.argv[3]));process.stdout.write(JSON.stringify(KGX.toJsonLd(a,m)));')
ld=subprocess.check_output(['node','/tmp/kgx_node.js',os.path.join(kgdir,'kg.json'),os.path.join(kgdir,'meta.json')]).decode()
def js(o):return json.dumps(o,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
kgblock=src[src.find('<!-- lab-kg:body -->'):src.find('<!-- /lab-kg:body -->')+len('<!-- /lab-kg:body -->')]
kgblock=re.sub(r'(<script type="application/json" id="kg-raw">).*?(</script>)',lambda m:m.group(1)+js(kg)+m.group(2),kgblock,flags=re.S)
kgblock=re.sub(r'(<script type="application/ld\+json" id="kg-ld">).*?(</script>)',lambda m:m.group(1)+ld.replace('</','<\\/')+m.group(2),kgblock,flags=re.S)
kgblock=re.sub(r'(<script type="application/json" id="refs-csl">).*?(</script>)',lambda m:m.group(1)+js(refs)+m.group(2),kgblock,flags=re.S)
kgblock=re.sub(r'(<script type="application/json" id="page-meta">).*?(</script>)',lambda m:m.group(1)+js(meta)+m.group(2),kgblock,flags=re.S)

# ---- 바닥글: 5장의 서베이 표 + 저자 줄을 쓰되 머리말을 고친다 ----
foot=src[src.find('<footer'):src.find('</footer>')+len('</footer>')]
foot=re.sub(r'<h3 style="color:var\(--text\)">출처 — .*?</h3>','<h3 style="color:var(--text)">출처 — 시리즈 서베이 26편 (이 페이지가 직접 기대는 것: [11] Deep Compression · 4장의 FGSM·방어 학습 문헌)</h3>',foot,flags=re.S)
foot=re.sub(r'<h3 style="color:var\(--text\)">예시값·설명용 모형인 것</h3>\s*<ul>.*?</ul>','''<h3 style="color:var(--text)">예시값·설명용 모형인 것</h3>
  <ul>
    <li>장면 A의 숫자 개수는 곱셈으로 바로 나오는 계산 값입니다. 예산(5만·10만·20만 개)과 토큰 하나의 숫자 줄 길이(128·384·768), 1초에 재는 횟수는 설명을 위해 고른 예시입니다.</li>
    <li>장면 B~D의 정확도는 설명용 모형 값입니다(시드 고정). 실제 AI 시스템의 측정값이 아닙니다.</li>
    <li>장면 B는 8 × 8 그림 세 가지를 위아래·좌우로 최대 2점 옮겼습니다(학습 시드 5, 시험 150장 시드 77). 필터 세 개(가로·세로·대각, 점 세 개 평균)는 사람이 정했고, 최댓값에서 0.5를 빼고 5를 곱해 판정기에 넣었습니다.</li>
    <li>장면 C·D는 4·5장과 같은 판정기(학습 60장, 시험 90장, 가중치 195개)입니다. 공격은 한 번짜리 방식(FGSM), 잡음 섞기는 세기 0.35, 다시 학습은 20번 반복, 위치 표시는 가중치마다 8비트로 셈했습니다. 기기 한도(400·1,560·6,240비트)는 예시입니다.</li>
    <li>이 페이지에는 문헌에서 새로 옮긴 숫자가 없습니다. 방법의 바탕은 4장(FGSM·방어 학습)과 5장(Deep Compression)의 문헌입니다.</li>
  </ul>''',foot,flags=re.S)
foot=re.sub(r'· 2026-11-21</p>','· 2026-11-22</p>',foot)
foot=re.sub(r'<p>이 페이지는 교육용 해설입니다\..*?</p>','<p>이 페이지는 교육용 해설입니다. 앞: <a href="05_lighter_models.html">5장 특별</a> · 처음으로: <a href="01_why_numbers.html">1장 도입</a> · <a href="index.html">시리즈 목차</a></p>',foot,flags=re.S)
assert '장면 A의 숫자' in foot and '2026-11-22' in foot

# 5장 꼬리 요소 (tip·study 등) 그대로 재사용
t5=src[src.find('</footer>')+len('</footer>'):]
t5=t5[:t5.find('<script>')].replace('읽은 곳 0% · 퀴즈 0/16','읽은 곳 0% · 미션 0/12 · 퀴즈 0/8')
out=head+style+body+kgblock+'\n'+foot+t5+sprite+'\n'+sim6+'\n'+page+'\n'+kgx+'\n</body>\n</html>\n'
open(os.path.join(REPO,'06_hands_on.html'),'w',encoding='utf-8').write(out)
print('written',len(out))
