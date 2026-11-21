import json
PG='data_to_numbers_01'
N=[];E=[]
def node(id,t,ko,en,anchor,level=1,cov='explained',fam='nn-basics',defi=None,src=None):
    n={"id":id,"type":t,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":"high","coverage":cov,"family":fam,"match":[],"domain":["ai"]}
    if defi:n["definition"]={"ko":defi}
    if src:n["source"]=[{"ref":r,"loc":""} for r in src]
    N.append(n)
def e(s,p,o,a):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":"high"})
C='lab:concept/';M='lab:method/';L='lab:limitation/';Q='lab:question/';CL='lab:claim/';S='lab:simulation/';T='lab:topic/'
node(C+'data-as-numbers','Concept','데이터의 숫자화','Data as numbers','#s1',1,defi='사진·영상·글·소리를 정해진 규칙으로 숫자 배열로 바꾸는 일')
node(C+'pixel','Term','픽셀과 밝기 값','Pixel intensity','#s1',1,fam='vision',defi='사진을 이루는 점. 흑백은 숫자 1개(0~255), 컬러는 RGB 숫자 3개')
node(C+'bit-depth','Term','비트 수와 표현 가짓수','Bit depth','#s1',1,defi='k비트로 2^k가지 값을 적는다. 8비트 = 256단계')
node(C+'image-tensor','Concept','사진의 숫자 판 (가로×세로×색)','Image as array','#s2',1,fam='vision',defi='224×224 컬러 사진 = 150,528개 숫자')
node(C+'video-tensor','Concept','영상의 숫자 (장면×가로×세로×색)','Video as array','#s2',2,fam='vision',defi='장면 수만큼 사진을 쌓은 숫자 배열')
node(C+'subword-token','Concept','하위 단어 토큰','Subword token','#s2',1,fam='language',defi='글을 자주 쓰는 조각으로 쪼개 번호를 붙인 단위')
node(C+'audio-sampling','Concept','소리 샘플링','Audio sampling','#s2',1,fam='sequence',defi='소리를 1초에 정해진 횟수만큼 재서 숫자로 적는 일')
node(C+'spectrogram','Term','스펙트로그램','Spectrogram','#s2',2,fam='sequence',defi='소리를 시간×높낮이로 펼친 그림')
node(C+'patch','Concept','조각(패치)으로 자르기','Patching','#s3',2,fam='attention',defi='사진·소리 그림을 16×16 조각으로 잘라 숫자 줄로 만드는 일')
node(C+'embedding','Concept','임베딩 (뜻을 담은 숫자 줄)','Embedding','#s3',2,fam='language',defi='학습으로 다듬어 뜻이 비슷하면 가깝게 놓이는 숫자 줄')
node(C+'softmax','Concept','소프트맥스 (점수 → 확률)','Softmax','#s3',2,defi='점수를 지수함수로 양수로 만든 뒤 합으로 나눠 확률로 바꾸는 계산')
node(C+'encoding-vs-learning','Concept','번역(규칙)과 학습(최적화)의 차이','Encoding vs learning','#s4',1,fam='ml-basics',defi='숫자로 바꾸는 일은 정해진 규칙, 숫자가 뜻을 담게 하는 일은 손실을 줄이는 학습')
node(C+'euclid-distance','Term','두 점 사이 거리','Euclidean distance','#s4',1,fam='math',defi='피타고라스 정리로 재는 두 숫자 줄 사이 거리')
node(M+'contrastive-margin','Method','같은 종류는 가깝게, 다른 종류는 멀게 (대조 손실)','Contrastive margin loss','#s4',2,fam='optimization',defi='같은 종류 거리², 다른 종류 (m−거리)²를 줄이는 손실')
node(C+'gd','Method','경사 하강','Gradient descent','#s4',2,fam='optimization',defi='손실이 줄어드는 방향으로 가중치를 조금씩 고치는 방법')
node(C+'info-loss','Concept','숫자로 바꿀 때 잃는 정보','Information loss in encoding','#s5',1,defi='해상도·밝기 단계·샘플링 횟수만큼만 담기고, 잃은 정보는 되찾을 수 없다')
node(C+'quantization','Term','양자화','Quantization','#s5',2,cov='mentioned',fam='optimization',defi='숫자를 더 적은 비트로 적는 것')
node(L+'raw-numbers-no-meaning','Limitation','원시 숫자는 뜻을 담지 않는다','Raw numbers carry no meaning','#s1',1)
node(L+'too-many-numbers','Limitation','원시 숫자가 너무 많다','Too many raw numbers','#s2',1)
node(L+'prob-among-candidates','Limitation','확률은 후보 중의 비율일 뿐','Probability only among candidates','#s3',2)
node(L+'learns-bias','Limitation','학습은 훈련 데이터의 치우침도 배운다','Learning picks up dataset bias','#s4',2)
node(L+'lost-info-unrecoverable','Limitation','잃은 정보는 되찾을 수 없다','Lost information is unrecoverable','#s5',1)
node(Q+'what-to-keep','Question','과제에 필요한 정보는 어디까지 남기나','How much to keep for the task','#s5',2)
src={'vit':'dosovitskiy2021image','vivit':'arnab2021vivit','bpe':'sennrich2016neural','w2v':'mikolov2013efficient','wav2vec':'baevski2020wav2vec','ast':'gong2021ast','facenet':'schroff2015facenet','dc':'han2016deep'}
node(CL+'vit-patches','Claim','순수 트랜스포머가 이미지 조각의 줄만으로 분류를 잘한다','Pure transformer on image patch sequences classifies well','#s3',2,src=[src['vit']])
node(CL+'vivit-tokens','Claim','영상에서 시간·공간 토큰을 뽑아 트랜스포머로 읽는다','Spatio-temporal tokens from video','#s2',2,src=[src['vivit']])
node(CL+'bpe-subword','Claim','드문 낱말을 하위 단어 조각의 줄로 적는다 (압축 알고리즘 BPE를 응용)','Rare words as subword units via BPE','#s2',2,src=[src['bpe']])
node(CL+'w2v-analogy','Claim','왕 − 남자 + 여자 ≈ 여왕','King − man + woman ≈ queen','#s4',2,src=[src['w2v']])
node(CL+'wav2vec-raw','Claim','녹음 파형에서 바로 음성 표현을 학습한다','Speech representations from raw audio','#s2',2,cov='mentioned',src=[src['wav2vec']])
node(CL+'ast-patches','Claim','스펙트로그램을 16×16 조각으로 잘라 768차원 숫자 줄로 바꾼다','Spectrogram split into 16×16 patches, 768-d embedding','#s3',2,src=[src['ast']])
node(CL+'facenet-128','Claim','얼굴 하나를 128바이트로 표현하고 거리 = 얼굴 유사도','128 bytes per face, distance = similarity','#s3',2,src=[src['facenet']])
node(CL+'deepcomp','Claim','연결 비트를 32에서 5로, AlexNet 240MB → 6.9MB','32→5 bits, AlexNet 240MB→6.9MB','#s5',2,src=[src['dc']])
sims=[('draw','대시보드 ① 그리기판','#p1'),('four','대시보드 ② 네 손님 숫자 세기','#p2'),('funnel','대시보드 ③ 깔때기와 확률','#p3'),('map','대시보드 ④ 학습 지도','#p4'),('shrink','대시보드 ⑤ 줄이기 실험실','#p5'),('duel','대결: 원시 숫자 vs 다듬은 숫자','#duel')]
for k,ko,a in sims:node(S+k,'Simulation',ko,k,a,2)
quizt={'s1':C+'pixel','s2':C+'subword-token','s3':C+'softmax','s4':C+'euclid-distance','s5':C+'info-loss','s6':C+'encoding-vs-learning'}
for s,tgt in quizt.items():
    for i in (1,2):
        qid='lab:quiz/d2n1-%s-%d'%(s,i);node(qid,'QuizItem','%s 확인 퀴즈 %d'%(s,i),'Quiz %s-%d'%(s,i),'#'+s,2,cov='mentioned');e(qid,'assesses',tgt,'#'+s)
works=[('dosovitskiy2021image','An Image is Worth 16x16 Words'),('arnab2021vivit','ViViT: A Video Vision Transformer'),('sennrich2016neural','Neural Machine Translation of Rare Words with Subword Units'),('mikolov2013efficient','Efficient Estimation of Word Representations in Vector Space'),('baevski2020wav2vec','wav2vec 2.0'),('gong2021ast','AST: Audio Spectrogram Transformer'),('schroff2015facenet','FaceNet'),('han2016deep','Deep Compression')]
for w,t in works:node('lab:work/'+w,'Work',t,t,'#export',2)
# edges
e(C+'data-as-numbers','broader',T+'feature-engineering','#s1')
e(C+'pixel','partOf',C+'data-as-numbers','#s1');e(C+'bit-depth','prerequisiteOf',C+'pixel','#s1')
e(C+'pixel','prerequisiteOf',C+'image-tensor','#s2');e(C+'image-tensor','prerequisiteOf',C+'video-tensor','#s2')
for x in ['image-tensor','video-tensor','subword-token','audio-sampling']:e(C+x,'partOf',C+'data-as-numbers','#s2')
e(C+'subword-token','broader',T+'tokenization','#s2');e(C+'audio-sampling','prerequisiteOf',C+'spectrogram','#s2')
e(C+'data-as-numbers','hasLimitation',L+'raw-numbers-no-meaning','#s1');e(L+'raw-numbers-no-meaning','addressedBy',C+'encoding-vs-learning','#s4')
e(C+'data-as-numbers','hasLimitation',L+'too-many-numbers','#s2');e(L+'too-many-numbers','addressedBy',C+'patch','#s3')
e(C+'patch','prerequisiteOf',C+'embedding','#s3');e(C+'embedding','prerequisiteOf',C+'softmax','#s3');e(C+'patch','broader',T+'transformer','#s3')
e(C+'softmax','hasLimitation',L+'prob-among-candidates','#s3');e(C+'embedding','broader',T+'word-embedding','#s3')
e(C+'euclid-distance','prerequisiteOf',M+'contrastive-margin','#s4');e(M+'contrastive-margin','partOf',C+'encoding-vs-learning','#s4')
e(C+'gd','partOf',C+'encoding-vs-learning','#s4');e(C+'gd','broader',T+'gradient-descent','#s4');e(M+'contrastive-margin','broader',T+'loss-function','#s4')
e(C+'encoding-vs-learning','broader',T+'rule-vs-learning','#s4');e(M+'contrastive-margin','hasLimitation',L+'learns-bias','#s4')
e(C+'encoding-vs-learning','prerequisiteOf',C+'embedding','#s4')
e(C+'info-loss','hasLimitation',L+'lost-info-unrecoverable','#s5');e(C+'info-loss','raises',Q+'what-to-keep','#s5');e(C+'quantization','relatedTo',C+'info-loss','#s5')
e(C+'bit-depth','prerequisiteOf',C+'quantization','#s5')
for cl,tgt,w in [('vit-patches','patch','dosovitskiy2021image'),('vivit-tokens','video-tensor','arnab2021vivit'),('bpe-subword','subword-token','sennrich2016neural'),('w2v-analogy','embedding','mikolov2013efficient'),('wav2vec-raw','audio-sampling','baevski2020wav2vec'),('ast-patches','spectrogram','gong2021ast'),('facenet-128','embedding','schroff2015facenet'),('deepcomp','quantization','han2016deep')]:
    e(CL+cl,'supports',C+tgt,'#s3');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt in [('draw','pixel'),('four','data-as-numbers'),('funnel','softmax'),('map','encoding-vs-learning'),('shrink','info-loss'),('duel','embedding')]:
    e(C+tgt,'demonstratedBy',S+k,'#'+('p1 p2 p3 p4 p5 duel'.split()[['draw','four','funnel','map','shrink','duel'].index(k)]))
e(M+'contrastive-margin','contrastsWith',C+'data-as-numbers','#duel')
for a,b in [('pixel','convolution'),('image-tensor','convolution'),('video-tensor','convolution'),('bit-depth','information-theory'),('audio-sampling','time-series'),('spectrogram','time-series'),('softmax','logistic-regression'),('euclid-distance','knn'),('info-loss','information-theory'),('quantization','information-theory')]:
    e(C+a,'broader',T+b,'#top')
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
def ref(id,typ,title,auth,yr,cont,url,arx=None,doi=None,role='primary'):
    r={"id":id,"type":typ,"title":title,"author":[{"family":a[0],"given":a[1]} if isinstance(a,tuple) else {"literal":a} for a in auth],"issued":{"date-parts":[[yr]]},"URL":url}
    if cont:r["container-title"]=cont
    r["lab"]={"work":"lab:work/"+id,"role":role,"locs":[],"verified":{"title":True,"author":True,"year":True,"container":True,"pages":False,"doi":False},"checkedBy":"arXiv 초록 페이지·학회 페이지와 대조 (2026-11-21)","checkedSource":"external"}
    return r
R=[ref('dosovitskiy2021image','paper-conference','An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale',[('Dosovitskiy','Alexey'),'et al.'],2021,'ICLR 2021','https://arxiv.org/abs/2010.11929'),
 ref('arnab2021vivit','paper-conference','ViViT: A Video Vision Transformer',[('Arnab','Anurag'),'et al.'],2021,'ICCV 2021','https://arxiv.org/abs/2103.15691'),
 ref('sennrich2016neural','paper-conference','Neural Machine Translation of Rare Words with Subword Units',[('Sennrich','Rico'),('Haddow','Barry'),('Birch','Alexandra')],2016,'ACL 2016','https://arxiv.org/abs/1508.07909'),
 ref('mikolov2013efficient','article-journal','Efficient Estimation of Word Representations in Vector Space',[('Mikolov','Tomas'),('Chen','Kai'),('Corrado','Greg'),('Dean','Jeffrey')],2013,'arXiv','https://arxiv.org/abs/1301.3781'),
 ref('baevski2020wav2vec','paper-conference','wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations',[('Baevski','Alexei'),('Zhou','Henry'),('Mohamed','Abdelrahman'),('Auli','Michael')],2020,'NeurIPS 2020','https://arxiv.org/abs/2006.11477'),
 ref('gong2021ast','paper-conference','AST: Audio Spectrogram Transformer',[('Gong','Yuan'),('Chung','Yu-An'),('Glass','James')],2021,'Interspeech 2021','https://arxiv.org/abs/2104.01778'),
 ref('schroff2015facenet','paper-conference','FaceNet: A Unified Embedding for Face Recognition and Clustering',[('Schroff','Florian'),('Kalenichenko','Dmitry'),('Philbin','James')],2015,'CVPR 2015','https://arxiv.org/abs/1503.03832'),
 ref('han2016deep','paper-conference','Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding',[('Han','Song'),('Mao','Huizi'),('Dally','William J.')],2016,'ICLR 2016','https://arxiv.org/abs/1510.00149')]
json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
meta={"title":"사진도, 목소리도, 결국 숫자다 — 모든 데이터는 숫자가 된다 1장","number":"D2N-1","series":"모든 데이터는 숫자가 된다 (연구실 해설)","about":[C+'data-as-numbers',C+'encoding-vs-learning',C+'embedding',C+'info-loss'],"basedOn":[r['id'] for r in R],"educationalLevel":"입문","creator":[{"name":"안상선","role":"author"}],"contributor":[{"name":"AI 보조 제작","role":"assistant"}],"date":"2026-11-21","version":"1.0","language":["ko"],"license":"","url":"https://adminmrobo.github.io/data_to_numbers_lab/01_why_numbers.html","registry":"KG_00_registry 0.2","learningResourceType":"interactive explainer","seeAlso":"","suggestedCitation":"안상선 (2026). 사진도, 목소리도, 결국 숫자다 — 모든 데이터는 숫자가 된다 1장. 연구실 해설, v1.0."}
json.dump(meta,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E))
