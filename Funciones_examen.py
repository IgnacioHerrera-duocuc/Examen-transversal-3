import random
import csv



trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]


def generar_sueldos():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos


def clasificar_sueldos(sueldos):
    menor_800000 = []
    entre_800000_2000000 = []
    mayor_2000000 = []

    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        sueldo = sueldos[i]

        if sueldo < 800000:
            menor_800000.append((nombre, sueldo))
        elif sueldo <= 2000000:
            entre_800000_2000000.append((nombre, sueldo))
        else:
            mayor_2000000.append((nombre, sueldo))
    
    print("sueldos menores a $800.000 TOTAL:", len(menor_800000))
    for nombre, sueldo in menor_800000:
        print(f"{nombre}: ${sueldo}")
    
    print("\nsueldos entre $800.000 y $2.000.000 TOTAL:", len(entre_800000_2000000))
    for nombre, sueldo in entre_800000_2000000:
        print(f"{nombre}: ${sueldo}")
    
    print("\nsueldos superiores a $2.000.000 TOTAL:", len(mayor_2000000))
    for nombre, sueldo in mayor_2000000:
        print(f"{nombre}: ${sueldo}")
    
    total_sueldos = sum(sueldos)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")


def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    
    
    producto_sueldos = 1
    for sueldo in sueldos:
        producto_sueldos *= sueldo
    
    media_geometrica = producto_sueldos ** (1 / len(sueldos))
    
    print(f"mayor sueldo: ${sueldo_max}")
    print(f"menor sueldo: ${sueldo_min}")
    print(f"promedio de sueldos: ${promedio:.2f}")
    print(f"media geométrica: ${media_geometrica:.2f}")


def generar_reporte(trabajadores, sueldos):
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for i in range(len(trabajadores)):
            nombre = trabajadores[i]
            sueldo_base = sueldos[i]
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            
           
            writer.writerow([nombre, sueldo_base, desc_salud, desc_afp, sueldo_liquido])
            
          
            print(f"{nombre}: ${sueldo_base} - Salud: ${desc_salud:.2f} - AFP: ${desc_afp:.2f} - Líquido: ${sueldo_liquido:.2f}")
    
    print("\nReporte generado en 'reporte_sueldos.csv'.")


