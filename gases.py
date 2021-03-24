def datos():
  print("*** Gases Ideales ***")
  print("     P V=n R T")
  print("     1 2 3   4")
  opcion = input("Seleccionar variable a calcularse: ")
  opcion = int (opcion)
  if opcion > 4 or opcion < 1:
    print("Opcion invalida!")
    return -1, 0, 0, 0
  if not (opcion == 1):
    presion = float(input("Ingresar presion en atmosferas:"))
  else:
    presion = 0
  if not (opcion == 2):
    volumen = float(input("Ingresar volumen en litros: "))
  else:
    volumen = 0
  if not (opcion == 3):
    moles = float(input("Ingresar cantidad de materia enmoles: "))
  else:
    moles = 0
  if not (opcion == 4):
    temperatura = float(input("Ingresar temperatura enKelvin: "))
  else:
    temperatura = 0
  return opcion, presion, volumen, moles, temperatura

def calcular(opc, P, V, n, T):
  R = 0.0821
  if opc == 1:
     return "La presion es: " + str(n * R * T / V)
  elif opc == 2:
     return "El volumen es: " + str(n * R * T / P)
  elif opc == 3:
     return "Los moles son: " + str(P * V / (R * T))
  elif opc == 4:
     return "La temperatura es: " + str(P * V / (R * n))
  else:
     return "Opcion mal ingresada."

