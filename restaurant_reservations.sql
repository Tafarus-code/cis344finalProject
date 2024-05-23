#restaurant_reservations.sql
  
CREATE DATABASE restaurant_reservations;
use restaurant_reservations;
CREATE TABLE Customers (
    customerId INT NOT NULL UNIQUE AUTO_INCREMENT,
    customerName VARCHAR(45) NOT NULL,
    contactInfo VARCHAR(200),
    PRIMARY KEY (customerId)
);
CREATE TABLE Reservations (
    reservationId INT NOT NULL UNIQUE AUTO_INCREMENT,
    customerId INT NOT NULL,
    reservationTime DATETIME NOT NULL,
    numberOfGuests INT NOT NULL,
    specialRequests VARCHAR(200),
    PRIMARY KEY (reservationId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);
CREATE TABLE DiningPreferences (
    preferenceId INT NOT NULL UNIQUE AUTO_INCREMENT,
    customerId INT NOT NULL,
    favoriteTable VARCHAR(45),
    dietaryRestrictions VARCHAR(200),
    PRIMARY KEY (preferenceId),
    FOREIGN KEY (customerId) REFERENCES Customers(customerId)
);

DELIMITER //
CREATE PROCEDURE findReservations(IN customerIdParam INT)
BEGIN
    SELECT * FROM Reservations WHERE customerId = customerIdParam;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE addSpecialRequest(IN reservationIdParam INT, IN requestsParam VARCHAR(200))
BEGIN
    UPDATE Reservations SET specialRequests = requestsParam WHERE reservationId = reservationIdParam;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE addReservation(IN customerNameParam VARCHAR(45), IN contactInfoParam VARCHAR(200), IN reservationTimeParam DATETIME, IN numberOfGuestsParam INT, IN specialRequestsParam VARCHAR(200), IN favoriteTableParam VARCHAR(45), IN dietaryRestrictionsParam VARCHAR(200))
BEGIN
    DECLARE customerIDNew INT;

    INSERT INTO Customers (customerName, contactInfo) VALUES (customerNameParam, contactInfoParam);
    SET customerIDNew = LAST_INSERT_ID();

    INSERT INTO Reservations (customerId, reservationTime, numberOfGuests, specialRequests) 
    VALUES (customerIDNew, reservationTimeParam, numberOfGuestsParam, specialRequestsParam);

    INSERT INTO DiningPreferences (customerId, favoriteTable, dietaryRestrictions) 
    VALUES (customerIDNew, favoriteTableParam, dietaryRestrictionsParam);
END //
DELIMITER ;

CALL addReservation('Mamadou Balde', 'mamadou.balde@example.com', '2022-12-31 11:00:00', 2, 'No specific requests', 'Table 4', 'No dietary restrictions');
CALL addReservation('David Wayne', 'david.wayne@example.com', '2024-08-31 12:00:00', 2, 'Outdoor table', 'Table 1', 'None');
CALL addReservation('Rashad Johnson', 'rashad.johnson@example.com', '2024-12-31 11:00:00', 2, 'No specific requests', 'Table 3', 'peanut');
CALL addReservation('Malik JDiallo', 'malik.diallo@example.com', '2024-05-31 18:00:00', 2, 'No specific requests', 'Table 7', 'none');

SELECT * FROM Customers;
SELECT * FROM DiningPreferences;
SELECT * FROM Reservations;



