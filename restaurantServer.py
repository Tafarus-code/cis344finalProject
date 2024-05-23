#restaurantServer

from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
from RestaurantDatabase import RestaurantDatabase
import cgi


class RestaurantPortalHandler(BaseHTTPRequestHandler):
    def __init__(self, *args):
        self.database = RestaurantDatabase()
        BaseHTTPRequestHandler.__init__(self, *args)
    def do_POST(self):
        try:
            if self.path == '/addReservation':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                customerId = int(form.getvalue("customerId"))
                reservationTime = form.getvalue("reservationTime")
                numberOfGuests = (form.getvalue("numberOfGuests"))
                specialRequests = form.getvalue("specialRequests")

                self.database.addReservation(customerId, reservationTime, numberOfGuests, specialRequests)
                print("Reservation added for customer ID:", customerId)
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>|\
                                     <a href='/addReservation'>Add Reservation</a>|\
                                     <a href='/viewReservations'>View Reservations</a></div>|\
                                     <a href='/addCustomer'>Add Customer</a></div>|\
                                     <a href='/findCustomer'>Find Customer</a></div>\
                                     ")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservation has been added</h3>")
                self.wfile.write(b"<div><a href='/addReservation'>Add Another Reservation</a></div>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/viewReservations':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                reservations = self.viewReservation()
                if reservations:
                    self.wfile.write(b"<html><head><title>Restaurant Portal - View Reservations</title></head>")
                    self.wfile.write(b"<body>")
                    self.wfile.write(b"<center><h1>VReservations</h1>")
                    self.wfile.write(b"<hr>")
                    self.wfile.write(b"<div> <a href='/'>Home</a>|\
                                            < a href='/addReservation'>AddReservation</a>|\
                                            <a href='/viewReservations'>ViewReservations</a>|\
                                            <a href='/addCustomer'>AddCustomer</a></div>|\
                                            <a href='/findCustomer'>Find Customer</a></div>")
                    self.wfile.write(b"<hr>")
                    self.wfile.write(b"<h3>Search Results:</h3>")
                    # Display reservation details here
                    for reservation in reservations:
                        self.wfile.write(f"<p>{reservation}</p>".encode('utf-8'))
                    self.wfile.write(b"</center></body></html>")
                else:
                    error_message = "No reservations found based on the provided criteria."
                    self.wfile.write(error_message.encode('utf-8'))
                return

            elif self.path == '/addCustomer':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                customerId = form.getvalue("customerId")
                customerName = form.getvalue("customerName")
                contactInfo = form.getvalue("ContactInfo")

                customerId = self.database.addCustomer(customerId, customerName, contactInfo)
                print("Customer added with ID:", customerId)
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>|\
                                 < a href='/addReservation'>AddReservation</a>|\
                                 <a href='/viewReservations'>ViewReservations</a>|\
                                 <a href='/addCustomer'>AddCustomer</a></div>|\
                                 <a href='/findCustomer'>Find Customer</a></div>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Customer has been added</h3>")
                self.wfile.write(b"<div><a href='/addCustomer'>Add Another Customer</a></div>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/findReservations':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                customerId = int(form.getvalue("customerId"))
          
                reservations = self.database.findReservations(customerId)
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>|\
                                     <a href='/addReservation'>Add Reservation</a>|\
                                     <a href='/viewReservations'>View Reservations</a>|\
                                     <a href='/addCustomer'>Add Customer</a></div>|\
                                     <a href='/findCustomer'>Find Customer</a></div>\
                                     ")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<h3>Reservations for Customer ID: " + str(customerId) + "</h3>")
                for reservation in reservations:
                    self.wfile.write(b"<p>" + str(reservation) + "</p>")
                self.wfile.write(b"<div><a href='/findReservations'>Find Another Customer's Reservations</a></div>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/addSpecialRequest':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )

                reservation_id = int(form.getvalue("reservationId"))
                special_request = form.getvalue("specialRequest")
                success = self.database.addSpecialRequest(reservation_id, special_request)
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>|\
                                         <a href='/addReservation'>Add Reservation</a>|\
                                         <a href='/viewReservations'>View Reservations</a>|\
                                         <a href='/addCustomer'>Add Customer</a></div>|\
                                         <a href='/findCustomer'>Find Customer</a></div>\
                                         ")
                self.wfile.write(b"<hr>")
                if success:
                    self.wfile.write(b"<h3>Special Request added to Reservation ID: " + str(reservation_id) + "</h3>")
                else:
                    self.wfile.write(
                        b"<h3>Failed to add Special Request to Reservation ID: " + str(reservation_id) + "</h3>")
                self.wfile.write(b"<div><a href='/addSpecialRequest'>Add Another Special Request</a></div>")
                self.wfile.write(b"</center></body></html>")
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_GET(self):
        try:
            if self.path == '/':
                data = []
                records = self.database.getAllReservations()
                data = records
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Restaurant Portal</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Restaurant Portal</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<div> <a href='/'>Home</a>| \
                                 <a href='/addReservation'>Add Reservation</a>|\
                                 <a href='/viewReservations'>View Reservations</a>|\
                                 <a href='/addCustomer'>Add Customer</a></div>")
                self.wfile.write(b"<hr><h2>All Reservations</h2>")
                self.wfile.write(b"<table border=2> \
                                <tr><th> Reservation ID </th>\
                                    <th> Customer ID </th>\
                                    <th> Reservation Time </th>\
                                    <th> Number of Guests </th>\
                                    <th> Special Requests </th></tr>")

                for row in data:
                    self.wfile.write(b' <tr> <td>')
                    self.wfile.write(str(row[0]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[1]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[2]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[3]).encode())
                    self.wfile.write(b'</td><td>')
                    self.wfile.write(str(row[4]).encode())
                    self.wfile.write(b'</td></tr>')

                self.wfile.write(b"</table></center>")
                self.wfile.write(b"</body></html>")
                return

            elif self.path == '/addReservation':

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Add Reservation</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Add Reservation</h1>")
                self.wfile.write(b"<hr>")
           
                self.wfile.write(b"<form method='post' action='/addReservation'>")
                self.wfile.write(b"Customer ID: <input type='text' name='customerId'><br>")
                self.wfile.write(b"Reservation Time: <input type='datetime-local' name='reservationTime'><br>")
                self.wfile.write(b"Number of Guests: <input type='text' name='numberOfGuest'><br>")
                self.wfile.write(b"<input type='submit' value='Add Reservation'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/viewReservations':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>View Reservations</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>View Reservations</h1>")
                self.wfile.write(b"<hr>")

                db = RestaurantDatabase()
                reservations = db.viewReservations()
                if reservations:
                    self.wfile.write(b"<ul>")
                    for reservation in reservations:
                        self.wfile.write(b"<li>" + str(reservation).encode() + b"</li>")
                    self.wfile.write(b"</ul>")
                else:
                    self.wfile.write(b"<p>No reservations found.</p>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/addCustomer':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Add Customer</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Add Customer</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<form method='post' action='/addCustomer'>")
                self.wfile.write(b"Customer ID: <input type='text' name='customerId'><br>")
                self.wfile.write(b"Customer Name: <input type='text' name='customerName'><br>")
                self.wfile.write(b"Contact: <input type='text' name='contactInfo'><br>")
                self.wfile.write(b"<input type='submit' value='Add Customer'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/findReservations':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Find Reservations</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Find Reservations</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<form method='post' action='/findReservations'>")
                self.wfile.write(b"Customer ID: <input type='text' name='customerId'><br>")
                self.wfile.write(b"<input type='submit' value='Search Reservations'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return

            elif self.path == '/addSpecialRequest':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><head><title>Add Special Request</title></head>")
                self.wfile.write(b"<body>")
                self.wfile.write(b"<center><h1>Add Special Request</h1>")
                self.wfile.write(b"<hr>")
                self.wfile.write(b"<form method='post' action='/addSpecialRequest'>")
                self.wfile.write(b"Reservation ID: <input type='text' name='reservation_id'><br>")
                self.wfile.write(b"Special Request: <input type='text' name='special_request'><br>")
                self.wfile.write(b"<input type='submit' value='Add Special Request'>")
                self.wfile.write(b"</form>")
                self.wfile.write(b"</center></body></html>")
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

def run(server_class=HTTPServer, handler_class=RestaurantPortalHandler, port=8000):
    server_address = ('localhost', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()


run()
