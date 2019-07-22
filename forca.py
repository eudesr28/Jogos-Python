import random
import efeitos
import menu
import forca
def jogo_forca():
	palavras = []
	with open("palavras.txt") as arquivo:
		for linha in arquivo:
			linha = linha.strip()
			palavras.append(linha)
	numero = random.randrange(0,len(palavras))

	palavra_secreta = palavras[numero]
	#print(palavra_secreta)
	letras_acertadas = ['_' for letra in palavra_secreta]		
	enforcou = False
	acertou = False
	erros = 0

	print ("Jogo da forca! Adivinhe a palavra")

	print (letras_acertadas)

	while (not enforcou and not acertou):
		chute = input("Letra: ")
		if chute in palavra_secreta:
			posicao = 0
			for letra in palavra_secreta:
				if (chute.upper() == letra.upper()):
					letras_acertadas[posicao] = letra
				posicao = posicao + 1
		else:
			erros += 1
			efeitos.desenha_forca(erros)
			print ("Você ERROU! Tente novamente")
			#print ("Você ainda possui {} tentativas.".format(5-erros))
		enforcou = erros == 7
		acertou = '_' not in letras_acertadas
		print (letras_acertadas)
	if (acertou):
		efeitos.msg_vencedor()
	else:
		efeitos.msg_perdedor(palavra_secreta)
	iniciar = int(input("(1) Jogar novamente \n(2) Menu principal \n(3) Encerrar\n"))
	if iniciar == 1:
		forca.jogo_forca()
	elif iniciar == 2:
		menu.inicio()	