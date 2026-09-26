// Frontend de Mi Control Corporal.
// Envía peso y talla al backend (Cloud Function /api/imc, escrita en Python).
// Si el backend no está disponible (por ejemplo, en el plan gratuito sin
// Cloud Functions), hace el mismo cálculo aquí en el navegador.

const CLAVE_HISTORIAL = "imc-historial";
const CLAVE_PERFIL = "imc-perfil";

const $ = (id) => document.getElementById(id);

// ---------- Cálculo local (copia de functions/imc.py) ----------

const CLASIFICACIONES = [
  [18.5, "Bajo Peso", "bajo", "Estás por debajo del peso saludable. Consulta con un profesional de salud para revisar tu alimentación."],
  [25, "Peso Normal (Saludable)", "normal", "¡Muy bien! Estás en el rango saludable. Mantén tu alimentación y actividad física."],
  [30, "Sobrepeso", "sobrepeso", "Estás un poco por encima del rango saludable. Caminar a diario y reducir azúcares y frituras ayuda mucho."],
  [35, "Obesidad Grado I", "obesidad1", "Es recomendable que un médico o nutricionista te acompañe con un plan."],
  [40, "Obesidad Grado II", "obesidad2", "Consulta con un médico: bajar de peso reducirá riesgos para tu salud."],
  [Infinity, "Obesidad Grado III (Mórbida)", "obesidad3", "Es importante que acudas a un médico lo antes posible para un control."],
];
const GRASA_HOMBRE = [[6, "Grasa esencial"], [14, "Atlético"], [18, "En forma"], [25, "Aceptable"], [Infinity, "Exceso de grasa"]];
const GRASA_MUJER = [[14, "Grasa esencial"], [21, "Atlético"], [25, "En forma"], [32, "Aceptable"], [Infinity, "Exceso de grasa"]];

const redondear = (n, d) => Math.round(n * 10 ** d) / 10 ** d;

function numero(valor, nombre) {
  const n = Number(String(valor ?? "").trim().replace(",", "."));
  if (String(valor ?? "").trim() === "" || Number.isNaN(n)) {
    throw new Error(`El dato '${nombre}' debe ser un número.`);
  }
  return n;
}

function calcularLocal({ peso, talla, edad, sexo }) {
  peso = numero(peso, "peso");
  talla = numero(talla, "talla");
  if (talla > 3) talla = talla / 100;

  if (peso < 2 || peso > 400) throw new Error("El peso debe estar entre 2 y 400 kg.");
  if (talla < 0.4 || talla > 2.5) throw new Error("La talla debe estar entre 0.40 y 2.50 metros.");

  const imc = peso / talla ** 2;
  const [, clasificacion, nivel, consejo] = CLASIFICACIONES.find(([limite]) => imc < limite);

  const pesoMin = 18.5 * talla ** 2;
  const pesoMax = 24.9 * talla ** 2;
  let diferencia = 0;
  if (peso < pesoMin) diferencia = pesoMin - peso;
  else if (peso > pesoMax) diferencia = pesoMax - peso;

  const resultado = {
    imc: redondear(imc, 2),
    clasificacion, nivel, consejo,
    talla: redondear(talla, 2),
    peso_min: redondear(pesoMin, 1),
    peso_max: redondear(pesoMax, 1),
    diferencia: redondear(diferencia, 1),
    grasa: null,
  };

  if (edad !== undefined && edad !== "" && (sexo === "hombre" || sexo === "mujer")) {
    edad = numero(edad, "edad");
    if (edad < 18 || edad > 110) throw new Error("La estimación de grasa corporal es para personas de 18 a 110 años.");
    const esHombre = sexo === "hombre" ? 1 : 0;
    const porcentaje = Math.max(1.2 * imc + 0.23 * edad - 10.8 * esHombre - 5.4, 2);
    const [, categoria] = (esHombre ? GRASA_HOMBRE : GRASA_MUJER).find(([limite]) => porcentaje < limite);
    resultado.grasa = {
      porcentaje: redondear(porcentaje, 1),
      categoria,
      kg: redondear(peso * porcentaje / 100, 1),
    };
  }
  return resultado;
}

// ---------- Llamada al backend ----------

async function calcular(datos) {
  let respuesta;
  try {
    respuesta = await fetch("/api/imc", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(datos),
    });
  } catch {
    return calcularLocal(datos); // sin conexión
  }

  const esJson = (respuesta.headers.get("content-type") || "").includes("application/json");
  if (!esJson) return calcularLocal(datos); // backend no desplegado

  const cuerpo = await respuesta.json();
  if (!respuesta.ok) throw new Error(cuerpo.error || "No se pudo calcular.");
  return cuerpo;
}

// ---------- Almacenamiento en el celular ----------

function leer(clave, porDefecto) {
  try {
    return JSON.parse(localStorage.getItem(clave)) ?? porDefecto;
  } catch {
    return porDefecto;
  }
}

function guardar(clave, valor) {
  try {
    localStorage.setItem(clave, JSON.stringify(valor));
  } catch {
    /* modo privado o almacenamiento bloqueado: la app sigue funcionando */
  }
}

// ---------- Pantalla ----------

const formatoFecha = new Intl.DateTimeFormat("es-PE", { day: "numeric", month: "short", year: "numeric" });
const kg = (n) => `${n.toLocaleString("es-PE", { maximumFractionDigits: 1 })} kg`;

function mostrarResultado(r) {
  $("r-imc").textContent = r.imc.toFixed(1);
  const insignia = $("r-clasificacion");
  insignia.textContent = r.clasificacion;
  insignia.className = `insignia ${r.nivel}`;
  $("r-consejo").textContent = r.consejo;

  const posicion = Math.min(Math.max((r.imc - 15) / 30, 0), 1) * 100;
  $("marcador").style.left = `${posicion}%`;

  $("r-rango").textContent = `${r.peso_min} – ${kg(r.peso_max)}`;
  if (r.diferencia > 0) {
    $("r-dif-titulo").textContent = "Para llegar al rango";
    $("r-dif").textContent = `subir ${kg(r.diferencia)}`;
  } else if (r.diferencia < 0) {
    $("r-dif-titulo").textContent = "Para llegar al rango";
    $("r-dif").textContent = `bajar ${kg(-r.diferencia)}`;
  } else {
    $("r-dif-titulo").textContent = "Diferencia";
    $("r-dif").textContent = "Estás en el rango";
  }

  $("bloque-grasa").hidden = !r.grasa;
  if (r.grasa) {
    $("r-grasa").textContent = `${r.grasa.porcentaje}% (${kg(r.grasa.kg)}) · ${r.grasa.categoria}`;
  }

  const seccion = $("resultado");
  seccion.hidden = false;
  seccion.scrollIntoView({ behavior: "smooth", block: "start" });
}

function pintarHistorial() {
  const historial = leer(CLAVE_HISTORIAL, []);
  const lista = $("historial");
  lista.replaceChildren();

  historial.forEach((m, i) => {
    const anterior = historial[i + 1]; // la lista va de la más reciente a la más antigua
    const li = document.createElement("li");

    const fecha = document.createElement("span");
    fecha.className = "fecha";
    fecha.textContent = formatoFecha.format(new Date(m.fecha));

    const valor = document.createElement("span");
    valor.className = "valor";
    valor.textContent = `IMC ${m.imc.toFixed(1)}`;

    const detalle = document.createElement("span");
    detalle.textContent = m.grasa ? `${kg(m.peso)} · grasa ${m.grasa}%` : `${kg(m.peso)} · ${m.clasificacion}`;

    const cambio = document.createElement("span");
    cambio.className = "cambio";
    if (anterior) {
      const d = redondear(m.peso - anterior.peso, 1);
      cambio.textContent = d === 0 ? "sin cambio" : `${d > 0 ? "+" : "−"}${kg(Math.abs(d))}`;
    }

    li.append(fecha, valor, detalle, cambio);
    lista.append(li);
  });

  $("vacio").hidden = historial.length > 0;
  $("borrar").hidden = historial.length === 0;
}

function cargarPerfil() {
  const perfil = leer(CLAVE_PERFIL, {});
  if (perfil.talla) $("talla").value = perfil.talla;
  if (perfil.edad) $("edad").value = perfil.edad;
  if (perfil.sexo) {
    const radio = document.querySelector(`input[name="sexo"][value="${perfil.sexo}"]`);
    if (radio) radio.checked = true;
  }
  if (perfil.edad || perfil.sexo) $("extra").open = true;
}

$("formulario").addEventListener("submit", async (evento) => {
  evento.preventDefault();
  const error = $("error");
  const boton = $("boton");
  error.hidden = true;

  const datos = {
    peso: $("peso").value,
    talla: $("talla").value,
    edad: $("edad").value,
    sexo: document.querySelector('input[name="sexo"]:checked')?.value,
  };

  boton.disabled = true;
  boton.textContent = "Calculando…";
  try {
    const r = await calcular(datos);
    mostrarResultado(r);

    guardar(CLAVE_PERFIL, { talla: r.talla, edad: datos.edad, sexo: datos.sexo });
    const historial = leer(CLAVE_HISTORIAL, []);
    historial.unshift({
      fecha: new Date().toISOString(),
      peso: numero(datos.peso, "peso"),
      imc: r.imc,
      clasificacion: r.clasificacion,
      grasa: r.grasa ? r.grasa.porcentaje : null,
    });
    guardar(CLAVE_HISTORIAL, historial.slice(0, 100));
    pintarHistorial();
  } catch (e) {
    error.textContent = e.message;
    error.hidden = false;
  } finally {
    boton.disabled = false;
    boton.textContent = "Calcular";
  }
});

$("borrar").addEventListener("click", () => {
  if (confirm("¿Borrar todo tu historial de este celular?")) {
    guardar(CLAVE_HISTORIAL, []);
    pintarHistorial();
  }
});

cargarPerfil();
pintarHistorial();
