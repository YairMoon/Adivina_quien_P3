# Adivina Quién - Versión Marvel
import random

# =============================
# Base de personajes MARVEL
# =============================

personajes = [
    {"nombre": "Iron Man", "atributos": {"armadura": True, "poderes": False, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Captain America", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Thor", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "dios": True,"humano": True, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Hulk", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Black Widow", "atributos": {"armadura": False, "poderes": False, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Spider-Man", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Doctor Strange", "atributos": { "magia": True, "armadura": False, "poderes": True, "vengador": True, "villano": False, "humano": True, "usa_arma": False, "dios": False, "alien": False, "robot": False, "mutante": False }},
    {"nombre": "Thanos", "atributos": {"armadura": True, "poderes": False, "vengador": False, "villano": True, "usa_arma": True, "alien": True,"humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Loki", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": True, "dios": True,"humano": True, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Ultron", "atributos": {"armadura": True, "poderes": False, "vengador": False, "villano": True, "usa_arma": True, "robot": True,"humano": False, "dios": False, "magia": False, "alien": False, "mutante": False}},
    {"nombre": "Black Panther", "atributos": {"armadura": True, "poderes": True, "vengador": True, "villano": False, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Deadpool", "atributos": { "mutante": True, "armadura": False, "poderes": True, "vengador": False, "villano": False, "usa_arma": True, "humano": False, "dios": False, "magia": False, "alien": False, "robot": False }},
    {"nombre": "Magneto", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": False, "mutante": True,"humano": False, "dios": False, "magia": False, "alien": False, "robot": False}},
    {"nombre": "Venom", "atributos": {"armadura": False, "poderes": True, "vengador": False, "villano": True, "usa_arma": False, "alien": True, "humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Wolverine", "atributos": { "mutante": True, "armadura": False, "poderes": True, "vengador": False, "villano": False, "usa_arma": True, "humano": False, "dios": False, "magia": False, "alien": False, "robot": False }},
    {"nombre": "Scarlet Witch", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "magia": True, "humano": True, "dios": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Ant-Man", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Green Goblin", "atributos": {"armadura": True, "poderes": True, "vengador": False, "villano": True, "usa_arma": True, "humano": True, "dios": False, "magia": False, "alien": False, "robot": False, "mutante": False}},
    {"nombre": "Gamora", "atributos": {"armadura": False, "poderes": False, "vengador": False, "villano": False, "usa_arma": True, "alien": True,"humano": False, "dios": False, "magia": False, "robot": False, "mutante": False}},
    {"nombre": "Vision", "atributos": {"armadura": False, "poderes": True, "vengador": True, "villano": False, "usa_arma": False, "robot": False,"humano": False, "dios": False, "magia": False, "alien": False, "mutante": False}},
]

atributos = list(personajes[0]["atributos"].keys())


# =============================
# Motor de inferencia básico
# =============================

def aplicar_regla(lista_actual, atributo, respuesta):
    """
    Encadenamiento hacia adelante:
    elimina personajes que no cumplan el atributo según la respuesta.
    """
    nueva_lista = []
    for p in lista_actual:
        valor = p["atributos"].get(atributo, None)
        if valor is None:
            continue  # ignora personajes que no tienen ese atributo
        if valor == respuesta:
            nueva_lista.append(p)
    return nueva_lista


def seleccionar_mejor_pregunta(candidatos, usados):
    """
    Selecciona un atributo que aún no se haya preguntado y
    que divida mejor el conjunto de personajes (para hacer el juego más eficiente).
    """
    mejor = None
    diferencia_minima = len(candidatos)
    for atributo in atributos:
        if atributo in usados:
            continue
        valores = [c["atributos"].get(atributo, None) for c in candidatos]
        positivos = sum(1 for v in valores if v is True)
        negativos = sum(1 for v in valores if v is False)
        if positivos + negativos == 0:
            continue  # ignora atributos que nadie tiene
        diferencia = abs(positivos - negativos)
        if diferencia < diferencia_minima:
            diferencia_minima = diferencia
            mejor = atributo
    return mejor

# =============================
# Juego principal
# =============================

def jugar():
    print("====================================")
    print("       Adivina Quién - Marvel       ")
    print("====================================")
    print("Piensa en un personaje del universo Marvel (héroe o villano).")
    print("Responde las preguntas con 's' (sí) o 'n' (no).")
    input("\nPresiona ENTER cuando estés listo...")

    posibles = personajes.copy()
    preguntas_hechas = []

    while len(posibles) > 1:
        atributo = seleccionar_mejor_pregunta(posibles, preguntas_hechas)
        if atributo is None:
            break

        preguntas_hechas.append(atributo)
        respuesta = input(f"\n¿Tu personaje tiene la característica '{atributo}'? (s/n): ").strip().lower()

        if respuesta in ("s", "si", "sí"):
            posibles = aplicar_regla(posibles, atributo, True)
        elif respuesta in ("n", "no"):
            posibles = aplicar_regla(posibles, atributo, False)
        else:
            print("Respuesta no válida, intenta de nuevo.")
            continue

        print(f"→ Personajes restantes: {len(posibles)}")

        if len(posibles) <= 3:
            print("\nCandidatos posibles:", [p["nombre"] for p in posibles])

    if len(posibles) == 1:
        print(f"\n Creo que tu personaje es: **{posibles[0]['nombre']}** ✨")
    elif len(posibles) > 1:
        print("\nHmm... tengo algunas dudas, tal vez sea uno de estos:")
        for p in posibles:
            print("-", p["nombre"])
    else:
        print("\nNo logré adivinar... ¡mejor suerte la próxima vez!")

    print("\nFin de la partida.")

# =============================
# Ejecución del juego
# =============================

if __name__ == "__main__":
    jugar()
