def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************")
   
    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas2 = []
   
    for letra in (palavra_secreta):
     letras_acertadas2.append("_")
       
    enforcou = False
    acertou = False
    erros = 0
       
    print(letras_acertadas)
       
    while (not enforcou and not acertou):
           
        chute = input("Qual letra?")
        chute = chute.strip().upper()
   
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
               
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
               
    if (acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    print("Fim de jogo")
                   
if (__name__ == "__main__"):
     jogar()
    
import forca 
import adivinhacao
        
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
             
    print("(1) Forca (2) Adivinhação")
             
    jogo = int(input("Qual jogo? "))
             
    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
         print("Jogando adivinhação")
         adivinhacao.jogar()
        
if(_name_ == "_main_"):
   escolhe_jogo()        
