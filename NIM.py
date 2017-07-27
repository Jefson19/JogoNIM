import os #Para detectar o sistema
from cliente import *
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

opcao = 1;
while (opcao >= 1 and opcao <=5):
	clear()
	print('***********NIM***********\nSeja bem-vindo ao jogo dos palitos!\n')
	print("Nim é um jogo matemático de estratégia em que dois jogadores se revezam removendo objetos de linhas distintas."
	"Em cada turno, um jogador deve remover pelo menos um objeto e pode remover qualquer número de objetos, desde que todos eles provêm da mesma linha.\n"
	"O objetivo do jogo é evitar ser o jogador que deve remover o último objeto.\n\n"
	"        ATENCAO: O Jogo funciona a partir de quatro fileiras de palitos, e um maximo de 30.\n"
	"    Você pode jogar contra um amigo ou contra um computador, a escolha é sua :)\n\n"
	"Escolha a opção:\n"
	"(1) Jogador x CPU\n"
	"(2) 2 Jogadores\n"
	"(3) Para conhecer mais sobre a História por trás do jogo\n"
	"(4) O funcionamneto do jogo/programa\n"
	"(5) Dica de como vencer\n"
	"(Outro) Para sair do programa\n"
	"\n   Copyright Eberty Alves & Jefson Matos - v1.0\n")
		
	try:
		opcao = int(input('Você escolheu: '))
		if opcao==1:
			clear()
			print("Jogador x CPU")
			try:
				jogar(1)
			except:
				print("Falha ao se comunicar com o servidor")
			aux = input('\nTecle enter para continuar\n')
			
		elif opcao==2:
			clear()
			print("2 Jogadores")
			try:
				jogar(2)
			except:
				print("Falha ao se comunicar com o servidor")
			aux = input('\nTecle enter para continuar\n')
			
		elif opcao==3:
			clear()
			clear()
			print("A História por trás do jogo\n\n"
			"    Para muitos, um dos ambientes mais saudáveis e produtivos para a mente humana é o bar. Num bar, quando se está sozinho, se pensa. Quando se está em grupo, se conversa. O contrário, por exemplo, da Televisão.\n"
			"    Incentivados pelo ambiente criativo, bem como pela abundância da matéria-prima, muitos jogos de boteco usam palitos de fósforo como equipamentos. Vamos conhecer um deles: o NIM.\n"
			"    O NIM é um jogo bastante simples de jogar, embora exija raciocínio matemático e geométrico bastante razoável. No entanto, durante os Happy Hours, depois de algumas cervejas, normalmente os jogadores não se mostram muito aptos a fazer cálculos o que torna o jogo bem interessante.\n"
			"    A origem exata desse jogo não é muito conhecida, sendo porém jogado desde a antiguidade. s primeiras referências europeias a Nim são desde o início do século XVI. Seu nome atual foi cunhado por Charles L. Bouton, da Universidade de Harvard, que também desenvolveu a teoria completa do jogo em 1901. Outro estudioso a respeito desse jogo foi o americano Martin Gardner, que descreveu o NIM em seu livro “Divertimentos Matemáticos”. Segundo Gardner, o NIM surgiu há mais de 2 mil anos na China antiga. Um de seus registros históricos (computacionalmente falando) data Estados Unidos 1940, quando foi patenteada uma máquina chamada NIMATRON, que era instalada em bares e cassinos desafiando as pessoas a jogar NIM contra a máquina.\n"
			"    Outro registro histórico famoso foi em 1951, no Festival Britânico, onde foi exibido um robô chamado Nimrod, que servia exclusivamente para jogar NIM com os visitantes da feira.\n"
			"    O NIM é jogado com palitos de dente ou de fósforos ou até mesmo moedas, e começa com fileiras com os palitos, uma embaixo da outra. A quantidade de fileiras pode ser variável, assim como a quantidade de jogadores (Vamos aqui jogar de 2, claro).\n"
			"    Cada jogador tem direito a tirar quantos palitos quiser, mas somente de uma fileira de cada vez. Assim, pode-se tirar um único palito da fileira de 4, ou todos da fileira de 3, ou dois da fileira de 5, passando então a vez ao adversário.\n"
			"    Nim normalmente é jogado como um jogo misère, no qual o jogador que tira o último objeto perde. Também pode ser jogado como um jogo de jogo normal (Não vamos fazer isso aqui), onde o jogador que tira o último objeto ganha. Não há uma única disposição possível para os palitos, existindo variações a respeito. Contudo, em todas elas a regra básica é mesma.\n"
			"    Pode parecer fácil mas, segundo Martin Gardner, existem milhões de possibilidades de sequências de jogo. Gardner, em seu livro, também mostra algumas fórmulas matemáticas e cálculos binários que garantem a vitória a quem tira o primeiro palito. Todavia, num bar, depois de algumas cervejas, são raríssimas as pessoas que conseguem fazer esses cálculos, ou usá-los, ou lembrar que tais artifícios existem. É exatamente aí que reside a diversão deste jogo. Todos jogadores acham que vão ganhar mas, a qualquer momento, podem ser surpreendidos por seus oponentes (talvez mais sóbrios) e perder de surpresa.\n")
			aux = input('\nTecle enter para continuar\n')
			
		elif opcao==4:
			clear()
			clear()
			print("O programa\n\n"
			"    A partida inicia pedindo a quantidade de fileiras de palitos, e em seguida mostra na tela um pequeno diagrama com pequenos traços verticais representando as fileiras de palitos. Inicialmente a primeira fileira possui um palito e cada uma das demais fileiras possui um palito a mais que a anterior. \n"
			"    Em seguida os jogadores, alternadamente, apresentam uma fileira e o número de palitos que devem ser removidos dela. Naturalmente, o programa não aceita uma fileira inexistente, ou uma quantidade de palitos maior do que a que está disponível naquele momento. Por exemplo, supondo que o diagrama represente o jogo da figura acima, não é admissível um jogador retirar palitos da fileira 6, ou 7, ou 0. Tampouco é possível retirar 0 palitos da fileira 4, ou 6 da fileira 5. Nestes casos, o programa reexibe o diagrama com as fileiras e repete a solicitação ao jogador.\n"
			"    Quando uma jogada válida é apresentada pelo jogador, o programa mostra o diagrama de palitos modificado, removidos os que foram retirados.\n"
			"    Perde o jogo aquele jogador que for obrigado a retirar o último palito. Caso algum jogador retire todos os palitos da última fileira existente (neste caso a estratégia para vencer seria óbvia), ele deve ser advertido de sua estupidez, e seu oponente é declarado o vencedor da partida.\n")
			aux = input('\nTecle enter para continuar\n')
			
		elif opcao==5:
			clear()
			clear()
			print("DICA – Como Vencer?\n\n"
			"    Uma versão de Nim é jogada - e tem importância simbólica - no filme *O Ano Passado em Marienbad* de Alain Resnais, em 1961. Um dos diálogos entre duas das personagens do filme referido relatava:\n"
			"        - Conheço um jogo em que eu ganho sempre.\n"
			"        - Se você ganha sempre não é um jogo.\n"
			"        - É um jogo mas eu ganho sempre.\n\n"
			"    A curiosidade deste jogo é o algoritmo que existe para ganhar de seu oponente. Para vencer matematicamente, é preciso ter um conhecimento de números binários, pois é através deles que roda todo algoritmo da vitória. Não daremos dicas muito óbvias (#DESCUBRA).\n"
			"    Este algoritmo consiste em fazer uma configuração segura nos palitos de modo que não interessa qual a jogada de seu oponente, você faz novamente a configuração, e acaba sempre vencendo. E mesmo que os dois saibam fazer este algoritmo, o que conseguir começar a desenvolvê-lo, ganha:\n"
			"    Primeiro deveos contar quantos números há em cada fileira, e transformá-los em números binários. A configuração segura consiste em somar estes números binários (somar como se fossem decimais). Vamos brincar de PAR OU IMPAR?\n")
			aux = input('\nTecle enter para continuar\n')
			
		else:
			print("\nAgradecemos sua visita!!!")
			
	except:
		clear()
