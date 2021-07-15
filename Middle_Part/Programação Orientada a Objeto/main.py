from pessoa import Pessoa

p1 = Pessoa("Vitoria", 20)
p2 = Pessoa("Giovane", 23)

#p1.falar()
#p1.outro_metodo()
#print(Pessoa.ano_atual) Print na variavel da classe 

'''
p1.comer("Bala")
p1.comer("Bala")
p1.falar("POO")
p1.para_comer()
p1.falar("POO")
p1.falar("POO")
p1.parar_de_falar()
p1.parar_de_falar()
p1.falar("poo")
p1.comer("Bolo")
'''

p1.falar("Filmes")
p2.comer("Chocolate")
p1.comer("Chocolate")
p2.falar("Filme")
p1.parar_de_falar()
p2.para_comer()
p1.comer("Chocolate")
p2.falar("Filmes")

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

