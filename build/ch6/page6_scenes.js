
/* ---------- 실전 연습장 공용 ---------- */
var MIS={},touched={desk:false,inspect:false,security:false,moving:false};
function pct(x){return fmt(x*100,1)+'%';}
function setLive(id,lines){var box=$('#'+id);if(!box)return;
  box.innerHTML=lines.map(function(l){return '<div class="say" data-who="'+l[0]+'"><img class="who" data-who="'+l[0]+'" data-mood="'+l[1]+'" alt="" aria-hidden="true"><div><b class="name">'+NAMES[l[0]]+'</b><p>'+l[2]+'</p></div></div>';}).join('');
  Cast.fill(box);}
var NAMES={doc:'박사',asst:'조수 (하루)',fly:'초파리 연구원',robo:'주판봇',sia:'시아',moa:'모아',x1:'X1',x2:'X2',x3:'X3'};
function kpi(id,val,cls){var e=$('#'+id);if(!e)return;e.textContent=val;var p=e.parentNode;p.className='kpi '+(cls||'i');}
function renderMis(sc){var box=$('#mis-'+sc);if(!box)return;var L=MIS[sc];
  box.innerHTML=L.map(function(m,i){return '<li class="'+(m.done?'done':'')+'"><span class="mk" aria-hidden="true">'+(m.done?'✔':(i+1))+'</span><div><b>'+m.kind+'</b> '+m.txt+(m.done?'<div class="ok">'+m.ok+'</div>':'')+'</div></li>';}).join('');
  var n=0,t=0;Object.keys(MIS).forEach(function(k){MIS[k].forEach(function(m){t++;if(m.done)n++;});});
  var g=$('#misTotal');if(g)g.textContent=n+' / '+t;var gs=$('#misBar');if(gs)gs.style.width=(100*n/t)+'%';
  updStudy();}
function checkMis(sc,st){if(!touched[sc])return;var ch=false;MIS[sc].forEach(function(m){if(!m.done&&m.check(st)){m.done=true;ch=true;}});if(ch)renderMis(sc);}
function bindGroup(sel,attr,fn){var bs=$$(sel);bs.forEach(function(b){b.addEventListener('click',function(){setPressed(bs,b);fn(b.getAttribute(attr));});});}
function lineAxes(c,W,H,pad,xl,yl,ymax,xs){c.strokeStyle=COL.rule;c.lineWidth=1;c.beginPath();c.moveTo(pad.l,pad.t);c.lineTo(pad.l,H-pad.b);c.lineTo(W-pad.r,H-pad.b);c.stroke();
  font(c,12);c.fillStyle=COL.muted;c.fillText(yl,pad.l,pad.t-8);var tw=c.measureText(xl).width;c.fillText(xl,W-pad.r-tw,H-6);}

/* ===================== 장면 A · 접수 창구 ===================== */
var SA={type:'photo',B:100000,photo:{side:224,color:3},video:{side:64,color:3,fps:30,dur:2},text:{tok:128,dim:768},sound:{sec:1,rate:16000}};
var TYPEN={photo:'사진',video:'영상',text:'글',sound:'소리'};
var MAINV={photo:['side','한 변(점)',8,320],video:['side','한 변(점)',8,320],text:['tok','토큰 수',1,400],sound:['sec','길이(초)',1,10]};
MIS.desk=[
 {kind:'① 가장 큰 값 찾기',txt:'예산 10만 개, 컬러 사진에서 예산을 넘지 않는 가장 큰 한 변을 찾으세요.',ok:'한 변 182점: 182 × 182 × 3 = 99,372개. 183이면 100,467개로 넘칩니다.',
  check:function(s){return s.type==='photo'&&s.B===100000&&s.photo.color===3&&s.photo.side===182;}},
 {kind:'② 함정 피하기',txt:'예산 10만 개, 컬러 영상(1초에 30장, 2초)에서 예산 안 가장 큰 한 변을 찾으세요. 사진에서 찾은 182를 그대로 넣으면 어떻게 될까요?',ok:'한 변 23점: 23 × 23 × 3 × 60 = 95,220개. 182를 넣으면 약 596만 개로 60배를 넘칩니다.',
  check:function(s){return s.type==='video'&&s.B===100000&&s.video.color===3&&s.video.fps===30&&s.video.dur===2&&s.video.side===23;}},
 {kind:'③ 조건 바꾸기',txt:'예산을 20만 개로 두 배 늘리면 컬러 사진의 한 변도 두 배가 될까요? 직접 찾아 보세요.',ok:'한 변 258점(182의 약 1.42배). 넓이가 두 배면 한 변은 √2 ≈ 1.41배만 늘어납니다.',
  check:function(s){return s.type==='photo'&&s.B===200000&&s.photo.color===3&&s.photo.side===258;}}
];
(function(){
  var cv1=$('#cA1'),cv2=$('#cA2'),sl=$('#aMain'),lab=$('#aMainL'),val=$('#aMainV');
  function cur(){return SA[SA.type];}
  function syncCtrl(){var m=MAINV[SA.type],s=cur();sl.min=m[2];sl.max=m[3];sl.value=s[m[0]];lab.textContent=m[1];val.textContent=num(s[m[0]]);
    $$('[data-agrp]').forEach(function(g){g.hidden=g.getAttribute('data-agrp').split(' ').indexOf(SA.type)<0;});
    $$('[data-acol]').forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-acol')===(s.color||0)));});
    $$('[data-afps]').forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-afps')===SA.video.fps));});
    $$('[data-adur]').forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-adur')===SA.video.dur));});
    $$('[data-adim]').forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-adim')===SA.text.dim));});
    $$('[data-arate]').forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-arate')===SA.sound.rate));});}
  function setMain(v){var m=MAINV[SA.type];v=Math.max(m[2],Math.min(m[3],Math.round(v)));cur()[m[0]]=v;}
  sl.addEventListener('input',function(){touched.desk=true;setMain(+sl.value);upd();});
  $$('[data-astep]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;var m=MAINV[SA.type];setMain(cur()[m[0]]+(+b.getAttribute('data-astep')));syncCtrl();upd();});});
  bindGroup('[data-atype]','data-atype',function(v){touched.desk=true;SA.type=v;syncCtrl();upd();});
  bindGroup('[data-abud]','data-abud',function(v){touched.desk=true;SA.B=+v;upd();});
  $$('[data-acol]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;cur().color=+b.getAttribute('data-acol');syncCtrl();upd();});});
  $$('[data-afps]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;SA.video.fps=+b.getAttribute('data-afps');syncCtrl();upd();});});
  $$('[data-adur]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;SA.video.dur=+b.getAttribute('data-adur');syncCtrl();upd();});});
  $$('[data-adim]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;SA.text.dim=+b.getAttribute('data-adim');syncCtrl();upd();});});
  $$('[data-arate]').forEach(function(b){b.addEventListener('click',function(){touched.desk=true;SA.sound.rate=+b.getAttribute('data-arate');syncCtrl();upd();});});
  function draw1(){var F=fit(cv1),c=F.c,W=F.W,H=F.H;grid(c,W,H);var m=MAINV[SA.type],s=JSON.parse(JSON.stringify(cur())),pad={l:58,r:16,t:30,b:30};
    var lo=m[2],hi=m[3],ys=[],ymax=SA.B*2.2;for(var v=lo;v<=hi;v++){s[m[0]]=v;ys.push(countNums(SA.type,s));}
    function X(v){return pad.l+(v-lo)/(hi-lo)*(W-pad.l-pad.r);}function Y(n){return H-pad.b-n/ymax*(H-pad.t-pad.b);}
    lineAxes(c,W,H,pad,m[1],'숫자 개수');
    font(c,11);c.fillStyle=COL.muted;[0,0.5,1,1.5,2].forEach(function(k){var n=SA.B*k;c.fillText(num(n),4,Y(n)+4);});
    c.setLineDash([6,4]);c.strokeStyle=COL.eye;c.lineWidth=2;c.beginPath();c.moveTo(pad.l,Y(SA.B));c.lineTo(W-pad.r,Y(SA.B));c.stroke();c.setLineDash([]);
    font(c,12,700);c.fillStyle=COL.eye;c.fillText('예산 '+num(SA.B)+'개',W-pad.r-110,Y(SA.B)-6);
    c.save();c.beginPath();c.rect(pad.l,pad.t,W-pad.l-pad.r,H-pad.t-pad.b);c.clip();c.strokeStyle=COL.info;c.lineWidth=2.5;c.beginPath();ys.forEach(function(n,i){var x=X(lo+i),y=Y(n);if(i)c.lineTo(x,y);else c.moveTo(x,y);});c.stroke();c.restore();
    var best=Math.min(hi,maxFit(SA.type,cur(),SA.B));if(best>=lo){c.fillStyle=COL.gfp;c.beginPath();c.arc(X(best),Y(ys[best-lo]),6,0,7);c.fill();font(c,12,700);c.fillText('예산 안 최대 '+best,Math.min(X(best)+8,W-130),Y(ys[best-lo])+18);}
    var me=cur()[m[0]],n=countNums(SA.type,cur()),yn=Math.max(pad.t,Y(n));c.fillStyle=n>SA.B?COL.eye:COL.text;c.beginPath();c.arc(X(me),yn,7,0,7);c.fill();c.strokeStyle='#fff';c.lineWidth=2;c.stroke();
    font(c,12,700);c.fillText('내 선택',Math.min(X(me)+10,W-70),Math.max(yn-10,pad.t+12));
    if(n>ymax){font(c,12,700);c.fillStyle=COL.eye;c.fillText('↑ 그래프 위로 넘침',Math.min(X(me)+10,W-130),pad.t+28);}
    stamp(c,W,'계산 값');}
  function draw2(){var F=fit(cv2),c=F.c,W=F.W,H=F.H;grid(c,W,H);font(c,13,700);c.fillStyle=COL.text;c.fillText('네 가지 데이터의 숫자 개수 (예산 = 100%)',14,24);
    var x0=70,w=W-x0-90;['photo','video','text','sound'].forEach(function(t,i){var n=countNums(t,SA[t]),r=n/SA.B,y=48+i*52;
      font(c,13,t===SA.type?700:400);c.fillStyle=t===SA.type?COL.info:COL.text;c.fillText(TYPEN[t],14,y+15);
      c.fillStyle='#eef2f6';c.fillRect(x0,y,w,20);c.fillStyle=r>1?COL.eye:COL.gfp;c.fillRect(x0,y,w*Math.min(1,r/3),20);
      c.strokeStyle=COL.eye;c.setLineDash([4,3]);c.beginPath();c.moveTo(x0+w/3,y-4);c.lineTo(x0+w/3,y+24);c.stroke();c.setLineDash([]);
      font(c,12,700);c.fillStyle=COL.text;c.fillText(r>=10?fmt(r,0)+'배':fmt(r*100,0)+'%',x0+w+6,y+15);
      font(c,11);c.fillStyle=COL.muted;c.fillText(num(n)+'개',x0+4,y+34);});
    font(c,11);c.fillStyle=COL.eye;c.fillText('예산선',x0+w/3-16,H-8);stamp(c,W,'계산 값');}
  function upd(){var s=cur(),m=MAINV[SA.type],n=countNums(SA.type,s),best=maxFit(SA.type,s,SA.B);val.textContent=num(s[m[0]]);sl.value=s[m[0]];
    kpi('kA1',num(n)+'개',n>SA.B?'r':'g');kpi('kA2',fmt(n/SA.B*100,1)+'%',n>SA.B?'r':'g');kpi('kA3',fmt(n*4/1024,0)+'KB','i');kpi('kA4',num(best)+(SA.type==='sound'?'초':SA.type==='text'?'개':'점'),'a');
    var over=n>SA.B,L=[];
    L.push(['doc',over?'judge':'verdict',over?'예산을 넘었어요. 어느 손잡이를 줄여야 가장 덜 잃을지 생각해 봅시다.':(s[m[0]]===best?'예산을 거의 꽉 채운 가장 큰 값입니다. 하나만 늘려도 넘쳐요.':'예산 안입니다. 아직 여유가 '+num(SA.B-n)+'개 남았어요.')]);
    L.push(['asst','report',TYPEN[SA.type]+' 숫자 '+num(n)+'개, 예산의 '+fmt(n/SA.B*100,1)+'%입니다. 32비트로 적으면 약 '+fmt(n*4/1024,0)+'KB예요.']);
    if(SA.type==='video')L.push(['fly','point','사진 한 장 기준으로 생각하면 안 돼. 1초에 '+SA.video.fps+'장 × '+SA.video.dur+'초 = '+(SA.video.fps*SA.video.dur)+'장을 곱해 봐.']);
    else if(SA.type==='photo'&&SA.B===200000)L.push(['fly','magnify','예산이 두 배면 넓이가 두 배야. 한 변도 두 배일까? 182 × 2 = 364를 넣어 봐.']);
    else L.push(['fly','magnify','한 변을 1만 늘려도 숫자는 줄 하나만큼이 아니라 테두리 전체만큼 늘어. 제곱이니까.']);
    L.push(['robo',SA.B===200000?'coin':'smile',SA.B===200000?'예산이 두 배니까 한 변도 두 배지! 계산할 것도 없어.':'컬러든 흑백이든 사진은 사진이지. 숫자 수는 같겠지?']);
    setLive('liveA',L);
    ins($('#iA'),[[over?'r':'g',over?'<b>예산 초과</b> — '+num(n-SA.B)+'개를 줄여야 합니다. 이 조건에서 예산 안 최댓값은 '+num(best)+'입니다.':'<b>예산 안</b> — 이 조건에서 예산 안 최댓값은 '+num(best)+'입니다.'],
      ['m','<b>계산</b> — '+formulaA(s)]]);
    draw1();draw2();checkMis('desk',SA);}
  function formulaA(s){if(SA.type==='photo')return s.side+' × '+s.side+' × '+s.color+' = '+num(countNums('photo',s));if(SA.type==='video')return s.side+' × '+s.side+' × '+s.color+' × '+s.fps+' × '+s.dur+' = '+num(countNums('video',s));
    if(SA.type==='text')return s.tok+' 토큰 × '+s.dim+' = '+num(countNums('text',s));return s.sec+'초 × '+num(s.rate)+' = '+num(countNums('sound',s));}
  syncCtrl();renderMis('desk');redraws.push(upd);window.__A={upd:upd,S:SA,sync:syncCtrl};
})();

/* ===================== 장면 B · 검수대 ===================== */
var SB={feat:'pixel',ts:0,n:90,test:2};
var TESTB={},MODB={};
function testB(s){if(!TESTB[s])TESTB[s]=setShift(150,77,s);return TESTB[s];}
function featOf(f,x){return f==='filter'?filterFeat(x):x;}
function modelB(f,ts,n){var k=f+ts+'_'+n;if(!MODB[k]){var D=setShift(n,5,ts);MODB[k]=trainLin(f==='filter'?D.map(function(d){return {x:filterFeat(d.x),y:d.y};}):D,{epochs:60});}return MODB[k];}
var ACCB={};function accB(f,ts,n,s){var k=f+ts+'_'+n+'_'+s;if(ACCB[k]==null){var M=modelB(f,ts,n);ACCB[k]=linAcc(M,testB(s),function(d){return featOf(f,d.x);});}return ACCB[k];}
var seenB={};
MIS.inspect=[
 {kind:'① 가장 좋은 설정',txt:'시험 그림이 위아래·좌우로 2점까지 옮겨질 때 정확도 95% 이상이 되는 설정을 찾으세요.',ok:'작은 필터 + 최댓값으로 읽으면 이동 2에서도 98% 안팎입니다. 픽셀 그대로는 어떤 조합도 63%를 넘지 못합니다.',
  check:function(s){return s.test===2&&accB(s.feat,s.ts,s.n,2)>=0.95;}},
 {kind:'② 함정 관찰',txt:'픽셀 그대로, 학습 때 이동 0으로 두고 학습 그림만 270장으로 늘린 뒤 시험 이동 2에서 정확도를 보세요.',ok:'270장으로 세 배 늘려도 40%. 같은 위치의 그림을 더 보여 줘도 옮겨진 그림은 못 알아봅니다(3장 대결과 같은 결론).',
  check:function(s){return s.feat==='pixel'&&s.ts===0&&s.n===270&&s.test===2;}},
 {kind:'③ 조건 바꾸기',txt:'설정 하나를 정하고, 시험 이동 폭을 0·1·2로 모두 바꿔 보세요. 세 경우 모두 95% 이상인 설정을 찾으면 통과입니다.',ok:'세 시험을 모두 지켰습니다. 좋은 설정은 시험 조건이 바뀌어도 결론이 같아야 합니다.',
  check:function(s){var k=s.feat+s.ts+'_'+s.n;return seenB[k]&&seenB[k][0]&&seenB[k][1]&&seenB[k][2];}}
];
var PAD=new Array(64).fill(0);
(function(){
  var cv1=$('#cB1'),cv2=$('#cB2');
  bindGroup('[data-bfeat]','data-bfeat',function(v){touched.inspect=true;SB.feat=v;upd();});
  bindGroup('[data-bts]','data-bts',function(v){touched.inspect=true;SB.ts=+v;upd();});
  bindGroup('[data-bn]','data-bn',function(v){touched.inspect=true;SB.n=+v;upd();});
  bindGroup('[data-btest]','data-btest',function(v){touched.inspect=true;SB.test=+v;upd();});
  function draw1(){var F=fit(cv1),c=F.c,W=F.W,H=F.H;grid(c,W,H);var pad={l:46,r:20,t:52,b:34};
    function X(i){return pad.l+20+i*(W-pad.l-pad.r-40)/2;}function Y(a){return H-pad.b-(a-0.3)/0.7*(H-pad.t-pad.b);}
    lineAxes(c,W,H,pad,'시험 그림 이동 폭','정확도');font(c,11);c.fillStyle=COL.muted;[0.4,0.6,0.8,1].forEach(function(a){c.fillText(fmt(a*100,0)+'%',6,Y(a)+4);});
    [0,1,2].forEach(function(i){font(c,12,i===SB.test?700:400);c.fillStyle=i===SB.test?COL.text:COL.muted;c.fillText(String(i),X(i)-3,H-pad.b+16);});
    c.setLineDash([4,4]);c.strokeStyle=COL.gfp;c.beginPath();c.moveTo(pad.l,Y(0.95));c.lineTo(W-pad.r,Y(0.95));c.stroke();c.setLineDash([]);font(c,11);c.fillStyle=COL.gfp;c.fillText('95%',W-pad.r-28,Y(0.95)-4);
    [['pixel','픽셀 그대로',COL.eye],['filter','작은 필터 + 최댓값',COL.info]].forEach(function(o){var mine=o[0]===SB.feat;
      c.strokeStyle=o[2];c.lineWidth=mine?3:1.5;c.setLineDash(mine?[]:[6,4]);c.beginPath();[0,1,2].forEach(function(i){var y=Y(accB(o[0],SB.ts,SB.n,i));if(i)c.lineTo(X(i),y);else c.moveTo(X(i),y);});c.stroke();c.setLineDash([]);
      [0,1,2].forEach(function(i){var a=accB(o[0],SB.ts,SB.n,i);c.fillStyle=o[2];c.beginPath();c.arc(X(i),Y(a),mine?5:3,0,7);c.fill();if(mine){font(c,12,700);c.fillText(fmt(a*100,1)+'%',X(i)+8,Y(a)-8);}});
      });
    font(c,12,700);c.fillStyle=COL.eye;c.fillText('— 픽셀 그대로',12,20);c.fillStyle=COL.info;c.fillText('— 작은 필터 + 최댓값',120,20);
    stamp(c,W,'설명용 모형');}
  function draw2(){var F=fit(cv2),c=F.c,W=F.W,H=F.H;grid(c,W,H);font(c,13,700);c.fillStyle=COL.text;c.fillText('이동 폭 '+SB.test+'의 시험 그림과 필터 최댓값',12,22);
    var T=testB(SB.test),cell=Math.min(15,(W-60)/3/8-2);
    [0,1,2].forEach(function(cl,i){var d=T.filter(function(t){return t.y===cl;})[SB.test?2:0],x0=14+i*(W-20)/3,y0=36;
      for(var k=0;k<64;k++){var v=d.x[k];var g=Math.round(255-(v-0.3)/0.4*200);g=Math.max(30,Math.min(250,g));c.fillStyle='rgb('+g+','+g+','+g+')';c.fillRect(x0+(k%8)*cell,y0+Math.floor(k/8)*cell,cell-1,cell-1);}
      font(c,12,700);c.fillStyle=COL.text;c.fillText(SHAPES[cl],x0,y0+8*cell+16);
      var fm=filterMax(d.x),names=['가로','세로','대각'],cols=[COL.amber,COL.stain,COL.gfp];
      fm.forEach(function(f,j){var yy=y0+8*cell+26+j*20,bw=(W-40)/3-46,r=Math.max(0,Math.min(1,(f-0.45)/0.2));font(c,11);c.fillStyle=COL.muted;c.fillText(names[j],x0,yy+10);
        c.fillStyle='#eef2f6';c.fillRect(x0+30,yy,bw,12);c.fillStyle=cols[j];c.fillRect(x0+30,yy,bw*r,12);});});
    stamp(c,W,'설명용 모형');}
  function upd(){var a=accB(SB.feat,SB.ts,SB.n,SB.test),a0=accB(SB.feat,SB.ts,SB.n,0),k=SB.feat+SB.ts+'_'+SB.n;
    seenB[k]=seenB[k]||{};if(touched.inspect&&a>=0.95)seenB[k][SB.test]=1;
    kpi('kB1',pct(a),a>=0.95?'g':a>=0.75?'a':'r');kpi('kB2',(a0-a>0.005?'−':'')+fmt(Math.abs(a0-a)*100,1)+'%p',a0-a>0.1?'r':'g');
    kpi('kB3',SB.feat==='filter'?'21개':'195개','i');kpi('kB4',SB.n+'장','m');
    var L=[];
    L.push(['doc',a>=0.95?'verdict':'judge',a>=0.95?'이동 '+SB.test+'에서 '+pct(a)+'. 그림이 옮겨져도 같은 모양을 같게 봅니다.':'이동 '+SB.test+'에서 '+pct(a)+'입니다. 그림이 옮겨지면 무엇이 달라지는지 생각해 봅시다.']);
    L.push(['asst','report','시험 150장 중 '+Math.round(a*150)+'장을 맞혔어요. 이동 0일 때보다 '+fmt(Math.max(0,a0-a)*100,1)+'%p 낮아요.']);
    L.push(['fly',SB.feat==='pixel'?'magnify':'point',SB.feat==='pixel'?'픽셀 그대로면 "몇 번째 점이 밝은가"를 외운 거야. 줄이 한 점만 옮겨져도 완전히 다른 그림이 되지.':'필터가 그림 전체를 훑고 가장 센 값만 남기니까, 줄이 어디 있든 같은 숫자가 나와.']);
    L.push(['robo',SB.n===270?'coin':'smile',SB.n===270?'그림을 270장이나 보여 줬으니 이제 무조건 맞히겠지!':'그림 수만 늘리면 다 해결돼. 데이터가 왕이야!']);
    setLive('liveB',L);
    ins($('#iB'),[[a>=0.95?'g':'r','<b>'+(SB.feat==='filter'?'작은 필터 + 최댓값':'픽셀 그대로')+'</b> · 학습 이동 '+SB.ts+' · '+SB.n+'장 → 시험 이동 '+SB.test+'에서 '+pct(a)],
      ['m','<b>숫자 수</b> — 픽셀 그대로는 그림 하나를 64개 숫자로, 필터는 3개 숫자로 읽습니다. 판정기의 가중치는 '+(SB.feat==='filter'?'3 × 3 + 3 = 12개, 필터 9개를 더해 21개':'64 × 3 + 3 = 195개')+'입니다.']]);
    padPredict();draw1();draw2();checkMis('inspect',SB);}
  /* 그리기판 */
  var pad=$('#padB');pad.innerHTML=PAD.map(function(v,k){return '<button class="px" data-k="'+k+'" aria-label="'+(Math.floor(k/8)+1)+'행 '+(k%8+1)+'열" aria-pressed="false"></button>';}).join('');
  $$('.px',pad).forEach(function(b){b.addEventListener('click',function(){var k=+b.getAttribute('data-k');PAD[k]=PAD[k]?0:1;b.setAttribute('aria-pressed',String(!!PAD[k]));touched.inspect=true;padPredict();});});
  function padSet(arr){PAD=arr.slice();$$('.px',pad).forEach(function(b,k){b.setAttribute('aria-pressed',String(!!PAD[k]));});padPredict();}
  $('#padClear').addEventListener('click',function(){padSet(new Array(64).fill(0));});
  $('#padEx').addEventListener('click',function(){var a=new Array(64).fill(0);for(var x=2;x<8;x++){a[1*8+x]=1;a[2*8+x]=1;}padSet(a);});
  function padPredict(){var on=PAD.reduce(function(s,v){return s+v;},0),out=$('#padOut');if(!on){out.innerHTML='점을 눌러 줄을 그려 보세요. 두 방법이 각각 무엇이라고 보는지 나옵니다.';return;}
    var x=PAD.map(function(v){return v?0.6:0.4;});
    out.innerHTML=[['pixel','픽셀 그대로'],['filter','작은 필터 + 최댓값']].map(function(o){var M=modelB(o[0],SB.ts,SB.n),p=softmax(scores(M,featOf(o[0],x))),bi=p.indexOf(Math.max.apply(null,p));
      return '<div><b>'+o[1]+'</b>: '+SHAPES[bi]+' <span class="muted">('+p.map(function(v,i){return SHAPES[i]+' '+fmt(v*100,0)+'%';}).join(' · ')+')</span></div>';}).join('')+'<div class="muted" style="font-size:13px">지금 고른 학습 설정(이동 '+SB.ts+', '+SB.n+'장)으로 배운 두 판정기입니다.</div>';}
  renderMis('inspect');redraws.push(upd);window.__B={upd:upd,S:SB};
})();

/* ===================== 장면 C · 보안실 ===================== */
var SC={mode:'plain',et:0.05,ns:0.35,ae:0.05};
var MODC={},ACCC={};
function modelC(mode,et){var k=mode+(mode==='adv'?et:'');if(!MODC[k])MODC[k]=trainLin(TR,mode==='noise'?{noise:0.35}:mode==='adv'?{adv:et}:{});return MODC[k];}
function accC(mode,et,kind,v){var k=mode+(mode==='adv'?et:'')+kind+v;if(ACCC[k]==null){var M=modelC(mode,et);ACCC[k]=kind==='clean'?linAcc(M,TE):kind==='noise'?noiseAcc(M,TE,v):advAcc(M,TE,v);}return ACCC[k];}
MIS.security=[
 {kind:'① 가장 좋은 설정',txt:'시험 공격 세기 0.05에서, 깨끗한 정확도 95% 이상을 지키면서 공격 정확도 75% 이상이 되는 학습 방법을 찾으세요.',ok:'공격 섞기(0.05)로 배우면 깨끗 97.8%, 공격 76.7%입니다. 그대로 배운 모델은 공격에 42.2%였습니다.',
  check:function(s){return s.ae===0.05&&accC(s.mode,s.et,'clean')>=0.95&&accC(s.mode,s.et,'adv',0.05)>=0.75;}},
 {kind:'② 함정 관찰',txt:'"잡음 섞기"로 배운 모델에 공격 세기 0.05 이상을 걸어 보세요. 잡음에 강하면 공격에도 강할까요?',ok:'잡음 섞기 모델은 공격 0.05에 45.6%로 그대로 배운 모델(42.2%)과 거의 같습니다. 우연한 잡음과 노린 잡음은 막는 법이 다릅니다.',
  check:function(s){return s.mode==='noise'&&s.ae>=0.05;}},
 {kind:'③ 조건 바꾸기',txt:'공격이 0.08로 세지면 0.05로 배운 모델은 38.9%로 내려갑니다. 이보다 공격 정확도가 높은 학습 설정을 찾고, 그 대가도 확인하세요.',ok:'공격 섞기 0.08로 배우면 40.0%로 조금 낫지만, 깨끗한 정확도가 90.0%로 내려갑니다. 세게 막을수록 평소 실력을 잃습니다.',
  check:function(s){return s.ae===0.08&&accC(s.mode,s.et,'adv',0.08)>0.392;}}
];
(function(){
  var cv1=$('#cC1'),cv2=$('#cC2');
  bindGroup('[data-cmode]','data-cmode',function(v){touched.security=true;SC.mode=v;$('#cEt').hidden=v!=='adv';upd();});
  bindGroup('[data-cet]','data-cet',function(v){touched.security=true;SC.et=+v;upd();});
  bindGroup('[data-cns]','data-cns',function(v){touched.security=true;SC.ns=+v;upd();});
  bindGroup('[data-cae]','data-cae',function(v){touched.security=true;SC.ae=+v;upd();});
  function draw1(){var F=fit(cv1),c=F.c,W=F.W,H=F.H;grid(c,W,H);font(c,13,700);c.fillStyle=COL.text;c.fillText('세 가지 시험: 내 모델 vs 그대로 배운 모델',12,22);
    var T=[['깨끗한 그림','clean',0],['잡음 '+SC.ns,'noise',SC.ns],['공격 '+SC.ae,'adv',SC.ae]],gw=(W-40)/3,bh=H-90;
    T.forEach(function(t,i){var x0=20+i*gw,a=accC(SC.mode,SC.et,t[1],t[2]),b=accC('plain',0,t[1],t[2]);
      [[b,'#b9c3cd','그대로'],[a,COL.info,'내 모델']].forEach(function(o,j){var x=x0+12+j*(gw/2-8),w=gw/2-24,h=bh*o[0];c.fillStyle=o[1];c.fillRect(x,40+bh-h,w,h);
        font(c,12,700);c.fillStyle=COL.text;c.fillText(fmt(o[0]*100,1),x,40+bh-h-6);font(c,11);c.fillStyle=COL.muted;c.fillText(o[2],x,H-30);});
      font(c,12,700);c.fillStyle=COL.text;c.fillText(t[0],x0+12,H-12);});
    stamp(c,W,'설명용 모형');}
  function draw2(){var F=fit(cv2),c=F.c,W=F.W,H=F.H;grid(c,W,H);var pad={l:46,r:18,t:52,b:34},E=[0,0.02,0.03,0.05,0.08,0.1];
    function X(e){return pad.l+e/0.1*(W-pad.l-pad.r);}function Y(a){return H-pad.b-a*(H-pad.t-pad.b);}
    lineAxes(c,W,H,pad,'공격 세기 ε','정확도');font(c,11);c.fillStyle=COL.muted;[0,0.5,1].forEach(function(a){c.fillText(fmt(a*100,0)+'%',6,Y(a)+4);});E.forEach(function(e){c.fillText(String(e),X(e)-8,H-pad.b+16);});
    c.fillStyle='rgba(30,85,200,.08)';c.fillRect(X(SC.ae)-10,pad.t,20,H-pad.t-pad.b);
    [['plain',0,'#9aa6b2','그대로 배운 모델',[6,4]],[SC.mode,SC.et,COL.info,'내 모델',[]]].forEach(function(o){c.strokeStyle=o[2];c.lineWidth=o[4].length?1.8:3;c.setLineDash(o[4]);c.beginPath();
      E.forEach(function(e,i){var a=e?accC(o[0],o[1],'adv',e):accC(o[0],o[1],'clean');if(i)c.lineTo(X(e),Y(a));else c.moveTo(X(e),Y(a));});c.stroke();c.setLineDash([]);});
    font(c,12,700);c.fillStyle=COL.info;c.fillText('— 내 모델',12,20);c.fillStyle='#7d8a96';c.fillText('- - 그대로 배운 모델',84,20);stamp(c,W,'설명용 모형');}
  function upd(){var a0=accC(SC.mode,SC.et,'clean'),a1=accC(SC.mode,SC.et,'noise',SC.ns),a2=accC(SC.mode,SC.et,'adv',SC.ae),av=(a0+a1+a2)/3;
    kpi('kC1',pct(a0),a0>=0.95?'g':'a');kpi('kC2',pct(a1),a1>=0.7?'g':a1>=0.55?'a':'r');kpi('kC3',pct(a2),a2>=0.75?'g':a2>=0.5?'a':'r');kpi('kC4',pct(av),'i');
    var MN={plain:'그대로 배우기',noise:'잡음 섞어 배우기',adv:'공격 섞어 배우기('+SC.et+')'},L=[];
    L.push(['doc',a2>=0.75&&a0>=0.95?'verdict':'think',a2>=0.75&&a0>=0.95?'평소 실력도 지키고 공격도 막았습니다. 다만 어느 세기까지 막는지는 따로 재 봐야 해요.':'공격 '+SC.ae+'에 '+pct(a2)+'. 이 방어가 무엇을 막고 무엇을 못 막는지 나눠 봅시다.']);
    L.push(['asst','report',MN[SC.mode]+': 깨끗 '+pct(a0)+', 잡음 '+pct(a1)+', 공격 '+pct(a2)+'입니다.']);
    L.push(['fly',SC.mode==='noise'?'magnify':'point',SC.mode==='noise'?'잡음은 아무 방향으로나 흔들고, 공격은 가장 약한 방향만 골라 밀어. 연습한 게 다르잖아.':'공격 세기를 배운 값보다 세게 올려 봐. 방어는 배운 세기 근처까지만 막아.']);
    L.push(['robo',SC.mode==='adv'&&SC.et===0.08?'coin':'smile',SC.mode==='adv'&&SC.et===0.08?'가장 센 공격으로 연습했으니 이제 완벽하겠지!':'잡음에 강하게 만들면 공격도 자동으로 막히는 거 아냐?']);
    setLive('liveC',L);
    ins($('#iC'),[[a2>=0.75?'g':a2>=0.5?'a':'r','<b>'+MN[SC.mode]+'</b> → 깨끗 '+pct(a0)+' · 잡음 '+SC.ns+' '+pct(a1)+' · 공격 '+SC.ae+' '+pct(a2)],
      ['m','<b>그대로 배운 모델과 비교</b> — 공격 '+SC.ae+'에서 '+pct(accC('plain',0,'adv',SC.ae))+' → '+pct(a2)+', 깨끗한 그림에서 '+pct(accC('plain',0,'clean'))+' → '+pct(a0)]]);
    draw1();draw2();checkMis('security',SC);}
  renderMis('security');redraws.push(upd);window.__C={upd:upd,S:SC};
})();

/* ===================== 장면 D · 이삿짐 센터 ===================== */
var SD={fr:0,rt:1,bits:32,dev:400};
var DEVN={6240:'X3 노트북',1560:'X2 휴대폰',400:'X1 시계'};
var PRUNED={},COMBO={};
function comboD(fr,rt,bits){if(!fr)rt=0;var k=fr+'_'+rt+'_'+bits;if(!COMBO[k]){var pk=fr+'_'+rt;
    if(!PRUNED[pk]){var P=fr?prune(M0,fr):cloneM(M0);if(fr&&rt)P=finetune(P,TR,20);PRUNED[pk]=P;}
    var P=PRUNED[pk],Q=bits<32?quantize(P,bits):P,nz=nonzero(P);
    COMBO[k]={nz:nz,size:packSize(nz,bits,fr>0),acc:linAcc(Q,TE),noise:noiseAcc(Q,TE,0.35),adv:advAcc(Q,TE,0.05)};}
  return COMBO[k];}
var FRS=[0,0.5,0.7,0.8,0.9,0.95],BITS=[32,8,4,2];
MIS.moving=[
 {kind:'① 가장 좋은 설정',txt:'X1 시계(400비트) 한도 안에 넣으면서 정확도 95% 이상을 지키는 조합을 찾으세요.',ok:'90% 지우고 다시 학습한 뒤 8비트(368비트) 또는 4비트(276비트)로 적으면 97.8%를 지킵니다.',
  check:function(s){var r=comboD(s.fr,s.rt,s.bits);return s.dev===400&&r.size<=400&&r.acc>=0.95;}},
 {kind:'② 함정 관찰',txt:'다시 학습하지 않고 90% 이상을 한 번에 지워 보세요. 크기는 시계에 들어가는데, 정확도는요?',ok:'다시 학습 없이 90%를 지우면 72.2%로 무너집니다(5장 대결의 주판봇 방식). 크기만 보면 통과처럼 보이는 것이 함정입니다.',
  check:function(s){return s.fr>=0.9&&!s.rt&&comboD(s.fr,s.rt,s.bits).acc<0.75;}},
 {kind:'③ 조건 바꾸기',txt:'기기를 X2 휴대폰(1,560비트)으로 바꾸고, 정확도 95% 이상이면서 잡음(0.35) 정확도도 60% 이상인 조합을 찾으세요.',ok:'한도가 넉넉하면 덜 줄여서 잡음 버팀을 지킬 수 있습니다. 시계용 조합(90%)은 잡음에 55.6%였습니다.',
  check:function(s){var r=comboD(s.fr,s.rt,s.bits);return s.dev===1560&&r.size<=1560&&r.acc>=0.95&&r.noise>=0.6;}}
];
(function(){
  var cv1=$('#cD1'),cv2=$('#cD2');
  bindGroup('[data-ddev]','data-ddev',function(v){touched.moving=true;SD.dev=+v;upd();});
  bindGroup('[data-dfr]','data-dfr',function(v){touched.moving=true;SD.fr=+v;upd();});
  bindGroup('[data-drt]','data-drt',function(v){touched.moving=true;SD.rt=+v;upd();});
  bindGroup('[data-dbits]','data-dbits',function(v){touched.moving=true;SD.bits=+v;upd();});
  function draw1(){var F=fit(cv1),c=F.c,W=F.W,H=F.H;grid(c,W,H);var pad={l:46,r:18,t:52,b:34},lo=Math.log10(100),hi=Math.log10(8000);
    function X(s){return pad.l+(Math.log10(s)-lo)/(hi-lo)*(W-pad.l-pad.r);}function Y(a){return H-pad.b-(a-0.4)/0.6*(H-pad.t-pad.b);}
    c.fillStyle='rgba(19,115,58,.08)';c.fillRect(pad.l,pad.t,X(SD.dev)-pad.l,H-pad.t-pad.b);
    lineAxes(c,W,H,pad,'크기(비트, 눈금은 10배씩)','정확도');font(c,11);c.fillStyle=COL.muted;[0.4,0.6,0.8,1].forEach(function(a){c.fillText(fmt(a*100,0)+'%',6,Y(a)+4);});[100,1000].forEach(function(s){c.fillText(num(s),X(s)-10,H-pad.b+16);});
    c.strokeStyle=COL.gfp;c.lineWidth=2;c.setLineDash([6,4]);c.beginPath();c.moveTo(X(SD.dev),pad.t);c.lineTo(X(SD.dev),H-pad.b);c.stroke();c.setLineDash([]);font(c,12,700);c.fillStyle=COL.gfp;c.fillText(DEVN[SD.dev]+' 한도',Math.min(X(SD.dev)+6,W-110),pad.t+14);
    FRS.forEach(function(fr){[0,1].forEach(function(rt){if(!fr&&rt)return;BITS.forEach(function(b){var r=comboD(fr,rt,b);c.fillStyle=rt?'rgba(30,85,200,.45)':'rgba(201,48,44,.45)';c.beginPath();c.arc(X(r.size),Y(r.acc),4,0,7);c.fill();});});});
    var me=comboD(SD.fr,SD.rt,SD.bits);c.fillStyle=COL.text;c.beginPath();c.arc(X(me.size),Y(me.acc),8,0,7);c.fill();c.strokeStyle='#fff';c.lineWidth=2;c.stroke();font(c,12,700);c.fillText('내 조합',Math.min(X(me.size)+10,W-60),Y(me.acc)-8);
    font(c,12,700);c.fillStyle=COL.info;c.fillText('● 다시 학습함',12,20);c.fillStyle=COL.eye;c.fillText('● 다시 학습 안 함',110,20);stamp(c,W,'설명용 모형');}
  function draw2(){var F=fit(cv2),c=F.c,W=F.W,H=F.H;grid(c,W,H);font(c,13,700);c.fillStyle=COL.text;c.fillText('줄인 뒤 세 가지 시험 (4장 시험 다시 걸기)',12,22);
    var o=comboD(0,0,32),m=comboD(SD.fr,SD.rt,SD.bits),T=[['깨끗한 그림','acc'],['잡음 0.35','noise'],['공격 0.05','adv']],gw=(W-40)/3,bh=H-90;
    T.forEach(function(t,i){var x0=20+i*gw;[[o[t[1]],'#b9c3cd','원래'],[m[t[1]],COL.info,'내 조합']].forEach(function(p,j){var x=x0+12+j*(gw/2-8),w=gw/2-24,h=bh*p[0];c.fillStyle=p[1];c.fillRect(x,40+bh-h,w,h);
      font(c,12,700);c.fillStyle=COL.text;c.fillText(fmt(p[0]*100,1),x,40+bh-h-6);font(c,11);c.fillStyle=COL.muted;c.fillText(p[2],x,H-30);});font(c,12,700);c.fillStyle=COL.text;c.fillText(t[0],x0+12,H-12);});
    stamp(c,W,'설명용 모형');}
  function upd(){$('#dRt').hidden=!SD.fr;var r=comboD(SD.fr,SD.rt,SD.bits),fit_=r.size<=SD.dev;
    kpi('kD1',num(r.size)+'비트',fit_?'g':'r');kpi('kD2',fmt(6240/r.size,1)+'배','i');kpi('kD3',pct(r.acc),r.acc>=0.95?'g':r.acc>=0.8?'a':'r');kpi('kD4',pct(r.noise),r.noise>=0.6?'g':'a');
    var L=[];
    L.push(['doc',fit_&&r.acc>=0.95?'verdict':'judge',fit_?(r.acc>=0.95?DEVN[SD.dev]+'에 들어가고 정확도도 지켰습니다. 잡음 시험 결과도 같이 봐 주세요.':'크기는 들어가지만 정확도가 '+pct(r.acc)+'예요. 이대로 내보내면 안 됩니다.'):'아직 '+num(r.size-SD.dev)+'비트가 넘칩니다. 무엇을 더 줄일까요?']);
    L.push(['asst','report','남은 가중치 '+r.nz+'개 + 편향 3개, '+SD.bits+'비트'+(SD.fr?' + 위치 표시 8비트':'')+' → '+num(r.size)+'비트, 원래의 '+fmt(r.size/6240*100,1)+'%예요.']);
    L.push(['fly',SD.fr&&!SD.rt?'magnify':'point',SD.fr&&!SD.rt?'지우고 나서 남은 가중치를 다시 학습 안 했지? 남은 애들이 빈자리를 메울 기회를 줘.':'크기만 보지 말고 "줄인 뒤 세 가지 시험" 그래프의 잡음 막대도 봐. 줄이면 버티는 힘이 달라져.']);
    L.push(['robo',SD.fr>=0.9&&!SD.rt?'happy':'smile',SD.fr>=0.9&&!SD.rt?'한 번에 확 지웠더니 시계에 쏙 들어가네! 끝!':'2비트면 제일 작으니까 제일 좋은 거지?']);
    setLive('liveD',L);
    ins($('#iD'),[[fit_&&r.acc>=0.95?'g':fit_?'a':'r','<b>'+(SD.fr?Math.round(SD.fr*100)+'% 지우기'+(SD.rt?' + 다시 학습':' (다시 학습 없음)'):'지우지 않음')+' · '+SD.bits+'비트</b> → '+num(r.size)+'비트 ('+(fit_?'한도 안':'한도 초과')+'), 정확도 '+pct(r.acc)],
      ['m','<b>계산</b> — ('+r.nz+' + 3) × ('+SD.bits+(SD.fr?' + 8':'')+') = '+num(r.size)+'비트']]);
    draw1();draw2();checkMis('moving',SD);}
  renderMis('moving');redraws.push(upd);window.__D={upd:upd,S:SD};
})();

/* ---------- 장면 고르기 (주소 끝 #desk·#inspect·#security·#moving) ---------- */
var TABS=['desk','inspect','security','moving'];
function openTab(t,scroll){if(TABS.indexOf(t)<0)return;TABS.forEach(function(k){var on=k===t;$('#sc-'+k).hidden=!on;var b=$('#tab-'+k);b.setAttribute('aria-selected',String(on));b.tabIndex=on?0:-1;});
  all();if(scroll){var el=$('#lab');if(el)el.scrollIntoView({behavior:RM?'auto':'smooth'});}}
TABS.forEach(function(k,i){var b=$('#tab-'+k);b.addEventListener('click',function(){openTab(k,false);if(history.replaceState)history.replaceState(null,'','#'+k);});
  b.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();var n=TABS[(i+(e.key==='ArrowRight'?1:3))%4];openTab(n,false);$('#tab-'+n).focus();}});});
function fromHash(){var h=(location.hash||'').slice(1);if(TABS.indexOf(h)>=0)openTab(h,true);}
window.addEventListener('hashchange',fromHash);
$$('[data-goto]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var t=a.getAttribute('data-goto');openTab(t,true);if(history.replaceState)history.replaceState(null,'','#'+t);});});

/* ---------- AI 판단 코너 ---------- */
(function(){
  var C=[
   {q:'사진 예산을 두 배로 늘리면 사진의 한 변도 두 배로 키울 수 있다.',a:'no',w:'아니에요. 숫자 개수는 한 변의 제곱이라, 예산이 두 배면 한 변은 약 1.41배(182 → 258)만 늘어납니다. → 장면 A ③'},
   {q:'같은 위치의 그림을 더 많이 모으면, 옮겨진 그림도 잘 알아본다.',a:'no',w:'아니에요. 픽셀 그대로 읽는 판정기는 270장을 봐도 이동 2에서 40%였습니다. 읽는 방법(필터 + 최댓값)을 바꿔야 했습니다. → 장면 B ②'},
   {q:'공격 섞기로 배운 모델은 더 센 공격도 막는다.',a:'part',w:'일부만 맞아요. 배운 세기 근처는 잘 막지만(0.05: 42% → 77%), 0.08처럼 더 세지면 39%로 내려갑니다. 세게 배우면 평소 정확도를 잃습니다. → 장면 C ③'},
   {q:'시계에 들어가는 크기면 배포해도 된다.',a:'no',w:'아니에요. 다시 학습 없이 90%를 지우면 크기는 들어가도 정확도가 72%입니다. 크기와 정확도, 잡음 시험을 함께 봐야 합니다. → 장면 D ②'},
   {q:'네 장면 모두 "숫자를 어떻게 남기고 어떻게 읽을지"를 고르는 일이다.',a:'yes',w:'맞아요. 담을 숫자 개수(A), 무시할 차이(B), 막을 흔들림(C), 줄일 정밀도(D) 모두 숫자를 고르는 결정입니다.'}
  ];
  var L={yes:'맞다',part:'일부만 맞다',no:'틀리다'},box=$('#claims');
  box.innerHTML=C.map(function(c,i){return '<div class="claim"><div class="cq">카드 '+(i+1)+'. "'+c.q+'"</div><div class="opts" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:6px">'+
    ['yes','part','no'].map(function(k){return '<button class="bt" data-i="'+i+'" data-k="'+k+'">'+L[k]+'</button>';}).join('')+'</div><div class="fb" aria-live="polite"></div></div>';}).join('')+
    '<p class="muted" style="margin:10px 0 0">다 확인했다면: AI의 요약을 받으면 ① 그 말이 어떤 조건에서 나온 숫자인지 ② 조건을 바꾸면 그대로인지 ③ 무엇을 대가로 냈는지를 묻는 습관이면 충분합니다.</p>';
  $$('button',box).forEach(function(b){b.addEventListener('click',function(){var i=+b.getAttribute('data-i'),k=b.getAttribute('data-k'),c=C[i],fb=$$('.fb',box)[i];
    $$('button[data-i="'+i+'"]',box).forEach(function(x){x.setAttribute('aria-pressed','false');});b.setAttribute('aria-pressed','true');
    fb.style.color=k===c.a?COL.gfp:COL.eye;fb.innerHTML=(k===c.a?'정답 — ':'정답은 "'+L[c.a]+'" — ')+c.w;});});
})();

/* ---------- 보이는 캔버스만 다시 그리기 ---------- */
function all(){redraws.forEach(function(f){var host=null;try{f();}catch(e){if(window.console)console.error(e);}});}
window.__MIS=MIS;all();updStudy();fromHash();
var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(all,150);});
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(all);
})();
