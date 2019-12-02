# Uso

Ferramenta desenvolvida para o Projeto da cadeira de Teoria da Computação
GEEE

Para usar nossa ferramenta: python3 main.py ou python3 main.py -h --Para ter um help
ex: $ python3 main.py

Argumentos:

-s  --simulador
-c  --conversao de AFN para AFD
-u  --uniao
-i  --intersecao
-e  --estrela
-l  --complemento

Exemplos:
$ python3 main.py -s arquivo.txt 10010
$ python3 main.py -u arquivo1.txt arquivo2.txt
$ python3 main.py -i arquivo1.txt arquivo2.txt
$ python3 main.py -c arquivo.txt
$ python3 main.py -e arquivo.txt
$ python3 main.py -l arquivo.txt

## Como executar

A projeto foi feito usando `python3`. E para executar comando deve ser de acordo com os exemplos a seguir.

### Simulador

O simulador deve receber a entrada no seguinte formato:

$ python3 main.py -s arquivo.txt palavra

exemplo de aplicação:

$ python3 main.py -s automatos/entrada.txt 101

### Transformação

A Operação de Transformação deve receber a entrada no seguinte formato:

$ python3 main.py -c arquivo.txt
Antes de realizar a conversão, é verificado se o autormato passado é uma AFN, caso sim é realizado a conversão, caso não é retornado uma mensagem informando que o mesmo ja é uma AFD.

exemplo de aplicação:

$ python3 main.py -c automatos/entrada.txt

### União

A Operação de União deve receber a entrada no seguinte formato:

$ python3 main.py -u arquivo.txt arquivo2.txt

exemplo de aplicação:

python3 main.py -u automatos/entrada1.txt automatos/entrada2.txt

### Intersecção

A Operação de Intersecção deve receber a entrada no seguinte formato:

$ python3 main.py -i arquivo.txt arquivo2.txt

exemplo de aplicação:

$ python3 main.py -i automatos/entrada1.txt automatos/entrada2.txt

### Estrela

A Operação de Estrela deve receber a entrada no seguinte formato:

$ python3 main.py -e arquivo.txt

exemplo de aplicação:

$ python3 main.py -e automatos/entrada1.txt

### Complemento

A Operação de Complemento deve receber a entrada no seguinte formato:

$ python3 main.py -l arquivo.txt
Antes de ser realizada a conversão é feita a verificação se o automato é um AFN. Se sim, é feita a conversão para AFD para facilitar a excução da operação.

exemplo de aplicação:

$ python3 main.py -l automatos/entrada1.txt