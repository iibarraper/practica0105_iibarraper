cantidad_depositada = float(input("Dinero depositado:"))
tasa_interes_anual = 0.04
saldo_después_1_año = cantidad_depositada * (1 + tasa_interes_anual)
saldo_después_2_años = saldo_después_1_año * (1+ tasa_interes_anual)
saldo_después_3_años = saldo_después_2_años * (1 + tasa_interes_anual)
print("Saldo después de un año:", round(saldo_después_1_año, 2))
print("Saldo después de dos años:", round(saldo_después_2_años,2))
print("Saldo después de tres años:", round(saldo_después_3_años,2))
