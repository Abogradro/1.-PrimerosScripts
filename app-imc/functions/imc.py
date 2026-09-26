# Lógica del cálculo, tomada de MasaCorporal.py.
# Está separada de main.py para poder probarla sin Firebase:  python3 imc.py

# (límite superior, nombre, clave de color, consejo)
CLASIFICACIONES = [
    (18.5, "Bajo Peso", "bajo",
     "Estás por debajo del peso saludable. Consulta con un profesional de salud "
     "para revisar tu alimentación."),
    (25.0, "Peso Normal (Saludable)", "normal",
     "¡Muy bien! Estás en el rango saludable. Mantén tu alimentación y actividad física."),
    (30.0, "Sobrepeso", "sobrepeso",
     "Estás un poco por encima del rango saludable. Caminar a diario y reducir "
     "azúcares y frituras ayuda mucho."),
    (35.0, "Obesidad Grado I", "obesidad1",
     "Es recomendable que un médico o nutricionista te acompañe con un plan."),
    (40.0, "Obesidad Grado II", "obesidad2",
     "Consulta con un médico: bajar de peso reducirá riesgos para tu salud."),
    (float("inf"), "Obesidad Grado III (Mórbida)", "obesidad3",
     "Es importante que acudas a un médico lo antes posible para un control."),
]

# Categorías de % de grasa corporal (American Council on Exercise).
# (límite superior, nombre)
GRASA_HOMBRE = [(6, "Grasa esencial"), (14, "Atlético"), (18, "En forma"),
                (25, "Aceptable"), (float("inf"), "Exceso de grasa")]
GRASA_MUJER = [(14, "Grasa esencial"), (21, "Atlético"), (25, "En forma"),
               (32, "Aceptable"), (float("inf"), "Exceso de grasa")]


def _numero(valor, nombre):
    """Convierte a float aceptando coma decimal ("1,70")."""
    try:
        return float(str(valor).replace(",", "."))
    except (TypeError, ValueError):
        raise ValueError(f"El dato '{nombre}' debe ser un número.")


def calcular(peso, talla, edad=None, sexo=None):
    peso = _numero(peso, "peso")
    talla = _numero(talla, "talla")

    # Si alguien escribe la talla en centímetros (170), la pasamos a metros (1.70).
    if talla > 3:
        talla = talla / 100

    if not 2 <= peso <= 400:
        raise ValueError("El peso debe estar entre 2 y 400 kg.")
    if not 0.4 <= talla <= 2.5:
        raise ValueError("La talla debe estar entre 0.40 y 2.50 metros.")

    masa_corporal = peso / (talla ** 2)

    for limite, clasificacion, nivel, consejo in CLASIFICACIONES:
        if masa_corporal < limite:
            break

    # Rango de peso saludable para esa talla (IMC entre 18.5 y 24.9).
    peso_min = 18.5 * talla ** 2
    peso_max = 24.9 * talla ** 2
    if peso < peso_min:
        diferencia = peso_min - peso      # kg que faltan
    elif peso > peso_max:
        diferencia = peso_max - peso      # kg que sobran (negativo)
    else:
        diferencia = 0

    resultado = {
        "imc": round(masa_corporal, 2),
        "clasificacion": clasificacion,
        "nivel": nivel,
        "consejo": consejo,
        "talla": round(talla, 2),
        "peso_min": round(peso_min, 1),
        "peso_max": round(peso_max, 1),
        "diferencia": round(diferencia, 1),
        "grasa": None,
    }

    # % de grasa corporal (fórmula de Deurenberg). Solo para adultos, necesita edad y sexo.
    if edad not in (None, "") and sexo in ("hombre", "mujer"):
        edad = _numero(edad, "edad")
        if not 18 <= edad <= 110:
            raise ValueError("La estimación de grasa corporal es para personas de 18 a 110 años.")
        es_hombre = 1 if sexo == "hombre" else 0
        porcentaje = 1.20 * masa_corporal + 0.23 * edad - 10.8 * es_hombre - 5.4
        porcentaje = max(porcentaje, 2)

        tabla = GRASA_HOMBRE if es_hombre else GRASA_MUJER
        for limite, categoria in tabla:
            if porcentaje < limite:
                break

        resultado["grasa"] = {
            "porcentaje": round(porcentaje, 1),
            "categoria": categoria,
            "kg": round(peso * porcentaje / 100, 1),
        }

    return resultado


if __name__ == "__main__":
    # Prueba rápida en la terminal, como tu script original.
    peso = input("Indicar tu peso en Kilogramos: ")
    talla = input("Ahora indícame tu talla en metros: ")
    r = calcular(peso, talla)
    print(f"Tu masa corporal es de {r['imc']:.2f} y te encuentras dentro "
          f"de la clasificación de {r['clasificacion']}")
