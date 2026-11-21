import json
PG='data_to_numbers_03'
N=[];E=[]
def node(id,t,ko,en,anchor,level=1,cov='explained',fam='ml-basics',defi=None,src=None):
    n={"id":id,"type":t,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":"high","coverage":cov,"family":fam,"match":[],"domain":["ai"]}
    if defi:n["definition"]={"ko":defi}
    if src:n["source"]=[{"ref":r,"loc":""} for r in src]
    N.append(n)
def e(s,p,o,a):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":"high"})
C='lab:concept/';M='lab:method/';L='lab:limitation/';CL='lab:claim/';S='lab:simulation/';T='lab:topic/'
def A(a,b,au,y,ti,ct,url,typ='paper-conference'):
    return {"id":a,"type":typ,"title":ti,"author":[{"family":f,"given":g} for f,g in au],"issued":{"date-parts":[[y]]},"URL":url,"container-title":ct,
     "lab":{"work":"lab:work/"+a,"role":"primary","locs":[],"verified":{"title":True,"author":True,"year":True,"container":True,"pages":False,"doi":False},"checkedBy":"arXiv 초록 페이지·학회 페이지와 대조 (2026-11-21)","checkedSource":"external"}}
NEW=[A('radford2021learning',0,[('Radford','Alec'),('Kim','Jong Wook'),('Hallacy','Chris')],2021,'Learning Transferable Visual Models From Natural Language Supervision','ICML 2021','https://arxiv.org/abs/2103.00020'),
 A('chen2020simple',0,[('Chen','Ting'),('Kornblith','Simon'),('Norouzi','Mohammad'),('Hinton','Geoffrey')],2020,'A Simple Framework for Contrastive Learning of Visual Representations','ICML 2020','https://arxiv.org/abs/2002.05709'),
 A('snyder2018xvectors',0,[('Snyder','David'),('Garcia-Romero','Daniel'),('Sell','Gregory'),('Povey','Daniel'),('Khudanpur','Sanjeev')],2018,'X-Vectors: Robust DNN Embeddings for Speaker Recognition','ICASSP 2018','https://danielpovey.com/files/2018_icassp_xvectors.pdf'),
 A('li2023trocr',0,[('Li','Minghao'),('Lv','Tengchao'),('Chen','Jingye')],2023,'TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models','AAAI 2023','https://arxiv.org/abs/2109.10282'),
 A('reimers2019sentence',0,[('Reimers','Nils'),('Gurevych','Iryna')],2019,'Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks','EMNLP 2019','https://arxiv.org/abs/1908.10084'),
 A('cao2017realtime',0,[('Cao','Zhe'),('Simon','Tomas'),('Wei','Shih-En'),('Sheikh','Yaser')],2017,'Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields','CVPR 2017','https://arxiv.org/abs/1611.08050'),
 A('carreira2017quo',0,[('Carreira','Joao'),('Zisserman','Andrew')],2017,'Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset','CVPR 2017','https://arxiv.org/abs/1705.07750')]
node(C+'cosine-similarity','Concept','코사인 유사도','Cosine similarity','#s1',1,fam='representation',defi='두 숫자 줄의 내적 ÷ 길이의 곱. 크기는 무시하고 방향만 본다')
node(C+'embedding-distance','Concept','임베딩 사이 거리','Embedding distance','#s1',1,fam='representation')
node(M+'augmentation-contrastive','Method','증강 + 대조 학습','Augmentation with contrastive learning','#s2',2,fam='representation',defi='한 사진의 두 모습은 가깝게, 다른 사진은 멀게. 바꿔 보여 준 차이가 무시된다')
node(M+'triplet-loss','Method','세 쌍 손실','Triplet loss','#s3',2,fam='representation',defi='max(0, d(기준, 같은)² − d(기준, 다른)² + α)')
node(C+'goal-defines-invariance','Concept','무엇을 지울지는 목표가 정한다','Task-dependent invariance','#s5',2,fam='representation',defi='같은 녹음도 낱말 목표면 음색을, 화자 목표면 낱말을 지운다')
node(M+'word-embedding-speech','Method','같은 낱말끼리 가깝게 (음색 무시)','Content embedding for speech','#s4',2,fam='sequence')
node(M+'speaker-embedding','Method','같은 사람끼리 가깝게 (낱말 무시)','Speaker embedding','#s5',2,fam='sequence')
node(C+'jaccard','Concept','글자 겹침 비율 (자카드)','Jaccard overlap','#s6',1,fam='language',defi='교집합 ÷ 합집합')
node(M+'sentence-embedding','Method','문장 뜻 숫자 줄','Sentence embedding','#s6',2,fam='language')
node(M+'pose-normalization','Method','관절 좌표 맞추기 (골반 기준·키로 나누기)','Keypoint normalization','#s7',1,fam='vision',defi='(관절 − 골반) ÷ 키. 위치와 체격을 지운다')
node(C+'temporal-window','Concept','여러 장면 보기 (시간 창)','Temporal window','#s8',1,fam='vision',defi='장면을 이어 봐야 변화의 방향이 보인다')
node(C+'joint-embedding-space','Concept','사진과 글의 한 공간','Joint image-text space','#s9',2,fam='representation')
node(L+'shortcut-color','Limitation','학습은 가장 쉬운 단서(색)만 배울 수 있다','Shortcut learning on color','#s2',1)
node(L+'imbalanced-pairs','Limitation','다른 쌍이 많으면 전체 정확도가 속인다','Pair imbalance inflates accuracy','#s3',2)
node(L+'content-erases-speaker','Limitation','낱말용 숫자는 화자를 잘 못 가린다','Content embeddings lose speaker identity','#s4',2)
node(L+'surface-overlap','Limitation','글자 겹침은 뜻을 대신하지 못한다','Surface overlap misses meaning','#s6',1)
node(L+'single-frame-ambiguity','Limitation','한 장면으로는 앉기와 일어서기를 가를 수 없다','Single frame is ambiguous','#s8',1)
node(L+'nearest-always-returns','Limitation','맞는 것이 없어도 가장 가까운 것은 늘 나온다','Nearest neighbour always returns something','#s9',1)
src={'clip':'radford2021learning','facenet':'schroff2015facenet','simclr':'chen2020simple','xvec':'snyder2018xvectors','trocr':'li2023trocr','sbert':'reimers2019sentence','openpose':'cao2017realtime','i3d':'carreira2017quo','w2v':'mikolov2013efficient','wav2vec':'baevski2020wav2vec'}
node(CL+'facenet-128','Claim','얼굴 하나를 128바이트로, 거리 = 닮은 정도','FaceNet 128 bytes per face','#s3',2,src=[src['facenet']])
node(CL+'clip-400m','Claim','사진·글 쌍 4억 개로 함께 학습','CLIP trained on 400M pairs','#s9',2,src=[src['clip']])
node(CL+'simclr-aug','Claim','증강 조합이 대조 학습 품질을 크게 좌우한다','Augmentation composition matters','#s2',2,src=[src['simclr']])
node(CL+'xvector','Claim','발화를 고정 길이 화자 숫자 줄로','Fixed-length speaker embeddings','#s5',2,src=[src['xvec']])
node(CL+'wav2vec-10min','Claim','정답 달린 녹음 10분으로도 음성 인식','10 minutes of labeled data','#s4',2,src=[src['wav2vec']])
node(CL+'trocr','Claim','인쇄체·손글씨·간판 글자 읽기에서 기존 모델을 앞섬','TrOCR outperforms prior models','#s6',2,src=[src['trocr']])
node(CL+'sbert-speed','Claim','가장 비슷한 문장 쌍 찾기 65시간 → 약 5초','65 hours to about 5 seconds','#s6',2,src=[src['sbert']])
node(CL+'openpose','Claim','여러 사람의 관절을 실시간으로 찾는다','Realtime multi-person pose','#s7',2,src=[src['openpose']])
node(CL+'kinetics','Claim','동작 400가지·동작마다 영상 400개 이상','Kinetics 400 classes','#s8',2,src=[src['i3d']])
node(CL+'w2v-analogy','Claim','왕 − 남자 + 여자 ≈ 여왕','King − man + woman ≈ queen','#s1',2,cov='mentioned',src=[src['w2v']])
for k,ko,a in [('words','대시보드 ① 낱말 지도','#p1'),('aug','대시보드 ② 증강 실험실','#p2'),('face','대시보드 ③ 얼굴 지도','#p3'),('word','대시보드 ④ 낱말 맞히기 학습','#p4'),('goal','대시보드 ⑤ 목표 바꾸기','#p5'),('text','대시보드 ⑥ 문의 분류','#p6'),('pose','대시보드 ⑦ 동작 무대','#p7'),('time','대시보드 ⑧ 시간 창','#p8'),('clip','대시보드 ⑨ 사진·글 한 공간','#p9'),('duel','대결: 같은 사진 두 배 vs 색 바꾸기','#duel')]:node(S+k,'Simulation',ko,k,a,2)
qt={'s1':C+'cosine-similarity','s2':M+'augmentation-contrastive','s3':M+'triplet-loss','s4':M+'word-embedding-speech','s5':C+'goal-defines-invariance','s6':C+'jaccard','s7':M+'pose-normalization','s8':C+'temporal-window','s9':C+'joint-embedding-space'}
for s,tgt in qt.items():
    for i in (1,2):
        q='lab:quiz/d2n3-%s-%d'%(s,i);node(q,'QuizItem','%s 확인 퀴즈 %d'%(s,i),'Quiz','#'+s,2,cov='mentioned');e(q,'assesses',tgt,'#'+s)
works=['schroff2015facenet','mikolov2013efficient','baevski2020wav2vec']+[r['id'] for r in NEW]
for w in works:node('lab:work/'+w,'Work',w,w,'#export',2)
e(C+'embedding-distance','prerequisiteOf',M+'augmentation-contrastive','#s2');e(C+'cosine-similarity','contrastsWith',C+'embedding-distance','#s1')
e(M+'augmentation-contrastive','prerequisiteOf',M+'triplet-loss','#s3');e(M+'word-embedding-speech','contrastsWith',M+'speaker-embedding','#s5')
e(C+'goal-defines-invariance','relatedTo',M+'word-embedding-speech','#s5');e(C+'goal-defines-invariance','relatedTo',M+'speaker-embedding','#s5')
e(C+'jaccard','contrastsWith',M+'sentence-embedding','#s6');e(M+'pose-normalization','prerequisiteOf',C+'temporal-window','#s8')
e(M+'augmentation-contrastive','prerequisiteOf',C+'joint-embedding-space','#s9');e(C+'cosine-similarity','prerequisiteOf',C+'joint-embedding-space','#s9')
for a,b in [(M+'augmentation-contrastive',L+'shortcut-color'),(M+'triplet-loss',L+'imbalanced-pairs'),(M+'word-embedding-speech',L+'content-erases-speaker'),(C+'jaccard',L+'surface-overlap'),(C+'temporal-window',L+'single-frame-ambiguity'),(C+'joint-embedding-space',L+'nearest-always-returns')]:e(a,'hasLimitation',b,'#top')
for a,b in [(C+'cosine-similarity','embedding-space'),(C+'embedding-distance','embedding-space'),(M+'augmentation-contrastive','contrastive'),(M+'augmentation-contrastive','data-augmentation'),(M+'triplet-loss','loss-function'),(M+'triplet-loss','contrastive'),(C+'goal-defines-invariance','embedding-space'),(M+'word-embedding-speech','self-supervised'),(M+'speaker-embedding','embedding-space'),(C+'jaccard','feature-engineering'),(M+'sentence-embedding','word-embedding'),(M+'pose-normalization','feature-engineering'),(C+'temporal-window','time-series'),(C+'joint-embedding-space','contrastive'),(L+'imbalanced-pairs','accuracy-metrics'),(L+'shortcut-color','generalization')]:e(a,'broader',T+b,'#top')
for cl,tgt,w in [('facenet-128',M+'triplet-loss',src['facenet']),('clip-400m',C+'joint-embedding-space',src['clip']),('simclr-aug',M+'augmentation-contrastive',src['simclr']),('xvector',M+'speaker-embedding',src['xvec']),('wav2vec-10min',M+'word-embedding-speech',src['wav2vec']),('trocr',M+'sentence-embedding',src['trocr']),('sbert-speed',M+'sentence-embedding',src['sbert']),('openpose',M+'pose-normalization',src['openpose']),('kinetics',C+'temporal-window',src['i3d']),('w2v-analogy',C+'embedding-distance',src['w2v'])]:
    e(CL+cl,'supports',tgt,'#top');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt in [('words',C+'cosine-similarity'),('aug',M+'augmentation-contrastive'),('face',M+'triplet-loss'),('word',M+'word-embedding-speech'),('goal',C+'goal-defines-invariance'),('text',M+'sentence-embedding'),('pose',M+'pose-normalization'),('time',C+'temporal-window'),('clip',C+'joint-embedding-space'),('duel',M+'augmentation-contrastive')]:e(tgt,'demonstratedBy',S+k,'#p1' if k=='words' else '#top')
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
RM=json.load(open('../refs.json'));have={r['id'] for r in RM}
for r in NEW:
    if r['id'] not in have:RM.append(r)
json.dump(RM,open('../refs.json','w'),ensure_ascii=False,indent=1)
R=[r for r in RM if r['id'] in works]
json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('../meta.json'))
m.update({"title":"겉모습이 달라도 같은 것은 같게 — 모든 데이터는 숫자가 된다 3장","number":"D2N-3","about":[C+'cosine-similarity',M+'augmentation-contrastive',M+'triplet-loss',C+'goal-defines-invariance',C+'joint-embedding-space'],"basedOn":[r['id'] for r in R],"url":"https://adminmrobo.github.io/data_to_numbers_lab/03_same_despite_looks.html","suggestedCitation":"안상선 (2026). 겉모습이 달라도 같은 것은 같게 — 모든 데이터는 숫자가 된다 3장. 연구실 해설, v1.0."})
json.dump(m,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E),len(R))
