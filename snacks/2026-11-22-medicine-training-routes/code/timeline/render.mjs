export const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const number = n => Number(n.toFixed(2)).toString();
export function origin(route, clock, data) {
 const s=data.schools.find(s=>s.school_id===route.school_id);
 return clock==='school'?+s.school_years:clock==='age18'?+s.school_leaving_age-18:0;
}
export function stageDisplay(data,route,stage){
 const v=data.visual, custom=v.stages[stage.id]||{};
 return {short:custom.short||v.kind_labels[stage.kind]||stage.label,permits:custom.permits||v.kind_permissions[stage.kind]||stage.note};
}
export function resolveStage(data,id,clock='leaving'){
 const route=data.routes.find(r=>r.stages.some(s=>s.id===id)||id===r.id+'-school');
 if(!route)return null;
 const school=data.schools.find(s=>s.school_id===route.school_id);
 return {route,stage:route.stages.find(s=>s.id===id)||{id,kind:'school',label:data.copy.legend.school,start:-(clock==='age18'?origin(route,clock,data):+school.school_years)*12,end:0,duration_basis:'standard_programme',sources:[],note:school.adjustment}};
}
export function chart(data,clock='leaving',specialties=true,view='routes'){
 const c=data.copy, max=clock==='school'?26:clock==='age18'?13:12,step=clock==='school'?4:2;
 const ticks=Array.from({length:Math.floor(max/step)+1},(_,i)=>i*step);if(ticks.at(-1)!==max)ticks.push(max);
 const header=`<div class="axis" data-max="${max}"><div class="axis-caption">${escape(c.clock_unit)}</div><div class="axis-track">${ticks.map((n,i)=>`<span class="${i===0?'first':i===ticks.length-1?'last':''}" style="left:${n/max*100}%">${n}</span>`).join('')}</div></div>`;
 const rows=data.routes.map(route=>{
  const off=origin(route,clock,data), school=data.schools.find(s=>s.school_id===route.school_id), endpoints=data.visual.milestones[route.id];
  const phases=route.stages.filter(s=>['prerequisite','degree','clinical','specialty'].includes(s.kind)&&(specialties||s.kind!=='specialty'));
  if(clock!=='leaving'){
   const end=clock==='school'?+school.school_years:+school.school_leaving_age-18;
   if(end>0)phases.unshift({id:route.id+'-school',kind:'school',label:c.legend.school,start:-off*12,end:(end-off)*12});
  }
  const attrs=s=>`href="#${escape(s.id)}" data-stage="${escape(s.id)}" aria-haspopup="dialog" aria-controls="stage-popover" aria-label="${escape(route.label+' · '+s.label+' · '+number(off+s.start/12)+' to '+number(off+s.end/12)+' years')}"`;
  const bars=view==='routes'?`<div class="phases">${phases.map(s=>{
   const start=off+s.start/12,len=(s.end-s.start)/12,display=stageDisplay(data,route,s);
   return `<a class="phase ${s.kind} ${len<1.5?'narrow':''}" ${attrs(s)} style="left:${start/max*100}%;width:${len/max*100}%" data-start="${start}" data-end="${start+len}"><span class="phase-label">${escape(display.short)}</span><b class="phase-duration">${number(len)}</b></a>`;
  }).join('')}</div>`:'';
  const markers=view==='milestones'?endpoints.filter((id,i)=>specialties||i!==2).map(id=>route.stages.find(s=>s.id===id)):[...endpoints.filter((id,i)=>specialties||i!==2),...(data.visual.extra_markers[route.id]||[])].map(id=>route.stages.find(s=>s.id===id));
  const dots=markers.map(s=>{
   const value=off+s.start/12,lane=s.kind==='first_registration'?0:s.kind==='full_registration'?1:2;
   const label=s.kind==='first_registration'?c.marker_labels.first:s.kind==='full_registration'?c.marker_labels.full:s.id===endpoints[2]?c.marker_labels.family:c.marker_labels.clinical;
   return `<a class="marker ${s.kind} ${value>max*.66?'label-before':'label-after'}" ${attrs(s)} style="left:${value/max*100}%;--lane:${lane};--label-room:${(value>max*.66?value/max:1-value/max)*100}" data-year="${value}"><span class="symbol" aria-hidden="true"></span><span class="marker-label"><span class="marker-name">${escape(label)}</span> <b>${number(value)}</b></span></a>`;
  }).join('');
  return `<div class="route-row" data-route="${escape(route.id)}"><div class="route-name"><strong>${escape(route.label)}</strong><span>${escape(data.visual.routes[route.id])}</span></div><div class="route-track" style="--grid-step:${step/max*100}%">${bars}<div class="markers">${dots}</div></div></div>`;
 }).join('');
 return `<div class="comparison-view ${view}">${header}${rows}</div>`;
}
export function popoverContent(data,route,stage,clock='leaving'){
 const c=data.copy,off=origin(route,clock,data), display=stageDisplay(data,route,stage);
 const links=(stage.sources||[]).map(id=>{const s=data.sources[id];return `<a href="${escape(s.url)}" target="_blank" rel="noopener">${escape(data.visual.sources[id]||s.publisher)}</a>`;}).join(' · ');
 const schoolLinks=data.uis.filter(s=>s.school_id===route.school_id).map(s=>`<a href="${escape(s.url)}" target="_blank" rel="noopener">UNESCO UIS</a>`);
 return `<button type="button" class="popover-close" aria-label="${escape(c.popover_close)}">×</button><p class="popover-country">${escape(route.label)}</p><h3 id="popover-title">${escape(stage.label)}</h3><p class="popover-period"><strong>${number(off+stage.start/12)}–${number(off+stage.end/12)} ${escape(c.detail_labels.years)}</strong> · ${escape(c.clocks.find(x=>x.id===clock).label)}</p><p>${escape(display.permits)}</p><p class="popover-sources">${links||schoolLinks[0]||''}</p><a class="full-record" href="#${escape(stage.id)}">${escape(c.full_record_label)}</a>`;
}
export function recordsTable(data,clock='leaving'){
 const rows=data.routes.flatMap(route=>route.stages.map(stage=>{
  const off=origin(route,clock,data),d=stageDisplay(data,route,stage);
  return `<tr class="static-record" id="${escape(stage.id)}" tabindex="-1"><th scope="row">${escape(route.label)}<br>${escape(stage.label)}</th><td>${number(off+stage.start/12)}–${number(off+stage.end/12)}</td><td><p>${escape(d.permits)}</p><p>${escape(stage.note)}</p><p>${escape(data.copy.basis_labels[stage.duration_basis])}</p></td><td>${stage.sources.map(id=>`<a href="#source-${escape(id)}">${escape(data.visual.sources[id]||data.sources[id].publisher)}</a>`).join('<br>')}</td></tr>`;
 }));
 const schoolRows=data.routes.map(route=>{
  const school=data.schools.find(s=>s.school_id===route.school_id),{stage}=resolveStage(data,route.id+'-school',clock),off=origin(route,clock,data);
  const urls=[...new Set(data.uis.filter(s=>s.school_id===route.school_id).map(s=>s.url))];
  return `<tr class="school-record" id="${escape(stage.id)}" tabindex="-1"><th scope="row">${escape(route.label)}<br>School baseline</th><td>${number(off+stage.start/12)}–${number(off)}</td><td><p>School years: ${escape(school.school_years)}. Primary entry age: ${escape(school.entry_age)}. Selected leaving age: ${escape(school.school_leaving_age)}.</p><p>${escape(school.adjustment)}</p><p>The interval shows the school segment on the selected clock. School study gives no medical practice licence.</p></td><td>${urls.map(url=>`<a href="${escape(url)}" target="_blank" rel="noopener">UNESCO UIS</a>`).join('<br>')}${school.additional_source?`<br><a href="${escape(school.additional_source)}" target="_blank" rel="noopener">School structure source</a>`:''}</td></tr>`;
 });
 return `<div class="table-scroll"><table class="stage-records"><caption>${escape(data.copy.clock_unit)} · ${escape(data.copy.clocks.find(x=>x.id===clock).label)}</caption><thead><tr><th scope="col">Route and stage</th><th scope="col">Years</th><th scope="col">Meaning and conditions</th><th scope="col">Sources below</th></tr></thead><tbody>${rows.join('')}${schoolRows.join('')}</tbody></table></div>`;
}
