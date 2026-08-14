# MÓDULO PENAL: Calendario de Pago de Días-Multa (Art. 41 Código Penal).
# SUMILLA: Imprimir mes a mes el cronograma de pago de la multa impuesta por sentencia.
# USUARIO OBJETIVO: Abogado Defensor para entregarle el cronograma de pagos a su patrocinado.
# Pide al usuario el número de cuotas mensuales a pagar (int) (ejemplo: 12).
# Usa un bucle 'for mes in range(1, cuotas + 1):' para contar cada mes.
# Si el mes es múltiplo de 3 ('mes % 3 == 0'): imprime "Mes {mes}: [PAGO + CONTROL] Acudir al juzgado a voucher".
# En cualquier otro caso ('else'): imprime "Mes {mes}: Pago ordinario en el banco".

meses = int (input (""" Indicar el número de meses a pagar la cuota penal \n >>>  """))

for numero in range (1,(meses+1)):
    if numero % 3 == 0:
        print (f""" Mes {numero} [PAGO + CONTROL] Acudir al juzgado a voucher """)
    else: 
        print (f""" Mes {numero} Pago ordinario en el banco """)
