#Menu
import adivinhacao
import forca
import palavras

def inicio():
	print ('Escolha seu jogo')
	print ("(1) Jogo da ADIVINHAÇÃO \n(2) Jogo da FORCA \n(3) Encerrar")
	jogo = int (input())

	if jogo == 1:
		print ('Jogo da ADIVINHAÇÃO')
		adivinhacao.jogo_adivinhacao()
	elif jogo == 2:
		print ("(1) Jogar \n(2) Cadastrar palavras")
		option = int (input())

		if option == 1:
			forca.jogo_forca()
		elif option == 2:
			print ('Palavras')
			palavras.palavras()
	elif jogo == 3:
		print("ok")