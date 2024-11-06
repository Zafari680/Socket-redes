-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-11-2024 a las 23:36:34
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `servidor_cliente`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `apodos` varchar(50) NOT NULL,
  `fechaDeCreacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `fechaDeUltimaConexion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `apodos`, `fechaDeCreacion`, `fechaDeUltimaConexion`) VALUES
(1, 'jose', '2024-11-06 14:49:37', '2024-11-06 22:29:07'),
(2, 'david', '2024-11-06 14:49:41', '2024-11-06 14:49:41'),
(3, 'nicolas', '2024-11-06 14:49:45', '2024-11-06 15:31:25'),
(4, 'fede', '2024-11-06 14:51:53', '2024-11-06 14:51:53'),
(5, 'nahuel', '2024-11-06 14:52:03', '2024-11-06 14:52:03'),
(6, 'juan', '2024-11-06 15:02:29', '2024-11-06 15:02:29'),
(7, 'martin', '2024-11-06 15:02:35', '2024-11-06 15:31:28'),
(8, 'pedro', '2024-11-06 15:02:37', '2024-11-06 16:17:59'),
(11, 'kioto', '2024-11-06 15:31:33', '2024-11-06 15:31:33'),
(13, 'miguel', '2024-11-06 16:17:55', '2024-11-06 16:17:55'),
(15, 'marcus', '2024-11-06 16:29:20', '2024-11-06 16:29:20'),
(16, 'romina', '2024-11-06 16:29:31', '2024-11-06 16:29:31'),
(17, 'nahuel cortes', '2024-11-06 22:28:45', '2024-11-06 22:28:45'),
(18, 'emmanuel', '2024-11-06 22:28:51', '2024-11-06 22:28:51');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `apodos` (`apodos`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
