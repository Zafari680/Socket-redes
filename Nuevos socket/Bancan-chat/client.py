import socket
import threading

# Función para manejar la recepción de mensajes desde el servidor
def receive_messages(client_socket):
    while True:
        try:
            # Recibir datos desde el servidor
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Decodificar y mostrar el mensaje
            print(f"\n {data.decode('utf-8')}")
        
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Función principal del cliente
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define la dirección IP y el puerto del servidor al que se conectará.
    host = '127.0.0.1'
    port = 12345
    
    # Establece una conexión con el servidor especificado.
    client_socket.connect((host, port))

    # Solicita el nombre de usuario y lo envía al servidor.
    username = input("Enter your username: ")
    client_socket.sendall(username.encode('utf-8'))
    
    # Crear un hilo para recibir mensajes del servidor de manera continua
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    # Bucle principal para enviar mensajes al servidor
    while True:
        # Solicita el mensaje que el usuario quiere enviar.
        message = input("Enter your message: ")
        
        # Envía el mensaje al servidor, codificándolo en formato UTF-8.
        client_socket.sendall(message.encode('utf-8'))
        
        # Si el usuario envía el comando '/salir', el cliente se desconecta.
        if message == "/salir":
            print("Disconnecting from server...")
            break

    # Cierra el socket del cliente al desconectarse
    client_socket.close()

# Punto de entrada del programa; llama a la función principal para arrancar el cliente.
if __name__ == "__main__":
    main()
