import socket
import threading
import pymysql
from datetime import datetime

# Conexión a la base de datos MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',        # Cambia esto si usas otro usuario
    password='',        # Ingresa tu contraseña de MySQL
    database='servidor_cliente'
)

# Diccionario para almacenar clientes activos (username: socket)
clients = {}

# Función para guardar usuario en la base de datos
def save_user_to_db(username):
    with connection.cursor() as cursor:
        # Guardar nuevo usuario o actualizar la última conexión
        sql = """
            INSERT INTO usuarios (apodos, fechaDeCreacion, fechaDeUltimaConexion)
            VALUES (%s, NOW(), NOW())
            ON DUPLICATE KEY UPDATE fechaDeUltimaConexion = NOW()
        """
        cursor.execute(sql, (username,))
        connection.commit()

# Función para manejar la comunicación con cada cliente
def handle_client(client_socket, username):
    save_user_to_db(username)  # Guardar o actualizar usuario al conectarse

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Decodificar el mensaje recibido
            message = data.decode('utf-8')
            
            # Verificar el tipo de mensaje y manejarlo
            if message.startswith("#"):
                # Mensaje privado al usuario especificado
                parts = message.split(" ", 2)
                if len(parts) >= 3:
                    target_user = parts[1]
                    private_message = parts[2]
                    
                    if target_user in clients:
                        clients[target_user].send(f"Private message from {username}: {private_message}".encode('utf-8'))
                    else:
                        client_socket.send(f"User {target_user} not found.".encode('utf-8'))

            elif message.startswith("/"):
                # Comando especial
                if message == "/listar":
                    # Listar usuarios conectados
                    user_list = "Connected users: " + ", ".join(clients.keys())
                    client_socket.sendall(user_list.encode('utf-8'))
                
                elif message == "/desconectar":
                    # Desconectar a todos los usuarios
                    for user_sock in clients.values():
                        user_sock.sendall("El servidor se ha desconectado.".encode('utf-8'))
                        user_sock.close()
                    clients.clear()
                    print("Todos los usuarios se han desconectado.")
                    break

                elif message == "/salir":
                    # Desconectar al usuario actual
                    client_socket.send("Te fuiste rey.".encode('utf-8'))
                    client_socket.close()
                    del clients[username]
                    print(f"Usuario {username} se ha desconectado.")
                    break

                else:
                    client_socket.send("Unknown command.".encode('utf-8'))

            else:
                # Mensaje público para todos los usuarios
                broadcast(f"{username}: {message}", client_socket)

        except Exception as e:
            print(f"Error handling message from {username}: {e}")
            break

    # Remover al cliente del diccionario cuando se desconecta
    if username in clients:
        del clients[username]
    client_socket.close()

# Función para enviar un mensaje a todos los clientes, excepto al emisor
def broadcast(message, sender_socket):
    for client_socket in clients.values():
        if client_socket != sender_socket:
            client_socket.send(message.encode('utf-8'))

# Función principal para el servidor
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_socket.sendall("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')
        
        # Agregar al usuario a la lista de clientes
        if username in clients:
            client_socket.sendall("Username already taken. Please try again.".encode('utf-8'))
            client_socket.close()
        else:
            clients[username] = client_socket
            print(f"Accepted connection from {username} at {client_address}")
            client_socket.sendall("You are now connected to the server.".encode('utf-8'))
            
            # Crear un hilo para manejar al cliente
            client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
            client_handler.start()

if __name__ == "__main__":
    main()
