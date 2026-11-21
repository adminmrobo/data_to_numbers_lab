import json
PG='data_to_numbers_04'
N=[];E=[]
def node(id,t,ko,en,anchor,level=1,cov='explained',fam='ml-basics',defi=None,src=None):
    n={"id":id,"type":t,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":"high","coverage":cov,"family":fam,"match":[],"domain":["ai"]}
    if defi:n["definition"]={"ko":defi}
    if src:n["source"]=[{"ref":r,"loc":""} for r in src]
    N.append(n)
def e(s,p,o,a):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":"high"})
C='lab:concept/';M='lab:method/';L='lab:limitation/';CL='lab:claim/';S='lab:simulation/';T='lab:topic/'
def A(a,au,y,ti,ct,url):
    return {"id":a,"type":"paper-conference","title":ti,"author":[{"family":f,"given":g} for f,g in au],"issued":{"date-parts":[[y]]},"URL":url,"container-title":ct,
     "lab":{"work":"lab:work/"+a,"role":"primary","locs":[],"verified":{"title":True,"author":True,"year":True,"container":True,"pages":False,"doi":False},"checkedBy":"arXiv 초록 페이지·학회 페이지와 대조 (2026-11-21)","checkedSource":"external"}}
PG='data_to_numbers_05'
NEW=[A('jacob2018quantization',[('Jacob','Benoit'),('Kligys','Skirmantas')],2018,'Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference','CVPR 2018','https://arxiv.org/abs/1712.05877'),
 A('hinton2015distilling',[('Hinton','Geoffrey'),('Vinyals','Oriol'),('Dean','Jeff')],2015,'Distilling the Knowledge in a Neural Network','NIPS 2014 Deep Learning Workshop','https://arxiv.org/abs/1503.02531'),
 A('howard2017mobilenets',[('Howard','Andrew G.'),('Zhu','Menglong')],2017,'MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications','arXiv','https://arxiv.org/abs/1704.04861')]
node(C+'model-size','Concept','모델 크기 = 가중치 수 × 비트','Model size','#s1',1,fam='efficiency',defi='크기(바이트) = 가중치 수 × 비트 ÷ 8')
node(M+'quantization','Method','양자화','Quantization','#s2',1,fam='efficiency',defi='가중치를 2ᵇ개 눈금 중 가장 가까운 값으로')
node(M+'pruning','Method','가지치기','Pruning','#s3',1,fam='efficiency',defi='절댓값이 작은 가중치부터 0으로')
node(M+'retrain-after-pruning','Method','가지치기 뒤 다시 학습','Fine-tuning after pruning','#s3',1,fam='efficiency')
node(M+'huffman-coding','Method','허프만 부호','Huffman coding','#s4',2,fam='efficiency')
node(M+'deep-compression','Method','압축 3단계 (가지치기·양자화·허프만)','Deep Compression pipeline','#s4',2,fam='efficiency')
node(M+'knowledge-distillation','Method','지식 증류','Knowledge distillation','#s5',2,fam='efficiency',defi='선생님 모델의 확률(온도 T)로 학생 모델 학습')
node(C+'temperature','Concept','온도 T (확률 펴기)','Softmax temperature','#s5',2,fam='efficiency')
node(M+'depthwise-separable','Method','깊이별 분리 합성곱','Depthwise separable convolution','#s6',2,fam='vision',defi='계산 비율 = 1/N + 1/k²')
node(C+'deployment-budget','Concept','기기별 크기·시간 한도','Deployment budget','#s7',1,fam='efficiency')
node(C+'compression-robustness','Concept','줄인 모델의 강건성 변화','Robustness after compression','#s8',2,fam='robustness')
node(L+'low-bit-collapse','Limitation','눈금이 너무 적으면(2비트) 가중치가 뭉개진다','Too few levels collapse weights','#s2',1)
node(L+'prune-without-retrain','Limitation','다시 학습 없이 크게 지우면 정확도가 무너진다','Pruning without retraining fails','#s3',1)
node(L+'index-overhead','Limitation','남은 가중치의 위치 표시가 따로 든다','Sparse index overhead','#s3',2)
node(L+'student-ceiling','Limitation','학생은 구조의 한계 때문에 선생님을 넘기 어렵다','Student capacity ceiling','#s5',2)
node(L+'separable-limit','Limitation','분리 합성곱의 절약은 k²배를 넘지 못한다','Saving bounded by k²','#s6',1)
node(L+'hardware-dependence','Limitation','실제 속도는 칩이 0 건너뛰기·정수 계산을 지원하는지에 달렸다','Speed depends on hardware support','#s7',2)
s={'h':'han2016deep','j':'jacob2018quantization','d':'hinton2015distilling','m':'howard2017mobilenets'}
node(CL+'dc-35x','Claim','AlexNet 240MB → 6.9MB, VGG-16 552MB → 11.3MB, 정확도 손실 없음','35× and 49× compression','#s4',2,src=[s['h']])
node(CL+'dc-5bit','Claim','연결 하나를 32비트에서 5비트로','32 to 5 bits per connection','#s4',2,src=[s['h']])
node(CL+'int8-4x','Claim','8비트 정수 계산으로 메모리 약 4분의 1, 휴대폰 CPU에서 빠르게','INT8 inference','#s2',2,src=[s['j']])
node(CL+'distill-soft','Claim','선생님의 부드러운 확률에 닮은 정도 정보가 담긴다','Soft targets carry dark knowledge','#s5',2,src=[s['d']])
node(CL+'mobilenet-8-9x','Claim','3×3 분리 합성곱은 계산량을 8~9배 줄인다','8–9× less computation','#s6',2,src=[s['m']])
for k,ko,a in [('size','대시보드 ① 모델 크기 계산기','#p1'),('quant','대시보드 ② 양자화','#p2'),('prune','대시보드 ③ 가지치기','#p3'),('pipe','대시보드 ④ 압축 3단계','#p4'),('distill','대시보드 ⑤ 지식 증류','#p5'),('conv','대시보드 ⑥ 합성곱 계산량','#p6'),('budget','대시보드 ⑦ 기기별 고르기','#p7'),('robust','대시보드 ⑧ 줄인 모델 점검','#p8'),('duel','대결: 한 번에 자르기 vs 여러 방법','#duel')]:node(S+k,'Simulation',ko,k,a,2)
qt={'s1':C+'model-size','s2':M+'quantization','s3':M+'pruning','s4':M+'deep-compression','s5':M+'knowledge-distillation','s6':M+'depthwise-separable','s7':C+'deployment-budget','s8':C+'compression-robustness'}
for st,tgt in qt.items():
    for i in (1,2):
        q='lab:quiz/d2n5-%s-%d'%(st,i);node(q,'QuizItem','%s 확인 퀴즈 %d'%(st,i),'Quiz','#'+st,2,cov='mentioned');e(q,'assesses',tgt,'#'+st)
works=['han2016deep']+[r['id'] for r in NEW]
for w in works:node('lab:work/'+w,'Work',w,w,'#export',2)
e(C+'model-size','prerequisiteOf',M+'quantization','#s2');e(M+'pruning','prerequisiteOf',M+'retrain-after-pruning','#s3')
e(M+'pruning','partOf',M+'deep-compression','#s4');e(M+'quantization','partOf',M+'deep-compression','#s4');e(M+'huffman-coding','partOf',M+'deep-compression','#s4')
e(C+'temperature','partOf',M+'knowledge-distillation','#s5');e(C+'deployment-budget','relatedTo',M+'deep-compression','#s7');e(C+'compression-robustness','relatedTo',M+'pruning','#s8')
for a,b in [(M+'quantization',L+'low-bit-collapse'),(M+'pruning',L+'prune-without-retrain'),(M+'pruning',L+'index-overhead'),(M+'knowledge-distillation',L+'student-ceiling'),(M+'depthwise-separable',L+'separable-limit'),(C+'deployment-budget',L+'hardware-dependence')]:e(a,'hasLimitation',b,'#top')
for a,b in [(C+'model-size','deployment'),(M+'quantization','deployment'),(M+'pruning','sparse-representation'),(M+'retrain-after-pruning','transfer-learning'),(M+'huffman-coding','information-theory'),(M+'deep-compression','deployment'),(M+'knowledge-distillation','transfer-learning'),(C+'temperature','activation-function'),(M+'depthwise-separable','convolution'),(C+'deployment-budget','deployment'),(C+'compression-robustness','ai-safety')]:e(a,'broader',T+b,'#top')
for cl,tgt,w in [('dc-35x',M+'deep-compression',s['h']),('dc-5bit',M+'quantization',s['h']),('int8-4x',M+'quantization',s['j']),('distill-soft',M+'knowledge-distillation',s['d']),('mobilenet-8-9x',M+'depthwise-separable',s['m'])]:
    e(CL+cl,'supports',tgt,'#top');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt in [('size',C+'model-size'),('quant',M+'quantization'),('prune',M+'pruning'),('pipe',M+'deep-compression'),('distill',M+'knowledge-distillation'),('conv',M+'depthwise-separable'),('budget',C+'deployment-budget'),('robust',C+'compression-robustness'),('duel',M+'retrain-after-pruning')]:e(tgt,'demonstratedBy',S+k,'#top')
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
RM=json.load(open('../refs.json'));have={r['id'] for r in RM}
for r in NEW:
    if r['id'] not in have:RM.append(r)
json.dump(RM,open('../refs.json','w'),ensure_ascii=False,indent=1)
R=[r for r in RM if r['id'] in works];json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('../meta.json'))
m.update({"title":"가볍게 만들기 — 모든 데이터는 숫자가 된다 5장","number":"D2N-5","about":[M+'quantization',M+'pruning',M+'knowledge-distillation',M+'depthwise-separable',C+'deployment-budget'],"basedOn":works,"url":"https://adminmrobo.github.io/data_to_numbers_lab/05_lighter_models.html","suggestedCitation":"안상선 (2026). 가볍게 만들기 — 모든 데이터는 숫자가 된다 5장. 연구실 해설, v1.0."})
json.dump(m,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E),len(R))
