'''
-O método de uma instancia é aquele que cria um objeto a partir do que é passado para a classe.
- Está relacionad a classe e pode construir o objeto sem estar relacionado ao __init__
'''
class Pessoa1:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
    
    def get_ano_nascimento(self):
        return print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

#p1 = Pessoa1.por_ano_nascimento('Vitoria', 2001)
p1 = Pessoa1('Vitoria', 20)
print(p1) #Printa o endereço na memória
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
