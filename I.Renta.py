ingreso_anual = float (input ("Hola, indica tu ingreso anual por favor:   ") )
uit = int (input ("Indica el valor de la UIT este año; el valor de la UIT de este año 2026 es de S/. 5350:   ")) 

renta_neta_imponible = ingreso_anual - (7*uit)

if renta_neta_imponible <= 0:
    impuesto = 0
elif renta_neta_imponible <= (5*uit):
    impuesto = renta_neta_imponible * 0.08
else:
    impuesto = renta_neta_imponible * 0.14

print (f""" Tienes que pagar de impuestos un total de S/. {impuesto} soles 
POr lo tanto, el total neto que recibirás es de S/. {ingreso_anual - impuesto} soles""") 

