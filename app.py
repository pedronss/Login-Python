import os
user=" "
senha= " "
while (user != "admin" or senha != "admin"):
  os.system('cls') or None
  user= input("Usuário: ")
  senha= input("Senha: ")
print ("Bem vindo!")