# Servidor de Chat en Python

Este es un servidor de chat simple implementado en Python utilizando sockets y una base de datos MySQL. Permite a los usuarios conectarse, registrarse y comunicarse entre sí de manera pública o privada.

## Requisitos

Antes de ejecutar el servidor, asegúrate de tener instalados los siguientes elementos:

- Python 3.x
- MySQL (XAMPP recomendado)
- Paquete `mysql-connector-python`

Puedes instalar el paquete necesario usando pip:

```bash
pip install mysql-connector-python

Configuración de MySQL
Instalar XAMPP:

Descarga e instala XAMPP desde Apache Friends.
Inicia el módulo de MySQL desde el panel de control de XAMPP.
Crear la base de datos:

Accede a phpMyAdmin (generalmente en http://localhost/phpmyadmin).
Crea una base de datos llamada chat_system.
Crear la tabla de usuarios:

El script de Python se encargará de crear automáticamente la tabla users cuando se ejecute, si no existe.


Conectarse al servidor:

Los clientes pueden conectarse al servidor utilizando un cliente de socket (puedes crear uno en Python o usar herramientas como telnet).
Asegúrate de conectarte a la dirección 127.0.0.1 (localhost) y al puerto 3308.
Registro de usuario:

Al conectarte, se te pedirá que ingreses un apodo (nickname).
Si el apodo ya existe, se actualizará tu última conexión. Si es nuevo, se registrará en la base de datos.
Enviar mensajes:

Puedes enviar mensajes públicos que serán visibles para todos los usuarios conectados.

Para enviar un mensaje privado, comienza tu mensaje con #, seguido del nombre del destinatario y el mensaje.
Comandos:

Puedes usar los siguientes comandos en el chat:
/listar: Muestra la lista de usuarios conectados.
/desconectar: Desconecta a todos los usuarios del servidor.
/salir: Desconecta al usuario actual.
Desconectar:

Para desconectarte, puedes utilizar el comando /salir o cerrar la ventana del cliente.
