from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os

now=time.time()
print(now)
#---------Funções-------------
print(" Registar funções ")
def carregar():
    #print("Inicio do carregamento")
    time.sleep(1)
    pront="n"
    get_source = navegador.page_source
    while pront=="n":
        if "Carregando" not in get_source:
            pront="s"
            #print("Fim do carregamento")
        time.sleep(0.5)
        get_source = navegador.page_source
    try:
        navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/a/span[2]").click()
    except:
        carregar()
def insistir_clique(ipath):
    prot="True"
    while prot=="True": #Tenta clicar
        try:
            navegador.find_element(By.XPATH,ipath).click()
            time.sleep(0.3)
            prot="False"
        except:
            time.sleep(0.3)

def insistir_preencher(ipath,text):
    print(text)
    prot="True"
    while prot=="True": #Tenta clicar
        try:
            navegador.find_element(By.CSS_SELECTOR,ipath).send_keys(text)
            time.sleep(0.3)
            prot="False"
            #input('pause')
        except:
            time.sleep(0.3)

def extrair_dados():
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[1]/div/button').click()
    carregar()
    time.sleep(1)
    print("preparar")

    ValorOriginal = "-"
    IDInfra = "-"
    DtNotifi = "-"
    Renainf = "-"
    Agente = "-"
    Local = "-"
    DtCometimento = "-"
    Hora = "-"
    CodInfra = "-"
    DtLimiteDefesa = "-"
    DtLimiteIdentific = "-"
    DtPenalidade = "-"
    DtLimiteInterRecurso = "-"
    DtVencDesconto = "-"
    Etapa = ""
    Pago = ""
    
                
    get_source = navegador.page_source
    termos=get_source.split(' ')
    print("apontar")

    for s in range(0,len(termos)):
        if "R$" in termos[s]:
            ValorOriginal =(((termos[s+1]).split(';')[1]).split('<'))[0]
        if "Infração</label>" in termos[s]:
            IDInfra = termos[s+1]
            DtNotifi = (((termos[s+18]).split('>')[1]).split('<'))[0]
        if "RENAINF" in termos[s]:
            Renainf = (((termos[s+2]).split('>')[1]).split('<'))[0]
        if "Competente" in termos[s]:
            Agente = str(termos[s+2].split('>')[1])+"-"+str(termos[s+4])+"-"+(str(termos[s+6]).split('<'))[0]
        if "Local" in termos[s]:
            Local =str(termos[s+1])+" "+str(termos[s+2])+" "+str(termos[s+3])+" "+str(termos[s+4])+" "+str(termos[s+5])+" "+str(termos[s+6])+" "+str(termos[s+7])+" "+str(termos[s+8])+" "+str(termos[s+9])+" "+str(termos[s+10])
            Local = str(Local.split('da Infração</th><td _ngcontent-hsa-c165="" class="col-md-8">'))
            Local = Local.split('" class="col-md-8">')[1]
        if "Hora" in termos[s]:
            DtCometimento =(str(termos[s+6]).split('>'))[1]
            Hora =(str(termos[s+7]).split('<'))[0]
        if "Código" in termos[s]:
            CodInfra = str(termos[s+4]).split('>')[1]+"-"+str(termos[s+6]).split('<')[0]
        if "Prévia" in termos[s]:
            DtLimiteDefesa = (str(termos[s+2]).split('>')[1]).split('<')[0]
        if "Condutor" in termos[s] and "Infrator</th><td" in termos[s+1]:
            DtLimiteIdentific = (str(termos[s+3]).split('>')[1]).split('<')[0]
        if "de" in termos[s] and "Penalidade</th><td" in termos[s+1]:
            DtPenalidade = (str(termos[s+3]).split('>')[1]).split('<')[0]
        if "de" in termos[s] and "Recurso</th><td" in termos[s+1]:
            DtLimiteInterRecurso = (str(termos[s+3]).split('>')[1]).split('<')[0]
        if "do" in termos[s] and "Desconto</th><td" in termos[s+1]:
            DtVencDesconto = (str(termos[s+3]).split('>')[1]).split('<')[0]
        if "Pagamento efetuado." in get_source:
            Pago = "SIM"
    print("Anotando")
    
    #Em qual etapa esta?
        #Baixar a notificação²
        #Baixar a penalidade
        #Baixar o boleto


    #Data Limite para Interposição de Defesa Prévia
        #Notificação
    #DtLimiteDefesa 
    Dt=DtLimiteDefesa.split('/')
    Dt1= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])
    Etapa = "Notf - " + Etapa
    print(Dt1,Dth)
    print((Dt1 > Dth))
    
    if 1:
        etapa1()


    try:
        #Data Limite para Interposição de Recurso
            #Penalidade
        #DtLimiteInterRecurso
        Dt=DtLimiteInterRecurso.split('/')
        Dt2= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])
        Etapa = "Penl - " + Etapa
        if Dt1 > Dth:
            etapa2()

    except:
        pass


    try:
        #Data do Vencimento do Desconto
            #Se estiver muito próximo (dentro de 9 dias)
        #DtVencDesconto
        Dt=DtVencDesconto.split('/')
        Dt3= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])
        Etapa = "Prox - " + Etapa
        if Dt1 <= Dtf:
            etapa2()
            etapa3()

    except:
        pass

    try:
        #Data do Vencimento do Desconto
            #Se estiver já vencida 
        #DtVencDesconto
        Dt=DtVencDesconto.split('/')
        Dt4= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])
        Etapa = "Venc - " + Etapa

        if Dt1 >= Dth:
            etapa4()

    except:
        pass
    
    ilog = open(logfilename, "a")
    ilog.writelines( str(placa) + ";"+
                     str(renavan) + ";"+
                     DtHoje+ ";"+
                     Etapa  + ";"+
                     ValorOriginal + ";"+
                     IDInfra + ";"+
                     DtNotifi + ";"+
                     Renainf + ";"+
                     Agente + ";"+
                     Local + ";"+
                     DtCometimento + ";"+
                     Hora + ";"+
                     CodInfra + ";"+
                     DtLimiteDefesa + ";"+
                     DtLimiteIdentific + ";"+
                     DtPenalidade + ";"+
                     DtLimiteInterRecurso + ";"+
                     DtVencDesconto +";"+
                     Pago+";"+
                     '\n')
    ilog.close()

    #Baixar arquivos








    
    #Voltar
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/div/div/div/div[1]/button[1]').click()





def procura_todos():
    if 1 : #mudar para todos desativado.
        try:
            time.sleep(0.2)
            navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[1]/br-select/div/div/div[1]/ng-select/div/div/div[3]/input').click()
            time.sleep(0.2)
            navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[1]/br-select/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[6]').click()
            time.sleep(1)
            carregar()
        except:
            pass


def etapa0(): #Não encontrou nada para o veículo em questão
    print("Escrever no doc final que não encontrou nada do veic em questão em aberto")
    ilog = open(logfilename, "a")
    ilog.writelines(placa + ";"+renavan + ";"+"ETAPA 0" + ";"+
                    "Nada encontrado" + ";"+DtHoje+ ";"+'\n')
    ilog.close()
    
    pass

def etapa1(): #Caso dentro do prazo de notificação de autuação, realizar download para o sato
    print(" etapa1 ")

    insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]')
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[3]/button').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[3]/div/div[1]/button').click()
    carregar()
    
def etapa2(): #Caso dentro do prazo de Penalidade
    print(" etapa2 ")

    insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]')
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[3]/button').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[3]/div/div[3]/button').click()
    carregar()
 
    pass

def etapa3(): # Ainda não venceu mas esta muito perto do prazo final
    print(" etapa3 ")
    
    # Caso não tenha identificado
    insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/button').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/div/div[5]/button').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/modal-container/div/div/form/div[3]/div/button[5]')
    carregar()
    time.sleep(0.2)
    navegador.refresh()
    carregar()
    insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/button')
    carregar()
    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/div/div[9]/button').click()
    carregar()
    navegador.find_element(By.XPATH,'/html/body/modal-container/div/div/form/div[3]/div/button[6]').click()
    carregar()


    
    pass

def etapa4(): #Caso com notificação vencida.
    print(" etapa4 ")

    try: # Infrator já foi identificado?
        insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]')
        carregar()
        navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/button').click()
        carregar()
        navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/div/div[3]/button').click()
        carregar()
        print("Infrator identificado")


    except: # Caso não tenha identificado
        insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]').click()
        carregar()
        navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/button').click()
        carregar()
        navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/div/div[5]/button').click()
        carregar()
        navegador.find_element(By.XPATH,'/html/body/modal-container/div/div/form/div[3]/div/button[5]')
        time.sleep(0.2)
        carregar()
        navegador.refresh()
        carregar()
        insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/button')
        carregar()
        navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/app-infracoes-detail/div/div/div[4]/div/div/div[1]/div/div[9]/button').click()
        carregar()
        navegador.find_element(By.XPATH,'/html/body/modal-container/div/div/form/div[3]/div/button[6]').click()
        carregar()
        #esperar e carregar

    
        print("Infrator NÃO identificado")
        pass

def etapa5(): 
    print(" etapa5 ")

    #esperar e carregar

    pass

def mudar_data(ii):
    if ii == 1:
        print(ii)
        #Faça parte 2, 1 ano anterior
        Dtpast = time.strftime("%d/%m")+"/20"+str( int(time.strftime("%y"))-3)
        Dtinter = time.strftime("%d/%m")+"/20"+str( int(time.strftime("%y"))-2)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').click()
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Keys.CONTROL, 'a')
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Keys.BACKSPACE)
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Dtpast)
        time.sleep(0.1)
        print(Dtpast)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').click()
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Keys.CONTROL, 'a')
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Keys.BACKSPACE)
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Dtinter)
        time.sleep(0.1)
        print(Dtinter)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[5]/button[1]').click()
        time.sleep(1)
    if ii == 2:
        print(ii)
        #Faça parte 2, 1 ano anterior
        Dtpast = time.strftime("%d/%m")+"/20"+str( int(time.strftime("%y"))-2)
        Dtinter = time.strftime("%d/%m")+"/20"+str( int(time.strftime("%y"))-1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').click()
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Keys.CONTROL, 'a')
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Keys.BACKSPACE)
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[2]/br-date-picker/div/div[1]/input').send_keys(Dtpast)
        time.sleep(0.1)
        print(Dtpast)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').click()
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Keys.CONTROL, 'a')
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Keys.BACKSPACE)
        time.sleep(0.1)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[4]/br-date-picker/div/div[1]/input').send_keys(Dtinter)
        time.sleep(0.1)
        print(Dtinter)
        navegador.find_element(By.XPATH, '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[2]/div[5]/button[1]').click()
        time.sleep(1)

 #= int(  [2])*10000+int(  [1])+int(  [0])
#--------------------- Preparar -------------------------
#611.359.681-87
print(" Preparar ")

#Dados necessários:

ctrl_in = input("Insira o n° de controle da planilha")

DtHoje = time.strftime("%d/%m/%Y")

Dt=DtHoje.split('/')
Dth= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])
print(Dth)
if int(Dt[0]) >= 21:
    Dtf= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])+100-30
else :
    Dtf= int(Dt[2])*10000+int(Dt[1])*100+int(Dt[0])+9

#Criação de pasta principal utilizada
pathdown = "\\Downloads\\Downloads - "+time.strftime("%d.%m.%Y", time.localtime())

try:
    os.mkdir(str(os.getcwd())+"\\Downloads")
except:
    pass

try:
    os.mkdir(str(os.getcwd())+pathdown)
except:
    pass 

try:
    os.mkdir(str(os.getcwd())+"\\Passado")
except:
    pass 

#Mover o último registro para a pasta "Passado"






#Arquivo do excel com as informações necessárias:
    #Coluna com os dados  (Quando possível):
ColControle = 0
ColPlaca = 1
ColRenavam = 2
#ColPrefixo = 3
NomeArquivo= "Controle.xlsx"
df = pd.read_excel(NomeArquivo)

#Preparar arquivos de diário de ocorrências:
logfilename="SENATRAN "+time.strftime("%d.%m.%Y, %H", time.localtime())+" Horas.csv"
ilog = open(logfilename, "w")
ilog.close()
ilog = open(logfilename, "a")
ilog.writelines("Placa"+";"+"Renavan"+";"+
                'Data "Recebida"'+";"+"Etapa"+";"+
                "Valor"+";"+"Cód Infração"+";"+
                "Data de Notificação"+";"+'Renainf' + ";"+
                'Agente' +";"+'Local' +";"+'Data Ocorrida' +";"+
                'Hora ocorrido' + ";"+'Id de Infra' + ";"+
                'DtLimiteDefesa' + ";"+'DtLimiteIdentific' + ";"+
                'DtPenalidade' + ";"+'DtLimiteInterRecurso' + ";"+
                "DtVencDesconto" +  ";"+'\n')
ilog.close()

##################### COLOCAR PRA MOVER O RELATÓRIO ANTERIOR CRIADO ############


#Configurações do navegador
dirdown = str(os.getcwd())+pathdown+"\\"
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument("--disable-setuid-sandbox")

options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])


options.add_experimental_option("prefs", {
    "download.default_directory": dirdown,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })


#options.add_experimental_option("prefs", ("download.default_directory", dirdown, "safebrowsing.enabled","false"))

####### fazer um try pra abrir com o drive, except sem ele
#navegador = webdriver.Chrome(chrome_options=options)
#navegador = webdriver.Chrome(ChromeDriverManager().install())
#navegador = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    webdriver.Chrome(ChromeDriverManager().install())
except:
    pass

navegador = webdriver.Chrome(options=options)
#navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
#navegador = webdriver.Chrome(service=ChromeService(options=options))
navegador.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
navegador.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

#Abrindo a janela:
site="https://portalservicos.senatran.serpro.gov.br/#/home"
navegador.get(site)
navegador.set_window_position(0, 0, windowHandle='current')
navegador.maximize_window()


p=1
while p==1:
    try:
        #navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/header/br-header/div/div/div[2]/div/button/span').click()
        p=0
    except:
        time.sleep(0.3)


input("Clique 'enter' para prosseguir")



#laço para cada uma das linhas em questão
for index,row  in df.iterrows():
    
    placa = row.iloc[1]
    placa = str(placa).replace("-","")
    placa = str(placa.replace(" ",""))
    
    renavan = str(row.iloc[2])
    try:
        renavan = renavan.split(".")[0]
    except:
        pass
    letras = int(len(renavan))
    ctrl = int(row.iloc[0])
    
    if letras == 10:
        renavan = "0"+renavan
    if letras == 9:
        renavan = "00"+renavan
    if letras == 8:
        renavan = "000"+renavan
    if letras == 7:
        renavan = "0000"+renavan

    print(placa,renavan)
    ctrl = str(ctrl) 
    ctrl_in = str(ctrl_in)
    
    if len(placa)==7:
        carregar()
        #Partindo de um ponto padrão"
        navegador.get("https://portalservicos.senatran.serpro.gov.br/#/home")

        try: # Abre o menu lateral e abre a parte de infrações
            navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/a/span[2]").click()
        except:
            navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/header/br-header/div/div/div[1]/div[1]/button/span").click()
            #Carregar
            carregar()
            #Novamente, erro aqui, ajustar esse erro ##########OBSERVAR ESSE ERRO, ele que faz o programa travar
            try:
                navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/a/span[2]").click()
            except:
                carregar()
                try: # Abre o menu lateral e abre a parte de infrações
                    navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/a/span[2]").click()
                except:
                    navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/header/br-header/div/div/div[1]/div[1]/button/span").click()
                    #Carregar
                    carregar()
                    #Novamente, erro aqui, ajustar esse erro ##########OBSERVAR ESSE ERRO, ele que faz o programa travar
                    navegador.find_element(By.XPATH,"/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/a/span[2]").click()

                
        
        carregar() #Clicar na opção lateral
        print(" a1 ")
        insistir_clique('/html/body/app-root/form/br-main-layout/div/div/div/br-side-menu/nav/div[4]/ul/li[1]/a/span[2]')
        carregar() #Pesquisar por Veics
        print(" a2 ")
        insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/div/div/div/div[1]/div[1]/div/div/i')
        carregar() #preencher placa
        print(" a3 ")
        time.sleep(1)

        insistir_preencher('input[placeholder="Renavam"]',renavan)
        carregar() #Clicar para pesquisar
        time.sleep(1)
        insistir_preencher('input[placeholder="Renavam"]',renavan)
        carregar() #Clicar para pesquisar

        
        #insistir_preencher('input[placeholder="Placa"]',placa)
        #carregar() #Clicar para pesquisar
        #time.sleep(1)
        #insistir_preencher('input[placeholder="Placa"]',placa)
        #carregar() #Clicar para pesquisar




        
        try:
                
            print(" a4 ")
            insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/div/div/app-infracao-veiculo-lista/form/div[2]/div[3]/button[1]')
            carregar() #Clicou no único carro enontrado

            time.sleep(1)
            get_source = navegador.page_source
            key=0
            while key<15: #Tenta clicar
                try:
                    navegador.find_element(By.XPATH,'/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/div/div/app-infracao-veiculo-lista/form/div[3]/div[2]/div[1]/div').click()
                    #insistir_clique('/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/div/div/app-infracao-veiculo-lista/form/div[3]/div[2]/div[1]/div').click()
                    ready=1
                    key=15
                except:
                    time.sleep(0.3)
                    key=key+1
                    if key == 14:
                        ilog = open(logfilename, "a")
                        ilog.writelines(placa + ";"+renavan + ";"+"" + ";"+
                                        "Veic não faz parte da base" + ";"+DtHoje+ ";"+'\n')
                        ilog.close()
                        print("veic não pertence a base")

            procura_todos()
            for ii in  range(0,3):
                procura_todos()
                mudar_data(ii)
                #o código não ta seguindo a partir daqui, verificar
                carregar()
                print("BAIXAR ", ii)
                time.sleep(1)
                get_source = navegador.page_source
                warning="Não foram encontradas infrações."
                if warning in get_source :
                    print("Saída warning")
                    etapa0()
                get_source = navegador.page_source
                if warning not in get_source and ready ==1:
                    print("autos encontrados")
                    #input("pause, encontrou algo 1")
                    get_source = navegador.page_source
                    texto = get_source.split('\n')
                    for i in range(0,len(texto)):
                        #nTotRegis=1
                        #Verficar a  Qntd de resultados
                        if 'Total de registros encontrados:' in texto[i]:
                            nTotRegis = (texto[i].split('Total de registros encontrados:')[-1])[1]
                            nTotRegis = int(nTotRegis)
                            print(nTotRegis)
                            
                            #'Não pagas - A vencer (3)'
                        if 'Não pagas - A vencer' in texto[i]:
                            nNPagas = ((texto[i].split('Não pagas - A vencer')[1]).replace(')',""))[2]
                            nNPagas = int(nNPagas)
                            print(nNPagas)
                            
                        if True:
                            nNPagasVencidas = 0
                   # input("pause, encontrou algo 2")
                    
                    #Verificar dados das não pagas:
                    for i in range(1,nTotRegis+1):
                        procura_todos()
                        mudar_data(ii)
                        try:
                            smart_path = '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[2]/div['+str(i)+']/div/span[2]'
                            navegador.find_element(By.XPATH,smart_path).click()
                            time.sleep(1)
                            carregar()
                            extrair_dados()
                            carregar()
                        
                        except:
                            pass
                        try:
                            smart_path = '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[3]/div['+str(i)+']/div/span[2]'
                            navegador.find_element(By.XPATH,smart_path).click()
                            time.sleep(1)
                            carregar()
                            extrair_dados()
                            carregar()
                        except:
                            pass
                            
                        try:
                            smart_path = '/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[4]/div['+str(i)+']/div/span[2]'
                            navegador.find_element(By.XPATH,smart_path).click()
                            time.sleep(1)
                            carregar()
                            extrair_dados()
                            carregar()  
                        except:
                            pass


                    
                        #for i in range(0,int(nNPagas)+1)
                        
                        #/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[2]/div[1]/div/span[2]
                        #/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[2]/div[2]/div/span[2]
                        #/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[2]/div[3]/div/span[2]
         


                

        except:
            print("Erro em ", renavan)
            ilog = open(logfilename, "a")
            ilog.writelines(placa + ";"+renavan + ";"+"" + ";"+"Erro durante a busca dos dados do veículo." + ";"+DtHoje+ ";"+'\n')
            ilog.close()




#  3 casos em aberto
#1 vencido e 2 a vencer , separadps

# 1 vencida
#/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[2]/div[1]/div
# 2 a vencer
#/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[3]/div[1]/div
#/html/body/app-root/form/br-main-layout/div/div/main/app-infracao/app-infracoes-list/app-infracoes-veiculo-list/app-infrator-list/div/div/app-infracao-lista/form/div[3]/div[3]/div[2]/div


#Alerta de erro:
# Erro:
# O veículo dessa infração não está em seu nome ou possui pendência de emissão do CRV (Certificado de Registro de Veículo). Regularize a situação no Detran.


 
end=time.time()-now
print(end)

print("FIM")

# ERRO no site

# Erro desconhecido.










































