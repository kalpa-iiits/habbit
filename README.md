This repo is to biuld a CRUD API of a user Course and Wishlist, and to implement token based authentication.

The following things are implemented in this repo.
  1. A course model, which will have basic data about the courses. It is accessible via a rest API(CRUD). You can ADD, EDIT, DELETE the course. 
  2. A wishlist model, which will have a user and a course. The users can add any course they want to wishlist, Users can ADD, EDIT, DELETE courses from the wishlist.-
  3. A user can be logged in using TokenAuthentication. This method is also a CRUD API. Standard Auth Library is used for authentication.
  4. We test the data using pytest.

How to Access the APIs:

  The code is hosted on heroku and the APIs can be directly acessed from an endpoint.
    
  To get the list of courses:
    Send a GET request to- https://127.0.0.1:8000/api/course/

  To add a courses:
    Send a POST request to- https://127.0.0.1:8000/api/course/ followed by JSON Input
    
   To update a course:
    Send a PUT request to- https://127.0.0.1:8000/api/course/<course_id>/ followed by JSON Input
    
   To delete a course:
    Send a DELETE request to- https://127.0.0.1:8000/api/course/<course_id>/

  To get the list of wishlist:
    Send a GET request to- https://127.0.0.1:8000/api/wishlist/

  To add a wishlist:
    Send a POST request to- https://127.0.0.1:8000/api/wishlist/ followed by JSON Input
    
  To update a wishlist:
    Send a PUT request to- https://127.0.0.1:8000/api/wishlist/<item_id>/ followed by JSON Input
    
   To delete a wishlist:
    Send a DELETE request to- https://127.0.0.1:8000/api/course/<item_id>/

  To get a token for authentication:
    Send a POST request to- https://127.0.0.1:8000/api/course/

  To add a courses:
    Send a POST request to- https://127.0.0.1:8000/api/course/ followed by JSON Input
    
    
To run the code in a local machine:
  1. Make sure you have pip intstalled in your system.
  2. Clone the repo into a folder .
  3. Install all the necessary dependencies by using pip install -r requirements.txt
  4. Now do python manage.py makemigrations and then python manage.py migrate. This will create database tables in your system.
  5. Now run the project by doing python manage.py runserver.
  6. You can now acess the AP from a different command line interface.
  
  
