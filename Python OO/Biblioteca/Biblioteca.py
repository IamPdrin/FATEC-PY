import Livro;
import Usuario;

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, livroSelecionado, usuarioSelecionado):
        usuario_existente = False
        
        for usuario in self.usuarios:
            if usuario.nome == usuarioSelecionado:
                usuario_existente = True
                break
    
        if not usuario_existente:
            print("\nUsuário não cadastrado!")
            return
    
        for livro in self.livros:
            if livro.titulo == livroSelecionado and livro.disponibilidade:
                livro.disponibilidade = False
                print(f"\nO livro {livro.titulo} foi emprestado para o usuário {usuarioSelecionado}")
                return
            
        print(f"\nLivro {livroSelecionado} não disponível ou não encontrado.")

            
    
    def listar_livros_disponiveis(self):
        if not self.livros:
            print("Ainda não há livros cadastrados!")
        else:
            for livros in self.livros:
                if livros.disponibilidade == True:
                    print(f"{livros.titulo}")

    def listar_livros_emprestados(self):
        cont = 0
        qtElementos = len(self.livros)
        for livros in self.livros:
            if livros.disponibilidade == False:
                print(f"{livros.titulo}")
            elif livros.disponibilidade == True:
                cont = cont + 1
                if cont == qtElementos:
                    print("Todos os livros estão diponíveis!")

    def listar_usuarios(self):
        for usuarios in self.usuarios:
            print(f"{usuarios.iden} - {usuarios.nome}")