import random
import csv 
import numpy as np 

from Funciones_examen import generar_sueldos, generar_reporte, clasificar_sueldos, ver_estadisticas
trabajadores = ["Juan perez", "maria ignacia","Carlos lopez", "Ana martinez",
                "pedro rodriguez", "laura hernandez", "miguel sanchez", "isabel gomez",
                   "francisco diaz", "elena fernandez"]
def main():
    sueldos = []
    
    while True:
        print("\n---- Menú Principal ----")
        print("1. asignar sueldos aleatorios")
        print("2. clasificar sueldos")
        print("3. ver estadísticas")
        print("4. reporte de sueldos")
        print("5. salir del programa")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            sueldos = generar_sueldos()
            print("sueldos aleatorios asignados.")
        elif opcion == '2':
            if not sueldos:
                print("primero debe seleccionar la opcion 1 para asignar sueldos de manera random.")
            else:
                print(" Aqui estan los sueldos clasificados")
                
                clasificar_sueldos(sueldos)
        elif opcion == '3':
            if not sueldos:
                print("primero debe seleccionar la opcion 1 para asignar sueldos de manera random.")
            else:
                print(" ↓ estadisticas ↓")
                ver_estadisticas(sueldos)
        elif opcion == '4':
            if not sueldos:
                print("primero debe seleccionar la opcion 1 para asignar sueldos de manera random.")
            else:
                print("↓ reporte ↓")
                generar_reporte(trabajadores, sueldos)
        elif opcion == '5' :
            break        