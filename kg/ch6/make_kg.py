import json
PG='data_to_numbers_06'
N=[];E=[]
def node(id,t,ko,en,anchor,level=1,cov='explained',fam='ml-basics',defi=None,src=None):
    n={"id":id,"type":t,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":"high","coverage":cov,"family":fam,"match":[],"domain":["ai"]}
    if defi:n["definition"]={"ko":defi}
    if src:n["source"]=[{"ref":r,"loc":""} for r in src]
    N.append(n)
def e(s,p,o,a):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":"high"})
C='lab:concept/';M='lab:method/';L='lab:limitation/';CL='lab:claim/';S='lab:simulation/';T='lab:topic/';TK='lab:task/'
node(C+'practice-room','Concept','실전 연습장 (조작판·성적표·미션)','Practice simulator','#lab',1,fam='pedagogy',defi='배운 결정을 가상 작업장에서 직접 내리고 자동 판정 미션으로 확인하는 대시보드')
node(C+'number-budget','Concept','숫자 예산','Input number budget','#desk',1,fam='representation',defi='숫자 개수 = 한 변 × 한 변 × 색 × 장면 수, 예산 안 최대 한 변 = √(예산 ÷ (색 × 장면 수))')
node(C+'square-growth','Concept','넓이는 한 변의 제곱으로 늘어난다','Quadratic growth of pixel count','#desk',1,fam='representation')
node(C+'shift-invariance','Concept','위치가 바뀌어도 같은 판정','Translation invariance','#inspect',1,fam='vision')
node(M+'filter-max','Method','작은 필터 + 최댓값 남기기 (합성곱·풀링)','Convolution filter with global max pooling','#inspect',2,fam='vision',defi='점 세 개 평균의 필터를 그림 전체에 밀고 최댓값만 남긴다')
node(M+'shift-augmentation','Method','학습 때 그림 옮겨 보여 주기 (증강)','Shift augmentation','#inspect',1,fam='vision')
node(M+'noise-training','Method','잡음 섞어 배우기','Training with random noise','#security',1,fam='robustness')
node(M+'adversarial-training','Method','공격 섞어 배우기 (적대적 학습)','Adversarial training','#security',2,fam='robustness',defi='학습 중 그때그때의 가장 약한 방향으로 바꾼 그림을 함께 보여 준다')
node(C+'fgsm-score-shift','Concept','공격이 움직이는 점수 = ε × 가중치 차이 절댓값의 합','FGSM score change','#security',2,fam='robustness')
node(C+'robustness-tradeoff','Concept','막는 세기와 평소 정확도의 맞바꿈','Robustness–accuracy trade-off','#security',2,fam='robustness')
node(C+'packed-size','Concept','줄인 크기 = (남은 가중치 + 3) × (비트 + 위치 표시)','Compressed size with index overhead','#moving',1,fam='efficiency')
node(M+'prune-retrain-quantize','Method','가지치기 + 다시 학습 + 양자화','Prune, retrain, quantize','#moving',2,fam='efficiency')
node(C+'retest-after-change','Concept','바꾼 뒤 같은 시험 다시 걸기','Re-evaluate after every change','#moving',1,fam='evaluation')
node(C+'condition-check','Concept','조건을 바꿔도 결론이 유지되는지 확인','Robustness of conclusions to conditions','#wrapup',1,fam='evaluation')
node(L+'linear-pixel-limit','Limitation','픽셀 그대로 읽는 선형 판정기는 큰 이동을 감당하지 못한다','Linear pixel model cannot absorb large shifts','#inspect',1)
node(L+'hand-made-filters','Limitation','필터 세 개는 사람이 정했다 (실제 모델은 학습)','Filters hand-designed here','#inspect',2)
node(L+'single-step-attack','Limitation','가장 단순한 한 번짜리 공격만 썼다','Only single-step attack tested','#security',2)
node(L+'size-not-speed','Limitation','크기만 셌고 실행 속도는 재지 않았다','Size counted, latency not measured','#moving',2)
node(L+'toy-model','Limitation','8 × 8 그림 세 종류의 단순 선형 모형, 설명용 값','Toy linear model','#wrapup',1)
node(CL+'fgsm-linear','Claim','선형 모델은 작은 변조가 여러 차원에서 모여 판정이 뒤집힌다','Linearity explains adversarial examples','#security',2,src=['goodfellow2015explaining'])
node(CL+'adv-training-robust','Claim','적대적 예시로 학습하면 공격에 대한 강건성이 커진다','Adversarial training improves robustness','#security',2,src=['madry2018towards'])
node(CL+'prune-quant-compose','Claim','가지치기·양자화를 이어 붙이면 정확도 손실 없이 크게 줄인다','Pruning and quantization compose','#moving',2,src=['han2016deep'])
node(TK+'practice','Task','배운 결정 직접 내려 보기','Hands-on decision practice','#lab',1)
for k,ko,a in [('desk','장면 A 접수 창구','#desk'),('inspect','장면 B 검수대 (그리기판 포함)','#inspect'),('security','장면 C 보안실','#security'),('moving','장면 D 이삿짐 센터','#moving')]:node(S+'d2n6-'+k,'Simulation',ko,k,a,2)
qt={'desk':C+'number-budget','inspect':M+'filter-max','security':M+'adversarial-training','moving':C+'packed-size'}
for st,tgt in qt.items():
    for i in (1,2):
        q='lab:quiz/d2n6-%s-%d'%(st,i);node(q,'QuizItem','%s 확인 퀴즈 %d'%(st,i),'Quiz','#'+st,2,cov='mentioned');e(q,'assesses',tgt,'#'+st)
works=['goodfellow2015explaining','madry2018towards','han2016deep']
for w in works:node('lab:work/'+w,'Work',w,w,'#export',2)
e(C+'square-growth','partOf',C+'number-budget','#desk');e(C+'number-budget','prerequisiteOf',C+'packed-size','#moving')
e(C+'shift-invariance','addressedBy',M+'filter-max','#inspect');e(C+'shift-invariance','addressedBy',M+'shift-augmentation','#inspect');e(M+'filter-max','contrastsWith',M+'shift-augmentation','#inspect')
e(M+'noise-training','contrastsWith',M+'adversarial-training','#security');e(C+'fgsm-score-shift','prerequisiteOf',M+'adversarial-training','#security');e(M+'adversarial-training','relatedTo',C+'robustness-tradeoff','#security')
e(C+'packed-size','partOf',M+'prune-retrain-quantize','#moving');e(M+'prune-retrain-quantize','relatedTo',C+'retest-after-change','#moving')
e(C+'retest-after-change','partOf',C+'condition-check','#wrapup');e(C+'practice-room','solves',TK+'practice','#lab')
for a,b in [(M+'filter-max',L+'hand-made-filters'),(C+'shift-invariance',L+'linear-pixel-limit'),(M+'adversarial-training',L+'single-step-attack'),(M+'prune-retrain-quantize',L+'size-not-speed'),(C+'practice-room',L+'toy-model')]:e(a,'hasLimitation',b,'#top')
for a,b in [(C+'number-budget','representation'),(C+'square-growth','representation'),(C+'shift-invariance','invariance'),(M+'filter-max','convolution'),(M+'shift-augmentation','data-augmentation'),(M+'noise-training','robustness'),(M+'adversarial-training','ai-safety'),(C+'fgsm-score-shift','ai-safety'),(C+'robustness-tradeoff','robustness'),(C+'packed-size','deployment'),(M+'prune-retrain-quantize','deployment'),(C+'retest-after-change','evaluation'),(C+'condition-check','evaluation'),(C+'practice-room','pedagogy')]:e(a,'broader',T+b,'#top')
for cl,tgt,w in [('fgsm-linear',C+'fgsm-score-shift','goodfellow2015explaining'),('adv-training-robust',M+'adversarial-training','madry2018towards'),('prune-quant-compose',M+'prune-retrain-quantize','han2016deep')]:
    e(CL+cl,'supports',tgt,'#top');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt in [('desk',C+'number-budget'),('inspect',M+'filter-max'),('security',M+'adversarial-training'),('moving',M+'prune-retrain-quantize')]:e(tgt,'demonstratedBy',S+'d2n6-'+k,'#top')
for k in ['desk','inspect','security','moving']:e(S+'d2n6-'+k,'partOf',C+'practice-room','#lab')
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
RM=json.load(open('../refs.json'));R=[r for r in RM if r['id'] in works];json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('../meta.json'))
m.update({"title":"직접 해 보기 — 모든 데이터는 숫자가 된다 6장","number":"D2N-6","about":[C+'practice-room',C+'number-budget',M+'filter-max',M+'adversarial-training',M+'prune-retrain-quantize'],"basedOn":works,"date":"2026-11-22","url":"https://adminmrobo.github.io/data_to_numbers_lab/06_hands_on.html","suggestedCitation":"안상선 (2026). 직접 해 보기 — 모든 데이터는 숫자가 된다 6장. 연구실 해설, v1.0."})
json.dump(m,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E),len(R))
