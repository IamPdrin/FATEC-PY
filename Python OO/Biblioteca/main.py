from Biblioteca import Biblioteca
from Livro import Livro
from Usuario import Usuario

biblioteca = Biblioteca()
iden = 0

#Criação de Livros Padrão para teste das funcionalidades:
"""
liv1 = Livro("A Culpa é das Estrelas", "John Green", 2015, "Romance", True)
liv2 = Livro("O Conto da Aia", "Margareth Atwood", 2018, "Romance", True)
liv3 = Livro("Percy Jackson e o Ladrão de Raios", "Rick Riordan", 2005, "Fantasia", True)

biblioteca.adicionar_livro(liv1)
biblioteca.adicionar_livro(liv2)
biblioteca.adicionar_livro(liv3)
"""

print("\nSeja Bem-Vindo(a) a Biblioteca Internacional do Silêncio!")

while True:
    print("\n\n\
          1 - Adicionar livro; \n\
          2 - Adicionar usuario; \n\
          3 - Emprestar livro; \n\
          4 - Listar livros disponíveis; \n\
          5 - Listar livros emprestados; \n\
          6 - Listar usuários; \n\
          7 - Sair \n\
          ")
    
    opcao = int(input("Digite a opção que você deseja: \n"))
    
    if opcao == 1:
        print("\nDigite as informações para adicionar o Livro..\n")
        titulo = input("Nome do livro: ")
        autor = input("Autor: ")
        anoPublicacao = input("Ano de publicação: ")
        genero = input("Gênero: ")
        disponibilidade = True;
        livro = Livro(titulo, autor, anoPublicacao, genero, disponibilidade)
            
        if isinstance(livro, Livro):
            biblioteca.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")
        else:
            print("As informações não foram devidamente preenchidas!")
            
    elif opcao == 2:
        print("\nDigite as informações do Usuário..\n")
        nome = input("Nome: ")
        iden = iden + 1
        user = Usuario(nome, iden)
            
        if isinstance(user, Usuario) and nome != "":
            biblioteca.adicionar_usuario(user)
            print("Usuário adicionado com sucesso!")
        else:
            print("As informações não foram devidamente preenchidas!")
        
    elif opcao == 3:
        if not biblioteca.livros:
            biblioteca.listar_livros_disponiveis()
        else: 
            print("\nQual livro você deseja levar?\n")
            
            biblioteca.listar_livros_disponiveis()
            
            livroSelecionado = input("\nDigite o nome que corresponde ao livro desejado: ")
            userSelecionado = input("Digite seu nome de usuário: ")
            
            biblioteca.emprestar_livro(livroSelecionado, userSelecionado)
    
    elif opcao == 4:
        print("\n")
        biblioteca.listar_livros_disponiveis()
        
  
    elif opcao == 5:
        print("\n")
        biblioteca.listar_livros_emprestados()
    
    elif opcao == 6:
        print("\n")
        biblioteca.listar_usuarios()
        
    elif opcao == 7:
        print("\nObrigado por visitar nossa biblioteca, até a próxima!")
        break
        
    else:
        print("Digite um opção válida")

