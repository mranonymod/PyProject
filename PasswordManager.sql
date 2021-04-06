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
    SharedID VARCHAR(256) UNIQUE ,
	Passwords VARCHAR(256) NOT NULL,
    SetOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

); 
CREATE TABLE SHDGRP(
	ID INT AUTO_INCREMENT PRIMARY KEY,
    SharedID VARCHAR(256),FOREIGN KEY(`SharedID`) REFERENCES `Passwords`(`SharedID`),
    Username VARCHAR(64) ,FOREIGN KEY (`Username`) REFERENCES `Users` (`Username`)
);

INSERT INTO Users values ('Yash18','Yash','mryash018@gmail.com','Yash');
INSERT INTO Users values('Eren','Eren','eren@gmail.com','Eren');
INSERT INTO Users values ('bruh','bruh','bruh@gmail.com','408f31d86c6bf4a8aff4ea682ad002278f8cb39dc5f37b53d343e63a61f3cc4f');
INSERT INTO ServicesR(Services) values ('NETFLIX');
INSERT INTO ServicesR(Services) values ('DISNEY+');
INSERT INTO Passwords(Username,AccUserName,Service,SharedID,Passwords) values ('Yash18','YashNetflix','NETFLIX','8989','Yashnflix');
INSERT INTO Passwords(Username,AccUserName,Service,SharedID,Passwords) values ('Eren','ErenDisney+','DISNEY+','0456','Erendney');
INSERT INTO SHDGRP(SharedID,Username) VALUES ('8989','Eren');
INSERT INTO SHDGRP(SharedID,Username) VALUES ('8989','bruh');
INSERT INTO SHDGRP(SharedID,Username) VALUES('0456','bruh');



SELECT * FROM Users;
SELECT * FROM Passwords;
SELECT * FROM ServicesR;
SELECT * FROM SHDGRP;