-- Base de datos modificada

DROP DATABASE smability;

CREATE DATABASE smability;
USE smability;

CREATE TABLE Device(
	ID_Device INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Nombre VARCHAR(20),
	Token VARCHAR(64),
)

CREATE TABLE Location_Data(
	ID_Location_Data INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Place VARCHAR(50),
	Latitude DECIMAL(10,8),
	Longitude DECIMAL(10,8)
    ID_Device INT NOT NULL REFERENCES Device(ID_Device) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE Sensor(
	ID_Sensor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Descript VARCHAR(20),
	ID_Device INT NOT NULL REFERENCES Device(ID_Device) ON DELETE NO ACTION ON UPDATE CASCADE
);

CREATE TABLE Measure(
	ID_Measure INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	ID_Smability INT, 
	Kind_Measure VARCHAR(20),
	Units VARCHAR(8)
);

CREATE TABLE Sample(
	ID_Sample INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	Time_Data TIMESTAMP NULL DEFAULT NULL,
	Sample_Data DECIMAL(10,7),
	ID_Sensor INT NOT NULL REFERENCES Sensor(ID_Sensor) ON DELETE NO ACTION ON UPDATE CASCADE, 
	ID_Measure INT NOT NULL REFERENCES Measure(ID_Measure) ON DELETE NO ACTION ON UPDATE CASCADE
);

SHOW TABLES;