from funçõesAcademia import *

while True:
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho) == True:
        i=1
        for el in baralho:
            print("{0}. {1}".format(i,el))
            i += 1
        try:
            perg2 = int(input("Escolha uma carta para empilhar (pelo número) "))
            mov = lista_movimentos_possiveis(baralho, perg2-1)
            if mov != []:
                print('Escolhas possíveis:')
                for el in mov:
                    print(str(el) + ". "+ str(baralho[el-1]))
                perg3 = int(input('Escolha um lugar para ser empilhado (pelo número) '))
                baralho = empilha(baralho, perg2-1, perg3-1)
            else:
              print('Não é possível fazer um movimento, escolha outra carta')
        except:
            print('Opção inválida. Digite um número inteiro.')
    perg = input('Quer iniciar uma rodada? s/n ')
    if perg == 'n':
        break