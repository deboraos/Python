class Musica:
    def __init__(musica, titulo, interprete, compositor, ano):
        musica.titulo = titulo
        musica.interprete = interprete
        musica.compositor = compositor
        musica.ano = ano

class Buscador:
    def busca_por_titulo(musica, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(musica):
        playlist = [Musica("Deixa A Pepeca", "Kevin O Chris", "Kondzilla", "2020"),
                    Musica("Sequência de Toma Toma", "MC Ingryd", "MC Ingryd", "2020"),
                    Musica("Sentadão", "Pedro Sampaio", "Pedro Sampaio", "2020")]

        onde_achou = musica.busca_por_titulo(playlist, "Sentadão")

        if onde_achou == -1:
            print("A música não está na playlist")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano, sep = ', ');
