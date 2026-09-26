# Backend: Cloud Function de Firebase (Python).
# Recibe  POST /api/imc  con JSON {"peso": 70, "talla": 1.70, "edad": 35, "sexo": "hombre"}
# y responde con el resultado de imc.calcular().

import json

from firebase_functions import https_fn, options

import imc


def _respuesta(datos, estado=200):
    return https_fn.Response(
        json.dumps(datos, ensure_ascii=False),
        status=estado,
        mimetype="application/json",
    )


@https_fn.on_request(
    region="us-central1",
    memory=options.MemoryOption.MB_256,
    max_instances=3,  # tope de instancias para que el costo no se dispare
)
def calcular_imc(req: https_fn.Request) -> https_fn.Response:
    if req.method != "POST":
        return _respuesta({"error": "Usa el método POST."}, 405)

    datos = req.get_json(silent=True) or {}
    try:
        resultado = imc.calcular(
            datos.get("peso"),
            datos.get("talla"),
            datos.get("edad"),
            datos.get("sexo"),
        )
    except ValueError as error:
        return _respuesta({"error": str(error)}, 400)

    return _respuesta(resultado)
