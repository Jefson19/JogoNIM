import socket #socket
import sys #encode e decode
from jogo import * #Funcoes do jogo
import os #Para detectar o sistema
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear') #Limpar tela


def jogar(tipo):
	# Criando socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Conectando o socket com a porta ouvida pelo servidor
	servidor = input('\nDigite o IP do servidor: ')
	server_address = (servidor, 5000) #Obtem endereço = host e porta
	print('Conectando ao servidor {} na porta {}'.format(server_address[0], server_address[1]))
	sock.connect(server_address) #conecao

	try:
		sock.sendall(bytes([tipo])) #Enviar tipo de jogo
		linpali = lerLinhas() #Leio a qtd de linhas
		board = Jogo(linpali) 
		sock.sendall(bytes([linpali])) #Enviar a qtd de linhas
		board.printa_jogo()
		
		while board.jogando:
			print('Faça a sua jogada:')
			board.jogador = 0 #Cliente
			
			#Ler e verifica leitura
			aux = True
			while aux:
				lin, qtd = lerLinQtd()
				try:
					board.jogada(lin, qtd)
					aux = False
				except:
					print('\nLinha ou coluna inválida. Tente novamente.')
			
			clear()
			print('Eu joguei:')
			board.printa_jogo()

			# Envia o tabuleiro para o servidor
			sock.sendall(board.salva().encode('utf-8'))
			if (not board.jogando):
				break;		

			# Recebe a jogada do servidor
			board.jogador = 1 #Servidor
			data = sock.recv(1024) #Recebe do servidor
			board.restaura(data.decode('utf-8'))
			print('\nO servidor jogou:')
			board.printa_jogo()

	finally:
		print('Encerrando o cliente')
		sock.close() #Fecha conexao
