import datetime, random

# Função para incrementar o NSR sequencialmente
def increment_nsr(nsr):
    nsr += 1
    return nsr

# Função para incrementar a data sequencialmente, considerando apenas dias úteis (segunda a sexta-feira)
def increment_data(data):
    date = datetime.datetime.strptime(data, "%d%m%Y")
    date += datetime.timedelta(days=1)
    while date.weekday() > 4:  # Dias da semana são numerados de 0 a 6 (0 = segunda-feira, 6 = domingo)
        date += datetime.timedelta(days=1)
    return date.strftime("%d%m%Y")

# Função para incrementar a hora aleatoriamente 
def increment_hour(hour,variacaominaba,variacaominaci):
    time = datetime.datetime.strptime(hour, "%H%M")
    minutes_offset = random.randint(variacaominaba, variacaominaci)
    time += datetime.timedelta(minutes=minutes_offset)
    return time.strftime("%H%M")

# Função para gerar as marcações do tipo 3
def geraMarcacoes(datainicio, datafim, pis, horarios, crc, nsr,variacaominaba,variacaominaci):
    tipo = "3"
    marcacoes = []
    while datainicio <= datafim:  # Data limite
        for p in pis:  # as 4 marcações do dia por colaborador
            for horario in horarios:
                horario = increment_hour(horario, variacaominaba, variacaominaci) #muda o horario baseado na variacao de minutos aleatoria entre as var variacaominaba e variacaominaci
                linha = str(nsr).zfill(9) + tipo + datainicio + horario + p + crc #monta nsr da primeira marcação
                marcacoes.append(linha) #coloca a linha em um array
                nsr = increment_nsr(nsr) #incrementa o nsr
        datainicio = increment_data(datainicio) #vai para o próximo dia
    return marcacoes