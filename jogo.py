base = int (input("Digite o valor da base:"))
expoente= int(input("Digite o valor do expoente:"))
R= base 

for k in range(1, expoente):
    R = R * base

print("Resultado: " , "{:.2f}" . format(R))
