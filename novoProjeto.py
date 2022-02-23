from time import sleep
from subprocess import run
import os

def novaPasta(diretório):
    return ['mkdir', f'{diretório}']

while True:
    temDiretórioNovo = input('Já criou uma pasta? ')

    if temDiretórioNovo == 's':
        print('Nome da pasta ou caminho do diretório')
        novoDiretório = input('Nem erre! ')
        break
    elif temDiretórioNovo == 'n':
        print('Ok vou criar uma pasta.')
        novoDiretório = input('Nome da pasta: ')
        run(novaPasta(novoDiretório))
        break

nomeArquivo = input('Nome do arquivo: ')

comando = ['cp', 'basicasso.py', f'{novoDiretório}/{nomeArquivo}.py']
print(f'{comando[0]} {comando[1]} {comando[2]}')
run(comando)
