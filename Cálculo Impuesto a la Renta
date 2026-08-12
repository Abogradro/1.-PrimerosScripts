# Un trabajador proyecta un ingreso anual bruto de 55000 soles.
# Resta 7 UIT (5350 cada una) para obtener la renta_neta_imponible.
# Si la renta_neta_imponible es <= 0, el impuesto es 0 soles.
# Si la renta_neta_imponible <= (5 * 5350), aplica 8%, sino 14% e imprime impuesto.

ingreso_anual = 55000
uit = 5350
renta_neta_imponible = ingreso_anual - (7*uit)

if renta_neta_imponible <= 0:
    impuesto = 0
elif renta_neta_imponible <= (5*uit):
    impuesto = ingreso_anual * 0.08
else:
    impuesto = renta_neta_imponible * 0.14

print (f""" Tienes que pagar de impuestos un total de S/. {impuesto} soles 
POr lo tanto, el total neto que recibirás es de S/. {ingreso_anual - impuesto} soles""") 

