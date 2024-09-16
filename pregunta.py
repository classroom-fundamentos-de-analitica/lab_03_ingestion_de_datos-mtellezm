"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd

def ingest_data():
    with open("clusters_report.txt", "r") as file:

        #Diccionario de las columnas del dataframe
        data = {"cluster": [], 
                "cantidad_de_palabras_clave": [], 
                "porcentaje_de_palabras_clave": [], 
                "principales_palabras_clave": []
                }
        #Cada fila se limpia y cada elemento se separa en una fila
        for line in file.readlines()[4:]: 
            line = line.replace("\n", "")
            data_in_file = list(filter(lambda x: x != "", line.split(" ")))

            #Se va agregando la inforción de cada fila y se diferencia por el %
            if "%" in data_in_file:
                data["cluster"].append(int(data_in_file[0]))
                data["cantidad_de_palabras_clave"].append(int(data_in_file[1]))
                data["porcentaje_de_palabras_clave"].append(float(data_in_file[2].replace(",", ".")))
                data["principales_palabras_clave"].append(" ".join(data_in_file[4:]).replace(".", "").strip() + " ")
            elif data_in_file:
                data["principales_palabras_clave"][-1] += " ".join(data_in_file).replace(".", "").strip() + " "

        # Eliminar el espacio al final de cada cadena de palabras clave
        data["principales_palabras_clave"] = list(map(lambda x: x.strip(), data["principales_palabras_clave"]))

        df = pd.DataFrame(data)

    return df