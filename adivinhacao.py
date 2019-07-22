# Jogo de adivinhação
import efeitos
import menu
import adivinhacao
def jogo_adivinhacao():
  import random  #função de sorteio

  nome = input("Seu nome: ")

  numRand = random.randint(1,10)

  print(nome,"estou pensando em um numero, entre 1 e 10.")
  print("Você tem 3 tentativas")
  print("Qual é o numero: ")

  tentativas = 0
  while tentativas < 3:
        numero = int (input())
      
        tentativas = tentativas + 1
      
        if numero < numRand:
               print("Você errou! Voçê digitou um número menor")

        if numero > numRand:
               print("Você errou! Voçê digitou um número maior")
          
        if numero == numRand:
      
              break
      
  if numero == numRand:
       print (nome,"você adivinhou!")
       efeitos.msg_vencedor()
  else: 
       print(" Você não conseguiu adivinhar.")
       print(" O número era: ",numRand)
       efeitos.perdedor_adv()
  iniciar = int(input("(1) Jogar novamente \n(2) Menu principal \n(3) Encerrar\n"))
  if iniciar == 1:
      adivinhacao.jogo_adivinhacao()
  if iniciar == 2:
       menu.inicio()

 