print("Seja muito bem vindo ao quiz do Bruno!\n")

# Inserção do usuário
answer_user = input("Quer começar? (S/N) ?")
print(answer_user)

# Validação
if answer_user != "S":
    # Sair do programa caso seja diferente de S
    quit()
    
score = 0
print("Começando...")
print( "Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print(" Correto ")
    score = score + 1
else:
    print("incorreto")
    
print( "Qual o nome do protagonista do jogo Grand Theft Auto (GTA)? \n (A) Carlos John \n (B) Carls Johnson \n (C) Carl Jaqueline \n (D) Carlos Johnson \n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print(" Correto ")
    score = score + 1
else:
    print("incorreto")
    
print(f"Quiz acabou... Pontuação: {score}/2")