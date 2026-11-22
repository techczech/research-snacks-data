import {chart,evidence} from './render.mjs';
const data=JSON.parse(document.querySelector('#payload').textContent);
let clock='leaving', specialties=true, selected=null;
const chartEl=document.querySelector('#chart'), panel=document.querySelector('#evidence');
function render(){chartEl.innerHTML=chart(data,clock,specialties);document.querySelector('#clock-note').textContent=data.copy.clock_notes[clock];if(selected)panel.innerHTML=evidence(data,selected.route,selected.stage,clock);}
for(const radio of document.querySelectorAll('[name=clock]'))radio.addEventListener('change',()=>{clock=radio.value;render();});
document.querySelector('#specialties').addEventListener('change',event=>{specialties=event.target.checked;render();});
chartEl.addEventListener('click',event=>{
 const link=event.target.closest('[data-stage]');if(!link)return;
 const id=link.dataset.stage, route=data.routes.find(r=>r.stages.some(s=>s.id===id)||id===r.id+'-school');
 if(!route)return;
 const school=data.schools.find(s=>s.school_id===route.school_id);
 const stage=route.stages.find(s=>s.id===id)||{id,kind:'school',label:data.copy.legend.school,start:-school.school_years*12,end:0,duration_basis:'standard_programme'};
 event.preventDefault();selected={route,stage};panel.innerHTML=evidence(data,route,stage,clock);panel.hidden=false;
 panel.querySelector('#detail-title').focus({preventScroll:true});
 panel.scrollIntoView({behavior:'auto',block:'nearest'});
});
function download(content,type,filename){const url=URL.createObjectURL(new Blob([content],{type}));const a=document.createElement('a');a.href=url;a.download=filename;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
document.querySelector('#export').addEventListener('click',()=>download(data.csv,'text/csv;charset=utf-8',data.copy.export_filename));
document.querySelector('#export-sources').addEventListener('click',()=>download(JSON.stringify(data.sources,null,2),'application/json',data.copy.source_export_filename));
const theme=document.querySelector('#theme');
if(theme)theme.addEventListener('change',()=>{document.documentElement.dataset.theme=theme.value;});

// Match the host site's sandboxed tool-height protocol without reading its DOM.
if(new URLSearchParams(location.search).get('embed')==='1'){
 document.documentElement.classList.add('embedded');
 const measure=()=>parent.postMessage({type:'research-snack:tool-height',height:Math.ceil(document.querySelector('main').getBoundingClientRect().height)+32},'*');
 new ResizeObserver(measure).observe(document.querySelector('main'));
 addEventListener('message',event=>{if(event.source===parent&&event.data==='research-snack:measure-tool')measure();});
 measure();
}
