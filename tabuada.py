def tabuada(valor, inicio = 0, fim = 10, *, imprimir = False):
    # Troca os valores de inicio e fim caso o valor de inicio seja maior que o valor de fim
    if inicio > fim: inicio, fim = fim, inicio
    # Inicia a variavel texto como string vazia
    texto = ''
    # Laco for para iterar sobre os valores inteiros a partir de inicio ate fim
    for i in range(inicio, fim + 1):
        # Acrescenta uma linha da tabuada a texto
        texto += f'{i} X {valor} = {i * valor}\n'
    # Imprime a tabuada completa no console se o parametro imprimir for True
    if imprimir: print(texto)
    # Retorna o texto gerado contendo a tabuada
    return texto