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

matrizT = tareas_a_matriz("tareas.txt")
print(matrizT)