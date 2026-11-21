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
NEW=[A('hendrycks2019benchmarking',[('Hendrycks','Dan'),('Dietterich','Thomas')],2019,'Benchmarking Neural Network Robustness to Common Corruptions and Perturbations','ICLR 2019','https://arxiv.org/abs/1903.12261'),
 A('koh2021wilds',[('Koh','Pang Wei'),('Sagawa','Shiori')],2021,'WILDS: A Benchmark of in-the-Wild Distribution Shifts','ICML 2021','https://arxiv.org/abs/2012.07421'),
 A('goodfellow2015explaining',[('Goodfellow','Ian J.'),('Shlens','Jonathon'),('Szegedy','Christian')],2015,'Explaining and Harnessing Adversarial Examples','ICLR 2015','https://arxiv.org/abs/1412.6572'),
 A('carlini2018audio',[('Carlini','Nicholas'),('Wagner','David')],2018,'Audio Adversarial Examples: Targeted Attacks on Speech-to-Text','IEEE S&P Workshops 2018','https://arxiv.org/abs/1801.01944'),
 A('jin2020bert',[('Jin','Di'),('Jin','Zhijing'),('Zhou','Joey Tianyi'),('Szolovits','Peter')],2020,'Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment','AAAI 2020','https://arxiv.org/abs/1907.11932'),
 A('greshake2023not',[('Greshake','Kai'),('Abdelnabi','Sahar')],2023,"Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection",'AISec 2023','https://arxiv.org/abs/2302.12173'),
 A('rossler2019faceforensics',[('Rössler','Andreas'),('Cozzolino','Davide'),('Verdoliva','Luisa'),('Riess','Christian'),('Thies','Justus'),('Nießner','Matthias')],2019,'FaceForensics++: Learning to Detect Manipulated Facial Images','ICCV 2019','https://arxiv.org/abs/1901.08971'),
 A('madry2018towards',[('Madry','Aleksander'),('Makelov','Aleksandar')],2018,'Towards Deep Learning Models Resistant to Adversarial Attacks','ICLR 2018','https://arxiv.org/abs/1706.06083')]
node(C+'common-corruption','Concept','흔한 손상 (잡음·흐림·밝기·대비)','Common corruptions','#s1',1,fam='robustness',defi='현장에서 우연히 생기는 입력 손상. 종류×세기별로 정확도를 잰다')
node(C+'snr-db','Concept','신호 대 잡음비 (dB)','Signal-to-noise ratio','#s2',1,fam='sequence',defi='10 × log₁₀(신호 세기 ÷ 잡음 세기)')
node(M+'longer-window','Method','더 오래 듣기 (평균으로 잡음 줄이기)','Longer integration window','#s2',1,fam='sequence',defi='n번 평균하면 잡음 흔들림이 1/√n')
node(C+'label-noise','Concept','정답 잡음 (틀린 라벨)','Label noise','#s3',1,defi='훈련 정답의 일부가 틀린 상태')
node(M+'knn-vote','Method','k-최근접 다수결','k-nearest-neighbour voting','#s3',1)
node(C+'distribution-shift','Concept','환경 변화 (분포 이동)','Distribution shift','#s4',1,fam='robustness',defi='훈련한 곳과 쓰는 곳의 자료 분포가 다름')
node(C+'spurious-correlation','Concept','우연한 엮임 (지름길 단서)','Spurious correlation','#s4',2,fam='robustness')
node(M+'multi-site-training','Method','여러 곳의 데이터로 학습','Multi-site training','#s4',1,fam='robustness')
node(C+'adversarial-example','Concept','적대적 변조','Adversarial example','#s5',2,fam='robustness',defi='판정을 뒤집도록 약한 방향으로 넣은 작은 변조')
node(M+'fgsm','Method','FGSM (기울기 부호 공격)','Fast Gradient Sign Method','#s5',2,fam='robustness',defi='모든 픽셀을 점수가 깎이는 부호 방향으로 ε씩')
node(M+'word-substitution-attack','Method','비슷한 낱말 바꿔치기 공격','Word substitution attack','#s6',2,fam='language')
node(C+'prompt-injection','Concept','간접 프롬프트 주입','Indirect prompt injection','#s7',2,fam='language',defi='AI가 읽어 온 자료 속 지시문으로 시키지 않은 일을 하게 함')
node(M+'data-instruction-separation','Method','자료와 명령 나누기 + 행동 확인','Separating data from instructions','#s7',1,fam='language')
node(M+'adversarial-training','Method','적대적 학습','Adversarial training','#s8',2,fam='robustness',defi='min 평균[max 손실(그림 + 변조)]')
node(C+'deepfake-detection','Concept','가짜 얼굴 영상 탐지','Deepfake detection','#s9',2,fam='vision')
node(L+'noise-destroys-info','Limitation','잡음이 신호 차이보다 크면 한 장 안의 정보가 묻힌다','Noise beyond signal destroys information','#s1',1)
node(L+'latency-tradeoff','Limitation','오래 들으면 판단이 늦어진다','Longer window adds latency','#s2',1)
node(L+'majority-fails-high-noise','Limitation','틀린 정답이 절반에 가까우면 다수결도 흔들린다','Voting fails at high label noise','#s3',1)
node(L+'shortcut-collapse','Limitation','지름길 단서는 다른 환경에서 무너진다','Shortcuts collapse under shift','#s4',1)
node(L+'robust-accuracy-tradeoff','Limitation','학습용 변조가 크면 깨끗한 정확도가 떨어진다','Robustness–accuracy trade-off','#s8',2)
node(L+'compression-erases-traces','Limitation','압축이 조작 흔적을 지운다','Compression erases manipulation traces','#s9',1)
node(L+'no-complete-injection-defense','Limitation','프롬프트 주입에는 아직 완벽한 방어가 없다','No complete defense against injection','#s7',2)
s={'c':'hendrycks2019benchmarking','w':'koh2021wilds','g':'goodfellow2015explaining','a':'carlini2018audio','t':'jin2020bert','p':'greshake2023not','f':'rossler2019faceforensics','m':'madry2018towards'}
node(CL+'imagenetc-75','Claim','흔한 손상 15종류 × 세기 5단계 = 75가지 조건','15 corruptions × 5 severities','#s1',2,src=[s['c']])
node(CL+'wilds-10','Claim','실제 환경 변화 자료 10가지','10 in-the-wild datasets','#s4',2,src=[s['w']])
node(CL+'fgsm-panda','Claim','픽셀당 0.007 변조로 판다 57.7% → 긴팔원숭이 99.3%','Panda to gibbon with ε = 0.007','#s5',2,src=[s['g']])
node(CL+'fgsm-linearity','Claim','적대적 예제는 모델이 너무 직선적이라 생긴다','Linearity explains adversarial examples','#s5',2,src=[s['g']])
node(CL+'audio-999','Claim','99.9% 비슷한 녹음으로 원하는 문장을 받아 적게 함','99.9% similar audio, targeted transcription','#s6',2,src=[s['a']])
node(CL+'textfooler','Claim','비슷한 낱말 바꿔치기로 BERT 등 분류를 속임','Synonym substitution fools BERT','#s6',2,src=[s['t']])
node(CL+'injection-boundary','Claim','자료와 명령의 경계가 흐려지는 것이 핵심 문제','Blurred line between data and instructions','#s7',2,src=[s['p']])
node(CL+'madry-minmax','Claim','방어를 가장 나쁜 경우 손실을 줄이는 min-max 문제로 정리','Robust optimisation view','#s8',2,src=[s['m']])
node(CL+'ffpp-1.8m','Claim','영상 1,000개·조작 방법 4가지·조작 그림 180만 장 이상, 압축이 탐지를 어렵게 함','FaceForensics++ scale and compression','#s9',2,src=[s['f']])
for k,ko,a in [('corrupt','대시보드 ① 손상 시험장','#p1'),('tone','대시보드 ② 시끄러운 공장','#p2'),('label','대시보드 ③ 틀린 정답 섞기','#p3'),('hosp','대시보드 ④ 두 병원','#p4'),('fgsm','대시보드 ⑤ 적대적 변조','#p5'),('text','대시보드 ⑥ 후기 바꿔치기','#p6'),('agent','대시보드 ⑦ 장난감 비서','#p7'),('advtrain','대시보드 ⑧ 적대적 학습','#p8'),('fake','대시보드 ⑨ 가짜 영상 탐지기','#p9'),('duel','대결: 깨끗한 그림 두 배 vs 적대적 학습','#duel')]:node(S+k,'Simulation',ko,k,a,2)
qt={'s1':C+'common-corruption','s2':C+'snr-db','s3':M+'knn-vote','s4':C+'distribution-shift','s5':M+'fgsm','s6':M+'word-substitution-attack','s7':C+'prompt-injection','s8':M+'adversarial-training','s9':C+'deepfake-detection'}
for st,tgt in qt.items():
    for i in (1,2):
        q='lab:quiz/d2n4-%s-%d'%(st,i);node(q,'QuizItem','%s 확인 퀴즈 %d'%(st,i),'Quiz','#'+st,2,cov='mentioned');e(q,'assesses',tgt,'#'+st)
works=[r['id'] for r in NEW]
for w in works:node('lab:work/'+w,'Work',w,w,'#export',2)
e(C+'snr-db','prerequisiteOf',M+'longer-window','#s2');e(C+'label-noise','prerequisiteOf',M+'knn-vote','#s3');e(C+'spurious-correlation','relatedTo',C+'distribution-shift','#s4')
e(M+'multi-site-training','relatedTo',C+'distribution-shift','#s4');e(C+'common-corruption','contrastsWith',C+'adversarial-example','#s5');e(M+'fgsm','relatedTo',C+'adversarial-example','#s5')
e(M+'fgsm','prerequisiteOf',M+'adversarial-training','#s8');e(M+'word-substitution-attack','relatedTo',C+'adversarial-example','#s6');e(M+'data-instruction-separation','relatedTo',C+'prompt-injection','#s7')
e(C+'common-corruption','relatedTo',C+'deepfake-detection','#s9')
for a,b in [(C+'common-corruption',L+'noise-destroys-info'),(M+'longer-window',L+'latency-tradeoff'),(M+'knn-vote',L+'majority-fails-high-noise'),(C+'spurious-correlation',L+'shortcut-collapse'),(M+'adversarial-training',L+'robust-accuracy-tradeoff'),(C+'deepfake-detection',L+'compression-erases-traces'),(M+'data-instruction-separation',L+'no-complete-injection-defense')]:e(a,'hasLimitation',b,'#top')
for a,b in [(C+'common-corruption','distribution-shift'),(C+'snr-db','time-series'),(M+'longer-window','time-series'),(C+'label-noise','data-splitting'),(M+'knn-vote','knn'),(C+'distribution-shift','distribution-shift'),(C+'spurious-correlation','generalization'),(M+'multi-site-training','generalization'),(C+'adversarial-example','ai-safety'),(M+'fgsm','gradient-descent'),(M+'word-substitution-attack','ai-safety'),(C+'prompt-injection','prompting'),(M+'data-instruction-separation','ai-safety'),(M+'adversarial-training','loss-function'),(C+'deepfake-detection','ai-safety'),(L+'robust-accuracy-tradeoff','accuracy-metrics')]:e(a,'broader',T+b,'#top')
for cl,tgt,w in [('imagenetc-75',C+'common-corruption',s['c']),('wilds-10',C+'distribution-shift',s['w']),('fgsm-panda',C+'adversarial-example',s['g']),('fgsm-linearity',M+'fgsm',s['g']),('audio-999',M+'word-substitution-attack',s['a']),('textfooler',M+'word-substitution-attack',s['t']),('injection-boundary',C+'prompt-injection',s['p']),('madry-minmax',M+'adversarial-training',s['m']),('ffpp-1.8m',C+'deepfake-detection',s['f'])]:
    e(CL+cl,'supports',tgt,'#top');e(CL+cl,'assertedIn','lab:work/'+w,'#export')
for k,tgt in [('corrupt',C+'common-corruption'),('tone',M+'longer-window'),('label',M+'knn-vote'),('hosp',C+'distribution-shift'),('fgsm',M+'fgsm'),('text',M+'word-substitution-attack'),('agent',C+'prompt-injection'),('advtrain',M+'adversarial-training'),('fake',C+'deepfake-detection'),('duel',M+'adversarial-training')]:e(tgt,'demonstratedBy',S+k,'#top')
json.dump({"version":"1.0","page":PG,"nodes":N,"edges":E},open('kg.json','w'),ensure_ascii=False,indent=1)
RM=json.load(open('../refs.json'));have={r['id'] for r in RM}
for r in NEW:
    if r['id'] not in have:RM.append(r)
json.dump(RM,open('../refs.json','w'),ensure_ascii=False,indent=1)
R=[r for r in RM if r['id'] in works];json.dump(R,open('refs.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('../meta.json'))
m.update({"title":"잡음이 섞였을 때 — 모든 데이터는 숫자가 된다 4장","number":"D2N-4","about":[C+'common-corruption',C+'distribution-shift',C+'adversarial-example',C+'prompt-injection',M+'adversarial-training'],"basedOn":works,"url":"https://adminmrobo.github.io/data_to_numbers_lab/04_noise_and_attacks.html","suggestedCitation":"안상선 (2026). 잡음이 섞였을 때 — 모든 데이터는 숫자가 된다 4장. 연구실 해설, v1.0."})
json.dump(m,open('meta.json','w'),ensure_ascii=False,indent=1)
print(len(N),len(E),len(R))
