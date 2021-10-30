# This is a Library Management System,
# where a user can perform following operations
### 1)Access all books in the library.
### 2)Filter by category.
### 3)Access his/her books.
### 4)Add a new book to the library.

## Role of Each module.
### 1) Authentication module handles all the login,logout,signup and sending mails to verify account
### 2)Library module handles all the core functionality of the app, adding new book, acessing all books/my books
### 3) utils handles generic services, like sending emails, defining permissions etc

## Steps to setup on local machine
### 1)Fork and clone this repository
### 2)Download python3 and configure its path
### 3)Install all the dependencies mentioned in requirements.txt by the command
```
pip install -r requirements.txt
```
### 4) Make sure migrations and DB data is in sync by running the following command
```
python manage.py makemigrations
python manage.py migrate
```
### 5) Run the command to start the local development server
```
python manage.py runserver
```

## Assumptions made in this project
### 1) There are three DB tables, i.e User,Books,Category
### 2) A category,user have a Foreign key relationship to Books Table
### 3) Data is taken from csv file and written it to sqlite3 database
### 3) Aunthentication is made with email,password
### 4) All pages are protected with aunthentication
### 5) Data is paginated into pages of size 10
