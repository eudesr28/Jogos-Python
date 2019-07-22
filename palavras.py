#Palavras
def palavras():
	palavras = []
	qtd_palavras = int (input('Quantidade de palavras: '))

	while len(palavras) <= qtd_palavras:
		palavra = input('Digite as palavras: ')
		palavras.append(palavra)
		arquivo = open("palavras.txt","w")
		for palavras_secretas in palavras:
			arquivo.writelines(palavras_secretas + "\n")
		arquivo.close()
	print ("Palavras salvas")		