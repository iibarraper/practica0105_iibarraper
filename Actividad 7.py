peso = float(input("Dime tu peso actual: "))
estatura = float(input("Dime tu altura actual: "))
imc = peso / (estatura ** 2 )
imc_redondeado = round(imc, 2 )
print("Tu masa corporal actual es: ", imc_redondeado)
