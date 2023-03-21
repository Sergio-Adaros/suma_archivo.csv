from pathlib import Path 

# Definiendo la ruta donde se encuentra el archivo a analizar.
current_path = Path.cwd()
current_path = current_path / 'Revenue Log for PJ-1108A337-02.csv'

# Abriendo el archivo.
with open(current_path) as file: 
    datos_ion = file.readlines() 

# Organizando los datos en un arreglo
arreglo = []

for linea in datos_ion:  
    line_in_list = linea.split(',')
    arreglo.append(line_in_list)

# Consultando por pantalla los datos requeridos por el usuario.
date_intro = str(input(("Ingrese fecha a calcular: ")))
dato_a_consultar = str.lower((input("Ingrese dato a consultar: ")))

# Definiendo el dato solicitado por usuario.
nombre_columnas = arreglo.pop(0)

for num, var in enumerate(nombre_columnas):
    if var.lower() == dato_a_consultar: 
        columna = num 

# Organizando en una lista los datos requeridos por el usuario según fecha
line = 0
lista_datos = []

for datos in arreglo:
    date = datos[line]
    date = date[0:10]
    if date == date_intro:
        lista_datos.append(float(datos[columna]))

# Imprimiendo la suma total por dia.
print(sum(lista_datos))