Vamos começar estudando um pouco sobre "string”: o que é, como usar e manipulação de strings. Veremos também 4 pequenos conceitos que irão nos ajudar muito na hora de programar. Além disso, a organização do programa ajuda o programador na sua tarefa, deixando o código mais fácil de ser entendido, conferido e arrumado, caso necessário. Para isso, vamos conhecer “modularização”.

## Exercício 1: Letras maiúsculas
Escreva a função maiusculas(frase) que recebe uma frase (uma string) como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

Para resolver este exercício, pode ser útil verificar uma tabela ASCII, que contém os valores de cada caractere. Ver https://pt.wikipedia.org/wiki/ASCII

Note que para simplificar a solução do exercício, as frases passadas para a sua função não possuirão caracteres que não estejam presentes na tabela ASCII apresentada, como ç, á, É, ã, etc.

Dica: Os valores apresentados na tabela são os mesmos devolvidos pela função ord apresentada nas aulas.

## Exercício 2: Menor nome
Como pedido no primeiro vídeo desta semana, escreva uma função menor_nome(nomes) que recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o primeiro nome com o menor comprimento presente na lista.

## Exercício 3: Contando vogais ou consoantes
Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

## Exercício 4: Ordem lexicográfica
Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

## Links Relacionados
- [Strings e arquivos](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula13.html)
- [Mais funções com números reais](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula14.html)
- [Mais funções com reais](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula15.html)
- [Exercícios](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula16.html)
