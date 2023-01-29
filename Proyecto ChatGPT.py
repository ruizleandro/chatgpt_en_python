# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 20:48:25 2023

@author: lmruiz
"""

#%% instalacion e importacion
!pip install pyChatGPT
import pyChatGPT

#%% autenticacion
# session token
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..IsqKOFU8Qt85sMYk.Ek65r4UavJsbnHQCEppUOPJW7DCg6ox8I4Z7CUFmImLbahfvTQkMD8t03UBQMjZVeGY8r9cr-aVAwh_1TR8qB2Shg9ugrGDFmR6P-lQ7L2zQ4eNiWnGEiBYA0_A0G5EySmzBRzycUE8-10eURrxcc5Bby7hApNJ4vYsIhkdTKk9VD_eL1lqm5f2O51XD1KrziCUA1uQ2axIYC9hHcZqi9hM18mdUixonuWUVaiDTHCgXB7BTGPIUBi-WA9Frz4z-WzLOF3i_-Co23rJ_pxvUTv1-D8GpweuhdkXOBzEPnoKFbXU3Zb2Sy4tF0zrpxOwqVXj00TL_s7AhFM0GYXDDuMT8Se9TN7OrrWoSj-MUlqDRBF2X3o7KChJ1CiyeTsXzVZESnixisya3pEB1vkkVnHG0wnGF81Uy_xDZRBv_Q9OmY9PcUJpetPWiSU6iyjDbIIEY5JX1164dXt9njp_vzxpJfdOSnnDR_l2ytMdlrM6QPLhX_5nu1kziBs9-3_dXb0yBSgu4kVZyGEjPBgrI6o_4vazHEsEXj_9d1BLDRsQZADAyMGv-yi8muRRJEmondk4LOMaQWuJL8urm_0ceQH8B084e_QR9IuGHaORbZbgi-M0TE0cFER2csaQMV3yTpRoLTNt7QiItsvdcVpwCuphOGOf81K5Hwwi2XtIkWsBmJxiexLobz_uYijf143iadf4O8VRkSBNqFj_XHW1sioN60I2JkQSTiyp2eDt4-rlgKaOec9mxKdQ0ze_S2-oNSYfYU4BlcN1TujQv-y4DBLdhxBIDNWxUynkJLvfd5XYtNif_mNnXSFwTectVHxQsRLEKX8hnEOywXW6fRkG5Yu_U7bzK5yZ56jG1EZ40r64wg2uf76LDmB2DMj9ynofGhJEhqH3eMQ0oO0TAbwIueyeUSMxz_GTUHQx4gTfTmhT_CRZekMC8q1pZRz1K0DrRgNDtAPmHi2Qy8o9rPIKMaNIMQeW9s2Uq_nW57_kkxfXhtZLxabILQ_zZZ0Jy7Oj8KMWl_1CJSCzyIVDE9vkeXgqMMzq3sQxSagNVgRn1UNwHTgQj5Je9T9KOcjCL5_aDk3umUYIzQb5ovk5X0pUcG_WYavX6yXNcBQcyBjUZ9c27ZPnceo0DuFFBbwB0rFcwms0xbn2qbM77fAe57V7XrgXyYpAyqJlpT5Tp7j1SVsc_B1aPBswG00-2sqUPDimif81W4iVTLcCn_5jrt6UfHOQJTl5NTsrPryZDPhMUH3fP1HY3fBxhpxFiHjk9UBeoTEu-fuO5jjjgWzAI2Pvi2vsKDM4rzoYw6dvB-Z3oA5wt1JLveuWlSlZtTQhnpT-Ozdr1BDPmVU2CE7rumjF4NbUPCW2uhlnMM-BbxmafIdKhmCfZzWDz09xzuws5Jx_hnagmGA7nuSWGklY2VWYe31rrOFwVBwGDapEV2MGS5oViXjMTmTJMVz0SnUe3xfWCNuXIptJPmhzddOHmSwSeYh8XAnvp8rsUtZgB4cZsuYGHUuH9aOtUQRVHIz7-oesOQLbzj78yhykM_0NQRM4hJa5WcdzoVKks3JnDIYtt4gphZXlXMsqqWhestz0P-6KS2b4DS4pOWLj0cfq3dhxT2alqGF6gjBNRe1zd7M1KztZgcKrB9TQ2sbsi7yN7OFHGcW8dGpY8klgEISQoOvfJxwJl1fQFvmBQaHKFU41-4m_I9LCxdR_kQd0Vn0tKw5fnACZw7QT3VH8k43gIM7LgxCU76eeTTO7YYZbC6QGIzUqj0VJcqhqooHPVducfedyIpHCLwanRrtyXlBnmyqTe7klw17IkAAuP43KibHmZ4ABRWs3dVFZribxWLlqmZKE5Sgh4GBmEhOkU7CWcYrG36rQwA4GM6Mk8Jrxgtx3JZalGbm5Log4oyiUD_aO7NRq6pe4nhhYeklLIpq9yPDVECb-2HwL56imJPLfB2VEMZygLrmK7w5pk7rze6oP_2vuo_hF9LtqDzC8Pps1c-YS4bofVd2clKrPHDKMUV54uaxnjKXnAVhQcjqnO9Z4HoLOYpPRQKUO3nXMwmWGIbOy8U-EtuTUxxMgb0AG2XJ3BleHS7fDzPR8WjHlKWgRbo3F8vPJjn0YcUvdUO-uNyHZrg-yKqD6WEzpqO7qpnsMK2sn914eGzaSqcGzimsYt5mxwC-demQ8Vup4lv0Q3YTnt_J1ESsISyLyIlk1ECAqpM0RV8c8alZCj5g_Vg4NEug0xaeWqjS_bIly3BEQ-v4fKgaQRFXnJjv-VXnFKybL4hgzFKfl4qmmICo1xBz2K8iidtTMev7Ilb2kYwwjQ4t5gIaH-pheNHOf5Oh4XKUsXN8yqo2oBiPxBZy8RxdqxiUbvpz81gcyRdlljq83dk8XivdhnXNSdwNVF9Wg_DJXoDCL-X3LZg7ExZ88Z6VmnuzkJMKIvdSg2zKRfSq56sMLiLuTuQg9HyxBA_i9zZJBkxhinnox2iRfZW5gkwT2_fyjTGh-sUHNUstTrI7YICXglsYJdSSwAuN9EjMpXb4w.UOCkogYKB7rXnaLEuvEAlA"

session_api = pyChatGPT.ChatGPT(session_token=session_token)

#%% crear tabla para guardar preguntas y respuestas
# columnas: ID, Pregunta, Respuesta, Fecha y hora, Etiquetas
# crear una lista para cada columna
_preguntas = []
_respuestas = []
_fechaHora = []
_etiqueta = []

#%% interaccion con chatgpt
import time

run = True
while run:
    # ingresar mensaje
    print("¡Hola! Ingrese su consulta: ")
    pregunta = input()

    # haciendo request
    respuesta = session_api.send_message(pregunta)

    # formatear respuesta
    respuesta = "".join(respuesta.get("message"))
    respuesta = respuesta.replace("\n", "")
    # imprimir respuesta
    print()
    print(respuesta)
    ahora = time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S")
    print("Fecha y hora: " + ahora)
    
    # preguntar si el usuario quiere guardar la pregunta y respuesta
    guardarPregunta = input("¿Desea guardar esta respuesta?: ")
    if guardarPregunta.lower() == "si":
        # guardar pregunta y respuesta
        _preguntas += [pregunta]
        _respuestas += [respuesta]
        # guardar hora de ejecucion
        _fechaHora += [ahora]
        # agregar etiquetas
        agregarEtiqueta = input("¿Desea agregar alguna etiqueta? ")
        if agregarEtiqueta.lower() == "si":
            nuevaEtiqueta = input("Escriba el nombre de la etiqueta (puede agregar varias separandolas con una coma): ")
            _etiqueta += [nuevaEtiqueta]
        else:
            _etiqueta += [""]

    # preguntar si el usuario continua
    run = bool(input("¿Desea continuar? "))
    print()

print("¡Hasta luego!")

# guardar datos en un archivo local
import pandas as pd

historial = {"Pregunta": _preguntas, 
             "Respuesta": _respuestas,
             "Fecha y hora": _fechaHora,
             "Etiquetas": _etiqueta}

# crear pandas dataframe con las listas
df_historial = pd.DataFrame(historial)

df_historial

#%% exportar a un archivo xlsx

import pandas as pd
import os
from pathlib import Path

# el nombre que tiene el archivo final
nombre_archivo = "Historial chatGPT.xlsx"

# obtener carpeta del proyecto
project_root = os.path.dirname(os.path.dirname(__file__))
carpeta_proyecto = os.path.join(project_root, 'Proyecto ChatGPT')
                     
direccion_archivo = Path(os.path.join(carpeta_proyecto), nombre_archivo)

# a partir de acá el código fue generado por chatgpt

try:
    # verifica si existe "HistorialChatGPT.xlsx" en la carpeta del proyecto
    if os.path.exists(direccion_archivo):
        # lee el archivo existe
        archivo_existente = pd.read_excel(direccion_archivo)
        # anexa la nueva info en el excel
        actualizar_archivo = pd.concat([archivo_existente, df_historial], ignore_index=True)
        # sobreescribe el archivo con la nueva info
        actualizar_archivo.to_excel(direccion_archivo, index=False)
        print("Se actualizó el archivo correctamente.")
    # si no existe lo crea con los datos que guardó
    else:
        df_historial.to_excel(direccion_archivo, index=False)
        print("Se creó el archivo exitosamente.")
# excepción por si el archivo existe y está abierto
except PermissionError:
    print("Por favor cierre el archivo antes de efectuar los cambios.")

# =============================================================================
# # este codigo sirve para saber de la existencia de un archivo
# if os.path.exists(file_path):
#     print("The file is saved at:", os.path.abspath(file_path))
# else:
#     print("The file does not exist.")
# =============================================================================

