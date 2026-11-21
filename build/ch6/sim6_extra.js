
/* ===== 6장 추가 시뮬레이션 (5장 핵심 함수에 이어 붙임) ===== */
/* 위치를 옮긴 그림 묶음: 가로·세로 모두 −s ~ +s 사이로 무작위 이동 */
function setShift(n,seed,sh,jit){var R=rng(seed),D=[];for(var i=0;i<n;i++){var c=i%3;
  var dx=sh?Math.floor(R()*(2*sh+1))-sh:0,dy=sh?Math.floor(R()*(2*sh+1))-sh:0;
  D.push({x:shapeImg(c,dx,dy).map(function(v){return clip01(v+(jit||0.05)*gauss(R));}),y:c,dx:dx,dy:dy});}return D;}
/* 작은 필터 세 개(가로·세로·대각, 점 세 개의 평균)를 그림 위로 밀고, 위치마다 나온 값 중 최댓값만 남긴다 */
function filterMax(x){function g(X,Y){return (X<0||Y<0||X>7||Y>7)?0.5:x[Y*8+X];}var h=-1,v=-1,d=-1;
  for(var y=0;y<8;y++)for(var X=0;X<8;X++){
    h=Math.max(h,(g(X-1,y)+g(X,y)+g(X+1,y))/3);
    v=Math.max(v,(g(X,y-1)+g(X,y)+g(X,y+1))/3);
    d=Math.max(d,(g(X-1,y-1)+g(X,y)+g(X+1,y+1))/3);}
  return [h,v,d];}
function filterFeat(x){return filterMax(x).map(function(t){return (t-0.5)*5;});}
/* 숫자 세기 */
function countNums(t,s){if(t==='photo')return s.side*s.side*s.color;if(t==='video')return s.side*s.side*s.color*s.fps*s.dur;
  if(t==='text')return s.tok*s.dim;return s.sec*s.rate;}
function maxFit(t,s,B){if(t==='photo')return Math.floor(Math.sqrt(B/s.color));if(t==='video')return Math.floor(Math.sqrt(B/(s.color*s.fps*s.dur)));
  if(t==='text')return Math.floor(B/s.dim);return Math.floor(B/s.rate);}
/* 이삿짐: 크기(비트) = (남은 가중치 + 편향 3) × (비트 + 위치 표시 8비트, 지웠을 때만) */
function packSize(nz,bits,pruned){return (nz+3)*(bits+(pruned?8:0));}
if(typeof module!=='undefined'){module.exports.setShift=setShift;module.exports.filterFeat=filterFeat;module.exports.filterMax=filterMax;module.exports.countNums=countNums;module.exports.maxFit=maxFit;module.exports.packSize=packSize;module.exports.finetune=finetune;module.exports.prune=prune;}
