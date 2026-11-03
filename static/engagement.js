// Improve the visual grouping without changing forms, inputs or event handlers.
function styleWatchRules(){
 const form=document.querySelector('#rules');
 if(!form||form.dataset.styled)return;
 form.dataset.styled='true';
 const layout=document.createElement('div');layout.className='rules-layout';
 form.before(layout);layout.append(form);
 const panels=[['01','Market movement','Set the moves that earn your attention.'],['02','Disclosure radar','Choose the company developments you follow.']].map(([n,title,desc])=>{
  const p=document.createElement('section');p.className='rule-panel';
  p.innerHTML=`<div class="rule-heading"><span class="rule-number">${n}</span><div><h3>${title}</h3><p>${desc}</p></div></div>`;return p;
 });
 const nodes=[...form.children];
 nodes.slice(0,6).forEach(n=>panels[0].append(n));
 nodes.slice(6,8).forEach(n=>panels[1].append(n));
 form.prepend(...panels);
 const footer=nodes[8];if(footer){footer.className='rule-footer';const hint=document.createElement('small');hint.textContent='Your preferences stay saved between visits.';footer.append(hint)}
 const note=document.createElement('section');note.className='rule-explainer';
 note.innerHTML='<span class="tag">YOUR SIGNAL, YOUR RULES</span><h3>A quieter desk.<br>A sharper focus.</h3><p>Higher thresholds surface fewer market moves. Select the disclosures that matter to your research.</p><div class="rule-example"><span class="tag">VOLUME TRIGGER</span><strong id="rule-volume"></strong><small>the recent average trading volume</small><div class="rule-meter" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div><p>Evaluated against the labelled demonstration EOD snapshot. Save to update your attention queue.</p>';
 layout.append(note);
 const volume=form.querySelector('[name=volume]');
 const update=()=>{note.querySelector('#rule-volume').textContent=volume.value+'×'};volume.addEventListener('input',update);update();
}
new MutationObserver(styleWatchRules).observe(document.querySelector('#app'),{childList:true,subtree:true});
styleWatchRules();
document.querySelector('#data-info').onclick=()=>{
 document.querySelector('#evidence').innerHTML='<h2>About this workspace</h2><p>Prices, volumes and corporate announcements are synthetic demonstration data, not current market information.</p><p>The EOD snapshot is dated 30 October 2026. Research retrieves only the source excerpts you add. Live feeds and generative AI are not connected.</p>';
 document.querySelector('#drawer').showModal();
};
