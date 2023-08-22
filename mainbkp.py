import headerFotterGenerico, tipo3
from datetime import datetime
# Variáveis iniciais para linhas do tipo 3 marcação de ponto
nsr = 1  #NSR inicial
datainicio = "01012023" #data inicial
datafim = "22062023" #data fim
horarios = ["0800","1200","1300","1800", "2000", "2200"] #horarios das marcações base
pis = ["010248480909", "010037812979", "20603799463", "12916553098"] #pis dos funcionarios
crc = "BDCE" #crc aleatorio até onde sei o sistema não valida isso mas qualquer coisa da para fazer uma função para gerar o valor e colocar dentro da funcao geraMarcacoes no arquivo tipo3.py
variacaominaba = -30 #variacao de tempo em minutos abaixo do horario base
variacaominaci = 5 #variacao de tempo em minutos acima do horario base

marcacoes = tipo3.geraMarcacoes(datainicio, datafim, pis, horarios, crc, nsr,variacaominaba,variacaominaci)# Gera as linhas tipo 3 registro/marcação de ponto 
headerFotter = headerFotterGenerico.headerFotterGenerico()#Gera header e footer

now = (datetime.now()).strftime("%Hh%Mm%Ss %d-%m-%Y")#Gera horario para o nome do arquivo


with open(f'AFD/afdGeradorFavaro {now}.txt', '+wt') as file: #Cria arquivo ou sobescreve um com o mesmo nome já existente
    file.write(headerFotter[0] + '\n') #insere header
    for marcao in marcacoes: # Loop para inserir os registros de ponto
        file.write(marcao + '\n') #insere marcação uma a uma
    file.write(headerFotter[1]) #insere fotter
file.close

