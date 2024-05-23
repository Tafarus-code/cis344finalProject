#restaurantDatabase.py
import datetime
import mysql.connector
from mysql.connector import Error


class RestaurantDatabase():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="restaurant_reservations",
                 user='root',
                 password=''):

        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password)

            if self.connection.is_connected():
                print("Successfully connected to the database")
                return
        except Error as e:
            print("Error while connecting to MySQL", e)

    def addReservation(self, customerId, reservationTime, numberOfguests, specialRequests):
        ''' Method to insert a new reservation into the reservations table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO reservations (customerId, reservationTime, numberOfGuests, specialRequests) VALUES (%s, %s, %s, %s)"

            self.cursor.execute(query, (customerId, reservationTime, numberOfguests, specialRequests))
            self.connection.commit()
            print("Reservation added successfully")
            return

    def getAllReservations(self):
        ''' Method to get all reservations from the reservations table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM reservations"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def viewReservations(self):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM reservations"
            self.cursor.execute(query)
            reservations = self.cursor.fetchall()
            return reservations

    def addCustomer(self, customerId, customerName, contactInfo):
        ''' Method to add a new customer to the customers table '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "INSERT INTO customers (customerId, customerName, contactInfo) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (customerId, customerName, contactInfo))
            self.connection.commit()
            print("Customer added successfully")
            return

    def getCustomerPreferences(self, customerId):
        ''' Method to retrieve dining preferences for a specific customer '''
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM diningPreferences WHERE customerId = %s"
            self.cursor.execute(query, (customerId,))
            preferences = self.cursor.fetchall()
            return preferences

    def addSpecialRequest(self, reservationId, specialRequests):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "UPDATE reservations SET special_requests = %s WHERE reservation_id = %s"
            self.cursor.execute(query, (specialRequests, reservationId))
            self.connection.commit()
            print("Special request added successfully")

    def findReservations(self, customerId):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM reservations WHERE customerId = %s"
            self.cursor.execute(query, (customerId,))
            reservations = self.cursor.fetchall()
            return reservations

    def deleteReservation(self, reservationId):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "DELETE FROM reservations WHERE reservation_id = %s"
            self.cursor.execute(query, (reservationId,))
            self.connection.commit()
            print("Reservation deleted successfully")

    def searchPreferences(self, preferenceId):
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM diningPreferences WHERE preference_id = %s"
            self.cursor.execute(query, (preferenceId,))
            preferences = self.cursor.fetchall()
            return preferences

    # Add more methods as needed for restaurant operations
