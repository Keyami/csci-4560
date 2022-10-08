# csci-4560
GitHub for CSCI 4560 database project; 2022.
Gage Richardson/Nathan Goodrum


1. Install Flask
2. Open a terminal instance in csci-4560
3. Run '. venv/bin/activate'
4. Run 'flask --app flaskr --debug run'
5. Navigate to localhost:5000


# File Structure and Corresponding URL:

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