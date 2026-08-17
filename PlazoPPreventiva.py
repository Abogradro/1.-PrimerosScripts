# MODULO PROCESAL PENAL 2: Control del plazo de prision preventiva.
# REGLA (art. 272 CPP): proceso comun 9 meses; complejo 18 meses; crimen organizado 36 meses.

# Pide el tipo de proceso: 1 comun, 2 complejo, 3 crimen organizado (int).
# Valida con while que la opcion sea 1, 2 o 3; si no, vuelve a pedirla.
# Asigna el plazo maximo segun el tipo usando if / elif / else.
# Pide los meses ya transcurridos en prision preventiva (int).
# Compara y decide: dentro del plazo, o plazo VENCIDO (procede cese).
# Imprime el resultado con un f-string que muestre el limite aplicable.
# DATO JURIDICO RELEVANTE: art. 272 del Codigo Procesal Penal (D. Leg. 957).

tipo_proce = int(input (f"""\n Por favor indicar el tipo de proceso que llevas:
1. Si es Proceso común, escribe el dígito 1
2. Si es proceso complejo, escribe el dígito 2
3. Si es proceso de crimen organizado, escribe el dígito 3 \n>>> """))

while (tipo_proce != 1) and (tipo_proce != 2) and (tipo_proce != 3):  
    print ("""\nEstás escribiendo mal, elige bien""")
    tipo_proce = int(input (f"""\n Por favor indicar el tipo de proceso que llevas:
    1. Si es Proceso común, escribe el dígito 1
    2. Si es proceso complejo, escribe el dígito 2
    3. Si es proceso de crimen organizado, escribe el dígito 3 \n>>> """))

# 1. Acá vienen los condicionales; pero el comentario no es Acá asignamos valores a nuestras variables contenedoras.
if tipo_proce == 1: 
    plazopp = 9 
    nombre_proce = "Proceso Común"   
elif tipo_proce == 2: 
    plazopp = 18 
    nombre_proce = "Proceso Complejo"
else:
    plazopp = 36 
    nombre_proce = "Proceso por Org. Criminal"

# 2. Pedimos los meses transcurridos UNA SOLA VEZ
tiempopreso = int (input (f"""\n Indícame cuánto tiempo llevas preso en meses: \n>>> """))
pendiente = plazopp - tiempopreso
#Acá quiero colocar un condicional adicional; porque, ¿Qué pasaría si alguien responde que lleva 200 meses preso; el programa 
#no diferenciará o no se dará cuenta que es un improperio. Por tanto necesito que el programa distinga eso. Por eso pienso que
#lo mejor sería otro condicional. Acá va mi intento

if tiempopreso > plazopp:
    print (f"""\nDebe haber un error, porque tu tiempo estando preso ({tiempopreso} meses) excede el plazo máximo
    del tipo de proceso que llevas ({nombre_proce}, tiene como máximo {plazopp} meses de prisión preventiva). 
    Por tanto lo que acá corresponde es solicitar inmediatamente 
    tu EXCARCELACIÓN DE MANERA DEFINITIVA... Salvo hayas cometido un error de tipeo.\n""")
elif tiempopreso == plazopp: 
    print (f"""\nLa cantidad de meses que llevas preso ({tiempopreso} meses) es el máximo de prisión preventiva 
    que puedes llevar por el tipo de proceso ({nombre_proce}, tiene como máximo {plazopp} meses de prisión preventiva). 
    Revisa con tu abogado los días que te quedan adentro, NO LE AVISES AL FISCAL hasta que sobrepases los días.
    Con esto sales libre a la brevedad.\n""") 
else: # 3. Evaluamos el tiempo pendiente e imprimimos UNA SOLA VEZ. 
    print (f"""\nLlevas {tiempopreso} meses preso, al estar en un {nombre_proce}, el plazo 
    máximo de prisión preventiva es de {plazopp}; por tanto te quedan {pendiente} meses 
    para poder salir en libertad\n""")

