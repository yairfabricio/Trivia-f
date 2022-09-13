BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time
import random
puntaje = random.randint (0,10)

iniciar_trivia = True
intentos=0

print (GREEN+"Bienvenido a mi trivia sobre la Selección de fútbol de Perú")
print ("Pondremos a prueba tus conocimientos"+RESET)
print ("\nComenzaras con:", puntaje, "puntos")
nombre = input("Ingresa tu nombre: ")

while iniciar_trivia == True:
  intentos += 1
  puntaje = random.randint (0,10)
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  
  print(MAGENTA+"\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  time.sleep(5)
  print ("1) ¿Quién es el delantero titular de la selecciòn peruana?")
  print (BLUE+"a) Raúl Ruidíaz ")
  print ("b) Santiago Ormeño")
  print ("c) Gabriel Jesus")
  print ("d) Gianluca Lapadula"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")

  while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "a":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Raúl Ruidíaz no es el delantero titular de la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_1 == "b":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Santiago Ormeño no es el delatero titular de la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_1 == "c":
      puntaje +=random.randint(-4,-1)
      print ("Incorrecto!", nombre, "Gabriel Jesus no es el delatero titular de la selecciòn")
      print ("Tu puntaje actual es", puntaje)
  else:
   puntaje += random.randint(5,10)
   print ("Muy bien", nombre, "!")
   print ("Tu puntaje actual es", puntaje)

 # Pregunta 2
  print ("\n2) ¿Cual es el estadio de la Selección de fútbol de Perú?")      
  print (RED+"a) Estadio Santiago Bernabeu")
  print ("b) Estadio Nacional del Perú")
  print ("c) Camp Nou")
  print ("d) Estadio Garcilaso de la Vega"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_2 = input("\nTu respuesta: ")

  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_2 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("Tu puntaje actual es", puntaje)
  elif respuesta_2 == "d":
    print ("Cerca")
    puntaje = puntaje + 1
    print("Tu puntaje actual es", puntaje)
  elif respuesta_2 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("Tu puntaje actual es", puntaje)
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("Tu puntaje actual es", puntaje)
#Pregunta 3
  print ("\n3) ¿En qué año asumió Ricardo Gareca como seleccionador nacional?")      
  print (RED+"a) 2020")
  print ("b) 2015")
  print ("c) 2017")
  print ("d) 2016"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ")

  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("Tu puntaje actual es", puntaje)
  elif respuesta_3 == "d":
    print ("Cerca")
    
    puntaje = puntaje + 1
    print("Tu puntaje actual es", puntaje)
  elif respuesta_3 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("Tu puntaje actual es", puntaje)
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("Tu puntaje actual es", puntaje)
#PREGUNTA 4
  print ("\n4) ¿En que posición termino la selecciòn peruana en las eliminatorias Qatar 2022?")
  print (BLUE+"a) Quinto ")
  print ("b) Sexto")
  print ("c) Octavo")
  print ("d) Tercero"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_4 = input("\nTu respuesta: ")

  while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_4 == "b":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "no termino sexto")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_4 == "d":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "no termino tercero")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_4 == "c":
      puntaje +=random.randint(-4,-1)
      print ("Incorrecto!", nombre, "no termino octavo")
      print ("Tu puntaje actual es", puntaje)
  else:
   puntaje += random.randint(5,10)
   print ("Muy bien", nombre, "!")
   print ("Tu puntaje actual es", puntaje)

 # Pregunta 5
  print (RED+"\n5) ¿Quien fue el goleador de las eliminatorias Qatar 2022 de la Selección de fútbol de Perú?"+RESET)      
  print ("a) Cristian Ramos")
  print ("b) Andre Carrillo")
  print ("c) Christian Cueva")
  print ("d) Paolo Guerrero")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_5 = input("\nTu respuesta: ")

  while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_5 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("Tu puntaje actual es", puntaje)
  elif respuesta_5 == "b":
    print ("Cerca")
    puntaje = puntaje + 1
    print("Tu puntaje actual es", puntaje)
  elif respuesta_5 == "d":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("Tu puntaje actual es", puntaje)
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("Tu puntaje actual es", puntaje)
  # Pregunta 6
  print ("\n6) ¿Quién es el nuevo director tecnico de la selecciòn peruana?")
  print (BLUE+"a) Pep Guardiola ")
  print ("b) Jurgen Klopp")
  print ("c) Juan Máximo Reynoso")
  print ("d) Antonio Conte"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_6 = input("\nTu respuesta: ")

  while respuesta_6 not in ("a", "b", "c", "d"):
        respuesta_6 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_6 == "a":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Pep Guardiola no es el nuevo director tecnico de la selecciòn peruana")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_6 == "b":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Jurgen Klopp no es el nuevo director tecnico de la selecciòn peruana")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_6 == "d":
      puntaje +=random.randint(-4,-1)
      print ("Incorrecto!", nombre, "Antonio Conte no es el nuevo director tecnico de la selecciòn peruana")
      print ("Tu puntaje actual es", puntaje)
  else:
   puntaje += random.randint(5,10)
   print ("Muy bien", nombre, "!")
   print ("Tu puntaje actual es", puntaje)

 # Pregunta 7
  print (RED+"\n7) ¿Quien es el maximo goleador de la Selección de fútbol de Perú?"+RESET)      
  print ("a) Jefferson Farfán")
  print ("b) Arturo Vidal")
  print ("c) Paolo Guerrero")
  print ("d) Juan Manuel Vargas")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_7 = input("\nTu respuesta: ")

  while respuesta_7 not in ("a", "b", "c", "d"):
    respuesta_7 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_7 == "b":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("Tu puntaje actual es", puntaje)
  elif respuesta_7 == "a":
    print ("Cerca")
    puntaje = puntaje + 1
    print("Tu puntaje actual es", puntaje)
  elif respuesta_7 == "d":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("Tu puntaje actual es", puntaje)
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("Tu puntaje actual es", puntaje)
    # Pregunta 8
  print ("\n8) ¿Contra quien jugo el partido de repechaje para la clasificacion al mundial de futbol Qatar 2022 la selecciòn peruana?")
  print (BLUE+"a) Taiwan ")
  print ("b) Paises bajos")
  print ("c) Nueva Zelanda")
  print ("d) Australia"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_8 = input("\nTu respuesta: ")

  while respuesta_8 not in ("a", "b", "c", "d"):
        respuesta_8 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_8 == "a":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Taiwan no jugo contra la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_8 == "b":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Paises bajos no jugo en contra  de la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_8 == "c":
      puntaje +=random.randint(-4,-1)
      print ("Incorrecto!", nombre, "Nueva zelanda no jugo en contra  de la selecciòn")
      print ("Tu puntaje actual es", puntaje)
  else:
   puntaje += random.randint(5,10)
   print ("Muy bien", nombre, "!")
   print ("Tu puntaje actual es", puntaje)

 # Pregunta 9
  print (RED+"\n9) ¿Contra quien fue el ultimo triunfo de la Selección de fútbol de Perú en un Mundial?"+RESET)      
  print ("a) Brazil")
  print ("b) Australia")
  print ("c) Francia")
  print ("d) dinamarca")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_9 = input("\nTu respuesta: ")

  while respuesta_9 not in ("a", "b", "c", "d"):
    respuesta_9 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_9 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
    print("Tu puntaje actual es", puntaje)
  elif respuesta_9 == "d":
    print ("Cerca")
    puntaje = puntaje + 1
    print("Tu puntaje actual es", puntaje)
  elif respuesta_9 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
    print("Tu puntaje actual es", puntaje)
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
    print("Tu puntaje actual es", puntaje)
  # Pregunta 10
  print ("\n10) ¿Quién es el arquero titular de la selecciòn peruana?")
  print (BLUE+"a) Diego Penny ")
  print ("b) Oscar Ivañez")
  print ("c) Raul Fernandez")
  print ("d) Pedro Gallese"+RESET)

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_10 = input("\nTu respuesta: ")

  while respuesta_10 not in ("a", "b", "c", "d","w"):
        respuesta_10 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

  if respuesta_10 == "a":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Diego Penny no es el arquero titular de la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_10 == "b":
     puntaje +=random.randint(-4,-1)
     print ("Incorrecto!", nombre, "Oscar Ivañez no es el arquero titular de la selecciòn")
     print("Tu puntaje actual es", puntaje)
  elif respuesta_10 == "c":
      puntaje +=random.randint(-4,-1)
      print ("Incorrecto!", nombre, "Raul Fernandez no es el arquero titular de la selecciòn")
      print ("Tu puntaje actual es", puntaje)
  elif respuesta_10 == "w":
      print("MENSAJE SECRETO")
      puntaje += 2999
      print (nombre, "Descurbiste el mesaje secreto")
      print("Tu puntaje actual es", puntaje)
  else:
   puntaje += random.randint(5,10)
   print ("Muy bien", nombre, "!")
   print ("Tu puntaje actual es", puntaje)
  lista1 =["1) ¿Quién es el delantero titular de la selecciòn peruana?","2) ¿Cual es el estadio de la Selección de fútbol de Perú?","3) ¿En qué año asumió Ricardo Gareca como seleccionador nacional?","4) ¿En que posición termino la selecciòn peruana en las eliminatorias Qatar 2022?","5) ¿Quien fue el goleador de las eliminatorias Qatar 2022 de la Selección de fútbol de Perú?","6) ¿Quién es el nuevo director tecnico de la selecciòn peruana?","7) ¿Quien es el maximo goleador de la Selección de fútbol de Perú?","8) ¿Contra quien jugo el partido de repechaje para la clasificacion al mundial de futbol Qatar 2022 la selecciòn peruana?","9) ¿Contra quien fue el ultimo triunfo de la Selección de fútbol de Perú en un Mundial?","10) ¿Quién es el arquero titular de la selecciòn peruana?"]
  print("\n imprimiendo todas tus respuestas para obtener tu puntaje final","10) ¿Quién es el arquero titular de la selecciòn peruana?","a")
  lista2= [respuesta_1,respuesta_2,respuesta_3,respuesta_4,respuesta_5,respuesta_6,respuesta_7,respuesta_8,respuesta_9,respuesta_10,]
  for number in range(0,10):
   print ("la pregunta es", lista1[number],"la respuesta que marcaste es",lista2[number])
  input ("enter para continuar")
  
  print (RED+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
  time.sleep(3)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero" ,nombre, "que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False 