Loops, Condicionais, Métodos e Funções

## Exercício 1:
Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

## Exercício 2:
Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

## Exercício 3:
Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

## Exercício 4:
Crie uma sequência de números pares entre 100 e 150 e imprima na tela

## Exercício 5:
Crie uma variável chamada temperatura e atribua o valor 40. Enquanto temperatura for maior que 35, imprima as temperaturas na tela

## Exercício 6:
Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela, mas quando for encontrado o valor 23, interrompa a execução do programa

## Exercício 7:
Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista

## Exercício 8:
Transforme o resultado desta função range em uma lista: range(5, 45, 2)

## Exercício 9:
Faça a correção dos erros no código abaixo e execute o programa. Dica: são 3 erros.
```python
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30
print('Vista roupas leves.')
else
    print('Busque seus casacos.')
```

## Exercício 10:
Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na sua instrução de impressão
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."

## Exercício 11:
Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e depois faça uma chamada à função para listar os números

## Exercício 12:
Crie uam função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string

## Exercício 13:
Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e  imprima a lista

## Exercício 14:
Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

## Exercício 15:
Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 números como parâmetro e retornar a soma deles

## Exercício 16:
Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
```python
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2;
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)
```

## Exercício 17:
Abaixo você encontra uma lista com temperaturas em graus Celsius. Crie uma função anônima que converta cada temperatura para Fahrenheit. Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função  (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista. Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
```python
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(coloque_aqui_sua_função_lambda)
print (list(Fahrenheit))
```

## Exercício 18:
Crie um dicionário e liste todos os métodos e atributos do dicionário

## Exercício 19:
Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados. Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
```python
import pandas as pd
dir(pd)
```

## Exercício 20:
Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo do arquivo. Dica, use Pandas e um de seus métodos, describe(). Arquivo: "binary.csv"
```python
import pandas as pd
file_name = "binary.csv"
```

## Link Relacionados
- [Condicionais Lógicos](http://www.unicamp.br/~chibeni/textosdidaticos/condicional.pdf)
- [Deep Learning Book](http://www.deeplearningbook.com.br/)
