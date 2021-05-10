from funçõesAcademia import *
import colorama
from colorama import Fore

while True:
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho) == True:
        i=1
        for el in baralho:
            if '♥' in el:
                print(Fore.RED + "{0}. {1}".format(i,el))
            elif '♠' in el:
                print(Fore.BLUE + '{0}. {1}'.format(i,el))
            elif '♣' in el:
                print(Fore.GREEN + '{0}. {1}'.format(i,el))
            elif '♦' in el:
                print(Fore.MAGENTA + '{0}. {1}'.format(i,el))
            i += 1
        try:
            perg2 = int(input("Escolha uma carta para empilhar (pelo número) "))
            mov = lista_movimentos_possiveis(baralho, perg2-1)
            if mov != []:
                print('Escolhas possíveis:')
                for el in mov:
                    if '♥' in baralho[el-1]:
                        print(Fore.RED + str(el) + ". "+ str(baralho[el-1]))
                    elif '♠' in baralho[el-1]:
                        print(Fore.BLUE + str(el) + ". "+ str(baralho[el-1]))
                    elif '♣' in baralho[el-1]:
                        print(Fore.GREEN+ str(el) + ". "+ str(baralho[el-1]))
                    elif '♦' in baralho[el-1]:
                        print(Fore.MAGENTA + str(el) + ". "+ str(baralho[el-1]))
                perg3 = int(input('Escolha um lugar para ser empilhado (pelo número) '))
                if perg3 in mov:
                    baralho = empilha(baralho, perg2-1, perg3-1)
                else:
                    print('Opção inválida')
            else:
              print('Não é possível fazer um movimento, escolha outra carta')
        except:
            print('Opção inválida. Digite um número inteiro.')
    perg = input('Quer iniciar uma rodada? s/n ')
    if perg == 'n':
        break