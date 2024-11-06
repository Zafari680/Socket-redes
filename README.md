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
