# Projeto TC 2019.2

Este projeto é parte da nota da disciplina de Teoria da Computação(TC) de 2019.2

# Problema

## Resumo

O projeto consistirá da implementação de um simulador para autômatos finitos e dos principais algoritmos existente sobre autômatos. O projeto deverá ser feito para ser usado através da linha de comando, e poderá ser desenvolvido em Java ou em Python.

## Formato do arquivo de entrada

O o arquivo de entrada contendo a descrição do autômato deverá obedecer ao seguinte formato:

```
estados <lista com os nomes dos estados>
inicial <nome do estado inicial>
aceita <lista com os nomes dos estados de aceitação>
<transições>
````

Note que estados, inicial e aceita são palavras reservadas.

`<transições>` descreve cada transição do autômato (é uma lista) e tem o formato:
```
estado1 estado2 0
````

siginifcando que a transição leva do estado1 para o estado2 lendo o símbolo 0.
Um exemplo de arquivo de entrada seria:
```
estados A, B
inicial A
aceita B
A B 0
B A 0
A A 1
B B 1
```
Todos os autômatos que serão testados terão esse formato. Use o símbolo e para denotar o símbolo vazio.

`Importante`: o autômato será fornecido como um arquivo. Eu não vou ficar digitando na entrada. Seu programa precisa ler esse arquivo com a descrição do autômato.

`Importante`: toda a execução de seu programa deverá ser feita via CLI. Tanto do simulador quando da computação das operações.

## Simulador (obrigatório)

O simulador deverá receber na entrada o nome de um arquivo contendo a descrição do autômato e a entrada que será processada pelo autômato. Por exemplo:
```
$ nome_do_executável arquivo_do_automato 101
```
Imprima um traço na tela mostrando em qual estado o autômato se encontra e o que falta ler. Ao final diga se a palavra foi aceita ou não. Por exemplo, para o autômato acima a saída poderia ser:
```
Estado           Palavra
A                101
A                01
B                1
B                e
A palavra foi aceita
````

## Operações

A seguinte operação é obrigatória:

1. Transformar de não-determinístico para determinístico: receba um autômato na entrada e mostre na saída padrão a versão determinística dele.

<p>Além da operação acima, cada grupo deverá escolher pelo menos duas das operações a seguir para serem implementadas.</p>

1. União: receba dois autômatos e gere um terceiro que é a união dos outros dois e mostre na saída padrão.
2. Intersecção: receba dois autômatos e gere um terceiro que é a intersecção dos outros dois e mostre na saída padrão.
3. Complemento: receba um autômato e gere um segundo que é o complemento do outro e mostre na saída padrão.
4. Estrela: receba um autômato e gere um segundo que é o resultado da operação estrela do outro e mostre na saída padrão.

Cada operação adicional valerá pontuação extra.

## Opcional
<p>
Minimização de autômatos. Existe um algoritmo para minimizar um autômato reduzindo o número de estados ao mínimo. Esse algoritmo não foi discutido em sala de aula. A implementação desse algoritmo vale pontuação adicional, inclusive podendo transferir para as provas se o projeto tiver atingido a nota máxima.</p>

# Solução
Nesta seção será discutida a resolução do problema
## Pseudo Código da Função de transição
Abaixo segue a ideia de uma função de transição de estado:
````
function transicao(estado_atual, lista_de_transicoes, palavra):
    if(estado_atual in estado_de_aceitacao):
        return "palavra aceita"
    else if (palavra.isvazia()):
        return "Palavra não aceita"
    else:
        for elemento in lista:
            if (elemento[0] == estado_atual and elemento[2] == palavra[0]):
                estado_atual = elemento[1]
                transicao(estado_atual, lista, palavra[1:])
            else:
                return "Palavra não aceita"
```
