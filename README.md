# LittleLemon
Back-End Developer Capstone Project

BEFORE DOING ANYTHING
activate virtual environment using pipenv shell 
(it will not runserver otherwise)

Login for Django Admin:
User | Testing
Passwird | test@123!

Paths for testing:
Generate Token (Using Post Request in Insomnia w/ Valid Login)| http://127.0.0.1:8000/restaurant/api-token-auth/
Reservations | http://127.0.0.1:8000/restaurant/booking/tables/
Users (GET list [or individual user using <int:pk>], POST new user w/ valid body) | http://127.0.0.1:8000/auth/users/
Menu | http://127.0.0.1:8000/restaurant/menu
Menu Item (GET PUT DELETE) |http://127.0.0.1:8000/restaurant/menu/<int:pk>




