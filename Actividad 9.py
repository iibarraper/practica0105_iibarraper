cantidad_invertir = float(input("¿Cuanta cantidad vas a invertir?"))
tasa_interes_anual = float(input("Tasa de interés anual (porcentaje):"))
tasa_interes_decimal = tasa_interes_anual / 100
num_años = int(input("Número de años de la inversión:"))
capital_obtenido = cantidad_invertir * (1 + tasa_interes_decimal) ** num_años
print(" Capital obtenido:", capital_obtenido)
