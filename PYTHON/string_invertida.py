palavra = list(input('Digite uma palavra: '))
copia = palavra.copy()
vazio = []

for i in range(len(copia) -1, -1, -1):
   vazio.append(copia[i])


#palavra[0], palavra[-1] = palavra[-1], palavra[0]

copia = ''.join(copia)
invertido = ''.join(vazio)
if copia == invertido:
   print(invertido)
   print('é um palíndromo')
else:
   print(invertido)
   print('não é palíndromo')
