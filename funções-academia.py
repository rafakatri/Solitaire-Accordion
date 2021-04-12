
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