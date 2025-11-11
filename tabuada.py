def tabuada(valor, inicio = 0, fim = 10, *, imprimir = False):
    if inicio > fim: inicio, fim = fim, inicio

    texto = ''

    for i in range(inicio, fim + 1):
        texto += f'{i} X {valor} = {i * valor}\n'
    
    if imprimir: print(texto)

    return texto