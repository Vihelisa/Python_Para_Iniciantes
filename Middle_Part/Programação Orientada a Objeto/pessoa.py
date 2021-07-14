'''
O self serve para que a classe saiba qual a instância que a classe deve se referir, 
como se estivessemos passando a variável dentro da função, só que nesse caso o self consegue
perceber ela sozinho apenas pela forma que passamos. EXEMPLO:
p1.falar() -> está querendo dizer q a instância que deve ser atendida é a p1, ou seja, deve ser tradado
apenas aquilo que se refere a p1

Cada instância será diferente dá outra pois os dados criados na classe, são salvos num lugar na memória e toda vez que 
é descrito uma instânia ele busca todas as características que já estão salvas para ela, se já estiverem sifo
criadas para ela.

class Pessoa:
    def falar(self): #Funções são métodos da classe
        print("Pessoa está falando")

'''

class Pessoa:
    def __init__(self, nome, idade,falando=False, comendo=False):
        self.nome = nome #mesma coisa de dizer que p1.nome = "Vitoria"
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

        '''Se definirmos uma variável dentro da classe, dependendo local que ela for chamada ela não estará
        definida, pois não é uma variável "global", ou seja, para toda a classe assim como as que estão dentro
        do parenteses do __init__

        variavel = "variável"
        print(variavel) #Toda vez que o __init__ for chamado ela será printada

        def outro_metodo(self):
        #print(variavel) #Neste caso a variável em questão não será chamada pois ela é exclusiva do __init__
        print(self.nome) #Neste caso essa variável já aparecerá de acordo com o comando, pois ela é uma 
        #Variável que atende a todos os métodos que forem criados dentro da classe.'''

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo\n")
            return
        if self.falando:
            print(f"{self.nome} já está falando\n")
            return
        print(f"{self.nome} está falando sobre {assunto}\n")
        self.falando = True
    
    def parar_de_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando\n")
            return
        print(f"{self.nome} parou de falar\n")
        self.falando = False
    
    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo {alimento}\n")
            return
        if self.falando:
            print(f"{self.nome} não pode comer falando\n")
            return
        print(f"{self.nome} está comendo {alimento}\n")
        self.comendo = True

    def para_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo\n")
            return
        print(f"{self.nome} parou de comer\n")
        self.comendo = False
