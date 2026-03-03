#Declarar

Ano_Nasc_ : int = 0
Ano_Atual : int = 0
Idade_Atual : int = 0
Idade_Futura : int = 0

#Inicio

Ano_Nasc_ = int (input("Digite o ano do Nascimento: "))
Ano_Atual = int (input ("Digite o ano atual: "))
Idade_Atual = Ano_Atual - Ano_Nasc_ 
Idade_Futura = Idade_Atual + 17
print("Sua idade atual é",Idade_Atual,"e daqui a 17 anos terá",Idade_Futura)

#Fim