import pandas as pd
from twilio.rest import Client
#Dados de sua conta twilio para "logar"
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

#Cria uma lista com os nomes dos meses
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#Looping para verificar cada mes tenha um vendedor que venda mais que 55 mil
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #usando Pandas para a variavel tabela_vendas leia os arquivos Excel
    if (tabela_vendas['Vendas'] > 55000).any(): #Determinando que o programa encontre um valor dentro da coluna Vendas maior que 55 mil
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #Definindo em que posição esta localizado o nome do vendedor que bateu a meta
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]#Definindo em que posição esta localizado o valor da venda que bateu a meta
        print(f'No mês de {mes} Alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}') #Confirmação dentro das linhas de código que foi encontrado

#Funcional para envio do SMS pelo Twilio
        message = client.messages.create(
            to="", #Telefone verificado em sua conta Twilio
            from_="", #Telefone recebido no site da Twilio ao se cadastrar
            body=f'No mês de {mes} Alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}') #Conteudo do SMS
        print(message.sid)


