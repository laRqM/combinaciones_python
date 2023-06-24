import itertools # IMPORTAMOS EL MÓDULO

# LA SIGUIENTE LISTA CONTIENE LOS DATOS QUE QUEREMOS COMBINAR. EN ESTE EJEMPLO, TENEMOS CUATRO VARIABLES. QUE GENERA 15 COMBINACIONES
datos = ['variable1', 'variable2', 'variable3', 'variable4']

combinaciones = [] # LISTA PARA ALMACENAR LAS COMBINACIONES GENERADAS

for r in range(1, len(datos) + 1): # CICLO for QUE ITERA DESDE 1 HASTA EL NÚMERO DE ELEMENTOS EN datos.
    combinaciones.extend(itertools.combinations(datos, r))
    # PARA CADA VALOR(LLAMADO r) EN EL CICLO for, UTILIZAMOS inertools.combinaciones PARA GENERAR TODAS LAS COMBINACIONES POSIBLES
    # CON LONGITUD r A PARTIR DE LOS ELEMENTOS EN datos
    # LAS COMBINACIONES SE AGREGAN A LA LISTA combinaciones USANDO extend

# DECLARAMOS LA VARIABLE Y LE DAMOS UN NOMBRE Y EXTENSIÓN AL ARCHIVO DE TEXTO
nombre_archivo = "combinaciones.txt"

with open(nombre_archivo, 'w') as archivo: # ABRIMOS EL ARCHIVO EN MODO ESCRITURA Y LO ASOCIAMOS A LA VARIABLE archivo
    numero_combinaciones = len(combinaciones)  # OBTENEMOS EL NÚMERO DE COMBINACIONES POSIBLES
    archivo.write("Número de combinaciones posibles: {}\n\n".format(numero_combinaciones)) # ESCRIBIMOS EL NÚMERO DE COMBINACIONES POSIBLES EN EL ARCHIVO DE TEXTO
    for combinacion in combinaciones: # ITERAMOS SOBRE CADA COMBINACIÓN EN LA LISTA combinaciones
        cadena_combinacion = ', '.join(combinacion) # CONVERTIMOS LA COMBINACIÓN A UNA CADENA Y LOS UNIMOS USANDO , COMO SEPARADOR
        archivo.write(cadena_combinacion + '\n') # ESCRIBIMOS LA COMBINACIÓN EN EL ARCHIVO DE TEXTO Y LE DAMOS UN SALTO DE LÍNEA

print("Número de combinaciones posibles:", numero_combinaciones)
print("Se han guardado las combinaciones en el archivo", nombre_archivo)