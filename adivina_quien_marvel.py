import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# =============================
# Archivo de conocimiento (persistencia)
# =============================
DB_FILE = "conocimiento_marvel.json"

def cargar_conocimiento():
    """Carga (o crea) la base de conocimiento en JSON."""
    if not os.path.exists(DB_FILE):
        data_inicial = {"personajes_extra": []}
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data_inicial, f, indent=2, ensure_ascii=False)
        return data_inicial
    with open(DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"personajes_extra": []}

def guardar_conocimiento(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)


# =============================
# Base MARVEL con más atributos distintivos
# =============================
personajes_base = [
    {
        "nombre": "Iron Man",
        "atributos": {
            "armadura": True,
            "poderes": False,
            "vengador": True,
            "villano": False,
            "usa_arma": True,
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Captain America",
        "atributos": {
            "armadura": False,
            "poderes": True,          # suero supersoldado
            "vengador": True,
            "villano": False,
            "usa_arma": True,         # escudo como arma
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Thor",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": True,         # Mjolnir
            "humano": True,           # convive como humano en la Tierra
            "dios": True,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Hulk",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,  # no se miniaturiza
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Black Widow",
        "atributos": {
            "armadura": False,
            "poderes": False,
            "vengador": True,
            "villano": False,
            "usa_arma": True,  # pistolas
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Spider-Man",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": True,      # <-- clave
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Doctor Strange",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": True,
            "dios": False,
            "magia": True,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": True,        # místico
            "garras": False
        }
    },
    {
        "nombre": "Thanos",
        "atributos": {
            "armadura": True,
            "poderes": False,          # sin guantelete, no magia/mutación
            "vengador": False,
            "villano": True,
            "usa_arma": True,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": True,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Loki",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": False,
            "villano": True,
            "usa_arma": True,
            "humano": True,
            "dios": True,
            "magia": True,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": True,
            "garras": False
        }
    },
    {
        "nombre": "Ultron",
        "atributos": {
            "armadura": True,
            "poderes": False,
            "vengador": False,
            "villano": True,
            "usa_arma": True,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": True,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Black Panther",
        "atributos": {
            "armadura": True,          # traje de vibranio
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": True,
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,  # Wakanda tech
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": True              # <-- distintivo
        }
    },
    {
        "nombre": "Scarlet Witch",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": True,
            "dios": False,
            "magia": True,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": True,
            "garras": False
        }
    },
    {
        "nombre": "Ant-Man",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": True,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": True,   # <-- mini / gigante
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Deadpool",
        "atributos": {
            "armadura": False,
            "poderes": True,        # regeneración
            "vengador": False,
            "villano": False,
            "usa_arma": True,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": True,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,          # medio asociado pero no formalmente X-Men
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Wolverine",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": False,
            "villano": False,
            "usa_arma": True,       # garras son arma
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": True,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": True,           # <-- separa de Deadpool
            "guardianes": False,
            "hechiceria": False,
            "garras": True          # <-- separa brutalmente
        }
    },
    {
        "nombre": "Magneto",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": False,
            "villano": True,
            "usa_arma": False,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": False,
            "mutante": True,
            "tecnologia_avanzada": False,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": True,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Venom",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": False,
            "villano": True,
            "usa_arma": False,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": True,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": False,
            "trepa_paredes": True,   # simbionte
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": True          # forma garras/armas
        }
    },
    {
        "nombre": "Gamora",
        "atributos": {
            "armadura": False,
            "poderes": False,
            "vengador": False,
            "villano": False,
            "usa_arma": True,       # espadas
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": True,
            "robot": False,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": True,     # Guardianes de la Galaxia
            "hechiceria": False,
            "garras": False
        }
    },
    {
        "nombre": "Vision",
        "atributos": {
            "armadura": False,
            "poderes": True,
            "vengador": True,
            "villano": False,
            "usa_arma": False,
            "humano": False,
            "dios": False,
            "magia": False,
            "alien": False,
            "robot": True,
            "mutante": False,
            "tecnologia_avanzada": True,
            "trepa_paredes": False,
            "tamaño_variable": False,
            "xmen": False,
            "guardianes": False,
            "hechiceria": False,
            "garras": False
        }
    }
]

# Importante: sacar la lista de atributos a partir del primero
atributos = list(personajes_base[0]["atributos"].keys())


# =============================
# Motor de inferencia / reglas
# =============================
def aplicar_regla(lista_actual, atributo, respuesta):
    """Filtra candidatos manteniendo solo los que cumplen el atributo según la respuesta."""
    nueva_lista = []
    for p in lista_actual:
        valor = p["atributos"].get(atributo, None)
        if valor is None:
            continue
        if valor == respuesta:
            nueva_lista.append(p)
    return nueva_lista

def seleccionar_mejor_pregunta(candidatos, usados):
    """
    Elige el atributo que mejor divide a los candidatos aún posibles.
    Evita atributos ya preguntados.
    """
    mejor = None
    diferencia_minima = len(candidatos)
    for atributo in atributos:
        if atributo in usados:
            continue
        vals = [c["atributos"].get(atributo, None) for c in candidatos]
        positivos = sum(1 for v in vals if v is True)
        negativos = sum(1 for v in vals if v is False)
        # Si nadie tiene info útil sobre ese atributo, lo saltamos
        if positivos + negativos == 0:
            continue
        diferencia = abs(positivos - negativos)
        if diferencia < diferencia_minima:
            diferencia_minima = diferencia
            mejor = atributo
    return mejor

def hay_pregunta_discriminante(candidatos, usados):
    """
    ¿Queda algún atributo sin preguntar que aún pueda separar
    a los candidatos (al menos uno True y uno False)?
    """
    for atributo in atributos:
        if atributo in usados:
            continue
        valores = [c["atributos"].get(atributo, None) for c in candidatos]
        positivos = sum(1 for v in valores if v is True)
        negativos = sum(1 for v in valores if v is False)
        if positivos > 0 and negativos > 0:
            return True
    return False

def resumen_personaje(p):
    atr = p["atributos"]
    rol = []
    if atr.get("vengador"): rol.append("Vengador")
    if atr.get("villano"):  rol.append("Villano")
    if atr.get("mutante"):  rol.append("Mutante")
    if atr.get("alien"):    rol.append("Alien")
    if atr.get("robot"):    rol.append("Sintético")
    if atr.get("dios"):     rol.append("Dios")
    if atr.get("magia"):    rol.append("Místico")
    if atr.get("guardianes"): rol.append("Guardián")
    if atr.get("xmen"):       rol.append("X-Men")
    if atr.get("garras"):     rol.append("Garras")
    if atr.get("tamaño_variable"): rol.append("Cambio de tamaño")
    if atr.get("trepa_paredes"):   rol.append("Trepa paredes")
    if not rol:
        rol.append("Independiente")
    return f"{p['nombre']}\nPerfil: " + " / ".join(rol)


# =============================
# Interfaz gráfica + lógica de juego
# =============================
class AdivinaQuienMarvel:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina Quién - MARVEL // S.H.I.E.L.D. Scanner v3.0")
        self.master.geometry("900x600")
        self.master.configure(bg="#0b0c10")
        self.master.resizable(False, False)

        self.db = cargar_conocimiento()
        self.reset_estado()

        # ----- Layout general -----
        self.left_frame = tk.Frame(master, bg="#0b0c10")
        self.left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.right_frame = tk.Frame(
            master,
            bg="#1f2833",
            width=260,
            height=400,
            highlightthickness=2,
            highlightbackground="#45a29e"
        )
        self.right_frame.pack(side="right", fill="y", padx=20, pady=20)

        # ----- Lado izquierdo -----
        self.titulo = tk.Label(
            self.left_frame,
            text="Adivina Quién - MARVEL",
            font=("Helvetica", 22, "bold"),
            fg="#ff1e1e",
            bg="#0b0c10"
        )
        self.titulo.pack(pady=(0, 5))

        self.subtitulo = tk.Label(
            self.left_frame,
            text="Unidad de Reconocimiento S.H.I.E.L.D.",
            font=("Helvetica", 11, "bold"),
            fg="#45a29e",
            bg="#0b0c10"
        )
        self.subtitulo.pack(pady=(0, 20))

        self.texto = tk.Label(
            self.left_frame,
            text=("Piensa en un personaje del universo Marvel.\n"
                  "Yo intentaré identificarlo haciendo preguntas.\n\n"
                  "Haz clic en 'Iniciar Escaneo' para comenzar."),
            font=("Helvetica", 13),
            fg="white",
            bg="#0b0c10",
            justify="center"
        )
        self.texto.pack(pady=20)

        # Controles superiores (Iniciar / Reiniciar)
        self.top_controls = tk.Frame(self.left_frame, bg="#0b0c10")
        self.top_controls.pack(pady=(0, 10))

        self.boton_comenzar = tk.Button(
            self.top_controls,
            text="Iniciar Escaneo",
            font=("Helvetica", 12, "bold"),
            bg="#45a29e",
            fg="white",
            activebackground="#66fcf1",
            activeforeground="#0b0c10",
            command=self.iniciar
        )
        self.boton_comenzar.grid(row=0, column=0, padx=5)

        self.boton_reiniciar = tk.Button(
            self.top_controls,
            text="Reiniciar",
            font=("Helvetica", 12, "bold"),
            bg="#222222",
            fg="#ffffff",
            activebackground="#444444",
            activeforeground="#ffffff",
            command=self.reiniciar_juego
        )
        self.boton_reiniciar.grid(row=0, column=1, padx=5)

        # Botones Sí / No (aparecen cuando arranca el juego)
        self.frame_botones = tk.Frame(self.left_frame, bg="#0b0c10")
        self.boton_si = tk.Button(
            self.frame_botones,
            text="Sí",
            font=("Helvetica", 14, "bold"),
            bg="#45a29e",
            fg="white",
            width=8,
            command=lambda: self.responder(True)
        )
        self.boton_no = tk.Button(
            self.frame_botones,
            text="No",
            font=("Helvetica", 14, "bold"),
            bg="#c3073f",
            fg="white",
            width=8,
            command=lambda: self.responder(False)
        )

        self.estado_label = tk.Label(
            self.left_frame,
            text="",
            font=("Helvetica", 10),
            fg="#c5c6c7",
            bg="#0b0c10",
            justify="center"
        )
        self.estado_label.pack(pady=10)

        # ----- Panel lateral -----
        self.side_header = tk.Label(
            self.right_frame,
            text="S.H.I.E.L.D. SCANNER v3.0",
            font=("Helvetica", 12, "bold"),
            fg="#66fcf1",
            bg="#1f2833"
        )
        self.side_header.pack(pady=(10, 2))

        self.side_sub = tk.Label(
            self.right_frame,
            text="Candidatos activos:",
            font=("Helvetica", 10),
            fg="#c5c6c7",
            bg="#1f2833"
        )
        self.side_sub.pack(pady=(0, 10))

        self.caja_scroll = tk.Frame(self.right_frame, bg="#1f2833")
        self.caja_scroll.pack(fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.caja_scroll, orient="vertical")
        self.lista_candidatos = tk.Listbox(
            self.caja_scroll,
            yscrollcommand=self.scrollbar.set,
            bg="#0b0c10",
            fg="white",
            font=("Consolas", 11),
            width=28,
            height=16,
            highlightthickness=1,
            highlightbackground="#45a29e",
            selectbackground="#45a29e",
            activestyle="none"
        )
        self.scrollbar.config(command=self.lista_candidatos.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lista_candidatos.pack(side="left", fill="both", expand=True)

        self.side_footer = tk.Label(
            self.right_frame,
            text="Estado objetivo: [ escaneando... ]",
            font=("Helvetica", 10, "bold"),
            fg="#66fcf1",
            bg="#1f2833",
            justify="center"
        )
        self.side_footer.pack(pady=(5, 10))

        self.creditos = tk.Label(
            self.left_frame,
            text="Proyecto IA - Reconocimiento de Entidad Marvel (aprendizaje incremental)",
            font=("Helvetica", 9),
            fg="#c5c6c7",
            bg="#0b0c10"
        )
        self.creditos.pack(side="bottom", pady=5)

        self._refrescar_lista_lateral()

    # =========================
    # Estado / utilidades
    # =========================
    def reset_estado(self):
        """Resetea la lógica del juego (sin tocar la UI)."""
        db = cargar_conocimiento()
        self.posibles = personajes_base.copy() + db["personajes_extra"].copy()
        self.preguntas_hechas = []
        self.atributo_actual = None
        self.juego_terminado = False

    def _refrescar_lista_lateral(self):
        self.lista_candidatos.delete(0, tk.END)
        for p in self.posibles:
            self.lista_candidatos.insert(tk.END, "• " + p["nombre"])
        self.side_sub.config(text=f"Candidatos activos: {len(self.posibles)}")

    # =========================
    # Flujo del juego
    # =========================
    def iniciar(self):
        """Arranca la partida. Oculta 'Iniciar Escaneo' y muestra Sí/No."""
        if self.juego_terminado:
            return

        # ocultar el botón "Iniciar Escaneo"
        self.boton_comenzar.grid_remove()

        # mostrar botones Sí / No
        self.frame_botones.pack(pady=10)
        self.boton_si.grid(row=0, column=0, padx=15)
        self.boton_no.grid(row=0, column=1, padx=15)

        self.estado_label.config(
            text="Escaneo en progreso... responde con sinceridad 😏",
            fg="#c5c6c7"
        )

        self.nueva_pregunta()

    def reiniciar_juego(self):
        """Reinicia la partida y vuelve a mostrar 'Iniciar Escaneo'."""
        self.reset_estado()
        self._refrescar_lista_lateral()

        self.texto.config(
            text=("Piensa en un personaje del universo Marvel.\n"
                  "Yo intentaré identificarlo haciendo preguntas.\n\n"
                  "Haz clic en 'Iniciar Escaneo' para comenzar."),
            fg="white"
        )
        self.estado_label.config(
            text="Juego reiniciado. Listo para un nuevo escaneo.",
            fg="#66fcf1"
        )
        self.side_footer.config(
            text="Estado objetivo: [ escaneando... ]",
            fg="#66fcf1"
        )

        # esconder botones Sí/No otra vez
        self.frame_botones.pack_forget()

        # volver a enseñar "Iniciar Escaneo"
        self.boton_comenzar.grid()

    def nueva_pregunta(self):
        """Genera la siguiente pregunta si todavía hay forma de distinguir candidatos."""
        # si ya solo queda uno o ninguno → ve a finalizar
        if len(self.posibles) <= 1:
            self.finalizar()
            return

        # si ya no quedan preguntas que los separen → finalizar (fase de confirmación / elección)
        if not hay_pregunta_discriminante(self.posibles, self.preguntas_hechas):
            self.finalizar()
            return

        # elegir mejor atributo entre los que no se han preguntado
        self.atributo_actual = seleccionar_mejor_pregunta(self.posibles, self.preguntas_hechas)
        if not self.atributo_actual:
            self.finalizar()
            return

        self.preguntas_hechas.append(self.atributo_actual)

        self.texto.config(
            text=f"¿El objetivo cumple con:\n'{self.atributo_actual}' ?",
            fg="white"
        )
        self.estado_label.config(
            text=f"Coincidencias actuales: {len(self.posibles)}",
            fg="#c5c6c7"
        )

    def responder(self, respuesta_bool):
        """Procesa clic en Sí / No y aplica filtrado."""
        if self.juego_terminado:
            return

        self.posibles = aplicar_regla(self.posibles, self.atributo_actual, respuesta_bool)
        self._refrescar_lista_lateral()

        if len(self.posibles) <= 1:
            self.finalizar()
        else:
            self.nueva_pregunta()

    def finalizar(self):
        """Decide el resultado final: adivina, pide confirmación o aprende."""
        if self.juego_terminado:
            return
        self.juego_terminado = True

        # ya no necesitamos los botones Sí / No
        self.frame_botones.pack_forget()

        # ---- CASO 1: solo queda uno ----
        if len(self.posibles) == 1:
            objetivo = self.posibles[0]
            ficha = resumen_personaje(objetivo)
            es_villano = objetivo["atributos"].get("villano", False)

            color_res = "#ff1e1e" if es_villano else "#45a29e"
            status_txt = "Estado objetivo: AMENAZA" if es_villano else "Estado objetivo: ALIADO"

            self.texto.config(
                text="Identidad detectada:\n" + ficha + "\n\n¿Adiviné correctamente?",
                fg=color_res
            )
            self.side_footer.config(text=status_txt, fg=color_res)
            self.estado_label.config(
                text="Selecciona Sí / No en la ventana emergente.",
                fg="#66fcf1"
            )

            correcto = messagebox.askyesno(
                "Confirmación",
                f"¿Tu personaje era {objetivo['nombre']}?"
            )
            if correcto:
                messagebox.showinfo("Listo", "Objetivo confirmado. Base de conocimiento intacta.")
            else:
                self.aprender_nuevo_personaje()

        # ---- CASO 2: quedan varios candidatos ----
        elif len(self.posibles) > 1:
            nombres = "\n".join(["• " + p["nombre"] for p in self.posibles])
            self.texto.config(
                text="Posibles coincidencias:\n" + nombres +
                     "\n\n¿Tu personaje está en esta lista?",
                fg="#ffffff"
            )
            self.side_footer.config(
                text="Estado objetivo: AMBIGUO",
                fg="#c5c6c7"
            )
            self.estado_label.config(
                text="Selecciona en la ventana emergente.",
                fg="#ffcc00"
            )

            esta_en_lista = messagebox.askyesno(
                "Está en la lista",
                "¿Tu personaje está en la lista mostrada?"
            )

            if esta_en_lista:
                nombres_solo = [p["nombre"] for p in self.posibles]
                elegido = simpledialog.askstring(
                    "¿Cuál era?",
                    "Escribe el nombre EXACTO de tu personaje de la lista:\n" +
                    "\n".join(nombres_solo)
                )

                if elegido:
                    match = None
                    for p in self.posibles:
                        if p["nombre"].lower().strip() == elegido.lower().strip():
                            match = p
                            break

                    if match:
                        ficha = resumen_personaje(match)
                        es_villano = match["atributos"].get("villano", False)

                        color_res = "#ff1e1e" if es_villano else "#45a29e"
                        status_txt = "Estado objetivo: AMENAZA" if es_villano else "Estado objetivo: ALIADO"

                        self.texto.config(
                            text="Identidad confirmada manualmente:\n" + ficha,
                            fg=color_res
                        )
                        self.side_footer.config(
                            text=status_txt,
                            fg=color_res
                        )
                        self.estado_label.config(
                            text="Gracias. Registrado como coincidencia conocida.",
                            fg="#66fcf1"
                        )
                    else:
                        messagebox.showinfo(
                            "No encontré coincidencia",
                            "No reconocí ese nombre dentro de la lista. Lo entrenaré como nuevo."
                        )
                        self.aprender_nuevo_personaje()
                else:
                    # canceló / no escribió
                    self.aprender_nuevo_personaje()

            else:
                # no estaba en la lista -> es personaje nuevo
                self.texto.config(
                    text="Ok, entonces no estabas pensando en ninguno de los conocidos.\nEntréname con ese personaje.",
                    fg="#ffffff"
                )
                self.side_footer.config(
                    text="Estado objetivo: DESCONOCIDO",
                    fg="#ff1e1e"
                )
                self.estado_label.config(
                    text="Aprendiendo nuevo registro...",
                    fg="#ff1e1e"
                )
                self.aprender_nuevo_personaje()

        # ---- CASO 3: 0 candidatos ----
        else:
            self.texto.config(
                text="No pude identificar al objetivo.\n"
                     "(No coincidió con nadie en mi base.)\n"
                     "Dime quién era para entrenarme.",
                fg="#ffffff"
            )
            self.side_footer.config(
                text="Estado objetivo: DESCONOCIDO",
                fg="#ff1e1e"
            )
            self.estado_label.config(
                text="Sin coincidencias en la base. Entrenando...",
                fg="#ff1e1e"
            )
            self.aprender_nuevo_personaje()

    # =========================
    # Aprendizaje
    # =========================
    def aprender_nuevo_personaje(self):
        """Pregunta quién era el personaje y lo guarda con sus atributos en JSON."""
        nombre_nuevo = simpledialog.askstring(
            "Aprendizaje",
            "¿Cuál era tu personaje?"
        )

        if not nombre_nuevo:
            messagebox.showinfo(
                "OK",
                "No se proporcionó nombre. No se aprendió nada nuevo."
            )
            return

        messagebox.showinfo(
            "Ahora dime...",
            "Te voy a hacer unas preguntas rápidas sobre ese personaje.\n"
            "Responde Sí o No.\n"
            "(Esto entrena mi base para la próxima vez.)"
        )

        nuevos_atributos = {}
        for atr in atributos:
            resp = messagebox.askyesno(
                "Atributo",
                f"¿{nombre_nuevo} cumple '{atr}'?"
            )
            nuevos_atributos[atr] = bool(resp)

        nuevo_personaje = {
            "nombre": nombre_nuevo,
            "atributos": nuevos_atributos
        }

        db = cargar_conocimiento()
        db["personajes_extra"].append(nuevo_personaje)
        guardar_conocimiento(db)

        messagebox.showinfo(
            "Entrenamiento completado",
            f"Registré a {nombre_nuevo}.\nLa próxima vez podré reconocerlo 😉"
        )

        self.texto.config(
            text=f"Nuevo objetivo agregado:\n{nombre_nuevo}\nGracias por entrenarme.",
            fg="#66fcf1"
        )
        self.side_footer.config(
            text="Estado objetivo: BASE ACTUALIZADA",
            fg="#66fcf1"
        )
        self.estado_label.config(
            text="Conocimiento guardado en conocimiento_marvel.json",
            fg="#66fcf1"
        )


# =============================
# Ejecutar
# =============================
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaQuienMarvel(root)
    root.mainloop()
