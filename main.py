def requerimientos_a_matriz():
    pass


def tareas_a_matriz(ruta_archivo):
    matriz = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            
            if len(datos) == 3:
                fila = [datos[0], int(datos[1]), datos[2]]
                matriz.append(fila)
                
    return matriz

def recursos_a_matriz(ruta_archivo):
    matriz = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            
            if len(datos) == 2:
                fila = [datos[0], datos[1]]
                matriz.append(fila)
                
    return matriz

def compatibilidad(tarea, recurso):
    cat_tarea = tarea[2]
    cat_recurso = recurso[1]
    return cat_tarea in cat_recurso

matrizT = tareas_a_matriz("tareas.txt")
print(matrizT)

matrizR = recursos_a_matriz("recursos.txt")
print(matrizR)

for i in range(len(matrizT)):
    for j in range(len(matrizR)):
        if compatibilidad(matrizT[i], matrizR[j]):
            print(f"El Recurso {matrizR[j][0]} puede hacer la Tarea {matrizT[i][0]}")