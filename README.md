# cis344finalProject
# ProjectReport

CIS 344 

Final Project Report 
 
The first source code, "restaurantServer.py," creates a straightforward restaurant portal web application using Python's `http. Server` module. It employs the `BaseHTTPRequestHandler` class to manage HTTP requests and responses. Different paths cater to functions like viewing reservations, adding customers, searching for reservations, and adding special requests. Error handling ensures a 404 response for missing files. The application launches an HTTP server on a specified port, offering users the ability to interact with the restaurant portal by accessing various endpoints. 

The second code introduces a `RestaurantDatabase` class that interacts with a MySQL database to handle restaurant reservations and customer data. It includes features like connecting to the database, adding reservations and customers, retrieving information, updating special requests, and managing preferences. The class facilitates tasks such as finding reservations by customer ID and deleting reservations, enhancing the database's functionality for restaurant operations.  
The SQL script details the establishment and usage of the "restaurant_reservations" database containing tables for Customers, Reservations, and DiningPreferences, along with related stored procedures. The script defines relationships between customer data, reservation details, and dining preferences, enabling operations like finding reservations, adding special requests, and creating new reservations with customer and dining preference details. Sample reservations are added to the database to validate the schema and procedures, showcasing the practical application of the database structure for restaurant reservation management. 
