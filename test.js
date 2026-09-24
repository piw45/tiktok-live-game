// node test.js — cek fisika game tanpa browser
const noop=new Proxy(function(){},{get:(t,k)=>k===Symbol.toPrimitive?()=>0:noop,apply:()=>noop,set:()=>true,construct:()=>noop});
global.THREE=noop;global.devicePixelRatio=1;let seed=13;Math.random=()=>(seed=seed*16807%2147483647)/2147483647;  // deterministik
const els={};const el=id=>els[id]||(els[id]={innerHTML:'',textContent:'',className:'',children:[],insertAdjacentHTML(){this.children.push(1)},classList:{add(){},remove(){},toggle(){}},offsetWidth:0,style:{},firstChild:{nodeValue:''},get lastChild(){const o=this;return{remove(){o.children.pop()}}}});
const cnv=()=>({getContext:()=>noop,width:0,height:0});
global.document={getElementById:id=>id==='c'?cnv():el(id),createElement:cnv,body:{classList:{toggle(){},add(){},remove(){}}}};
global.innerWidth=480;global.innerHeight=800;global.addEventListener=()=>{};global.matchMedia=()=>({matches:false});
global.localStorage={getItem:()=>null,setItem(){}};global.requestAnimationFrame=()=>{};global.WebSocket=function(){};
global.frames=[];global.requestAnimationFrame=f=>{};
let src=require('fs').readFileSync(__dirname+'/game.html','utf8').split('<script>')[1].split('</script>')[0].replace(/^const /gm,'var ').replace(/^let /gm,'var ').replace(/^function /gm,'var _=function ');
src=src.replace(/var _=function (\w+)/g,'var $1=function');
eval(src);
// generation invariant: every platform reachable from the previous.
// Dicek di menara hasil gen murni (pakai posisi dasar pijakan geser), sebelum ada yang runtuh/dihapus.
const cx=q=>(q.bx??q.x)+q.w/2;
for(let i=0;i<40;i++){camY-=300;gen()}
for(let i=2;i<plats.length;i++){const a=plats[i-1],b=plats[i];console.assert(a.y-b.y<=130&&Math.abs(cx(a)-cx(b))<=140+(a.w+b.w)/2,'unreachable',i)}
plats.length=1;topY=0;lastX=170;camY=200-VH;seed=13;gen();   // balikin dunia + seed, biar simulasi selalu dunia yang sama
// simulate: dumb climber (hold jump, swap direction periodically)
keys[' ']=1;keys.ArrowRight=1;
for(let i=0;i<3000;i++){tNow=i*16.67;step(1);if(i%400===0)keys.ArrowRight=!keys.ArrowRight,keys.ArrowLeft=!keys.ArrowRight}
console.log('height after 3000 frames:',height.toFixed(1),'m plats:',plats.length);
console.assert(height>5,'should climb');
// sabotage: reset must drop to 0 and blame
const h0=height;keys[' ']=keys.ArrowRight=keys.ArrowLeft=0;sabotage({type:'reset',user:'budi',gift:'Galaxy',coins:1000});for(let i=0;i<10;i++){tNow+=16.67;step(1)}
console.assert(height<1&&board.budi.n===1,'reset+blame failed',height,board);
// wind applies force
sabotage({type:'wind',dir:-1,user:'x',gift:'Rose',coins:1});keys[' ']=0;keys.ArrowRight=keys.ArrowLeft=0;p.vx=0;step(1);
console.assert(p.vx<0,'wind should push left',p.vx);
// vanish removes standing platform
keys[' ']=1;for(let i=0;i<300;i++){tNow+=16.67;step(1)};keys[' ']=0;for(let i=0;i<60;i++)step(1);
const on=p.on;sabotage({type:'vanish',user:'y',gift:'Galaxy',coins:100});for(let i=0;i<50;i++){tNow+=16.67;step(1)}
console.assert(on.floor||on.gone,'vanish failed');
for(let i=0;i<200;i++){tNow+=16.67;step(1)}console.assert(!on.gone,'vanished platform should come back');
// bantuan: perisai nangkis sabotase, tangga nambah pijakan, penolong masuk papan
sabotage({type:'shield',user:'ani',gift:'Rose',coins:1});const h1=height;
sabotage({type:'reset',user:'jahat',gift:'Galaxy',coins:1000});step(1);
console.assert(height>h1-1&&hboard.ani.n===1,'shield should block reset',height,h1,hboard);
fx.shield=0;const n2=plats.length;sabotage({type:'stair',user:'ani',gift:'GG',coins:100});
console.assert(plats.length===n2+3,'stair failed',plats.length,n2);
console.log('ALL OK');
