#Operações Basicas 
#num1 = 10
#num2 = 20
#total = num1 + num2


#Agregação 
#n1 = "40 "
#n2 = "60 "
#total = n1 + n2
#print(total)
#num1 = int(input('Insira um número: ') )
#num2 = int(input('Insira segundo número: ') )
#total = num1 + num2 
#print(f"O valor da soma é {total}")


#Exemplo do Salário
#salario = int(input("Insira seu salario: " ))

#if salario >= 1000:
  #aumento = salario + (salario*0.2)
#elif salario <= 5000:#aumento de 10%
  #aumento = salario
#print(f"Seu salario sofreu um almento de 10% totalizando {aumento}")


#Boletim 
#nota1 nota2 caucular a média 
#média for maior ou igual a 6 aprovado 
#se não reprovado 

#Nota1 = int(input("Insira sua nota: "))
#Nota2 = int(input("Insira sua nota: "))
#Media = (Nota1 + Nota2) /2 

#if Media >= 6: 
  #print ("Aprovado") 
#else:  
 #print ("Reprovado")


#Pedir o nome
# pedir a idade 
# se for maior que 18 maior de idade 
# senao menor

#Nome = (input("Insira seu Nome: "))
#Idade = int(input("Insira sua Idade: "))
#if Idade >=18: 
 #print ("Maior de Idade ")
#else:
  #print ("Menor de Idade ")

#Case Tabuada 

#Tabuada = int(input("Qual tabuada você deseja: "))
#cont = 9
#soma = 0
#while cont != 0:
    #soma = tabuada + cont 
    #print("f{tabuada} + {cont} = {soma}")
    #cont= cont -1 

parada = ""
while True:
  fruta = input("Insira o nome de uma fruta: ")
  parada = input("Deseja continuar S/N: "). upper( )
  if parada != "S":
    break

    