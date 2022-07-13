import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!!!')

host = 'localhost'
port = 5432

s.bind((host, port))
menssagem = 'Servidor: Olá cliente!'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('Servidor enviando menssagen...')
        s.sendto(dados + (menssagem.encode()), endereco)