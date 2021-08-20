
# resolucion GUIA Nº1
# 01/08/2021
# Imprimir "Hello world!
ejercicio = int((input)('Elegi el numero de ejercicio (1 al 23)  '))
if ejercicio == 1:
    print('¡Hello world!')
if ejercicio == 2:
    msj = 'hola mundo'
    print(msj)
if ejercicio == 3:
    print('Por favor, a continuacion, escribe tu nombre')
    minombre = input()
    print('A continuacion escribe tu edad')
    edad = input()
    print(minombre, '\n', edad)
if ejercicio == 4:
    nombre = input('ingrese su nombre')
    numero = int(input(''))
    print((f'{nombre}\n' + numero))
if ejercicio == 5:
    cont = 0
    for letra in nombre:
        cont += 1
    print(f'{nombre} tiene {cont} letras')
if ejercicio == 6:
    resultado = ((3+2) / 2*5) ** 2
    print(f'El resultado es {resultado}')
if ejercicio == 7:
    numero_1 = int(input('ingrese un numero:'))
    numero_2 = int(input('Ingrese otro numero'))
    cociente, resto = numero_1 // numero_2, numero_1 % numero_2
    print(
        f'La division entre {numero_1} y {numero_2} da un cociente {cociente} y un resto {resto}')
if ejercicio == 8:
    capital = float(input('¿Cuanto dinero vas invertir?  '))
    interes = float(input('¿Cual es el interes anual ofrecido?  '))
    anios = int(
        input('¿Durante cuantos años vas a tener invertido el dinero?  '))
    if interes >= 1:
        interes /= 100
        capital_obtenido = capital + capital + interes + anios
    print(f'El capital obtenido es {capital}')
if ejercicio == 9:
    peso_payaso = 112  # gr
    peso_muñeca = 75  # gr
    payasos = int(input('Cantidad de payasos a enviar:  '))
    muñecas = int(input('Cantidad de muñecas a enviar:  '))
    # peso_total /= 1000
    # if peso_payaso >= 1000: para pasarlo a Kgs
    #   payaso /= 1000
    peso_total = peso_payaso * payasos + peso_muñeca * muñecas
    print(f'El peso total del paquete a enviar es {peso_total}')
if ejercicio == 10:
    if 0 <= edad < 18:
        print('Es mayor de edad')
    elif edad >= 18:
        print('es mayor de edad')
    else:
        print('no ingreso una edad correcta')
if ejercicio == 11:
    basic = 'contraseña'  # almacenar en variable
    password = input('Introduce la contraseña:  ')
    if basic == password.lower():  # lower: convierte todos los caracteres de mayusculas a minusculas. luna=LUNA
        print('La contaseña coincide')
    else:
        print('La contraseña no coincide')
if ejercicio == 12:
    numero = float(input('Dividendo:  '))
numero_dos = float(input('Divisor:  '))
if numero_dos == 0:
    print('Prueba de nuevo. No se puede dividir por 0')
else:
    print(numero/numero_dos)
if ejercicio == 13:
    numero = int(input('Escribe un numero entero:  '))
if numero % 2 == 0:
    print('El numero  ' + str(numero) + ' es par ')
else:
    print('el numero  ' + str(numero) + ' es impar')
if ejercicio == 14:
    bonificacion = 100000  # datos
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input('Escribe tu puntuación:  '))

if puntos == inaceptable:  # Clasifiación por niveles de rendimiento
    nivel = 'Inaceptable'
elif puntos == aceptable:
    nivel = 'Aceptable'
elif puntos >= 0.6:
    nivel = 'Meritorio'
else:
    print('No ingreso la puntacion correcta')

print('Tu nivel de rendimiento es %s' % nivel)
print('Te corresponde cobrar %.2f' % (puntos * bonificacion))
if ejercicio == 15:

    anios = int(input('Ingrese edad:  '))
    if anios <= 4:
       precio = 0
    print('Puedes pasar GRATIS')

   elif anios <= 18:
     precio = 500
   print('Debes abonar: $', precio)

  elif anios >= 18:
      precio = 1000
  print('Debes abonar: $', precio)

else:
    print('No ingreso una edad correcta')
if ejercicio == 16:
    anios = int(input('Ingrese su edad:  '))
for i in range(anios):
    print('Cumpliste  ', (i+1),  ' años ')
if ejercicio == 17:
    tabla_desde = 1  # arranca en la tabla del uno
tabla_hasta = 10  # recorre las tablas hasta la del diez
desde = 1  # empieza multiplicar desde el uno
hasta = 10  # llega a multiplicar hasta el 10

for F1 in range(tabla_desde, tabla_hasta + 1):  # toma el primer y segundo dato
    print('---------------')
    for F2 in range(desde, hasta + 1):  # toma el segundo dato
        print(f'{F1} x {F2} = {F1 * F2}')  # multiplica e imprime por consola
        print()
if ejercicio == 18:
    palabra = input('Escribe una palabra:  ')
# len calcula el numero de caracteres, en este caso desde el input. -1 indica posicion
for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])
if ejercicio == 19:
    frase = input('Escribe una palabra o frase:  ')
letra = i = input('Ahora, escoge una letra de tu frase:  ')
contador = 0
for i in frase.lower:
    if i == letra:
        contador += 1

print('La letra que escogiste  ',  letra,
      ' aparece  ' + str(contador) + ' vez/veces')
if ejercicio == 20:
    rta = input('ingrese una palabra')
    while rta != 'salir':
        print('rta')
    rta = input('ingrese una palabra o escriba 'salir' para fializar: ').lower()
if ejercicio == 21:
    materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    while True:
        rta = input('desea agregar materias a la lsita? responder si o no: ')
    if rta == 'n':
     break
    elif rta == 's':
        materia = input('ingrese una materia')
        materias.append(materia)
    else:
        print('no ingreso rta corrrecta')

    if materias:
        for asigantura in materias:
            print(f' yo estudio {asignatura}')
if ejercicio == 22:
    print('TENEMOS: Banana, Manzana, Pera, Naranja ')
frutas = {'Banana': 80, 'Manzana': 100, 'Pera': 120, 'Naranja': 150}
fruta = input('¿Qué fruta quieres? ').capitalize()

if fruta in frutas:
    # que pasa si es medio?
    kg = float(input('¿Cuántos kilos vas a llevar?  '))
    print(kg, 'kilos de ', fruta, ' cuestan  ', '$', frutas[fruta]*kg)
else:
    print('Lo siento,', fruta, ' no tenemos')
if ejercicio == 23:
    curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)
