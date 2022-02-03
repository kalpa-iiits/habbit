This repo is to biuld a CRUD API of a user Course and Wishlist, and to implement token based authentication.

The following things are implemented in this repo.
  1. A course model, which will have basic data about the courses. It is accessible via a rest API(CRUD). You can ADD, EDIT, DELETE the course. 
  2. A wishlist model, which will have a user and a course. The users can add any course they want to wishlist, Users can ADD, EDIT, DELETE courses from the wishlist.-
  3. A user can be logged in using TokenAuthentication. This method is also a CRUD API. Standard Auth Library is used for authentication.
  4. We test the data using pytest.
  5. We use Swagger, which is an opensource tool for accessing the API through an interface.

How to Access the APIs:
    
To run the code in a local machine:
  1. Make sure you have pip intstalled in your system.
  2. Clone the repo into a folder .
  3. Install all the necessary dependencies by using the command pip install -r requirements.txt
  4. Now do python manage.py makemigrations and then python manage.py migrate. This will create database tables in your system.
  5. Now run the project by doing python manage.py runserver.
  6. You can now acess the AP from a different command line interface.
  
  
