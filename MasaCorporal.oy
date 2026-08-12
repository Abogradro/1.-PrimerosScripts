#Programa para calcular masa corporal (bmi) o body mass index

peso = float ( input ("Indicar tu peso en Kilogramos: "))
talla = float ( input ("Ahora indícame tu talla en metros: "))

masa_corporal = peso/(talla ** 2)


if masa_corporal < 18.5:
    clasificacion =  "Bajo Peso"
elif masa_corporal <= 24.9:
    clasificacion =  "Peso Normal (Saludable)"
elif masa_corporal <= 29.9:
    clasificacion = "Sobrepeso"
elif masa_corporal <= 34.9:
    clasificacion = "Obesidad Grado I"
elif masa_corporal <= 39.9:
    clasificacion = "Obesidad Grado II"
else: 
    clasificacion = "Obesidad Grado III (Mórbida)"

print (f""" Tu masa corporal es de {masa_corporal:.2f} 
       y te encuentras entro de la clasificación de {clasificacion}""")

