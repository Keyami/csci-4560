Installing flask:
    1. cd flask
    2. sudo apt install python3.10-venv
	3. sudo python3 -m venv venv
	4. . venv/bin/activate
	5. sudo pip install Flask
	
Running the LMD website:
    1. cd flask
	2. flask --app flaskr run
	3. Navigate to localhost:5000


File Structure and Corresponding URL:

flaskr/auth.py - 
  Python code for authenticating user accounts.
 
flaskr/templates/auth/login.html
flaskr/templates/auth/register.html
  UI for user authentication.
  
flaskr/media.py - 
  Getters and setters for media database.
  
flaskr/schema.sql - 
  Current working schema for the DB.
  
flaskr/__init__.py -
  Python main.
  
flaskr/templates/media/create.html
flaskr/templates/media/index.html
flaskr/templates/media/update.html - 
  Respective frontend UI for adding a new book to inventory, 
  removing a book, and viewing a specific book.
  
flaskr/templates/nav.html - 
  Persistent HTML code imported to all other HTML files for navbar.
  
flaskr/templates/base.html - 
  The base HTML that all other HTML files are input into when viewing. 
  Handles CSS & navbar integration.