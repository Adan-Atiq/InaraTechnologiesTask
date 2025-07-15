# InaraTechnologiesTask
Blogging Platform with User Authentication – Django REST Framework
# Overview:
This is a simple blogging platform built using Django and Django REST Framework (DRF). It features:
User registration (Writer/Viewer roles),
JWT-based login & authentication,
Role-based access control:
Writers can create, update, and delete blog posts.
Viewers can only view blog posts.
Blog post CRUD operations
Pagination for listing blogs

# Technologies Used
Django 5.2.4,
Django REST Framework,
Simple JWT (Token-based Authentication),
SQLite3 (default Django DB),

# User Roles

# Writer Can:
Register/login,
Create blog posts,
Edit and delete their posts,
View all posts.

# Viewer Can:
Register/login,
View all blog posts only.

# Features Implemented
 1. User Authentication
Registration endpoint: POST /api/register/
Fields: username, email, mobile_number, password, role
Custom user model using AbstractUser
JWT-based login: POST /api/login/
Token refresh: POST /api/token/refresh/

 2. Blog Post Management
Blog model: title, content, publication_date, author.
CRUD operations only allowed for authenticated Writers.
Viewers and public users can only perform GET requests.
Automatically saves the logged-in user as the blog author.

3. API & Permissions
Implemented using Django REST Framework's ModelViewSet.
Custom permission class IsWriterOrReadOnly:
Only writers can write/delete.
All users can read.
Pagination for blogs: /api/blogs/?page=1.

#  Postman Testing 
test all APIs using Postman.
 "postman_collection.json is provided."
Positive tests (writer/blog creation),
Negative tests (viewer trying to post),
Token-based authentication tests,
Pagination check.

# How to Run the Project
# Clone project
git clone <https://github.com/Adan-Atiq/InaraTechnologiesTask.git>

# Navigate into the project
cd blogproject

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the server
python manage.py runserver

# Submission Checklist
Django project with working API,
JWT authentication,
Role-based blog access,
Pagination,
Postman collection (.json) included,
Code is commented and follows best practices,

# Author
Adan Atiq
Software Engineering Graduate
