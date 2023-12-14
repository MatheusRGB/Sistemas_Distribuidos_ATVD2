import socket
import threading
from datetime import datetime

def conexao_cliente(client,address):
    
    while (True):    
        '''
        PROTOCOLO
        '''
        mensagem = client.decode()
        if (mensagem!='hora'):
            sock.sendto('0'.encode, address)
        else:
            sock.sendto(f'{datetime.now()}'.encode(), address)

    #Fechando o socket
    sock.close()

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
server_address = ('localhost', 20001)
print ("Iniciando servidor na porta %s %s" % server_address)
#Reservando porta
sock.bind(server_address)

while True:
    client = sock.recvfrom(2048)
    conexao = threading.Thread(target=conexao_cliente,args=(client[0],client[1],))
    conexao.start()

