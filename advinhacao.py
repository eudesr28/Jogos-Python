# Jogo de adivinhação
def jogo_adivinhacao():
  import random  #função de sorteio

  resp = input()
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
       print(nome,"você adivinhou! Parabéns!")
    else: 
       print(" Você não conseguiu adivinhar.")
       print(" O número era: ",numRand)
  print("Menu principal: (1) Sim (2) Não")
    menu = int(input())
    if menu == 1:
        menu.menu()
  iniciar = int(input("Menu principal: (1) Sim (2) Não"))
    if iniciar == 1:
            menu.inicio()      