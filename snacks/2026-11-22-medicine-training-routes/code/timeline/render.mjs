export const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const number = n => Number(n.toFixed(2)).toString();
export function origin(route, clock, data) {
  const school = data.schools.find(s => s.school_id === route.school_id);
  return clock === 'school' ? +school.school_years : clock === 'age18' ? +school.school_leaving_age - 18 : 0;
}
export function chart(data, clock = 'leaving', specialties = true) {
  const c=data.copy, max=clock==='school'?26:13, step=clock==='school'?4:2;
  const ticks=Array.from({length:Math.floor(max/step)+1},(_,i)=>i*step);
  const header=`<div class="axis"><div>${escape(c.clock_unit)}</div><div class="axis-track">${ticks.map(n=>`<span style="left:${n/max*100}%">${n}</span>`).join('')}</div></div>`;
  const rows=data.routes.map(route=>{
    const off=origin(route,clock,data), school=data.schools.find(s=>s.school_id===route.school_id);
    const phases=route.stages.filter(s=>['prerequisite','degree','clinical','specialty'].includes(s.kind)&&(specialties||s.kind!=='specialty'));
    if(clock!=='leaving') {
      const start=clock==='school'?0:0, end=clock==='school'?+school.school_years:+school.school_leaving_age-18;
      if(end>start)phases.unshift({id:route.id+'-school',kind:'school',label:c.legend.school,start:(start-off)*12,end:(end-off)*12});
    }
    const blocks=phases.map(s=>{
      const start=off+s.start/12, len=(s.end-s.start)/12, label=len<2?number(len):(s.short_label||s.label);
      return `<a class="phase ${s.kind}" href="#${escape(s.id)}" data-stage="${escape(s.id)}" style="left:${start/max*100}%;width:${len/max*100}%" title="${escape(s.label)} · ${number(len)} ${escape(c.detail_labels.years)}" aria-label="${escape(route.label+' · '+s.label+' · '+number(start)+' '+c.detail_labels.until+' '+number(start+len)+' '+c.detail_labels.years)}"><span class="phase-label">${escape(label)}</span><span class="phase-duration" aria-hidden="true">${number(len)}</span></a>`;
    }).join('');
    const markers=route.stages.filter(s=>['first_registration','full_registration','practice_endpoint'].includes(s.kind));
    // Coincident first/full registration is represented by one full-registration symbol.
    const marks=markers.filter(s=>!(s.kind==='first_registration'&&markers.some(t=>t.kind==='full_registration'&&t.start===s.start)));
    const dots=marks.map(s=>`<a href="#${escape(s.id)}" data-stage="${escape(s.id)}" class="marker ${s.kind}" style="left:${(off+s.start/12)/max*100}%" title="${escape(s.label)}" aria-label="${escape(route.label+' · '+s.label+' · '+number(off+s.start/12)+' '+c.detail_labels.years)}"><span></span></a>`).join('');
    const roleBars=specialties?route.stages.filter(s=>s.kind==='later_role').map(s=>`<a class="phase later_role" href="#${escape(s.id)}" data-stage="${escape(s.id)}" style="left:${(off+s.start/12)/max*100}%;width:${(s.end-s.start)/12/max*100}%" aria-label="${escape(s.label)}"><span class="phase-label">${escape(s.short_label||s.label)}</span><span class="phase-duration" aria-hidden="true">${number((s.end-s.start)/12)}</span></a>`).join(''):'';
    const extra=route.stages.filter(s=>['exam','embedded'].includes(s.kind)).map(s=>`<a href="#${escape(s.id)}" data-stage="${escape(s.id)}">${escape(s.label)}</a>`).join(' · ');
    const phasesList=phases.map(s=>`<a href="#${escape(s.id)}" data-stage="${escape(s.id)}"><i class="swatch ${s.kind}" aria-hidden="true"></i><span>${escape(s.label)} <b>${number((s.end-s.start)/12)}</b> ${escape((s.end-s.start)===12?c.detail_labels.year:c.detail_labels.years)}</span></a>`).join('');
    const rowAxis=`<div class="axis-track row-axis" aria-hidden="true">${ticks.map(n=>`<span style="left:${n/max*100}%">${n}</span>`).join('')}</div>`;
    const labels=marks.map(s=>`<a class="milestone-label ${s.kind}" href="#${escape(s.id)}" data-stage="${escape(s.id)}"><span class="symbol"></span><span class="milestone-name">${escape(s.label)} <b>${number(off+s.start/12)}</b></span></a>`).join('');
    return `<div class="route-row" data-route="${escape(route.id)}"><div class="route-name"><strong>${escape(route.label)}</strong><span>${escape(route.pathway)}</span></div><div class="route-track">${rowAxis}<div class="phases">${blocks}</div><div class="markers">${dots}</div><div class="phases-list">${phasesList}</div><div class="milestones">${labels}</div>${roleBars?`<div class="role-label">${escape(c.legend.later_role)}: ${route.stages.filter(s=>s.kind==='later_role').map(s=>escape(s.label)).join('; ')}</div><div class="phases role-track">${roleBars}</div>`:''}${extra?`<details><summary>${escape(c.extra_stages)}</summary><div class="extra-stages">${extra}</div></details>`:''}</div></div>`;
  }).join('');
  return header+rows;
}
export function evidence(data, route, stage, clock='leaving') {
  const c=data.copy, l=c.detail_labels, school=data.schools.find(s=>s.school_id===route.school_id), off=origin(route,clock,data);
  const schoolOnly=stage.kind==='school';
  let body=`<p class="eyebrow">${escape(route.label)}</p><h3 tabindex="-1" id="detail-title">${escape(stage.label)}</h3>`;
  body+=`<dl><dt>${escape(l.period)}</dt><dd>${number(off+stage.start/12)} ${escape(l.until)} ${number(off+stage.end/12)} ${escape(l.years)}</dd><dt>${escape(l.basis)}</dt><dd>${escape(c.basis_labels[stage.duration_basis]||stage.duration_basis||'')}</dd></dl>`;
  if(!schoolOnly)body+=`<p>${escape(stage.note)}</p>`;
  body+=`<details><summary>${escape(l.route_note)}</summary><p>${escape(route.notes)}</p><p>${escape(route.evidence_status)}</p></details>`;
  body+=`<details><summary>${escape(l.school)}</summary><dl>${[['primary_age',school.entry_age],['school_duration',school.school_years],['leaving_age',school.school_leaving_age],['school_year',school.reference_year]].map(([k,v])=>`<dt>${escape(l[k])}</dt><dd>${escape(v)}</dd>`).join('')}</dl><p>${escape(school.adjustment)}</p>${data.uis.filter(s=>s.school_id===route.school_id).map(s=>`<p><a href="${escape(s.url)}">${escape(c.uis_label)} · ${escape(s.sheet)} · ${escape(s.row)}</a> · ${escape(s.programme)} · ${escape(s.entrance_age)} / ${escape(s.duration_years)}</p>`).join('')}${school.additional_source?`<p><a href="${escape(school.additional_source)}">${escape(route.label)}</a></p>`:''}</details>`;
  for(const id of stage.sources||[]){const s=data.sources[id];body+=`<section class="source"><h4>${escape(l.source)}</h4><p><a href="${escape(s.url)}">${escape(s.publisher)} — ${escape(s.title)}</a></p><blockquote>${escape(s.passage)}</blockquote><p>${escape(l.source_date)}: ${escape(s.source_date)} · ${escape(l.accessed)}: ${escape(s.accessed)}</p><p>${escape(l.locator)}: ${escape(s.locator)}</p><p class="reading">${escape(l.reading)}: ${escape(s.reading)}</p>${s.corroboration?`<a href="${escape(s.corroboration)}">${escape(l.evidence)}</a>`:''}</section>`;}
  return body;
}
