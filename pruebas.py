import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

DB_FILE = "conocimiento_marvel.json"

def cargar_conocimiento():
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

personajes_base = [
    {"nombre": "Iron Man", "atributos": {"armadura": True, "poderes": False, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Captain America", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Thor", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "dios": True, "humano": True, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Hulk", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Black Widow", "atributos": {"armadura": False, "poderes": False, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Spider-Man", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Doctor Strange", "atributos": {"magia": True, "armadura": False, "poderes": True, "vengador": True, "villano": False, "humano": True, "usa_arma": False, "dios": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Thanos", "atributos": {"armadura": True, "poderes": False, "vengador": False, "villano": True, "usa_arma": True, "alien": True, "humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Loki", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": True, "dios": True, "humano": True, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Ultron", "atributos": {"armadura": True, "poderes": False, "vengador": False, "villano": True, "usa_arma": True, "robot": True, "humano": False, "dios": False, "magia": False, "alien": False, "mutante": False}},
    {"nombre": "Black Panther", "atributos": {"armadura": True, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Scarlet Witch", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "magia": True, "humano": True, "dios": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Ant-Man", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Deadpool", "atributos": {"mutante": True, "armadura": False, "poderes": True, "vengador": False, "villano": False, "usa_arma": True, "humano": False, "dios": False, "magia": False, "alien": False, "robot": False}},
    {"nombre": "Wolverine", "atributos": {"mutante": True, "armadura": False, "poderes": True, "vengador": False, "villano": False, "usa_arma": True, "humano": False, "dios": False, "magia": False, "alien": False, "robot": False}},
    {"nombre": "Magneto", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": False, "mutante": True, "humano": False, "dios": False, "magia": False, "alien": False, "robot": False}},
    {"nombre": "Venom", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": False, "alien": True, "humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Gamora", "atributos": {"armadura": False, "poderes": False, "vengador": False, "villano": False, "usa_arma": True, "alien": True, "humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Vision", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "robot": True, "humano": False, "dios": False, "magia": False, "alien": False, "mutante": False}},
]

atributos = list(personajes_base[0]["atributos"].keys())


def aplicar_regla(lista_actual, atributo, respuesta):
    nueva_lista = []
    for p in lista_actual:
        valor = p["atributos"].get(atributo, None)
        if valor is None:
            continue
        if valor == respuesta:
            nueva_lista.append(p)
    return nueva_lista

def seleccionar_mejor_pregunta(candidatos, usados):
    mejor = None
    diferencia_minima = len(candidatos)
    for atributo in atributos:
        if atributo in usados:
            continue
        valores = [c["atributos"].get(atributo, None) for c in candidatos]
        positivos = sum(1 for v in valores if v is True)
        negativos = sum(1 for v in valores if v is False)
        if positivos + negativos == 0:
            continue
        diferencia = abs(positivos - negativos)
        if diferencia < diferencia_minima:
            diferencia_minima = diferencia
            mejor = atributo
    return mejor

def resumen_personaje(p):
    atr = p["atributos"]
    rol = []
    if atr.get("vengador"): rol.append("Vengador")
    if atr.get("villano"): rol.append("Villano")
    if atr.get("mutante"): rol.append("Mutante")
    if atr.get("alien"): rol.append("Alien")
    if atr.get("robot"): rol.append("Sintético")
    if atr.get("dios"): rol.append("Dios")
    if atr.get("magia"): rol.append("Místico")
    if not rol: rol.append("Independiente")
    detalle = " / ".join(rol)
    return f"{p['nombre']}\nPerfil: {detalle}"


class AdivinaQuienMarvel:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina Quién - MARVEL // S.H.I.E.L.D. Scanner v2.1")
        self.master.geometry("900x580")
        self.master.configure(bg="#0b0c10")
        self.master.resizable(False, False)

        # estado inicial del juego
        self.db = cargar_conocimiento()
        self.reset_estado()

        # layout izquierda/derecha
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

        # lado izquierdo UI
        self.titulo = tk.Label(self.left_frame, text="Adivina Quién - MARVEL",
                               font=("Helvetica", 22, "bold"),
                               fg="#ff1e1e", bg="#0b0c10")
        self.titulo.pack(pady=(0, 5))

        self.subtitulo = tk.Label(self.left_frame,
                                  text="Unidad de Reconocimiento S.H.I.E.L.D.",
                                  font=("Helvetica", 11, "bold"),
                                  fg="#45a29e", bg="#0b0c10")
        self.subtitulo.pack(pady=(0, 20))

        self.texto = tk.Label(self.left_frame,
                              text=("Piensa en un personaje del universo Marvel.\n"
                                    "Yo intentaré identificarlo haciendo preguntas.\n\n"
                                    "Haz clic en 'Iniciar Escaneo' para comenzar."),
                              font=("Helvetica", 13),
                              fg="white", bg="#0b0c10",
                              justify="center")
        self.texto.pack(pady=20)

        # fila de botones de control arriba del juego
        self.top_controls = tk.Frame(self.left_frame, bg="#0b0c10")
        self.top_controls.pack(pady=(0, 10))

        self.boton_comenzar = tk.Button(self.top_controls,
                                        text="Iniciar Escaneo",
                                        font=("Helvetica", 12, "bold"),
                                        bg="#45a29e", fg="white",
                                        activebackground="#66fcf1",
                                        activeforeground="#0b0c10",
                                        command=self.iniciar)
        self.boton_comenzar.grid(row=0, column=0, padx=5)

        self.boton_reiniciar = tk.Button(self.top_controls,
                                         text="Reiniciar",
                                         font=("Helvetica", 12, "bold"),
                                         bg="#222222", fg="#ffffff",
                                         activebackground="#444444",
                                         activeforeground="#ffffff",
                                         command=self.reiniciar_juego)
        self.boton_reiniciar.grid(row=0, column=1, padx=5)

        # botones Sí / No (por ahora ocultos)
        self.frame_botones = tk.Frame(self.left_frame, bg="#0b0c10")
        self.boton_si = tk.Button(self.frame_botones,
                                  text="Sí",
                                  font=("Helvetica", 14, "bold"),
                                  bg="#45a29e", fg="white",
                                  width=8,
                                  command=lambda: self.responder(True))
        self.boton_no = tk.Button(self.frame_botones,
                                  text="No",
                                  font=("Helvetica", 14, "bold"),
                                  bg="#c3073f", fg="white",
                                  width=8,
                                  command=lambda: self.responder(False))

        self.estado_label = tk.Label(self.left_frame,
                                     text="",
                                     font=("Helvetica", 10),
                                     fg="#c5c6c7",
                                     bg="#0b0c10",
                                     justify="center")
        self.estado_label.pack(pady=10)

        # panel lateral scanner
        self.side_header = tk.Label(self.right_frame,
                                    text="S.H.I.E.L.D. SCANNER v2.1",
                                    font=("Helvetica", 12, "bold"),
                                    fg="#66fcf1", bg="#1f2833")
        self.side_header.pack(pady=(10, 2))

        self.side_sub = tk.Label(self.right_frame,
                                 text="Candidatos activos:",
                                 font=("Helvetica", 10),
                                 fg="#c5c6c7", bg="#1f2833")
        self.side_sub.pack(pady=(0, 10))

        self.caja_scroll = tk.Frame(self.right_frame, bg="#1f2833")
        self.caja_scroll.pack(fill="both", expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.caja_scroll, orient="vertical")
        self.lista_candidatos = tk.Listbox(
            self.caja_scroll,
            yscrollcommand=self.scrollbar.set,
            bg="#0b0c10", fg="white",
            font=("Consolas", 11),
            width=28, height=16,
            highlightthickness=1,
            highlightbackground="#45a29e",
            selectbackground="#45a29e",
            activestyle="none",
        )
        self.scrollbar.config(command=self.lista_candidatos.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lista_candidatos.pack(side="left", fill="both", expand=True)

        self.side_footer = tk.Label(self.right_frame,
                                    text="Estado objetivo: [ escaneando... ]",
                                    font=("Helvetica", 10, "bold"),
                                    fg="#66fcf1", bg="#1f2833",
                                    justify="center")
        self.side_footer.pack(pady=(5, 10))

        self.creditos = tk.Label(self.left_frame,
                                 text="Proyecto IA - Reconocimiento de Entidad Marvel (con aprendizaje)",
                                 font=("Helvetica", 9),
                                 fg="#c5c6c7", bg="#0b0c10")
        self.creditos.pack(side="bottom", pady=5)

        self._refrescar_lista_lateral()

    def reset_estado(self):
        """Resetea la lógica del juego (sin tocar la UI todavía)."""
        # recargar db en RAM
        self.db = cargar_conocimiento()
        # reconstruir lista de candidatos con lo aprendido
        self.posibles = personajes_base.copy() + self.db["personajes_extra"].copy()
        self.preguntas_hechas = []
        self.atributo_actual = None
        self.juego_terminado = False

    def reiniciar_juego(self):
        """Click en botón Reiniciar: limpia estado y resetea textos."""
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

        # ocultar botones sí/no si estaban visibles
        self.frame_botones.pack_forget()
        # volver a mostrar el botón de iniciar si lo quieres visible
        # (no lo removemos, solo lo dejamos ahí)
        # nota: el botón "Iniciar Escaneo" siempre está, no se esconde más

    def _refrescar_lista_lateral(self):
        self.lista_candidatos.delete(0, tk.END)
        for p in self.posibles:
            self.lista_candidatos.insert(tk.END, "• " + p["nombre"])
        self.side_sub.config(text=f"Candidatos activos: {len(self.posibles)}")

    def iniciar(self):
        if self.juego_terminado:
            return  # si ya cerró una partida, mejor que le dé Reiniciar
        self.frame_botones.pack(pady=10)
        self.boton_si.grid(row=0, column=0, padx=15)
        self.boton_no.grid(row=0, column=1, padx=15)
        self.estado_label.config(text="Escaneo en progreso... responde con sinceridad 😏", fg="#c5c6c7")
        self.nueva_pregunta()

    def nueva_pregunta(self):
        if len(self.posibles) <= 1:
            self.finalizar()
            return
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
        if self.juego_terminado:
            return
        self.posibles = aplicar_regla(self.posibles, self.atributo_actual, respuesta_bool)
        self._refrescar_lista_lateral()
        if len(self.posibles) <= 1:
            self.finalizar()
        else:
            self.nueva_pregunta()

    def finalizar(self):
        if self.juego_terminado:
            return
        self.juego_terminado = True
        self.frame_botones.pack_forget()

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
            self.estado_label.config(text="Selecciona Sí / No en la ventana emergente.", fg="#66fcf1")

            correcto = messagebox.askyesno("Confirmación", f"¿Tu personaje era {objetivo['nombre']}?")

            if correcto:
                messagebox.showinfo("Listo", "Objetivo confirmado. Base de conocimiento intacta.")
            else:
                self.aprender_nuevo_personaje()

        elif len(self.posibles) > 1:
            nombres = "\n".join(["• " + p["nombre"] for p in self.posibles])
            self.texto.config(
                text="Posibles coincidencias:\n" + nombres + "\n\nNo pude aislar uno solo.\nAyúdame diciéndome cuál era tu personaje.",
                fg="#ffffff"
            )
            self.side_footer.config(text="Estado objetivo: INCONCLUSO", fg="#c5c6c7")
            self.estado_label.config(text="Aprendiendo nuevo registro...", fg="#ff1e1e")
            self.aprender_nuevo_personaje()

        else:
            self.texto.config(
                text="No pude identificar al objetivo.\n(No coincidió con nadie en mi base.)\nDime quién era para entrenarme.",
                fg="#ffffff"
            )
            self.side_footer.config(text="Estado objetivo: DESCONOCIDO", fg="#ff1e1e")
            self.estado_label.config(text="Sin coincidencias en la base. Entrenando...", fg="#ff1e1e")
            self.aprender_nuevo_personaje()

    def aprender_nuevo_personaje(self):
        nombre_nuevo = simpledialog.askstring("Aprendizaje", "¿Cuál era tu personaje?")
        if not nombre_nuevo:
            messagebox.showinfo("OK", "No se proporcionó nombre. No se aprendió nada nuevo.")
            return

        messagebox.showinfo(
            "Ahora dime...",
            "Te voy a hacer unas preguntas rápidas sobre ese personaje.\nResponde Sí o No.\n(Eso entrena mi base para la próxima vez.)"
        )

        nuevos_atributos = {}
        for atr in atributos:
            resp = messagebox.askyesno("Atributo", f"¿{nombre_nuevo} cumple '{atr}'?")
            nuevos_atributos[atr] = bool(resp)

        nuevo_personaje = {"nombre": nombre_nuevo, "atributos": nuevos_atributos}

        self.db["personajes_extra"].append(nuevo_personaje)
        guardar_conocimiento(self.db)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaQuienMarvel(root)
    root.mainloop()
