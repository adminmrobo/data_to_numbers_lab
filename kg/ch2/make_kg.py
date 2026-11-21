import json
PG='data_to_numbers_02'
N=[];E=[]
def node(id,t,ko,en,anchor,level=1,cov='explained',fam='ml-basics',defi=None,src=None):
    n={"id":id,"type":t,"label":{"ko":ko,"en":en},"page":PG,"anchor":anchor,"level":level,"status":"known","confidence":"high","coverage":cov,"family":fam,"match":[],"domain":["ai"]}
    if defi:n["definition"]={"ko":defi}
    if src:n["source"]=[{"ref":r,"loc":""} for r in src]
    N.append(n)
def e(s,p,o,a):E.append({"s":s,"p":"lab:"+p,"o":o,"anchor":a,"confidence":"high"})
C='lab:concept/';M='lab:method/';L='lab:limitation/';CL='lab:claim/';S='lab:simulation/';T='lab:topic/'
node(C+'rgb-channel','Concept','RGB 채널','RGB channels','#s1',1,fam='vision',defi='컬러 점 하나를 빨강·초록·파랑 숫자 셋으로 적는다. 색 하나의 숫자 판이 채널')
node(M+'grayscale','Method','흑백 변환 (가중 평균)','Grayscale conversion','#s1',1,fam='vision',defi='0.299R + 0.587G + 0.114B')
node(C+'frame-difference','Concept','장면 사이 차이','Frame difference','#s2',1,fam='vision',defi='지금 장면에서 앞 장면을 빼면 움직인 곳만 남는다')
node(C+'video-tensor','Concept','영상의 숫자 (장면×가로×세로×색)','Video as array','#s2',1,fam='vision')
node(M+'longest-match-tokenize','Method','가장 긴 조각부터 맞추는 토큰화','Longest-match tokenization','#s3',1,fam='language',defi='어휘에서 가장 긴 조각부터 찾고, 없는 글자는 한 글자씩 번호를 붙인다')
node(C+'one-hot','Concept','원-핫','One-hot encoding','#s3',1,fam='language',defi='어휘 수만큼 긴 줄에서 제 번호 자리에만 1')
node(C+'spectrogram','Concept','스펙트로그램','Spectrogram','#s4',1,fam='sequence',defi='짧은 창마다 높낮이별 세기를 재 시간×높낮이 그림으로 펼친 것')
node(C+'window-tradeoff','Concept','창 길이의 맞바꿈 (시간 vs 높낮이)','Time-frequency trade-off','#s4',2,fam='sequence',defi='높낮이 간격 = 1초에 재는 횟수 ÷ 창 길이')
node(C+'label-encoding','Concept','정답의 숫자: 번호·상자·마스크','Label encoding','#s5',1,defi='분류는 번호 1개, 위치는 상자 4개, 영역은 마스크')
node(C+'iou','Concept','IoU (겹침 비율)','Intersection over Union','#s5',2,fam='evaluation',defi='겹친 넓이 ÷ 합친 넓이')
node(M+'standardize','Method','표준화 (z점수)','Standardization','#s6',1,defi='평균을 빼고 표준편차로 나눠 전체 밝기·대비를 지운다')
node(M+'scale01','Method','0~1로 나누기','Min-max scaling to 0–1','#s6',1)
node(C+'patching','Concept','조각으로 잘라 숫자 줄로 펼치기','Patch flattening','#s7',2,fam='attention',defi='p×p 조각을 한 줄로 펼친다. 조각 수 (한 변 ÷ p)², 조각 하나 p×p×색 수')
node(M+'color-rule','Method','색 규칙 판정 (빨강 − 초록 > 기준)','Hand-written color rule','#s8',1)
node(L+'gray-loses-color','Limitation','흑백은 색 정보를 버린다','Grayscale discards color','#s1',1)
node(L+'onehot-sparse','Limitation','원-핫은 길고 거의 다 0이다','One-hot is long and sparse','#s3',1)
node(L+'small-object-iou','Limitation','작은 물체는 조금만 어긋나도 IoU가 크게 떨어진다','Small objects are sensitive to box offset','#s5',2)
node(L+'z-erases-brightness','Limitation','표준화는 밝기 자체를 지운다','Standardization erases absolute brightness','#s6',2)
node(L+'rule-ceiling','Limitation','색 규칙은 어떤 기준으로도 62.5%가 한계','Color rule ceiling 62.5%','#s8',1)
src={'vit':'dosovitskiy2021image','vivit':'arnab2021vivit','bpe':'sennrich2016neural','w2v':'mikolov2013efficient','wav2vec':'baevski2020wav2vec','ast':'gong2021ast'}
node(CL+'vit-patches','Claim','사진을 16×16 조각 줄로 읽는 순수 트랜스포머','ViT reads 16×16 patch sequences','#s7',2,src=[src['vit']])
node(CL+'vivit-tokens','Claim','영상에서 시간·공간 토큰을 뽑는다','Spatio-temporal tokens','#s2',2,src=[src['vivit']])
node(CL+'bpe-compression','Claim','압축 알고리즘 BPE를 단어 쪼개기에 응용','BPE adapted for word segmentation','#s3',2,src=[src['bpe']])
node(CL+'w2v-analogy','Claim','왕 − 남자 + 여자 ≈ 여왕','King − man + woman ≈ queen','#s3',2,cov='mentioned',src=[src['w2v']])
node(CL+'ast-patches','Claim','스펙트로그램을 16×16 조각으로 잘라 읽는다','AST splits spectrogram into 16×16 patches','#s4',2,src=[src['ast']])
node(CL+'wav2vec-raw','Claim','녹음 파형에서 바로 배운다','Learns from raw waveform','#s4',2,cov='mentioned',src=[src['wav2vec']])
for k,ko,a in [('mix','대시보드 ① 색 섞기','#p1'),('flip','대시보드 ② 플립북','#p2'),('tok','대시보드 ③ 조각 내기','#p3'),('spec','대시보드 ④ 소리 그림','#p4'),('label','대시보드 ⑤ 정답 적기','#p5'),('norm','대시보드 ⑥ 밝기 맞추기','#p6'),('patch','대시보드 ⑦ 조각 내기','#p7'),('rule','대시보드 ⑧ 색 규칙 심사','#p8'),('duel','대결: 원본 vs 표준화','#duel')]:node(S+k,'Simulation',ko,k,a,2)
qt={'s1':M+'grayscale','s2':C+'frame-difference','s3':C+'one-hot','s4':C+'window-tradeoff','s5':C+'iou','s6':M+'standardize','s7':C+'patching','s8':M+'color-rule'}
for s,tgt in qt.items():
    for i in (1,2):
        q='lab:quiz/d2n2-%s-%d'%(s,i);node(q,'QuizItem','%s 확인 퀴즈 %d'%(s,i),'Quiz','#'+s,2,cov='mentioned');e(q,'assesses',tgt,'#'+s)
works=[('dosovitskiy2021image','An Image is Worth 16x16 Words'),('arnab2021vivit','ViViT'),('sennrich2016neural','Subword Units'),('mikolov2013efficient','Word2Vec'),('baevski2020wav2vec','wav2vec 2.0'),('gong2021ast','AST')]
for w,t in works:node('lab:work/'+w,'Work',t,t,'#export',2)
e(C+'rgb-channel','prerequisiteOf',M+'grayscale','#s1');e(C+'rgb-channel','prerequisiteOf',C+'video-tensor','#s2');e(C+'video-tensor','prerequisiteOf',C+'frame-difference','#s2')
e(M+'longest-match-tokenize','prerequisiteOf',C+'one-hot','#s3');e(C+'spectrogram','hasLimitation',C+'window-tradeoff','#s4')
e(C+'label-encoding','prerequisiteOf',C+'iou','#s5');e(M+'scale01','contrastsWith',M+'standardize','#s6');e(C+'patching','relatedTo',C+'spectrogram','#s7')
e(M+'grayscale','hasLimitation',L+'gray-loses-color','#s1');e(C+'one-hot','hasLimitation',L+'onehot-sparse','#s3');e(C+'iou','hasLimitation',L+'small-object-iou','#s5')
e(M+'standardize','hasLimitation',L+'z-erases-brightness','#s6');e(M+'color-rule','hasLimitation',L+'rule-ceiling','#s8')
e(M+'standardize','contrastsWith',M+'color-rule','#duel')
for a,b in [('rgb-channel','convolution'),('frame-difference','convolution'),('video-tensor','convolution'),('one-hot','word-embedding'),('spectrogram','time-series'),('window-tradeoff','time-series'),('label-encoding','supervised-learning'),('iou','object-detection'),('patching','transformer')]:e(C+a,'broader',T+b,'#top')
e(M+'grayscale','broader',T+'feature-engineering','#top');e(M+'longest-match-tokenize','broader',T+'tokenization','#top');e(M+'standardize','broader',T+'normalization-layers','#top');e(M+'scale01','broader',T+'feature-engineering','#top');e(M+'color-rule','broader',T+'rule-vs-learning','#top')
for cl,tgt,w in [('vit-patches',C+'patching','dosovitskiy2021image'),('vivit-tokens',C+'video-tensor','arnab2021vivit'),('bpe-compression',M+'longest-match-tokenize','sennrich2016neural'),('w2v-analogy',C+'one-hot','mikolov2013efficient'),('ast-patches',C+'spectrogram','gong2021ast'),('wav2vec-raw',C+'spectrogram','baevski2020wav2vec')]:
    e(CL+cl,'supports',tgt,'#top');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt,a in [('mix',M+'grayscale','#p1'),('flip',C+'frame-difference','#p2'),('tok',M+'longest-match-tokenize','#p3'),('spec',C+'spectrogram','#p4'),('label',C+'iou','#p5'),('norm',M+'standardize','#p6'),('patch',C+'patching','#p7'),('rule',M+'color-rule','#p8'),('duel',M+'standardize','#duel')]:e(tgt,'demonstratedBy',S+k,a)
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
R=json.load(open('../refs.json'));R=[r for r in R if r['id'] in [w for w,_ in works]]
json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('../meta.json'))
m.update({"title":"숫자로 바꾸는 네 개의 창구 — 모든 데이터는 숫자가 된다 2장","number":"D2N-2","about":[C+'rgb-channel',C+'one-hot',C+'spectrogram',M+'standardize',C+'patching'],"basedOn":[r['id'] for r in R],"url":"https://adminmrobo.github.io/data_to_numbers_lab/02_rules_to_numbers.html","suggestedCitation":"안상선 (2026). 숫자로 바꾸는 네 개의 창구 — 모든 데이터는 숫자가 된다 2장. 연구실 해설, v1.0."})
json.dump(m,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E))
