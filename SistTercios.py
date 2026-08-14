# MÓDULO REPOSITORIO 5: Motor Universal de Penas por Tercios (Art. 45-A C.P. Peruano).
# REGLA GENERAL: Amplitud = (Pena Máxima - Pena Mínima) / 3. Límite Tercio Inferior = Pena Mínima + Amplitud.
# CLÁUSULA DE GUARDIA: Pide si es procesado primario (SI/NO). Si es "no", muestra mensaje y aborta con exit().

# Pide pena mínima (int) y pena máxima (int) en meses de cualquier delito usando \n.
# Pide pena propuesta en meses (int) para el procesado.
# Calcula amplitud = (maxima - minima) / 3.0 y limite_inferior = minima + amplitud.
# Usa if / else para evaluar si pena propuesta es <= limite_inferior (Conforme a Ley) o > limite_inferior (Observada).

proc_primario = input (f""" Hola, primero dime si eres o no un procesado primario. Responde (SÍ/NO): \n>>>  """).lower().translate(str.maketrans("áéíóú", "aeiou")).strip()
while proc_primario != "si" and proc_primario != "no":
    print (f""" \n La opción "{proc_primario}" no es una respuesta """)
    proc_primario = input (f""" Intenta nuevamente. \n\n¿Eres o no un procesado primario? \n Responde: (SÍ/NO) \n >>> """).lower().translate(str.maketrans("áéíóú", "aeiou")).strip()

if proc_primario == "no":
    print (f""" Lo siento, no accedes al beneficio \n Te sugiero acceder a una confesión anticipada """)
    exit ()

#No olvidar que todo lo que venga en adelante está en MESES. 
pena_propuesta = int (input (f"""\nAhora indica cuál es la pena que ha pedido el fiscal para tu caso: \n>>> Dilo en MESES por favor: \n>>> """))
pena_max = int ( input (f"""\nAhora indica cuál es la pena máxima del delito que se te imputa según el Código Penal: \n>>> Dilo en MESES por favor: \n>>> """))
pena_min = int (input (f"""\nAhora indica cuál es la pena mínima del delito que se te imputa según el Código Penal: \n>>> Dilo en MESES por favor:  \n>>> """))
amplitud =  float ((pena_max - pena_min) / 3)
lim_tercio_inf =  pena_min + amplitud

if pena_min <= pena_propuesta <= lim_tercio_inf: #fiscal propone bien la pena
    print (f""" La pena propuesta por el fiscal de {pena_propuesta} meses 
    sí está dentro del límite de tercios ya que tu pena mínima es de {pena_min} meses y 
    el límite del tercio inferior es de {lim_tercio_inf:.2f} meses. Muy bien\n""") 
elif pena_propuesta > lim_tercio_inf: #fiscal no propone bien, es medio abusivo
    print (f""" La pena propuesta por el fiscal de {pena_propuesta} meses 
        NO está dentro del límite de tercios ya la pena mínima es de {pena_min} meses y
        el límite del tercio inferior es de {lim_tercio_inf:.2f} meses. Ten cuidado\n """)
elif pena_propuesta < pena_min: #fiscal se pasó de sano
    print (f""" La pena propuesta por el fiscal de {pena_propuesta} meses 
        ESTÁ DEBAJO inclusive de la pena mínima. No te emociones 
        ya que debe haber un error. Ten cuidado \n""")
else: #creo que este else es por las... 
    print (f""" Hay un error en los datos, intenta de nuevo \n """) 
