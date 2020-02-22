Existem situações em que precisamos trabalhar com repetições de repetições.

## Exercício 1:
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Dica: lembre-se que a função print pode receber um parametro 'end', que altera o último caractere da cadeia, tornando possível a remoção da quebra de linha (reveja as vídeo-aulas)

## Exercício 2:
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

## Exercício 3: Primos
Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

## Exercício 4: Soma das hipotenusas
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, nn é uma hipotenusa se existem números inteiros i e j tais que: n² = i² + j²

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo nn e devolva a soma de todos os inteiros entre 1 e nn que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até nn testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

## Links Relacionados
- [Repetições Encaixadas](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula07.html)
- [Exercícios](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula08.html)
