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
Services VARCHAR(128) NOT NULL UNIQUE,
Website VARCHAR(50),
LogP varchar(100),
EmailI VARCHAR(100),
PasswordI VARCHAR(100),
SignB VARCHAR(100)
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

INSERT INTO Users values ('Yash18@','Yash','mryash018@gmail.com','5014cf14bc63c47d74306feb4e0c1498313cfd71ae309462d44b8a97c763e990');
INSERT INTO Users values('Eren7@','ERENYEAGAR','eren@gmail.com','0f26fc7f966c6e83fc7424fef46ec96ea37a3503edc5bf52c379aaf374720436');
INSERT INTO Users values ('bruh','bruh','bruh@gmail.com','408f31d86c6bf4a8aff4ea682ad002278f8cb39dc5f37b53d343e63a61f3cc4f');
INSERT INTO ServicesR(Services,Website,LogP,EmailI,PasswordI,SignB) values ('NETFLIX','https://www.netflix.com','/html/body/div[1]/div/div/div/div/div/div[1]/div/a','/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/input','/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input','/html/body/div[1]/div/div[3]/div/div/div[1]/form/button');
INSERT INTO ServicesR(Services) values ('DISNEY+');
INSERT INTO ServicesR(Services) values ('WIFI');
INSERT INTO Passwords(Username,AccUserName,Service,SharedID,Passwords) values ('bruh','bruh','WIFI','63hWc7S#Te3v6iU4v','T2hNDPX8VUxdojDhoVxFsGmYyrFaqOjRDpA41KP6Ldo=');
INSERT INTO Passwords(Username,AccUserName,Service,SharedID,Passwords) values ('Yash18@','Yash18@','NETFLIX','-LCMBkcsf*X9i#Bm5','SZlHMYTTmOltAXEqZ5eZTFzeVq6tJ1ZvgVNvl6jpsaM=');
INSERT INTO Passwords(Username,AccUserName,Service,SharedID,Passwords) values ('Eren7@','Eren7@','DISNEY+','7v3dmnol1OapsN&xP','UVwaU7ksW+1NYwPe4f2JWpdj/i9EIto+3Py79Sh5/9w=');
INSERT INTO SHDGRP(SharedID,Username) VALUES ('63hWc7S#Te3v6iU4v','Eren7@');
INSERT INTO SHDGRP(SharedID,Username) VALUES ('7v3dmnol1OapsN&xP','bruh');
INSERT INTO SHDGRP(SharedID,Username) VALUES('-LCMBkcsf*X9i#Bm5','bruh');



SELECT * FROM Users;
SELECT * FROM Passwords;
SELECT * FROM ServicesR;
SELECT * FROM SHDGRP;