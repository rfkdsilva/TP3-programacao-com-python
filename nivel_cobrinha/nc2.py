def data_por_extenso(data):
    """
    Converte uma data fornecida no formato 'dd/mm/aaaa' para sua forma por extenso, incluindo o dia, o mês e o ano.

    Args:
        data (str): A data no formato 'dd/mm/aaaa' (ex: "25/12/2024").

    Returns:
        str: A data por extenso no formato 'dia de mês de ano', onde o dia e o ano são escritos por extenso.
    """
    dia, mes, ano = data.split("/")
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas2 = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    
    extenso = ""

    dia_int = int(dia)
    if dia_int <= 19:
        extenso += dezenas[dia_int-10] if dia_int >= 10 else unidades[dia_int]
    else:
        extenso += dezenas2[dia_int // 10 - 2]
        if dia_int % 10 != 0:
            extenso += " e " + unidades[dia_int % 10]
    
    extenso += " de " + meses[int(mes) - 1] + " de "
    
    ano_int = int(ano)
    if ano_int == 2000:
        extenso += "dois mil"
    elif ano_int < 2100:
        extenso += "dois mil e " + unidades[ano_int % 100] if ano_int % 100 != 0 else "dois mil"
    elif ano_int == 1000:
        extenso += "mil"
    elif ano_int > 1000 and ano_int < 2000:
        extenso += "mil " + centenas[(ano_int // 100) % 10 - 1]
        if ano_int % 100 != 0:
            if ano_int % 100 < 20:
                extenso += " e " + unidades[ano_int % 100]
            else:
                extenso += " e " + dezenas2[(ano_int % 100) // 10 - 2]
                if ano_int % 10 != 0:
                    extenso += " e " + unidades[ano_int % 10]
    
    return extenso

data = input("Digite uma data no formato 'dd/mm/aaaa': ")
print(data_por_extenso(data))