# MÓDULO PROCESAL PENAL: Control de Plazos de Detención Policial (Art. 264 NCPP)
# SUMILLA: Monitoreo hora a hora de los hitos procesales en detención por flagrancia.
# USUARIO OBJETIVO: Asistente Fiscal o Abogado Defensor en turno de flagrancia.
# 
# REQUERIMIENTOS TÉCNICOS:
# 1. Crear un bucle 'for' que recorra desde la hora 1 hasta la hora 48 (inclusive).
# 2. Evaluar de forma jerárquica las siguientes alertas usando el operador módulo (%):
#    - Múltiplos de 48: Imprimir con f-string:
#      f"Hora {hora}: [ALERTA MÁXIMA] Evaluación de Requerimiento de Prisión Preventiva"
#    - Múltiplos de 24 (solamente): Imprimir con f-string:
#      f"Hora {hora}: [INFORME DIARIO] Vencimiento del ciclo de 24 horas"
#    - Múltiplos de 12 (solamente): Imprimir con f-string:
#      f"Hora {hora}: [CONTROL FISCAL] Revisión de diligencias urgentes e inaplazables"
#    - Para cualquier otra hora (else): Imprimir con f-string:
#      f"Hora {hora}: Detención procesal en curso"

for hora in range (1,49):
    if hora == 48: 
        print(f"""Hora {hora}: [ALERTA MÁXIMA] Evaluación de Requerimiento de Prisión Preventiva""")
    elif hora % 24 == 0: 
        print (f"""Hora {hora}: [INFORME DIARIO] Vencimiento del ciclo de 24 horas""")
    elif hora % 12 == 0: 
        print (f"""Hora {hora}: [CONTROL FISCAL] Revisión de diligencias urgentes e inaplazables""")         
    else:
        print (f"""Hora {hora}: Detención procesal en curso  """)    
