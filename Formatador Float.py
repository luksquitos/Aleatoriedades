string = "43.121212"


def formatador(valor: str, quant_decimais: int):
    """
    Um simples formatador de números flutuantes, humilde.
    """
    try:
        valor = float(valor)
    except:
        raise Exception ("Número não é válido")
    
    valor = str(valor)
    posicao_ponto = string.find('.')
    quant_casas_decimais = len(valor) - posicao_ponto - 1
    zeros_adicionados = quant_decimais - quant_casas_decimais 
    
    if quant_decimais > quant_casas_decimais:
        return float(valor + '0' * zeros_adicionados)
    
    return float(valor[:posicao_ponto + quant_decimais + 1:]) # O último nunca é pego

print(formatador(string, 2))