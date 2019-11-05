# email_parsing
Different APIs to parse an email headers

1) A Javascipt and HTML interface.
 - Start a basic webserver on any port you wish:  python -m SimpleHTTPServer 5554
  . Must start the web server from the same directory as the email.html file.
 - In a browser: http://localhost:5554/email.html
 
2) An HTTP API with a python backend
 - A Docker container hosts a Flask app
 - Build the image from the contained Dockerfile
 - Run the container with ports <host port>:5555
 - OR without a container: python3 app_email.py
 - TODO: Update to pass a port argument into the container or CLI
