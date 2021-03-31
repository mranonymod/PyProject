CREATE DATABASE PasswordManager; 
USE PasswordManager;

CREATE TABLE Users(	 
	Username VARCHAR(64) PRIMARY KEY,
	Name VARCHAR(128),
	Email VARCHAR(128) NOT NULL UNIQUE,
	Password VARCHAR(100)
); 

CREATE TABLE ServicesR (
ServiceID INT auto_increment PRIMARY KEY,
Services VARCHAR(128) NOT NULL UNIQUE
);

CREATE TABLE Passwords (
	ID INT AUTO_INCREMENT PRIMARY KEY,
	Username VARCHAR(64), FOREIGN KEY (`Username`) REFERENCES `Users` (`Username`),
    AccUserName VARCHAR(64) NOT NULL,
	Service VARCHAR(128) NOT NULL , FOREIGN KEY (`Service`) REFERENCES `ServicesR`(`Services`),
    SharedID INT ,
	Passwords VARCHAR(256) NOT NULL,
    SetOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

); 

CREATE TABLE SHDGRP(
    SharedID INT PRIMARY KEY,
    ServiceID INT, FOREIGN KEY (`ServiceID`) REFERENCES `ServicesR`(`ServiceID`),
    Services VARCHAR(128), FOREIGN KEY (`Services`) REFERENCES `ServicesR`(`Services`),
    Username VARCHAR(64) ,FOREIGN KEY (`Username`) REFERENCES `Users` (`Username`)
);
ALTER TABLE Passwords
ADD constraint SharedID
FOREIGN KEY (`SharedID`) REFERENCES `SHDGRP` (`SharedID`);

INSERT INTO Users values ('Yash18','Yash','mryash018@gmail.com','Yash');
INSERT INTO ServicesR(Services) values ('NETFLIX');
INSERT INTO Passwords(Username,AccUserName,Service,Passwords) values ('Yash18','YashNetflix','NETFLIX','Yashnflix');

SELECT * FROM Users;
SELECT * FROM Passwords;
SELECT * FROM ServicesR;
SELECT * FROM SHDGRP;