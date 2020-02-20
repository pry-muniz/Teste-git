import datetime
dia_de_nasc = datetime.date(year=1993, month=2, day=20)
def calcular_dias_de_vida(data):
    if data is None:
        erro = 'ops'
        return error
    hoje = datetime.date.today()    
    dias_de_vida = hoje - data
    return dias_de_vida

retorno = calcular_dias_de_vida(dia_de_nasc)
print(retorno)