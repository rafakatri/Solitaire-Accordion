
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
    return baralho

# Função 2 --> Extrair naipe da carta

def extrai_naipe(carta):
    naipe = ['♠', '♦', '♥', '♣' ]
    for i in naipe:
        if i in carta:
            return i  

# Função 3 --> Extrair valor da carta

def extrai_valor(carta):
    valor = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    for el in valor:
        if el in carta:
            return el
            break 