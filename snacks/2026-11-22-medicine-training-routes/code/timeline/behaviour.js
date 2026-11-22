import {chart,popoverContent,recordsTable,resolveStage} from './render.mjs';
document.documentElement.classList.add('js');
const data=JSON.parse(document.querySelector('#payload').textContent);
const chartEl=document.querySelector('#chart'),scrollbox=document.querySelector('.comparison-scroll'),pop=document.querySelector('#stage-popover');
let clock='leaving',specialties=true,view='routes',trigger=null,pinned=false,closeTimer=null;
let parentBounds=null,restoring=false;
const supportsPopover=typeof pop.showPopover==='function';
if(!supportsPopover)pop.removeAttribute('popover');
const isOpen=()=>!pop.hidden;
function visibleBounds(){return parentBounds&&parentBounds.bottom>parentBounds.top?parentBounds:{top:0,bottom:innerHeight};}
function place(){
 if(!isOpen()||!trigger?.isConnected)return;
 const r=trigger.getBoundingClientRect(),bounds=visibleBounds(),margin=12;
 pop.style.maxHeight=`${Math.max(110,Math.min(500,bounds.bottom-bounds.top-2*margin))}px`;
 const p=pop.getBoundingClientRect();
 const left=Math.max(margin,Math.min(r.left+r.width/2-p.width/2,innerWidth-p.width-margin));
 let top=r.bottom+8;if(top+p.height>bounds.bottom-margin)top=r.top-p.height-8;
 top=Math.max(bounds.top+margin,Math.min(top,bounds.bottom-p.height-margin));
 pop.style.left=`${left}px`;pop.style.top=`${top}px`;
}
function close({restore=false}={}){
 clearTimeout(closeTimer);if(!isOpen())return;
 const previous=trigger;trigger=null;pinned=false;
 if(supportsPopover&&pop.matches(':popover-open'))pop.hidePopover();
 pop.hidden=true;previous?.removeAttribute('aria-describedby');previous?.removeAttribute('aria-expanded');
 if(restore&&previous?.isConnected){restoring=true;previous.focus({preventScroll:true});restoring=false;}
}
function open(target,{pin=false,focus=false}={}){
 clearTimeout(closeTimer);if(pinned&&target!==trigger&&!pin)return;
 const record=resolveStage(data,target.dataset.stage,clock);if(!record)return;
 const same=target===trigger;if(!same)close();
 trigger=target;pinned=pinned||pin;
 if(!same||!isOpen()){
  pop.innerHTML=popoverContent(data,record.route,record.stage,clock);pop.hidden=false;
  if(supportsPopover&&!pop.matches(':popover-open'))pop.showPopover();
 }
 target.setAttribute('aria-describedby','stage-popover');target.setAttribute('aria-expanded','true');place();
 if(focus)pop.querySelector('.popover-close').focus({preventScroll:true});
}
function updateSticky(){
 const top=parentBounds?.top||0,box=scrollbox.getBoundingClientRect();
 scrollbox.style.setProperty('--axis-top',`${Math.max(0,Math.min(top-box.top,scrollbox.clientHeight-55))}px`);
}
function render(){
 close();chartEl.innerHTML=chart(data,clock,specialties,view);
 document.querySelector('#clock-note').textContent=data.copy.clock_notes[clock];
 document.querySelector('#record-table').innerHTML=recordsTable(data,clock);updateSticky();
}
for(const radio of document.querySelectorAll('[name=clock]'))radio.addEventListener('change',()=>{clock=radio.value;render();});
for(const radio of document.querySelectorAll('[name=view]'))radio.addEventListener('change',()=>{view=radio.value;render();});
document.querySelector('#specialties').addEventListener('change',e=>{specialties=e.target.checked;render();});
chartEl.addEventListener('pointerover',event=>{
 if(event.pointerType==='touch'||!matchMedia('(hover:hover)').matches)return;
 const target=event.target.closest('[data-stage]');if(target)open(target);
});
chartEl.addEventListener('pointerout',event=>{
 if(pinned||event.relatedTarget?.closest?.('[data-stage]')===trigger||pop.contains(event.relatedTarget))return;
 clearTimeout(closeTimer);closeTimer=setTimeout(()=>close(),160);
});
chartEl.addEventListener('focusin',event=>{if(restoring)return;const target=event.target.closest('[data-stage]');if(target)open(target);});
chartEl.addEventListener('focusout',event=>{
 if(pinned||pop.contains(event.relatedTarget))return;
 closeTimer=setTimeout(()=>{if(!pop.contains(document.activeElement)&&document.activeElement!==trigger)close();},0);
});
chartEl.addEventListener('click',event=>{const target=event.target.closest('[data-stage]');if(!target)return;event.preventDefault();open(target,{pin:true,focus:true});});
chartEl.addEventListener('keydown',event=>{
 if(event.key!==' ')return;const target=event.target.closest('[data-stage]');if(!target)return;
 event.preventDefault();open(target,{pin:true,focus:true});
});
pop.addEventListener('pointerenter',()=>clearTimeout(closeTimer));
pop.addEventListener('pointerleave',()=>{if(!pinned)closeTimer=setTimeout(()=>close(),160);});
pop.addEventListener('click',event=>{
 if(event.target.closest('.popover-close')){close({restore:true});return;}
 const full=event.target.closest('.full-record');if(!full)return;
 event.preventDefault();const id=trigger.dataset.stage;close();
 const records=document.querySelector('#all-records');records.open=true;
 const row=document.getElementById(id);if(!row)return;row.focus({preventScroll:true});row.scrollIntoView({block:'center',behavior:'auto'});
});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&isOpen()){event.preventDefault();event.stopPropagation();close({restore:pinned});}},true);
document.addEventListener('pointerdown',event=>{if(isOpen()&&!pop.contains(event.target)&&!event.target.closest('[data-stage]'))close();});
scrollbox.addEventListener('scroll',()=>{if(isOpen()&&!pinned)close();else place();});
addEventListener('resize',()=>{updateSticky();place();});addEventListener('scroll',place,{passive:true});
function download(content,type,filename){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=filename;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
document.querySelector('#export').addEventListener('click',()=>download(data.csv,'text/csv;charset=utf-8',data.copy.export_filename));
document.querySelector('#export-sources').addEventListener('click',()=>download(JSON.stringify(data.sources,null,2),'application/json',data.copy.source_export_filename));
document.querySelector('#theme')?.addEventListener('change',event=>{document.documentElement.dataset.theme=event.target.value;});
if(new URLSearchParams(location.search).get('embed')==='1'){
 document.documentElement.classList.add('embedded');
 const measure=()=>parent.postMessage({type:'research-snack:tool-height',height:Math.ceil(document.querySelector('main').getBoundingClientRect().height)+32},'*');
 new ResizeObserver(measure).observe(document.querySelector('main'));
 addEventListener('message',event=>{
  if(event.source!==parent)return;
  if(event.data==='research-snack:measure-tool')measure();
  if(event.data?.type==='research-snack:tool-viewport'&&Number.isFinite(event.data.top)&&Number.isFinite(event.data.bottom)){
   if(['light','dark'].includes(event.data.theme))document.documentElement.dataset.theme=event.data.theme;
   parentBounds={top:Math.max(0,event.data.top),bottom:Math.min(innerHeight,event.data.bottom)};updateSticky();place();
  }
 });
 measure();
}
