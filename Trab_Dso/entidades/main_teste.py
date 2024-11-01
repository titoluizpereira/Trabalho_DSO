#Arquivo para testar o código

from artista import Artista
from genero import Genero
from idioma import Idioma
from artista import Artista
from bibliotecademusicas import BibliotecaDeMusicas
from filakaraoke import Fila_Karaoke
from cliente import Cliente
from mesa import Mesa
from musica import Musica


print("TESTE DE MESAS -------------")
Mesa1 = Mesa(1)
print(Mesa1)
print("")

print("TESTE CLIENTES -------------")
Cliente1 = Cliente("Vitor", 12345, "vitor.as.af.a", 3423526)
print(Cliente1)
Cliente2 = Cliente("Vitor2", 12222345, "vitorsgsh.as.af.a", 3423526)
print(Cliente2)

Mesa1.clientes.append(Cliente1)
print(Mesa1.numero)
Mesa1.clientes.append(Cliente2)
print(Mesa1.clientes)

Mesa1.desalocar_cliente(Cliente1)
print(Mesa1.clientes)
print("")
print('TESTE CLIENTES --------------')
Biblioteca = BibliotecaDeMusicas()
Fila1 = Fila_Karaoke()

print("")
print('TESTE MUSICA, GENERO, IDIOMA, ARTISTA----')
Idioma1 = Idioma("Novo_idioma")
Artista1 = Artista("novo_artista")
Genero1 = Genero("Genro_Novo")
Musica1 = Musica("nova_musica", Artista1, Genero1, Idioma1)


Cliente1.adicionar_musica_biblioteca(Biblioteca, Musica1)


print("Musicas na biblioteca:")
print(Biblioteca.generos)
print(Biblioteca.idiomas)
Cliente1.pedir_musica(Biblioteca, Fila1)

print('Musica na biblioteca:')
print(Fila1.fila_karaoke)
