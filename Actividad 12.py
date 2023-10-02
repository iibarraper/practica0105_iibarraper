precio_pan = 3.49
descuento = 0.60
barras_vendidas_no_del_dia = int(input("Barras no del día:"))
precio_total_sin_descuento = barras_vendidas_no_del_dia * precio_pan
descuento_aplicado = precio_total_sin_descuento * descuento
ganancia_total = precio_total_sin_descuento * descuento_aplicado
print("Precio de una barra de pan: €", precio_pan)
print("Descuento por no ser del día: €", round(descuento_aplicado,2 ))
print("Ganancia final: €", round(ganancia_total,2))
