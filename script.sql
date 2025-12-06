CREATE DATABASE fitlife;
USE fitlife;

CREATE TABLE usuarios ( --TODAS
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO usuarios (nombre_usuario, email, password)
VALUES
('sol123', 'sol@gmail.com', '1234'),
('antoFit', 'anto@hotmail.com', 'fitlife2024'),
('zooee', 'LopezZ@fitlife.com', 'admin123'),
('lourdess', 'AcunaLou@gmail.com', 'melania123')

CREATE TABLE datos_personales (--TODAS
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    altura DECIMAL(4,1),
    peso DECIMAL(5,1),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT INTO datos_personales (usuario_id, nombre, apellido, edad, altura, peso)
VALUES
(1, 'Sol', 'Bracamonte', 16, 1.55, 55),
(2, 'Anto', 'Castillo', 16, 1.72, 50),
(3, 'Zoe', 'Lopez', 16, 1.65, 55),
(4, 'Lourdes', 'Acuña', 16, 1.59, 56)

CREATE TABLE home (--ANTONELLA
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    mensaje_bienvenida VARCHAR(255),
    objetivo VARCHAR(255),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT INTO home (usuario_id, mensaje_bienvenida, objetivo)
VALUES
(1, 'Bienvenida a FitLife Sol!', 'Mejorar hábitos diarios'),
(2, 'Bienvenida Anto!', 'Mejorar el sueño'),
(3, 'Bienvenida a FitLife Zoel!', 'Mejorar alimentación'),
(4, 'Bienvenida a FitLife Lourdesl!', 'Mejorar actividad física')

SELECT id, nombre_usuario --Verificar si el email existe(ANTO)
FROM usuarios
WHERE email = 'sol@gmail.com';

SELECT id, nombre_usuario --Verificar credenciales (correcto ANTO)--
FROM usuarios
WHERE email = 'sol@gmail.com'
  AND password = '1234';
|

CREATE TABLE sueño (--ZOE
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    horas_dormidas DECIMAL(3,1),
    calidad VARCHAR(50),
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT INTO sueño (usuario_id, horas_dormidas, calidad, fecha)
VALUES
(1, 7.5, 'Buena', '2024-12-01'),
(2, 6.0, 'Regular', '2024-12-01'),
(3, 8.0, 'Muy buena', '2024-12-01'),
(4, 6.5, 'Regular', '2024-12-01')

select from sueño;--ver todos los registros de sueño
select from sueño;
where usuario_id=1--ver el sueño especifico de un usuario(por ejemplo usuario_id=1)
CREATE TABLE actividad_fisica (-- SOL
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    tipo VARCHAR(100),
    duracion INT, -- minutos
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT INTO actividad_fisica (usuario_id, tipo, duracion, fecha)
VALUES
(1, 'Caminata ligera', 30, '2024-12-02'),
(2, 'Gimnasio', 45,'2024-12-02'),
(3, 'Yoga', 60, '2024-12-02'),
(4, 'Correr', 55,'2024-12-02')

DELETE FROM actividad_fisica
WHERE usuario_id = 1;

DELETE FROM usuarios
WHERE id=1;

CREATE TABLE alimentacion (--LOURDES
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    comida VARCHAR(100),
    calorias INT,
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
INSERT INTO alimentacion (usuario_id, comida, fecha)
VALUES
(1, 'Ensalada + pollo', '2024-12-02'),
(2, 'Tostadas con palta','2024-12-02'),
(3, 'Pastas caseras', '2024-12-02'),
(4, 'Licuado de frutos rojos', '2024-12-02')

UPDATE alimentacion--actualiza una comida que fue registrada por el usuario
SET comida="Ensaladacon pollo y arroz"
WHERE id=1;

UPDATE alimentacion
SET calorias=450
WHERE id=2;