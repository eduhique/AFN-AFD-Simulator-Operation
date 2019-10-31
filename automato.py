import sys

# Argumentos iniciais

entrada = sys.argv
arg = ""
arquivo = ""

# Maquinda de estados

maquina = {}

try:
    arg = entrada[1]
    arquivo = open(entrada[2], 'r')
except:
  print('Ocorreu algum erro com os argumentos de entrada. arguemnto: ' + str(entrada))
  exit()

print('Argumento: %s\nLinhas do arquivo: %s\n' % (arg, entrada[2]))

while True:
    a = arquivo.readline()
    if a == '':
      break
    if a.startswith("estados "):
        aux = entrada.replace("estados ", "")
        split = aux.split(",")
        for i in range(len(split)):
            split[i] = split[i].strip()
        maquina["estados"] = split
    if a.startswith("inicial "):
        aux = entrada.replace("inicial ", "")
        maquina["inicial"] = aux
    if a.startswith("aceita "):
        aux = entrada.replace("aceita ", "")
        split = aux.split(",")
        for i in range(len(split)):
            split[i] = split[i].strip()
        maquina["aceita"] = split
        
