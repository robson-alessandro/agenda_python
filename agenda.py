"""
Desenvolva uma classe Agenda para gerenciar contatos. Cada contato deve ter atributos como nome , telefone e email .
Implemente métodos para adicionar, remover e listar contatos da agenda
"""

class Agenda:
    def __init__(self):

        self.contatos= []

    def adicionar(self,contato):
        self.contatos.append(contato)
        print('\ncontato adicionado com sucessso')

    def remover(self, contato):
        self.contatos.pop(contato)

    def mostrar(self,contato):
        posicao=0
        for elemento in contato:
            print('------------------------------')
            print(f'{posicao})- {elemento}')
            print('------------------------------')
            posicao += 1 
            

class Contatos:
    def __init__(self):
        self.nome = input("\ndigite o nome do contato:")
        self.telefone = input("digite o telefone do contato:")
        self.email = input("digite o email do contato:")

    def __repr__(self):
        return "{}, {}, {}".format(self.nome, self.telefone, self.email)
        


listaContatos = Agenda()
escolha = 5
print('------------agenda--------------')
while escolha != 0:
    escolha =int( input('\ndigite o numero referente a sua escolha:\n 1-adicionar contato\n 2-remover contato\n 3-mostrar lista de contatos\n 0-sair do aplicativo : '))

    match escolha:
        case 1:
            contato = Contatos()
            listaContatos.adicionar(contato)

        case 2 :
            contato = int(input('\ndigite a posição do contato que deseja apagar: '))
            listaContatos.remover(contato)
            
  
        case 3:
            listaContatos.mostrar(listaContatos.contatos)

        