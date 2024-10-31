import mysql.connector
import socket
import threading
from datetime import datetime

# Conexión a la base de datos MySQL de XAMPP
db = mysql.connector.connect(
    host="localhost",  # XAMPP por defecto usa localhost
    user="root",  # El usuario por defecto de MySQL en XAMPP es 'root'
    password="",  # Deja la contraseña vacía por defecto, a menos que la hayas cambiado
    database="chat_system",  # Nombre de la base de datos que creaste en phpMyAdmin
    port = 3306
)
cursor = db.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL,
    creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_conexion DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

db.commit()

# Variables para obtener los clientes y los nombres
clients = []
nickNames = []

# Configuración del servidor
host = '127.0.0.1'
port = 3308
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


# Función para aceptar al cliente
def clienteAceptado():
    while True:
        client, address = server.accept()
        print("Conexión establecida con:", address)

        client.send("Nick".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        # Verificar si el nickname ya existe en la base de datos
        cursor.execute("SELECT id FROM users WHERE nickname = %s", (nickname,))
        result = cursor.fetchone()

        if result:
            # Si el nickname ya existe, actualizar la fecha de ultima_conexion
            cursor.execute("UPDATE users SET ultima_conexion = %s WHERE nickname = %s", (datetime.now(), nickname))
            db.commit()
            print(f"El usuario {nickname} se ha reconectado, fecha de última conexión actualizada.")
        else:
            # Si el nickname no existe, insertar un nuevo usuario en la base de datos
            cursor.execute("INSERT INTO users (nickname, ultima_conexion) VALUES (%s, %s)", (nickname, datetime.now()))
            db.commit()
            print(f"Nuevo usuario {nickname} registrado en la base de datos.")

        # Añadir el cliente y el nickname a las listas
        nickNames.append(nickname)
        clients.append(client)

        broadcast(f"{nickname} se ha unido al chat.".encode('utf-8'))
        client.send("Conectado con el servidor".encode('utf-8'))

        # Iniciar el hilo para manejar los mensajes del cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()



# Función para manejar los mensajes de los clientes
def handle_client(client):
    while True:
        try:
            mensaje = client.recv(1024).decode('utf-8')
            if mensaje.startswith('#'):
                # Mensaje privado entre clientes
                target_nickname, private_msg = mensaje[1:].split(' ', 1)
                if target_nickname in nickNames:
                    target_index = nickNames.index(target_nickname)
                    target_client = clients[target_index]
                    target_client.send(f"Privado de {nickNames[clients.index(client)]}: {private_msg}".encode('utf-8'))
                else:
                    client.send("El usuario no existe prueba con los nombres de arriba.".encode('utf-8'))
            elif mensaje.startswith('/'):
                # Comando
                handle_commands(mensaje.strip(), client)
            else:
                # Mensaje público
                broadcast(f"{nickNames[clients.index(client)]}: {mensaje}".encode('utf-8'))
        except:
            disconnect_client(client)
            break

# Función para manejar los comandos tambien en los clientes 
def handle_commands(command, client):
    if command == "/listar":
        user_list = ', '.join(nickNames)
        client.send(f"Usuarios conectados: {user_list}".encode('utf-8'))
    elif command == "/desconectar":
        broadcast("El servidor está desconectando.".encode('utf-8'))
        for c in clients:
            c.close()
        clients.clear()
        nickNames.clear()
    elif command == "/salir":
        disconnect_client(client)

# Función para desconectar a un cliente lo ve el otro cliente no el servidor
def disconnect_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nickNames[index]
        clients.remove(client)
        nickNames.remove(nickname)
        client.close()
        broadcast(f'{nickname} se ha desconectado.'.encode('utf-8'))

# Función para manejar la difusión de mensajes a todos los clientes
def broadcast(message, _client=None):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                disconnect_client(client)

# Iniciar el servidor
print("Servidor escuchando...")
clienteAceptado()
