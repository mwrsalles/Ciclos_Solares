
"""
Created on Sat Feb  5 17:29:12 2022

@author: Marina Sales Reis
"""

#0 função que organiza as coisas em dicionários
#1 ok
#2 ok
#3 quase ok
#4 quase ok
#5 ok
#6 
#7 ok
#8
#9
#10 ok
#11 nao sei se entendi essa 
#12 ok

#posso tentar juntar a 1 e 2 com a 8 e a 9 

def main_function():
    programa_aberto = True
    print("\nBem-vindo(a) ao programa sobre manchas solares. O que gostaria de saber?")
    while programa_aberto:
        print("\n1- Máximo de manchas em determinado ano\n\
2- Mínimo de manchas em determinado ano\n\
3- Menor média mensal de dado período\n\
4- Maior média mensal de dado período\n\
5- Em quantos dias de um dado mês em um dado ano não foram observadas manchas\n\
6- Qual ano e qual mês tiveram mais dias sem manchas solares\n\
7- Qual ano e qual mês tiveram mais manchas solares\n\
8- Máximo de manchas solares em determinado período\n\
9- Mínimo de manchas solares em determinado período\n\
10- Média mensal de um dado mês para um dado ano\n\
11- O desvio padrão mensal\n\
12- Terminar programa\n")
    
        user_input = input("Digite o número referente à sua escolha \
(apenas os algarismos): ")
        if user_input == "1" or user_input == "2":
            ano = input("Por favor, digite o ano desejado no formato XXXX,\
os anos disponíveis estão entre 1818 e 2018: ")
            ColetaDadosMinMax(ano, user_input)
            
        elif user_input == "3":
            print("\nOs dados disponíveis vão de 01/1749 a 02/2021\n")
            periodo = input("Digite o período desejado para análise no formato MM/AAAA \
(exemplo: 01/1928 a 11/1929): ")
            periodo.split()
            #Media_Manchas(periodo, user_input)
            
        elif user_input == "4":
            print("\nOs dados disponíveis vão de 01/1749 a 02/2021\n")
            periodo = input("Digite o período desejado para análise no formato MM/AAAA \
(exemplo: 10/1928 a 11/1929): ")
            periodo.split()
            #Media_Manchas(periodo, user_input)
            
        elif user_input == "5":
            ano = input("Por favor, digite o ano desejado no formato XXXX, \
os anos disponíveis estão entre 1818 e 2018: ")
            mes = input("Por favor, digite o número relatvio ao mês desejado \
(exemplo: janeiro = 1)\n*OBS.: temos somentes dados até 10/2018\nDigite sua escolha: ")
            mes.replace(" ", "")
            if mes != "10":
                mes.replace("0", "")
            NenhumaMancha(mes, ano)
            
        elif user_input == "7":
            Mais_Manchas()
            
        elif user_input == "10":
            ano = input("Por favor, digite o ano desejado no formato XXXX, \
os anos disponíveis estão entre 1749 e 2021: ")
            mes = input("Por favor, digite o número relatvio ao mês desejado \
(exemplo: janeiro = 1)\n*OBS.: temos somentes dados até 02/2021\nDigite sua escolha: ")
            Media_Mes_Ano(mes, ano)
            
        elif user_input == "12":
            print("Execução finalizada.")
            programa_aberto = False
            
        elif int(user_input) < 1 or int(user_input) > 6:
            print("Entrada inválida, por favor, tente novamente.")
    return 

#def VerificarEntrada(user_input):
    

def SemDados(): #caso não existam dados para certo ano ou certo período
    erro = input("Lamentamos muito, porém não há dados disponíveis.\n\
Tecle 1 para tentar novamente com outro valor ou 2 para voltar ao menu inicial: ")
    if erro != 1 and erro != 2:
        while erro != 1 and erro != 2:
            erro = input("Valor inválido! \
Tecle 1 para tentar outro dia ou 2 para voltar ao menu inicial: ")
    elif erro == 1:
        ano = input("Por favor, digite o ano desejado no formato XXXX: ")
        return ano
    elif erro == 2:
        print("\nO que mais gostaria de saber?")
        
        
def Min_and_Max(num_manchas,user_input, ano):
    max_num = int(num_manchas[0])
    min_num = int(num_manchas[0])
    i = 0
    for elemento in num_manchas:
        if min_num > int(num_manchas[i]):
            min_num = int(num_manchas[i])
        elif int(num_manchas[i]) > max_num:
            max_num = int(num_manchas[i])
        i+=1
        
    if user_input == '1':
        print("\nO número máximo de manchas detectadas em um dia em", ano, "foi", max_num)
        print("\nO que mais gostaria de saber? ")
    elif user_input == "2":
        print("\nO número mínimo de manchas detectadas em um dia em", ano, "foi", min_num)
        print("\nO que mais gostaria de saber? ")
    elif user_input == "3":
        print("\nA menor média mensal para o período foi de", min_num, "manchas.")
        print("\nO que mais gostaria de saber? ")
    elif user_input == "4":
        print("\nA maior média mensal para o período foi de", max_num, "manchas.")
        print("\nO que mais gostaria de saber? ")
        
        
def ColetaDadosMinMax(ano,user_input):
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')
    if int(ano) < 1818 or int(ano) > 2018:
        SemDados()
        ano = SemDados()
        ColetaDadosMinMax(ano,user_input)
    else:
        num_manchas = []
        for linha in arquivo_dias: 
            if linha.startswith(ano):   
                manchas = linha[19:24]
                manchas.split()
                if manchas != "   -1":
                    num_manchas.append(manchas) 
                
        if len(manchas) == 0:
            if len(manchas) == 0:
                SemDados()
                ano = SemDados()
                ColetaDadosMinMax(ano,user_input)
    
    Min_and_Max(num_manchas,user_input, ano)
    
           
    
def NenhumaMancha(mes, ano):
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')   
    if int(ano) < 1818 or int(ano) > 2018:
        while int(ano) < 1818 or int(ano) > 2018:
            SemDados()
            ano = SemDados()
            mes = input("Por favor, digite o número relatvio ao mês desejado \
(exemplo: janeiro = 1):" )
            NenhumaMancha(mes, ano)
    elif int(mes) not in range(1, 13):
        while int(mes) not in range(1,13):
            mes = input("Entrada inválida.OBS.: temos somentes dados até 10/2018\n \
Por favor, digite o número relatvio ao mês desejado \
(exemplo: janeiro = 1): ")
            ano = input("Por favor, redigite o ano desejado no formato XXXX, \
os anos disponíveis estão entre 1818 e 2018: ")
        NenhumaMancha(mes, ano)    
        
    else:
        qtd_zeros = []
        count_zeros = 0
        for linha in arquivo_dias: 
            if linha.startswith(ano):  
                if linha[5:7] == mes or linha[5:7] == int(mes):
                    manchas = linha[19:24]
                    manchas.split()
                    if manchas != "-1":
                        qtd_zeros.append(manchas)
        for elemento in qtd_zeros:
            if int(elemento) == 0:
                count_zeros += 1
    print("\nPara", mes, "de", ano, "houve", count_zeros, 'dias em que não foi \
observada nenhuma mancha.')
    print("\nO que mais gostaria de saber? ")
    

def Media_Mes_Ano(mes, ano):
    arquivo_meses = open('SN_m_tot_V2.0.txt', 'r')
    if len(mes) == 1:
        mes = "0"+mes
    if int(ano) not in range(1749, 2022):
        SemDados()
        ano = SemDados()
        Media_Mes_Ano(mes, ano)
    elif mes not in ['01', '02', '03', '04', '05', '06', '07', '08',
                     '09', '10', '11', '12']:
        mes = input("Entrada inválida. Por favor, digite um número de 1 a 12: ")
        Media_Mes_Ano(mes, ano)
    else:
        for linha in arquivo_meses:
            if linha[:4] == ano and linha[5:7] == mes:
                media = linha[18:23]
                media.split
                data = mes+"/"+ano
                print("\nA média para", data, "é de", media, "manchas.")
                print("\nO que mais gostaria de saber? ")
            
            
def Mais_Manchas(): 
#talvez add o arquivo de dias e fazer a soma das qtd de manchas solares nesse mes e ano
    arquivo_meses = open('SN_m_tot_V2.0.txt', 'r')
    num = 0
    ano = 0
    mes = 0
    for linha in arquivo_meses:
        manchas = linha[17:24]
        manchas.split()
        if float(manchas) > float(num):
            num = manchas
            ano= linha[:4]
            mes = linha[5:7] 
            mes.split()
            data = mes+"/"+ano
        
    print("\nO maior número de manchas observado entre 1749 e fevereiro de 2021 \
foi em", data)


main_function()
