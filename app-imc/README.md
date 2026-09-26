# Mi Control Corporal

App web para el celular, basada en `MasaCorporal.py`. La persona escribe su peso y talla, y la página le muestra:

- su **índice de masa corporal (IMC)** y la clasificación (bajo peso, normal, sobrepeso, obesidad I, II y III),
- el **rango de peso saludable** para su talla y cuántos kilos le faltan o le sobran para llegar a él,
- su **% de grasa corporal estimado**, si también escribe su edad y sexo (fórmula de Deurenberg, solo para adultos),
- un **historial** de sus mediciones con el cambio de peso entre una y otra.

El historial se guarda solo en el celular de cada persona. No hay cuentas ni base de datos, así que nadie ve los datos de otro.

## Estructura

```
app-imc/
├── firebase.json          configuración de Hosting y Functions
├── .firebaserc            aquí va el ID de tu proyecto de Firebase
├── public/                FRONTEND (lo que se ve en el celular)
│   ├── index.html
│   ├── styles.css
│   ├── app.js
│   ├── manifest.webmanifest   permite "Agregar a pantalla de inicio"
│   └── icon.svg
└── functions/             BACKEND (Python)
    ├── main.py            Cloud Function que responde en /api/imc
    ├── imc.py             el cálculo (tu MasaCorporal.py mejorado)
    └── requirements.txt
```

El frontend envía los datos a `/api/imc` y el backend en Python responde con el resultado. Si el backend no está desplegado o no hay conexión, `app.js` hace el mismo cálculo en el navegador. Por eso la app funciona también en el plan gratuito de Firebase.

Si cambias una regla del cálculo, cámbiala en `functions/imc.py` **y** en la parte "Cálculo local" de `public/app.js`.

## Probar el cálculo en la terminal

```bash
cd functions
python3 imc.py
```

## Cómo subirla a Firebase

### 1. Preparar (una sola vez)

1. Instala [Node.js](https://nodejs.org) y, para el backend, **Python 3.12**.
2. Instala la herramienta de Firebase e inicia sesión:
   ```bash
   npm install -g firebase-tools
   firebase login
   ```
3. En <https://console.firebase.google.com> crea un proyecto (por ejemplo `control-corporal-familia`).
4. Abre `.firebaserc` y cambia `TU-PROYECTO-FIREBASE` por el ID de tu proyecto.

### 2A. Subir solo el frontend (plan gratuito Spark)

```bash
cd app-imc
firebase deploy --only hosting
```

Así ya funciona: el cálculo lo hace el navegador.

### 2B. Subir frontend y backend en Python (plan Blaze)

Firebase exige el plan **Blaze** (pago por uso) para las Cloud Functions. Para una familia el consumo cabe de sobra en la cuota gratuita, y `main.py` limita la función a 3 instancias. Aun así, te recomiendo poner una alerta de presupuesto en Google Cloud.

```bash
cd app-imc/functions
python3.12 -m venv venv
source venv/bin/activate          # en Windows: venv\Scripts\activate
pip install -r requirements.txt
deactivate
cd ..
firebase deploy
```

### 3. Compartir

Al terminar, Firebase te da un enlace como `https://TU-PROYECTO.web.app`. Envíalo por WhatsApp a tu familia.

En el celular pueden abrirlo y elegir **"Agregar a pantalla de inicio"** en el menú del navegador, y les quedará como una app.

## Aviso

Los resultados son una referencia general. El IMC y la fórmula de grasa corporal son estimaciones y no reemplazan la evaluación de un médico o nutricionista.
