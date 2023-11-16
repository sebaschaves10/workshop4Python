import random
import os

victoriaHumano = 0
victoriaMaquina = 0
OPCIONES = ['piedra', 'papel', 'tijera', 'chipote']
nombre = input("Ingresa tu nombre, jugador: ")

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Unix/Linux

while True:
    limpiar_pantalla()
    print(f"Hola, {nombre}. ¡Bienvenido al juego!")
    print('-----------------------------------------------')
    print('Mira, solo hay una forma de arreglar esto:')
    print('1. PIEDRA ✊\n2. PAPEL ✋\n3. TIJERA 🖖\n4. CHIPOTECHILLON 🔨')

    while True:
        try:
            opcion_elegida = int(input("Ingresa el número correspondiente a tu elección: "))
            if opcion_elegida in range(1, len(OPCIONES) + 1):
                break
            else:
                print("Ups, opción no válida. Por favor ingresa un número entre 1 y", len(OPCIONES))
        except ValueError:
            print("Ups, opción no válida. Por favor ingresa un número entre 1 y", len(OPCIONES))

    humano = OPCIONES[opcion_elegida - 1]

    maquina = random.choice(OPCIONES)
    print('-----------------------------------------------')

    if humano == 'chipote' and maquina == 'chipote':
        print('No contavan con su astucia.\nDoble Chipote Chillon, les resta una victoria a cada uno')
        victoriaMaquina -= 1
        victoriaHumano -= 1

    elif humano == 'chipote' and (maquina == 'piedra' or maquina == 'papel'):
        print(f'{maquina} no es digno rival del Chipote Chillon')
        victoriaHumano += 1

    elif maquina == 'chipote' and (humano == 'piedra' or humano == 'papel'):
        print(f'El Chipote Chillon contraresta los poderes de tu {humano}')
        victoriaMaquina += 1

    elif humano == 'tijera' and maquina == 'chipote':
        print('La tijera pincha al Chipote y quita su poder de chillon')
        victoriaHumano += 1

    elif maquina == 'tijera' and humano == 'chipote':
        print('La tijera pincha al Chipote y quita su poder de chillon')
        victoriaMaquina += 1

    elif humano == 'piedra' and maquina == 'tijera':
        print('¡La buena piedra, nada le gana!')
        print(f'La maquina perdió con {maquina}')
        victoriaHumano += 1

    elif maquina == 'papel' and humano == 'piedra':
        print('Pobre humano, tan predecible. Siempre escoge piedra XD')
        print(f'La maquina gana con {maquina}')
        victoriaMaquina += 1

    elif humano == maquina:
        print(f'Quedamos en empate. Yo tambien escogí {maquina}')

    elif humano == 'papel' and maquina == 'piedra' or humano == 'tijera' and maquina == 'papel':
        print(f'Gana el humano con {humano}. La maquina perdió con {maquina}')
        victoriaHumano += 1
    else:
        print(f'Gana la maquina con {maquina}')
        victoriaMaquina += 1

    print(f'Marcador: {nombre} {victoriaHumano} | Maquina {victoriaMaquina}')

    jugar_de_nuevo = input('Juguemos otra vez (ingresa "S" para continuar jugando o "N" para salir): ').lower()

    if jugar_de_nuevo == 'n':
        if victoriaHumano > victoriaMaquina:
            nombre = nombre.upper()
            print(f'¡{nombre} ES EL GANADOR LEGÍTIMO! {victoriaHumano} - {victoriaMaquina}🎉')
        elif victoriaHumano == victoriaMaquina:
            print('EMPATE 🤝🏼. HA SIDO UNA GRAN JUEGO')
        else:
            print(f'¡VICTORIA SUPREMA PARA LA MAQUINA! {victoriaHumano} - {victoriaMaquina}😱')
        break
print(f'¡Hasta luego, {nombre}! 😋')