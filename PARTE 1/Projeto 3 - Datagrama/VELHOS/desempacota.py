# LER 65536 BITS!!!!!!!!!!!!!!!!!!!! O tamanho reflete na representacao em hexa, mas nao na contagem necessaria

def main(dado):
    # Info de HEAD
    headSize = 4
  
    # Info de EOP
    confirmaEop = [hex(255), hex(254), hex(253), hex(252)]
  
    count = 0
    head = []
    pay = []
    eop = []
  
    for i in dado:
        while count < headSize:
            head.append(i)
            count += 1
        tamanho = head[0] * 256 + head[1]
        pacote = head[2]
        maxPacotes = head[3]

    count = 0
    for i in dado:    
        if count >= headSize & count < (headSize + tamanho):
            pay.append(i)
        elif count >= (headSize + tamanho) & count < (tamanho + 2*headSize):
            eop.append(i)
        else:
            break
        count += 1
    
    pontos = 0
    correto = False
    corretoEop = False
    corretoPay = False

    for i in len(eop):
        if eop[i] == confirmaEop[i]:
            pontos += 1 
    if pontos == 4:
        corretoEop = True

    if len(head) + len(pay) + len(eop) == tamanho + 2*headSize:
        corretoPay == True
    
    if corretoPay == True & corretoEop == True:
        correto = True


if __name__ == "__main__":
    pass