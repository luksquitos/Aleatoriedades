# Este exercício é somente para registrar um método dos dicionários que ví num vídeo do Youtube.

from pprint import pprint

frase = "estou estudando atualmente sobre machine learning".replace(" ", "")
letras_separadas = {}

for letra in frase:
    letras_separadas.setdefault(letra, 0)
    letras_separadas[letra] += 1
pprint(letras_separadas)

