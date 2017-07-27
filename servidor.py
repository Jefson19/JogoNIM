import socket
from jogo import *
import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereco IP do Servidor + Porta que o Servidor esta
server_address = ('localhost', 5000) 
#server_address = (socket.gethostbyname(socket.gethostname()), 5000) 
sock.bind(server_address)#enviar para rede o meu endereço

# Fica ouvindo por conexoes, apenas um pode se comunicar
sock.listen(1)

while True:
	# Servidor sempre ativo
	clear()
	#print ("Nome do servidor: ", socket.gethostbyname(socket.gethostname()))
	print ("Nome do servidor: localhost")
	print('Aguardando a conexao do jogador')
	con, cliente = sock.accept()
	#print('con: ', end);
	#print('cliente: ', cliente);

	try:
		print('O Jogador <{}, {}> acaba de se conectar'.format(cliente[0], cliente[1]))
		
		#Recebe o tipo de jogo
		data = con.recv(1024)
		tipo = int.from_bytes(data, byteorder='big', signed=False)
		if (tipo == 1):
			print("Modo de jogo: Jogador x CPU")
		else:
			print("Modo de jogo: 2 jogadores")
			
		# Cria um tabuleiro de jogo
		data = con.recv(1024)
		board = Jogo(int.from_bytes(data, byteorder='big', signed=False))

		# Processa em loop
		while board.jogando:
			# Recebe a jogada do jogador
			data = con.recv(1024)
			clear()

			# Checa se a conexao do jogador foi terminada
			if not data:
				print('Jogador Desconectado.')
				break

			# Restaura no tabuleiro apos a jogada do jogador
			board.restaura(data)

			board.jogador = 0
			print('O jogador jogou:')
			board.printa_jogo()
			
			if (not board.jogando):
				break;
			
			board.jogador = 1
			if (tipo==1): # Faz uma jogada aleatoria
				board.jogadaAleatoria()
			else: # Faz uma jogada
				print('Faça a sua jogada:')
				aux = True
				while aux:
					lin, qtd = lerLinQtd()
					try:
						board.jogada(lin, qtd)
						aux = False
					except:
						print('\nLinha ou coluna inválida. Tente novamente.')
						
			print('O servidor jogou:')
			board.printa_jogo()
				
			# Envia o tabuleiro para o jogador
			con.sendall(board.salva().encode('utf-8'))
	finally:
		# Clean up the connection
		con.close()
