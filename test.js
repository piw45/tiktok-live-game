// node test.js — cek fisika game tanpa browser
const noop=new Proxy(function(){},{get:()=>noop,apply:()=>noop,set:()=>true});
const els={};const el=id=>els[id]||(els[id]={innerHTML:'',textContent:'',className:'',children:[],insertAdjacentHTML(){this.children.push(1)},classList:{add(){},remove(){},toggle(){}},offsetWidth:0,style:{},firstChild:{nodeValue:''},lastChild:{remove(){}}});
const cnv=()=>({getContext:()=>noop,width:0,height:0});
global.document={getElementById:id=>id==='c'?cnv():el(id),createElement:cnv,body:{classList:{toggle(){},add(){},remove(){}}}};
global.innerWidth=480;global.innerHeight=800;global.addEventListener=()=>{};global.matchMedia=()=>({matches:false});
global.localStorage={getItem:()=>null,setItem(){}};global.requestAnimationFrame=()=>{};global.WebSocket=function(){};
global.frames=[];global.requestAnimationFrame=f=>{};
let src=require('fs').readFileSync(__dirname+'/game.html','utf8').split('<script>')[1].split('</script>')[0].replace(/^const /gm,'var ').replace(/^let /gm,'var ').replace(/^function /gm,'var _=function ');
src=src.replace(/var _=function (\w+)/g,'var $1=function');
eval(src);
// simulate: dumb climber (hold jump, swap direction periodically)
keys[' ']=1;keys.ArrowRight=1;
for(let i=0;i<3000;i++){tNow=i*16.67;step(1);if(i%400===0)keys.ArrowRight=!keys.ArrowRight,keys.ArrowLeft=!keys.ArrowRight}
// generation invariant: every platform reachable from the previous
for(let i=2;i<plats.length;i++){const a=plats[i-1],b=plats[i];console.assert(a.y-b.y<=130&&Math.abs((a.x+a.w/2)-(b.x+b.w/2))<=140+(a.w+b.w)/2,'unreachable',i)}
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
const n=plats.length,on=p.on;sabotage({type:'vanish',user:'y',gift:'Heart',coins:100});for(let i=0;i<50;i++){tNow+=16.67;step(1)}
console.assert(on.floor||plats.length===n-1,'vanish failed',plats.length,n);
console.log('ALL OK');
