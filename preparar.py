import sys,os,json
from PIL import Image
F={}
for r,_,fs in os.walk(os.path.expanduser(sys.argv[1])):
    for f in fs:
        if "-WA" in f and f.lower().endswith(".jpg"): F[f.split("-WA")[1][:4]]=os.path.join(r,f)
def sv(n,dst,crop=False,mx=900):
    if n not in F: print("FALTA imagem WA"+n); return False
    im=Image.open(F[n]).convert("RGB")
    if crop:
        w,h=im.size; im=im.crop((0,int(h*308/1600),w,int(h*1292/1600)))
    im.thumbnail((mx,mx)); im.save(dst,quality=80,optimize=True); return True
P=[("0200","Alfa Look's Lemon — Loção Pós Barba","Pós-barba","350ml"),
("0193","Alfa Look's Menthol — Loção Pós Barba","Pós-barba","350ml"),
("0191","Alfa Look's Menthol — Loção Pós Barba (kit)","Pós-barba","350ml"),
("0195","Alfa Look's Element — Pomada Modeladora","Pomadas e géis","Alta fixação · Sem álcool · 150g"),
("0185","Alfa Look's Lemon — Loção Pós Barba","Pós-barba","240ml"),
("0192","Alfa Look's Grooming","Cabelo","Preparação e finalização do cabelo · 240ml"),
("0197","Alfa Look's Lemon — Loção Pós Barba (refil)","Pós-barba","Refil · 1L"),
("0189","Alfa Look's Black — Pomada Modeladora","Pomadas e géis","150g"),
("0177","Alfa Look's Menthol — Creme Pós Barba","Pós-barba",""),
("0198","Two Brothers — Pós Barba","Pós-barba","Efeito refrescante · 250g"),
("0181","Two Brothers — Dr. Shaving Barbershop","Barba","1kg"),
("0194","Alfa Look's — Creme Pós Barba Menthol e Creme Esfoliante Pré Barba Lemon","Barba","350g"),
("0188","Two Brothers — Balm para Barba","Barba","Hidratação e nutrição · 250g"),
("0179","Two Brothers — Shampoo 2 em 1 Cabelo e Barba","Cabelo","500ml"),
("0199","Two Brothers — Gel Profissional","Pomadas e géis","250g"),
("0172","Two Brothers — Gel Cera Hidratante","Pomadas e géis","Ultra fixação · Sem álcool · 300g"),
("0203","Two Brothers — Pomada em Pó","Pomadas e géis","Efeito matte · 15g"),
("0202","Two Brothers — Gel Super Cola","Pomadas e géis","300g"),
("0190","Two Brothers — Pomada Incolor","Pomadas e géis","150g"),
("0039","Fox For Men — Pasta Premium","Pomadas e géis","Fixação extra forte · 80g"),
("0184","Alfa Look's — Pomada Modeladora For Men","Pomadas e géis","Uso profissional · 150g"),
("0040","Fox For Men — Linha de pastas e wax","Pomadas e géis",""),
("0196","Two Brothers — Pomada Black","Pomadas e géis","150g"),
("0180","Vip Hair — Pomada Modeladora","Pomadas e géis","130g"),
("0037","Fox For Men — Gel Cola","Pomadas e géis","Fixação extra forte"),
("0178","Two Brothers — Beard Oil","Barba","60ml"),
("0183","Two Brothers — Pomada Matte","Pomadas e géis","150g"),
("0038","Fox For Men — Pasta Orange","Pomadas e géis","Fixação forte · Incolor"),
("0186","Two Brothers — Gromming","Cabelo","Volume e textura · 250g"),
("0176","Two Brothers — Pomada Caramelo","Pomadas e géis","150g"),
("0174","Vip Hair — Pomada Modeladora Teia","Pomadas e géis","130g"),
("0182","Alfa Look's Prime — Pomada Efeito Matte","Pomadas e géis",""),
("0187","Two Brothers — Minoxidil 8%","Barba","Tônico para cabelo e barba · 60ml"),
("0173","Two Brothers — Pomada Teia","Pomadas e géis","150g"),
("0175","Alfa Look's — Pomada Teia For Men","Pomadas e géis","150g")]
def dump(n,o): json.dump(o,open("data/"+n+".json","w"),ensure_ascii=False,indent=1)
prod=[dict(nome=nm,categoria=c,descricao=i,imagem=f"assets/produtos/{n}.jpg",preco=None,disponibilidade="consultar") for n,nm,c,i in P if sv(n,f"assets/produtos/{n}.jpg",mx=700)]
dump("produtos",prod)
for n in("0119","0115","0122"): sv(n,f"assets/portfolio/{n}.jpg",True)
sv("0119","assets/barbearia/capa.jpg",True,1200)
for a,b in(("0120","0117"),("0121","0118")):
    sv(a,f"assets/antes-depois/{a}-antes.jpg"); sv(b,f"assets/antes-depois/{b}-depois.jpg")
dump("cortes",[dict(nome="Degradê",categoria="Degradê",descricao="",imagem="assets/portfolio/0119.jpg"),dict(nome="Degradê com franja",categoria="Degradê",descricao="",imagem="assets/portfolio/0115.jpg"),dict(nome="Cabelo e barba",categoria="Barba",descricao="",imagem="assets/portfolio/0122.jpg")])
dump("antes-depois",[dict(titulo="Antes e depois",antes="assets/antes-depois/0120-antes.jpg",depois="assets/antes-depois/0117-depois.jpg"),dict(titulo="Antes e depois",antes="assets/antes-depois/0121-antes.jpg",depois="assets/antes-depois/0118-depois.jpg")])
dump("categorias",dict(cortes=["Degradê","Social","Tesoura","Navalhado","Barba","Infantil","Outros"],produtos=["Pomadas e géis","Pós-barba","Barba","Cabelo"]))
dump("avisos",[dict(ativo=False,texto="Escreva aqui o aviso e mude ativo para true.")])
D=lambda r,m:dict(rotulo=r,msg=m)
dump("configuracao",dict(nome="BARBEARIA NAZARO",whatsapp="554199196309",dev_whatsapp="5541996523235",instagram="https://www.instagram.com/nazarobarbearia",
endereco="Rua Silvino Trípole, 29 — Alexandra, Paranaguá, PR",busca_mapa="Rua Silvino Trípole 29 Paranaguá PR",
contador=dict(ativo=True,namespace="barbearia-nazaro-site",chave="visitas"),
sobre=dict(texto="Somos a Barbearia Nazaro, em Alexandra. Atendemos dos 3 aos 99 anos: cortes, barba, desenhos, luzes e platinado."),fotos=[],
msg=dict(padrao="Olá! Gostaria de obter mais informações sobre a Barbearia Nazaro.",local="Olá! Gostaria de saber onde fica a Barbearia Nazaro.",corte="Olá! Vi um corte no portfólio da Barbearia Nazaro e gostaria de saber mais sobre ele.",produto="Olá! Gostaria de saber se o produto [NOME DO PRODUTO] está disponível na Barbearia Nazaro.",duvida="Olá! Gostaria de tirar uma dúvida sobre a Barbearia Nazaro.",dev="Olá! Vi o site da Barbearia Nazaro e gostaria de falar com o desenvolvedor."),
duvidas=[D("📍 Onde fica?","Olá! Gostaria de saber onde fica a Barbearia Nazaro."),D("✂️ Vocês fazem este corte?","Olá! Gostaria de saber se vocês fazem um corte que vi."),D("🛍️ Este produto está disponível?","Olá! Gostaria de saber se um produto está disponível na Barbearia Nazaro."),D("📅 Como funciona o atendimento?","Olá! Gostaria de saber como funciona o atendimento na Barbearia Nazaro."),D("💳 Quais formas de pagamento são aceitas?","Olá! Gostaria de saber quais formas de pagamento a Barbearia Nazaro aceita."),D("❓ Outra dúvida","Olá! Gostaria de tirar uma dúvida sobre a Barbearia Nazaro.")]))
print("Pronto:",len(prod),"produtos")
