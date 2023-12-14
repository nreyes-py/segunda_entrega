from cliente import Cliente
from miembro_vip import MiembroVIP

def crear_cliente():
    nombre = input('Ingrese el nombre del cliente: ')
    email = input('Ingrese el email del cliente: ')
    direccion = input('Ingrese la direccion del cliente: ')
    saldo = float(input('Ingrese el saldo inicial del cliente: '))
    return Cliente(nombre, email, direccion, saldo)

def crear_miembro_vip():
    nombre = input('Ingrese el nombre del miembro VIP: ')
    email = input('Ingrese el email del miembro VIP: ')
    direccion = input('Ingrese la direccion del miembro VIP: ')
    saldo = float(input('Ingrese el saldo inicial del miembro VIP: '))
    username = input('Ingrese el nombre de usuario del miembro VIP: ')
    password = input('Ingrese la contraseña del miembro VIP: ')
    descuento = float(input('Ingrese el porcentaje de descuento del miembro VIP: '))
    return MiembroVIP(nombre, email, direccion, saldo, username, password, descuento)

def listar_clientes(clientes):
    print('\nListado de Clientes:')
    print('-' * 80)  # Crea una línea divisora.
    print(f'{"ID":<3} {"Tipo":<12} {"Nombre":<20} {"Email":<25} {"Dirección":<20} {"Saldo":<10}')
    print('-' * 80)  # Crea una línea divisora.
    for idx, cliente in enumerate(clientes):
        tipo_cliente = 'Miembro VIP' if isinstance(cliente, MiembroVIP) else 'Cliente'
        # Ajusta el ancho de cada columna según sea necesario
        print(f'{idx:<3} {tipo_cliente:<12} {cliente.nombre:<20} {cliente.email:<25} {cliente.direccion:<20} {cliente.saldo:<10.2f}')
    print('-' * 80)  # Crea una línea divisora.

def menu():
    clientes = []
    
    while True:
        print('\nMenu:')
        print('1. Crear un nuevo cliente')
        print('2. Crear un nuevo miembro VIP')
        print('3. Listar clientes')
        print('4. Realizar una compra')
        print('5. Actualizar datos de un cliente')
        print('6. Salir')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            clientes.append(crear_cliente())
            print('Cliente creado exitosamente.')
        elif opcion == '2':
            clientes.append(crear_miembro_vip())
            print('Miembro VIP creado exitosamente.')
        elif opcion == '3':
            listar_clientes(clientes)
        elif opcion == '4':
            if not clientes:
                print('No hay clientes disponibles.')
                continue
            id_cliente = int(input('Ingrese el ID del cliente (0 a {}): '.format(len(clientes) - 1)))
            monto = float(input('Ingrese el monto de la compra: '))
            print(clientes[id_cliente].realizar_compra(monto))
        elif opcion == '5':
            if not clientes:
                print('No hay clientes disponibles.')
                continue
            id_cliente = int(input('Ingrese el ID del cliente (0 a {}): '.format(len(clientes) - 1)))
            nombre = input('Ingrese el nuevo nombre del cliente (dejar en blanco para no cambiar): ')
            email = input('Ingrese el nuevo email del cliente (dejar en blanco para no cambiar): ')
            direccion = input('Ingrese la nueva direccion del cliente (dejar en blanco para no cambiar): ')
            print(clientes[id_cliente].actualizar_datos(nombre=nombre or None, email=email or None, direccion=direccion or None))
        elif opcion == '6':
            print('Gracias por usar el sistema.')
            break
        else:
            print('Opción no válida, intente de nuevo.')

if __name__ == "__main__":
    menu()
