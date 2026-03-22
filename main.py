
from dataclasses import dataclass
from typing import List

@dataclass
class Tarea:
    id_tarea: str
    duracion: int
    categoria: str

@dataclass
class Recurso:
    id_recurso: str
    categorias_soportadas: List[str]

def leer_tareas(ruta: str = "tareas.txt") -> List[Tarea]:
    tareas = []
    with open(ruta, "r") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) >= 3:
                tareas.append(Tarea(partes[0], int(partes[1]), partes[2]))
    return tareas

def leer_recursos(ruta: str = "recursos.txt") -> List[Recurso]:
    recursos = []
    with open(ruta, "r") as f:
        for linea in f:
            partes = [p.strip() for p in linea.strip().split(",")]
            if len(partes) >= 2:
                id_rec = partes[0]
                cats = partes[1:]
                recursos.append(Recurso(id_rec, cats))
    return recursos

mis_tareas = leer_tareas("tareas_2.txt")
mis_recursos = leer_recursos("recursos_2.txt")

for t in mis_tareas:
    print(f"ID: {t.id_tarea} | Duración: {t.duracion} | Cat: {t.categoria}")

for r in mis_recursos:
    print(f"ID: {r.id_recurso} | Categorías soportadas: {r.categorias_soportadas}")