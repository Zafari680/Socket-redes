# Socket-redes
Este proyecto implementa un servidor de chat utilizando sockets en Python. Los usuarios pueden enviar mensajes públicos a todos los clientes conectados y también pueden enviar mensajes privados a usuarios específicos.

Requisitos
Python 3.x
Biblioteca pymysql para la conexión a MySQL (puedes instalarla con pip install pymysql)

Configuración de MySQL
Este proyecto utiliza MySQL para almacenar los usuarios y sus últimas conexiones. Se debe tener una base de datos llamada servidor_cliente en MySQL con la siguiente tabla:

sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    apodos VARCHAR(255) UNIQUE,
    fechaDeCreacion DATETIME,
    fechaDeUltimaConexion DATETIME
);
Para que logre funcionar correctamente


Aquí tienes un ejemplo de README que explica cómo usar el servidor y el cliente:

Chat Server con Mensajes Privados
Este proyecto implementa un servidor de chat utilizando sockets en Python. Los usuarios pueden enviar mensajes públicos a todos los clientes conectados y también pueden enviar mensajes privados a usuarios específicos.

Requisitos
Python 3.x
Biblioteca pymysql para la conexión a MySQL (puedes instalarla con pip install pymysql)
Configuración de MySQL
Este proyecto utiliza MySQL para almacenar los usuarios y sus últimas conexiones. Asegúrate de tener una base de datos llamada servidor_cliente en MySQL con la siguiente tabla:

sql
Copiar código
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    apodos VARCHAR(255) UNIQUE,
    fechaDeCreacion DATETIME,
    fechaDeUltimaConexion DATETIME
);


MODO DE USO:
1. Ejecutar el Servidor
Para iniciar el servidor, ejecuta el archivo servidor.py:
ingresando a la terminal y ejecutar el comando "python server.py" una vez hecho esto.
El servidor escuchará en 127.0.0.1 (localhost) en el puerto 12345.

2. Conectar Clientes al Servidor
Para conectar un cliente al servidor, ejecuta el archivo cliente.py en diferentes terminales o máquinas (asegurándote de que el servidor esté en funcionamiento): al igual que el modo anterior se debe ejecutar el archivo usando el comando "python client.py" una vez hecho esto.
El cliente solicitará un nombre de usuario, el cual será utilizado para identificar al usuario en el servidor.

Mensajes Privados
Para enviar un mensaje privado a otro usuario, usa el siguiente formato:

#nombre_usuario Mensaje privado aquí
Por ejemplo, para enviar un mensaje privado a un usuario llamado "Faustino", escribe:

#Faustino Hola pedro, ¿cómo estás che?
El mensaje será enviado solo a "Pedro", y recibirás una confirmación de que el mensaje fue enviado correctamente.
Si intentas enviar un mensaje privado a un usuario que no está conectado, recibirás un mensaje indicando que el usuario no existe.


4. Comandos Especiales
Puedes usar los siguientes comandos para interactuar con el servidor:

/listar - Muestra la lista de usuarios conectados.
/desconectar - Desconecta a todos los usuarios del servidor.
/salir - Desconecta al cliente actual del servidor.

