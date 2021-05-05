import random

# Função 1 --> Cria baralho

def cria_baralho():
    num =['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    espadas=[]
    copas=[]
    ouros=[]
    paus=[]
    for el in num:
        espadas.append(el+'♠')
        copas.append(el+'♥')
        ouros.append(el+'♦')
        paus.append(el+'♣')
    baralho= espadas+copas+ouros+paus
    random.shuffle(baralho)
    return baralho

# Função 2 --> Extrair naipe da carta

def extrai_naipe(carta):
    naipe = ['♠', '♦', '♥', '♣' ]
    for i in naipe:
        if i in carta:
            return i  
            break

# Função 3 --> Extrair valor da carta

def extrai_valor(carta):
    valor = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for el in valor:
        if el in carta:
            return el
            break 

# Função 4 --> Lista dos movimentos possíveis

def lista_movimentos_possiveis(baralho,ind):
    mov=[]
    try:
        valor = extrai_valor(baralho[ind])
        naipe = extrai_naipe(baralho[ind])
    except:
        return []
    if ind == 0:
        return []
    if ind >= 3:
        if naipe in baralho[ind-3] or valor in baralho[ind-3]:
            mov.append(ind-2)
    if ind > 0:
        if naipe in baralho[ind-1] or valor in baralho[ind-1]:
            mov.append(ind)
    return mov

# Função 5 --> Empilha as cartas

def empilha(baralho,origem,destino):
    cima = baralho[origem]
    baixo = baralho[destino]
    baralho.remove(baralho[origem])
    baralho.remove(baralho[destino])
    baralho.insert(destino,cima)
    return baralho

# Função 6 --> Conferir se existem movimentos possíveis

def possui_movimentos_possiveis(baralho):
    for el in range(0,len(baralho)+1):
        try:
            if lista_movimentos_possiveis(baralho,el) != []:
                return True
                break
        except:
            pass
    return False