Vamos estudar agora conceitos sobre programação orientada a objetos. Serão muitos novos conceitos e sua atenção na hora de ver os vídeos e fazer os exercícios será fundamental.

## Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

## Exercício 2: Tipos de triângulos
Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que devolve uma string dizendo se o triângulo é:
- isósceles (dois lados iguais)
- equilátero (todos os lados iguais)
- escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.

## Exercício 3: Triângulos retângulos
Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.

## Exercício 4: Triângulos semelhantes
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False.

Verifique a semelhança dos triângulos através do comprimento dos lados.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

## Links Relacionados
- [Programação orientada a objetos](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula17.html#programacao-orientada-a-objetos)
- [Exercícios com objetos](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula18.html)
- [Exercícios](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula19.html)
- [Modularização, testes e reuso](https://panda.ime.usp.br/aulasPython/static/aulasPython/aula20.html)
