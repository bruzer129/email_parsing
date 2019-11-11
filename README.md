# email_parsing
Different APIs to parse a email headers

1) A Javascipt and HTML interface.
 - Start a basic webserver on any port you wish:  python -m SimpleHTTPServer 5554
  . Must start the web server from the same directory as the emailjs.html file.
 - In a browser: http://localhost:5554/emailjs.html
 - Select the email.txt file from src/js

2) A Flask HTTP API with a python backend
 - A Docker container hosts a Flask app
 - Build the image from the contained Dockerfile
  . cd src/py
  . docker build -t flask_ubu_img .
 - Run the container
  . docker run -d -t --name flask_email_app -p 5000:5000 flask_ubu_img
 - OR without a container: python3 app_email.py
 - Open a web browser to: http://localhost:5000 or http://0.0.0.0:5000
  . http://localhost:5000/api/email
