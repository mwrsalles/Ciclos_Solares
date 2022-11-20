def main_function():
"""
Essa função deve ser chamada para que o programa inicie, ela se refere ao menu para o usuário.

Args.: nenhum 

Returns: varia de acordo com o input do usuário; 

chama cada função de coleta de dados dependendo da escolha do usuário, ou fecha o programa.

"""
    programa_aberto = True
    print("\nBem-vindo(a) ao programa sobre manchas solares. O que gostaria de saber?") #menu do programa
    while programa_aberto:
        print("\n1- Máximo de manchas em determinado ano\n\
2- Mínimo de manchas em determinado ano\n\
3- Menor média mensal de dado período\n\
4- Maior média mensal de dado período\n\
5- Em quantos dias de um dado mês em um dado ano não foram observadas manchas\n\
6- Qual ano e qual mês tiveram mais dias sem manchas solares\n\
7- Qual ano e qual mês tiveram mais manchas solares\n\
8- Máximo e mínimo de manchas solares em determinado período\n\
9- Média mensal de um dado mês para uma data específica\n\
10- Média anual de manchas para o ano escolhido\n\
11- O desvio padrão mensal de cada mês para um ano específico\n\
12- As datas de início e término e a duração de um ciclo solar específico\n\
13- Terminar programa\n")
    
        user_input = input("Digite o número referente à sua escolha \
(apenas os algarismos): ")                                      #escolha da informação desejada pelo usuário
        if user_input == "1" or user_input == "2":
            ano = input("Por favor, digite o ano dos dados desejados no formato XXXX, \
os anos disponíveis estão entre 1818 e 2018: ")
            try: #verificação de entrada
                if type(int(ano)) == int:
                    ColetaDadosMinMax(ano, user_input)
                    print("\n=============================================================\
============") #organização do menu
                    print("\nO que mais gostaria de saber? ")
            except:
                print("\nEntrada inválida. Tente novamente.")
            
        elif user_input == "3"or user_input == "4":
            periodo = input("Digite o período desejado para análise no formato MM/AAAA \
(exemplo: 01/1928 a 11/1929): ")
            periodo.split()
            Media_Manchas(periodo, user_input)
            print("\n=============================================================\
============")
            print("\nO que mais gostaria de saber? ")
            
        elif user_input == "5":
            ano = input("Por favor, digite o ano dos dados desejados no formato XXXX, \
os anos disponíveis estão entre 1818 e 2018: ")
            
            try: #verificação de entrada
                if type(int(ano)) == int:
                    mes = input("Por favor, digite o número relativo ao mês desejado \
(exemplo: janeiro = 1)\n*OBS.: temos somentes dados até 10/2018\nDigite sua escolha: ")
                    mes.replace(" ", "")
                    try:
                        if type(int(mes)) == int:
                            if mes != "10":
                                mes.replace("0", "") #ajuste na entrada do usuário
                            NenhumaMancha(mes, ano)
                            print("\n=============================================================\
============")
                  
                            print("\nO que mais gostaria de saber? ")
                    except:
                        print("\nEntrada inválida. Tente novamente")
            
            except:
                print("\nEntrada inválida. Tente novamente")
            
            
        elif user_input == "6":
            DataSem()
            print("\n=============================================================\
============")
            print("\nO que mais gostaria de saber? ")
            
        elif user_input == "7":
            Mais_Manchas()
            print("\n=============================================================\
============")
            print("\nO que mais gostaria de saber? ")
            
        elif user_input == "8":
            periodo = input("Digite o período desejado para análise no formato MM/AAAA \
(exemplo: 01/1928 a 11/1929): ")
            periodo.split()
            Manchas_Periodo(periodo, user_input)
            print("\n=============================================================\
============")
            print("\nO que mais gostaria de saber? ")
            
        elif user_input == "9":
            ano = input("Por favor, digite o ano dos dados desejados no formato XXXX, \
os anos disponíveis estão entre 1749 e 2021: ")
            
            try: #verificação de entrada
                if type(int(ano)) == int:
                    mes = input("Por favor, digite o número relativo ao mês desejado \
(exemplo: janeiro = 1)\n*OBS.: temos somentes dados até 10/2018\nDigite sua escolha: ")
                    mes.replace(" ", "")
                    try:
                        if type(int(mes)) == int:
                            if mes != "10":
                                mes.replace("0", "") #ajuste na entrada do usuário
                            Media_Mes_Ano(mes, ano)
                            print("\n=============================================================\
============")
                  
                            print("\nO que mais gostaria de saber? ")
                    except:
                        print("\nEntrada inválida. Tente novamente")
            
            except:
                print("\nEntrada inválida. Tente novamente")
            
        elif user_input == "10":
            year = int(input("Por favor, digite o ano dos dados desejados no formato XXXX: "))
            try: #verificação de entrada
                if type(int(year)) == int:
                    Media_ano(year)
                    print("\n=============================================================\
============") #organização do menu
                    print("\nO que mais gostaria de saber? ")
            except:
                print("\nEntrada inválida. Tente novamente.")
            
        elif user_input == "11":
            ano = input("Por favor, digite o ano dos dados desejados no formato XXXX: ")
            try:
                if type(int(ano)) == int:
                    DesvioMensalAno(int(ano))
                    print("\n=============================================================\
============") #organização do menu
                    print("\nO que mais gostaria de saber? ")
            except:
                print("\nEntrada inválida. Tente novamente.")
            
        elif user_input == "12":
            ciclo = int(input("Por favor, digite o número do ciclo desejado, \
escrevendo apenas o número referente ao ciclo (exemplo: ciclo 1 = 1): "))
            try:
                if type(int(ciclo)) == int:
                    CicloSolar(ciclo)
                    print("\n=============================================================\
============") #organização do menu
                    print("\nO que mais gostaria de saber? ")
            except:
                print("\nEntrada inválida. Tente novamente.")
            
        elif user_input == "13":
            print("Execução finalizada. Obrigada por utilizar o programa :)")
            programa_aberto = False
            
        elif type(user_input) != int or int(user_input) < 1 or int(user_input) > 13: #tratamento da entrada do usuário no menu
            print("Entrada inválida, por favor, tente novamente.")
    return 


def dicionario_dias():
"""
Lê os dados de dia, mês, ano e número de manchas do arquivo 'SN_d_tot_V2.0.txt' e organiza em dicionário aninhado 

Arquivos necessários: SN_d_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo

Args.: nenhum 

Return: dic_dias (o dicionário elaborado com os dados)
"""
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')
    dic_dias = {} #dicionário que ao final conterá as informações desejadas
    ano = 0
    mes = 0 
    for linha in arquivo_dias:
        novo_ano = int(linha[:4])
        if ano != novo_ano:
            ano = novo_ano
            dic_dias[ano] = {} #adiciona o ano e cria um novo dicionário para cada ano
        novo_mes = int(linha[5:7])
        if mes != novo_mes:
            mes = novo_mes 
            dic_dias[ano][mes] = {} #adiciona o mês e cria um novo dicionário para cada mês
        dia = int(linha[8:10])
        manchas = linha[20:24]
        manchas = int(manchas)
        dic_dias[ano][mes][dia] = manchas #adiciona os dias e número de manchas em cada dia 
    return dic_dias

def dicionario_desvio_dias():
"""
Lê os dados de dia, mês, ano e desvio padrão do arquivo 'SN_d_tot_V2.0.txt' e organiza em dicionário aninhado 

Função usada no cálculo do desvio padrão mensal 

Arquivos necessários: SN_d_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo

Args.: nenhum 

Return: dic_dias (o dicionário elaborado com os dados)
"""
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')
    desv_dias = {} #dicionário que no final conterá as informações desejadas
    ano = 0
    mes = 0 
    for linha in arquivo_dias:
        novo_ano = int(linha[:4])
        if ano != novo_ano:
            ano = novo_ano
            desv_dias[ano] = {} #adiciona os anos e cria um dicionário para cada ano
        novo_mes = int(linha[5:7])
        if mes != novo_mes:
            mes = novo_mes 
            desv_dias[ano][mes] = {} #adiciona os meses e cria um dicionário para cada mês
        dia = int(linha[8:10])
        desvio = linha[26:30]
        desvio = float(desvio)
        desv_dias[ano][mes][dia] = desvio #adiciona os dias e os valores de desvio padrão para cada dia 
    return desv_dias

def dicionario_observacoes_dias():
"""
Lê os dados de dia, mês, ano e número de observações do arquivo 'SN_d_tot_V2.0.txt' e organiza em dicionário aninhado

Função usada no cálculo do desvio padrão mensal

Arquivos necessários: SN_d_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo

Args.: nenhum 

Return: dic_dias (o dicionário elaborado com os dados)
"""
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')
    obs_dias = {} #dicionário que ao final conterá a informação desejada
    ano = 0
    mes = 0 
    for linha in arquivo_dias:
        novo_ano = int(linha[:4])
        if ano != novo_ano:
            ano = novo_ano
            obs_dias[ano] = {} #adiciona os anos e um dicionário para cada ano
        novo_mes = int(linha[5:7])
        if mes != novo_mes:
            mes = novo_mes 
            obs_dias[ano][mes] = {} #adiciona os meses e um dicionário para cada mês
        dia = int(linha[8:10])
        num_obs = linha[31:36]
        num_obs = int(num_obs)
        obs_dias[ano][mes][dia] = num_obs #adiciona os dias e o número de observações para cada dia 
    return obs_dias

def dicionario_meses():
"""
Lê os dados de mês, ano e média de manchas do arquivo 'SN_m_tot_V2.0.txt' e organiza em dicionário aninhado 

Arquivos necessários: SN_m_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo

Args.: nenhum 

Return: dic_meses (o dicionário elaborado com os dados)
"""
    arquivo_meses = open('SN_m_tot_V2.0.txt', 'r')
    dic_meses = {} #dicionário que ao final conterá as informações desejadas
    ano = 0
    mes = 0 
    for linha in arquivo_meses:
        novo_ano = int(linha[:4])
        if ano != novo_ano:
            ano = novo_ano
            dic_meses[ano] = {} #adiciona o ano e um dicionário novo para cada ano
        novo_mes = int(linha[5:7])
        if mes != novo_mes:
            mes = novo_mes 
            manchas = linha[18:23]
            manchas = float(manchas)
            dic_meses[ano][mes] = manchas #adiciona os meses e a média de manchas para cada mês
    return dic_meses

def SemDados(): #caso não existam dados para certo ano ou certo período
"""
Pede novos dados para usuário quando as informações solicitadas não são encontradas nos arquivos

Args.: nenhum 

Return: novo ano escolhido pelo usuário ou o menu, caso ele deseje retornar para o menu
"""
    erro = input("Lamentamos muito, porém não há dados disponíveis.\n\
Tecle 1 para tentar novamente com outro valor ou 2 para voltar ao menu inicial: ") #dá chance de escolha ao usuário para o que o programa fará 
    if erro != "1" and erro != "2":
        while erro != "1" and erro != "2":
            erro = input("Valor inválido! \
Tecle 1 para tentar outro dia ou 2 para voltar ao menu inicial: ")
    if str(erro) == "1":#deixa que o usuário escolha uma nova entrada de ano
        ano = input("Por favor, digite o ano desejado no formato XXXX: ")
        return ano
    elif str(erro) == "2": #finaliza essa função > retorna ao menu inicial 
        print("\nRetornando ao menu inicial...")
        print("\n=============================================================\
============")
        main_function()
        
def Min_and_Max(num_manchas,user_input, ano):
"""
A função é chamada por outra função (ColetaDadosMinMax) e usa os dados para:

- retornar o valor máximo de manchas vistas em um único dia para um ano X; 

- retornar o valor mínimo de manchas vistas em um único dia para um ano X; 

- retonar a maior média mensal em um ano; 

- retornar a menor média mensal em um ano;

- retornar o número mínimo e máximo de manchas em um período dado. 

Args.: uma lista com o número de manchas do dado ano (num_manchas), 

o input incial do usuário no menu, referente ao que ele gostaria de saber (user_input),

o ano referente aos dados desejados (ano)

Return: retorna os dados desejados a depender do valor de user_input
"""
    max_num = num_manchas[0]
    min_num = num_manchas[0]
    i = 0
    for elemento in num_manchas:
        if min_num > float(num_manchas[i]):
            min_num = float(num_manchas[i])
        elif float(num_manchas[i]) > max_num:
            max_num = float(num_manchas[i])
        i+=1
        
    if str(user_input) == '1':
        print("\nO número máximo de manchas detectadas em um dia em", ano, "foi", int(max_num))
    elif str(user_input) == "2":
        print("\nO número mínimo de manchas detectadas em um dia em", ano, "foi", int(min_num))
    elif str(user_input) == "3":
        print("\nA menor média mensal para o período foi de", min_num, "manchas.")
    elif str(user_input) == "4":
        print("\nA maior média mensal para o período foi de", max_num, "manchas.") 
    elif str(user_input) == "8":
        print("\nO número máximo de manchas no período foi", int(max_num), "manchas o número \
mínimo de manchas no período foi", int(min_num), "manchas.")
        
def ColetaDadosMinMax(ano,user_input):
"""
A função é intermediária entre o menu e a função Min_and_Max

Arquivos necessários: SN_d_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo, o arquivo ter anos além do arquivo padrão utilizado (1818-2018)

Args.: ano e user_input (entradas do usuário no menu)

Return: chama a função Min_and_Max se as entradas estiverem corretas e a função SemDados se as entradas forem inválidas
"""    
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')
    if int(ano) < 1818 or int(ano) > 2018:
        ano = SemDados()
        num_manchas = []
        for linha in arquivo_dias: #lê as linhas do arquivo 
            if linha.startswith(str(ano)):   #compara se a linha possui as informações desejadas
                manchas = int(linha[19:24])
                if manchas != -1:
                    num_manchas.append(manchas)
    else:
        num_manchas = []
        for linha in arquivo_dias: #lê as linhas do arquivo 
            if linha.startswith(str(ano)):   #compara se a linha possui as informações desejadas
                manchas = int(linha[19:24])
                if manchas != -1:
                    num_manchas.append(manchas) 
                
        if len(num_manchas) == 0:
            ano = SemDados()
            ColetaDadosMinMax(ano,user_input)
    
    Min_and_Max(num_manchas,user_input, ano)
    
def Media_Manchas(periodo, user_input): 
"""
A função é intermediária entre o menu e a função Min_and_Max

Ela se refere ao cálculo da maior ou menor média mensal em um período dado.

Para que ela funcione, é necessária a função dicionario_meses()

Possíveis erros: o código não roda se não houver a função dicionario_meses

A função dicionario_meses() não roda se não houver o arquivo de dados mensais.

Args.: periodo e user_input (entradas do usuário no menu)

Return: chama a função Min_and_Max se as entradas estiverem corretas e a função SemDados se as entradas forem inválidas
"""    
    dicionario = dicionario_meses() #pega os dados no dicionario de dados mensais 
    num_manchas = []
    if len(periodo) != 17 or int(periodo[13:]) < int(periodo[3:7]): #verifica a entrada do usuário 
        periodo = input("\nEntrada não aceita. Por favor, digite o período desejado para análise no formato MM/AAAA \
(exemplo: 01/1928 a 11/1929): ") 
        Media_Manchas(periodo, user_input)
    if int(periodo[3:7]) not in dicionario or int(periodo[13:]) not in dicionario: #verifica se os dados solicitados existem
        periodo = input("\nNão encontramos dados para esse período. Por favor, \
digite um novo período para análise no formato MM/AAAA (exemplo: 01/1928 a 11/1929): ")
        Media_Manchas(periodo, user_input)
    for ano in dicionario.keys():
        if str(ano) == (periodo[3:7]): #distribui a entrada do usuário nas variáveis necessárias
            mes1 = periodo[:2]
            mes2 = periodo[10:12]
            ano2 = periodo[13:]
            for mes in dicionario[ano]: #corrige as variáveis para ficarem de acordo como os dados do dicionário 
                if mes1.startswith("0"):
                    mes1 = mes1[1:]
                if mes2.startswith("0"):
                    mes2 = mes2[1:]
                if mes1 == str(mes):
                    while mes <= int(mes2) or str(ano) != ano2: #coleta os dados necessários e adiciona na lista
                        if mes == 13:
                            mes = 1
                            ano +=1
                        media = dicionario[ano][mes]
                        num_manchas.append(media)
                        mes += 1
           
    Min_and_Max(num_manchas, user_input, 0)    
    
def NenhumaMancha(mes, ano):
"""
Função referente à contagem de dias em um determinado mês de um determinado ano em que não foram observadas manchas solares

Arquivos necessários: SN_d_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo, o arquivo ter anos além do arquivo padrão utilizado (1818-2018)

Args.: ano e mês (entradas do usuário no menu)

Return: printa o número de dias no mês e ano em que não houve manchas solares 
"""    
    arquivo_dias = open('SN_d_tot_V2.0.txt', 'r')   
    if int(ano) < 1818 or int(ano) > 2018: #tratamento de dados relacionado ao arquivo utilizado 
        while int(ano) < 1818 or int(ano) > 2018:
            ano = SemDados()
            mes = input("Por favor, digite o número relativo ao mês desejado \
(exemplo: janeiro = 1):" )
        qtd_zeros = []
        count_zeros = 0
        for linha in arquivo_dias: #lê os dados de cada linha do arquivo 
            if linha.startswith(ano):  #compara os dados de cada linha com os dados solicitados pelo usuário
                if linha[5:7] == mes or int(linha[5:7]) == int(mes):
                    manchas = linha[19:24]
                    qtd_zeros.append(manchas)
        for elemento in qtd_zeros:
            if int(elemento) == 0:
                count_zeros += 1  
            
    elif int(mes) not in range(1, 13):
        while int(mes) not in range(1,13):
            mes = input("Entrada inválida. OBS.: temos somentes dados até 10/2018\n\
Por favor, digite o número relativo ao mês desejado \
(exemplo: janeiro = 1): ")
            ano = input("Por favor, redigite o ano desejado no formato XXXX, \
os anos disponíveis estão entre 1818 e 2018: ") 
        qtd_zeros = []
        count_zeros = 0
        for linha in arquivo_dias: #lê os dados de cada linha do arquivo 
            if linha.startswith(ano):  #compara os dados de cada linha com os dados solicitados pelo usuário
                if linha[5:7] == mes or int(linha[5:7]) == int(mes):
                    manchas = linha[19:24]
                    qtd_zeros.append(manchas)
        for elemento in qtd_zeros:
            if int(elemento) == 0:
                count_zeros += 1  
        
    else:
        qtd_zeros = []
        count_zeros = 0
        for linha in arquivo_dias: #lê os dados de cada linha do arquivo 
            if linha.startswith(ano):  #compara os dados de cada linha com os dados solicitados pelo usuário
                if linha[5:7] == mes or int(linha[5:7]) == int(mes):
                    manchas = linha[19:24]
                    qtd_zeros.append(manchas)
        for elemento in qtd_zeros:
            if int(elemento) == 0:
                count_zeros += 1
    print("\nPara", mes, "de", ano, "houve", count_zeros, 'dias em que não foi \
observada nenhuma mancha.')   
    
def Manchas_Periodo(periodo, user_input): 
"""
Função referente ao cálculo do maior e menor número de manchas em determinado período

Para que ela funcione, é necessária a função dicionario_dias(), a qual necessita do arquivo SN_d_tot_V2.0.txt

Possíveis erros: a função não roda sem a outra função dicionario_dias(). 
O código da função dicionario_dias() não roda se não houver arquivo.

Args.: periodo, user_input (entradas do usuário no menu)

Return: chama a função Max_and_Min que printa o maior e o menor número de manchas no período escolhido
"""    
    dicionario = dicionario_dias() #pega os dados do dicionario de dados diários
    num_manchas = []
    if len(periodo) != 17 or int(periodo[13:]) < int(periodo[3:7]): #verifica a entrada do usuário
        periodo = input("\nEntrada não aceita. Por favor, digite o período desejado para análise no formato MM/AAAA \
(exemplo: 01/1928 a 11/1929): ") 
        Manchas_Periodo(periodo, user_input)
    if int(periodo[3:7]) not in dicionario or int(periodo[13:]) not in dicionario: #verifica se os dados pedidos existem 
        periodo = input("\nNão encontramos dados para esse período. Por favor, \
digite um novo período para análise no formato MM/AAAA (exemplo: 01/1928 a 11/1929): ")
        Manchas_Periodo(periodo, user_input)
    for ano in dicionario.keys():
        if str(ano) == (periodo[3:7]): #arruma as variaveis de acordo com os dados do periodo 
            mes1 = periodo[:2]
            mes2 = periodo[10:12]
            ano2 = periodo[13:]
            for mes in dicionario[ano]: #corrige as variaveis para ficarem de acordo com os dados do dicionario 
                if mes1.startswith("0"):
                    mes1 = mes1[1:]
                if mes2.startswith("0"):
                    mes2 = mes2[1:]
                if mes1 == str(mes):
                    while mes <= int(mes2) or str(ano) != ano2:
                        if mes == 13:
                            mes = 1
                            ano +=1
                        for dia in dicionario[ano][mes]: #seleciona os dados necessários e insere esses dados na lista 
                            if dicionario[ano][mes][dia] != -1:
                                manchas = dicionario[ano][mes][dia]
                                num_manchas.append(manchas)
                        mes += 1
           
    Min_and_Max(num_manchas, user_input, 0)  
    
def Media_Mes_Ano(mes, ano):
"""
Função devolve qual foi o número médio de manchas observadas em uma data específica 

Arquivos necessários: SN_m_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo, o arquivo ter anos além do arquivo padrão utilizado (1749-2021)

Args.: ano e mês (entradas do usuário no menu)

Return: printa o número média de manchas observadas no mês e ano solicitados
"""    
    arquivo_meses = open('SN_m_tot_V2.0.txt', 'r')
    if len(mes) == 1: #tratamento do input do usuário para o funcionamento efetivo da função
        mes = "0"+mes
    if int(ano) not in range(1749, 2022): #tratamento de dados relativo ao arquivo utilizado 
        ano = SemDados()
        for linha in arquivo_meses: #lê cada linha do arquivo 
            if linha[:4] == ano and linha[5:7] == mes: #verifica se dados são compatíveis com o desejado pelo usuário
                media = float(linha[18:23]) #pega a média 
                data = mes+"/"+ano
                print("\nA média para", data, "é de", media, "manchas.")
    elif mes not in ['01', '02', '03', '04', '05', '06', '07', '08',
                     '09', '10', '11', '12']:
        mes = input("Entrada inválida. Por favor, digite um número de 1 a 12: ")
        for linha in arquivo_meses: #lê cada linha do arquivo 
            if linha[:4] == ano and linha[5:7] == mes: #verifica se dados são compatíveis com o desejado pelo usuário
                media = float(linha[18:23]) #pega a média 
                data = mes+"/"+ano
                print("\nA média para", data, "é de", media, "manchas.")
    else:
        for linha in arquivo_meses: #lê cada linha do arquivo 
            if linha[:4] == ano and linha[5:7] == mes: #verifica se dados são compatíveis com o desejado pelo usuário
                media = float(linha[18:23]) #pega a média 
                data = mes+"/"+ano
                print("\nA média para", data, "é de", media, "manchas.")    
                
def Mais_Manchas(): 
"""
Função devolve qual foi o mês e o ano em que foram observadas mais manchas solares 

Arquivos necessários: SN_m_tot_V2.0.txt

Possíveis erros: o código não roda se não houver arquivo
Args.: nenhum

Return: printa os dados solicitados e depois retorna o usuário para o menu
"""    
    arquivo_meses = open('SN_m_tot_V2.0.txt', 'r')
    num = 0
    ano = 0
    mes = 0
    for linha in arquivo_meses: #lê as linhas do arquivo
        manchas = linha[17:24] #pega o dado de manchas de cada data 
        manchas.split()
        if float(manchas) > float(num): #pega a maior média de manchas 
            num = manchas
            ano= linha[:4]
            mes = linha[5:7]
            mes.split()
            data = mes+"/"+ano #organiza corretamente os dados para a data
        
    print("\nA data em que foi observado o maior número de manchas solares \
entre 1749 e fevereiro de 2021 foi em", data)
    
def DataSem():
"""
Função devolve qual foi o mês e o ano que tiveram mais dias sem manchas solares

Possíveis erros: o código não roda se a função de dicionário (dicionario_dias) não estiver presente no mesmo arquivo de código,
além disso, caso a amostra de dados usada para o teste não tenha nenhum dia sem manchas solares, haverá erro.
O caso citado foi desconsiderado pois em amostras grandes como do arquivo analisado (de 1818 a 2018), é impossível que isso ocorra. 

Args.: nenhum

Return: printa os dados solicitados e depois retorna o usuário para o menu
"""
    conta_zeros = {} #dicionário para armazenar quantos dias tiveram 0 manchas observadas em um mês
    dicionario = dicionario_dias()
    for ano in dicionario.keys(): 
        conta_zeros[ano] = {}
        for mes in dicionario[ano]: 
            count = 0
            for dia in dicionario[ano][mes]:
                if dicionario[ano][mes][dia] == 0: #verifica se no dia houve 0 manchas 
                    count += 1
            conta_zeros[ano][mes] = count #insere o mês no dicionário e adiciona a quantidade de dias nesse mês com 0 manchas 
    

    zero_anos = {} #novo dicionário para uma nova coleta de dados 
    for ano in conta_zeros.keys():
        zero_anos[ano] = {} #adiciona os anos no dicionário e cria um dicionário para cada ano
        reference_value = 0
        for mes in conta_zeros[ano]:
            if conta_zeros[ano][mes] > reference_value: #para cada ano, pega o mês com maior número de dias com 0 manchas 
                reference_value = conta_zeros[ano][mes]
                mes_zeros = mes
        zero_anos[ano][mes_zeros] = reference_value #para cada ano, insere o mês e o número de dias com 0 manchas no dicionário 
    
    reference_value2 = 0
    year = 0 #variável de ano com nome diferente para não confundir 
    month = 0 #variável de mês com nome diferente para não confundir 
    for ano in zero_anos.keys():
        for mes in zero_anos[ano]: #compara o número de dias para o mês anteriormente selecionado de cada ano 
            if zero_anos[ano][mes] > reference_value2:
                reference_value2 = zero_anos[ano][mes]
                year = ano #renova o ano caso o número de dias com 0 manchas seja maior 
                month = mes #renova o mês caso o número de dias com 0 manchas seja maior 
    data = str(month)+"/"+str(year) #tratamento do dado de data para a saída 
    print("\nO mês e ano com mais dias sem manchas solares foi", data, ", com", reference_value,\
"dias sem manchas solares.")    
    
def DesvioPadraoGeral():
"""
Função calcula o desvio padrão de cada mês para cada ano presente no arquivo com dados diários,

os resultados obtidos foram semelhantes àqueles disponíveis no arquivo de dados mensais, sendo, portanto, satisfatórios.

A função devolve um dicionário com os anos e meses e o desvio padrão referente a cada mês de cada ano.

Função usada como intermediária para a função que printa os dados de desvio para o ano escolhido pelo usuário.

Possíveis erros: o código não roda se a função de dicionário (dicionario_desvio_dias) não estiver presente no mesmo arquivo de código

Args.: nenhum

Return: dicionário
"""    
    desvio_mensal1 = {} #dicionário auxiliar
    dic_desvio = dicionario_desvio_dias()
    dic_obs = dicionario_observacoes_dias()
    for ano in dic_obs.keys():
        desvio_mensal1[ano] = {}
        for mes in dic_obs[ano]:
            SUM_Nd = 0
            for dia in dic_obs[ano][mes]:
                SUM_Nd += dic_obs[ano][mes][dia] #soma do número de observações de cada dia no mês
            desvio_mensal1[ano][mes] = SUM_Nd
            
    desvio_mensal = {} #dicionário final
    for year in dic_desvio.keys():
        desvio_mensal[year] ={}
        for month in desvio_mensal1[year]:
            SUM_numerador = 0
            for day in dic_obs[year][month]:  
                SUM_numerador += (dic_obs[year][month][day]*(dic_desvio[year][month][day])**2)
            if desvio_mensal1[year][month] != 0: 
                desvio = (SUM_numerador/desvio_mensal1[year][month])**(1/2)
            else:
                desvio = None #para evitar divisão por zero
            desvio_mensal[year][month] = desvio
    return desvio_mensal  

def DesvioMensalAno(ano):
"""
Função usada para fornecer os dados de desvio padrão mensal para um dado ano 

Possíveis erros: o código não roda se a função DesvioPadraoGeral() não estiver presente no mesmo arquivo de código

Args.: ano escolhido pelo usuário

Return: printa os dados de desvio padrão desejados pelo usuário
"""    
    desvios = DesvioPadraoGeral()#guarda o dicionário retornado na função chamada
    if ano in desvios.keys():
        for year in desvios.keys():
            if year == ano:
                dados = desvios[ano]
                print("\nPara o ano de", ano, "temos os seguintes dados de desvio padrão mensal: ") 
                print(dados)
                print("\n OBS.: os números antes dos dois pontos (:) referem-se aos meses.")
    else:
        print("\nDados não disponíveis para esse ano. Tente novamente com outro ano.")
        
def Media_ano(year): #cálculo da média anual pela fórmula de média combinada 
"""
Função calcula a média anual de manchas solares por meio da média combinada dos dados mensais

Usa do dicionário retornado pela função dicionario_meses()

Possíveis erros: o código não roda se a função de dicionário (dicionario_meses) não estiver presente no mesmo arquivo de código

Args.: ano (input do usuário pego no menu)

Return: print com os dados solicitados
"""    
    dic_anos = {} #cria um novo dicionário para as médias anuais
    dic_meses = dicionario_meses() #pega os dados do diconário com as médias mensais
    for ano in dic_meses.keys():
        dic_aux = {} #dicionário para auxiliar no armazenamento de dados para o cálculo
        for mes in dic_meses[ano]:
            dic_aux[mes] = {}
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                dias = 31
            elif mes == 2: #aproximação desconsiderando anos bissextos
                dias = 28 
            else:
                dias = 30
            dic_aux[mes][dias] = dic_meses[ano][mes]
        numerador = 0 #inicializar a variável de soma para a média
        for mes in dic_aux.keys():
            for dias in dic_aux[mes]:
                numerador+= dias*(dic_aux[mes][dias]) 
        media = numerador/365 #cálculo da média anual 
        dic_anos[ano] = media
        
    for ano in dic_anos.keys(): 
        if ano == year: #termo em ingles usado para nao confundir com "ano" com o input do usuário
            print("\nA média anual de manchas para", year, "foi de", round(dic_anos[ano], 2), 'manchas.')
    if year not in dic_anos.keys():
        print("\nAno não encontrado nos nossos dados.")  
        
def CicloSolar(ciclo):
"""
Função calcula a duração dos ciclos solares e informa as datas de início e término.

Usa do dicionário retornado pela função dicionario_meses()

Possíveis erros: o código não roda se a função de dicionário (dicionario_meses) não estiver presente no mesmo arquivo de código

Args.: ciclo (input do usuário pego no menu)

Return: print com os dados solicitados
"""   
    dicionario = dicionario_meses() #guarda o dicionário de dados mensais na variável
    lista_ciclos = [] #cria uma lista para os ciclos
    lista_aux = list(dicionario.items())
    ano = lista_aux[0][0] #pega o primeiro ano presente no dicionário 
    while ano in dicionario.keys():
        if ano in dicionario.keys(): #esse if é para inicializar a variável min_manchas
            mes = 1
            if mes in dicionario[ano]:
                min_manchas = dicionario[ano][mes] 
        for i in range(0,11):
            year = ano+i #mudança de variável para não perder o ano inicial
            for mes in dicionario[ano]: 
                if year in dicionario.keys():
                    if mes in dicionario[year]: #para os anos que não tiverem dados até o mês 12
                        if dicionario[year][mes] <= min_manchas:
                            min_manchas = dicionario[year][mes] #pontos de mínimo de manchas
                            data = str(mes)+"/"+str(year)
        lista_ciclos.append(data)
        ano += 10
    
    lista_final = [] #eliminar qualquer data que tenha se repetido por algum erro
    for data in lista_ciclos:
        if data not in lista_final and data != "1/1813":  #em 1813 houve uma anomalia nos dados:
            lista_final.append(data)
    
    if ciclo in range(1, len(lista_final)):
        print("\nO ciclo", ciclo, "foi de", lista_final[ciclo-1], "até", lista_final[ciclo])
        
        from datetime import datetime #calcular o ciclo em meses
        from dateutil import relativedelta
        data_1 = lista_final[ciclo-1]
        data_2 = lista_final[ciclo]
        start = datetime.strptime(data_1, "%m/%Y")
        end =   datetime.strptime(data_2, "%m/%Y")

        diferenca = relativedelta.relativedelta(end, start)
        diferenca_meses = diferenca.months + diferenca.years * 12
            
        if diferenca_meses > 12: #transformar em anos
            anos = 0
            meses = diferenca_meses
            while meses >= 12:
                meses -= 12
                anos += 1 
        else: 
            print("Tal ciclo durou", diferenca_meses, "meses.")
            
        if meses >= 1:
            print("Tal ciclo durou", anos, "anos e", meses, "meses.")
                
        else: 
            print("Tal ciclo durou", anos, "anos.")
    else:
        ciclo = int(input("\nCiclo não encontrado. Por favor, digite algum outro valor \
de ciclo desejado, escrevendo apenas o número referente ao ciclo (exemplo: ciclo 1 = 1): "))
        CicloSolar(ciclo)        
        
        
main_function() #chama a função principal para dar início ao programa
