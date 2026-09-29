const $=(s,e=document)=>e.querySelector(s),$$=s=>[...document.querySelectorAll(s)],J=u=>fetch(u).then(r=>r.json()),E=encodeURIComponent;
let C,CUTS=[],VIEW=[],I=0,PROD=[];
const wa=(t,n)=>`https://wa.me/${n||C.whatsapp}?text=${E(t)}`;
const chips=(el,cats,fn)=>{el.innerHTML=['Todos',...cats].map((c,i)=>`<button class="chip${i?'':' on'}">${c}</button>`).join('');
 el.onclick=e=>{const b=e.target.closest('button');if(!b)return;[...el.children].forEach(x=>x.classList.toggle('on',x===b));fn(b.textContent)}};
const cuts=cat=>{VIEW=CUTS.filter(c=>cat==='Todos'||c.categoria===cat);
 $('#g-cortes').innerHTML=VIEW.map((c,i)=>`<figure data-i="${i}"><img loading="lazy" src="${c.imagem}" alt="${c.nome}"><figcaption><b>${c.nome}</b><small>${c.categoria}</small></figcaption></figure>`).join('')};
const show=i=>{I=(i+VIEW.length)%VIEW.length;const c=VIEW[I];$('#lb-i').src=c.imagem;$('#lb-i').alt=c.nome;
 $('#lb-t').innerHTML=`<b>${c.nome}</b> <small>${c.categoria}</small>${c.descricao?`<p>${c.descricao}</p>`:''}`;
 $('#lb-w').href=wa(`${C.msg.corte} (Corte: ${c.nome})`);$('#lb').hidden=false};
const prods=cat=>{$('#g-prod').innerHTML=PROD.filter(p=>cat==='Todos'||p.categoria===cat).map(p=>`<article><img loading="lazy" src="${p.imagem}" alt="${p.nome}"><div><small>${p.categoria}</small><h3>${p.nome}</h3>${p.descricao?`<p>${p.descricao}</p>`:''}${p.preco?`<b>${p.preco}</b>`:''}${p.disponibilidade==='esgotado'?'<em>Esgotado</em>':''}<a class="btn sm" target="_blank" rel="noopener" href="${wa(C.msg.produto.replace('[NOME DO PRODUTO]',p.nome))}">Perguntar disponibilidade</a></div></article>`).join('')};
Promise.all([J('data/configuracao.json'),J('data/categorias.json'),J('data/cortes.json'),J('data/antes-depois.json'),J('data/produtos.json'),J('data/avisos.json')]).then(([c,cat,cortes,ad,pr,av])=>{
 C=c;CUTS=cortes;PROD=pr;
 $$('[data-wa]').forEach(a=>a.href=wa(C.msg[a.dataset.wa],a.hasAttribute('data-dev')?C.dev_whatsapp:0));
 $('#ig').href=$('#ig2').href=C.instagram;$('#end').textContent=C.endereco;
 $('#mapa').src=`https://www.google.com/maps?q=${E(C.busca_mapa)}&output=embed`;
 $('#rota').href=`https://www.google.com/maps/dir/?api=1&destination=${E(C.busca_mapa)}`;$('#abrir').href=`https://www.google.com/maps/search/?api=1&query=${E(C.busca_mapa)}`;
 if(C.sobre.texto){$('#sobre').hidden=$('#n-sobre').hidden=false;$('#sobre-t').textContent=C.sobre.texto}
 if(C.fotos.length){$('#fotos').hidden=false;$('#g-fotos').innerHTML=C.fotos.map(f=>`<img loading="lazy" src="${f}" alt="Barbearia Nazaro">`).join('')}
 $('#g-duv').innerHTML=C.duvidas.map(d=>`<a class="btn alt" target="_blank" rel="noopener" href="${wa(d.msg)}">${d.rotulo}</a>`).join('');
 chips($('#f-cortes'),cat.cortes.filter(x=>cortes.some(c=>c.categoria===x)),cuts);cuts('Todos');
 chips($('#f-prod'),cat.produtos,prods);prods('Todos');
 $('#g-ad').innerHTML=ad.map(a=>`<div class="ba"><img loading="lazy" src="${a.depois}" alt="Depois"><img class="top" loading="lazy" src="${a.antes}" alt="Antes"><i></i><input type="range" min="0" max="100" value="50" aria-label="Comparar antes e depois"></div>`).join('');
 $('#g-ad').oninput=e=>e.target.parentNode.style.setProperty('--p',e.target.value+'%');
 $('#avisos').innerHTML=av.filter(a=>a.ativo).map(a=>`<p>📢 ${a.texto}</p>`).join('');
 if(C.contador.ativo){const seen=localStorage.getItem('nz_visita');
  fetch(`https://api.counterapi.dev/v1/${C.contador.namespace}/${C.contador.chave}/${seen?'':'up'}`).then(r=>r.json()).then(d=>{localStorage.setItem('nz_visita','1');
   const n=d.count??d.Count??d.value;if(n!=null){$('#vis').textContent=Number(n).toLocaleString('pt-BR');$('#visw').hidden=false}}).catch(()=>{})}
});
$('#g-cortes').onclick=e=>{const f=e.target.closest('figure');if(f)show(+f.dataset.i)};
$('#lb-x').onclick=()=>$('#lb').hidden=true;$('#lb-p').onclick=()=>show(I-1);$('#lb-n').onclick=()=>show(I+1);
$('#lb').onclick=e=>{if(e.target.id==='lb')$('#lb').hidden=true};
addEventListener('keydown',e=>{if($('#lb').hidden)return;if(e.key==='Escape')$('#lb').hidden=true;if(e.key==='ArrowLeft')show(I-1);if(e.key==='ArrowRight')show(I+1)});
$('#menu').onclick=()=>$('#nav').classList.toggle('open');$('#nav').onclick=()=>$('#nav').classList.remove('open');
