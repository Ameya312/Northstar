# Cafe Northstar

This is a python Django application for a food aggregator app.
<br /><br /><br />
# DB structure
### Snack
| Column | Description |
| ------ | ------ |
| id | Unique identifier for table |
| name | Name of Snack |
| price | Price of snack |
| is_active | Flag for soft delete |
### Cart
| Column | Description |
| ------ | ------ |
| emp_id | Id of employee |
| cart_id | Unique identifier for cart  |
| snack_id | Foreign key linking to snack table |
| quantity | Quantity of the snacks to be ordered |
| date_time | The date and time the order was placed |
| total | The total amount of snacks |
| payment_status | The status of the payment of the order |
| emp_name | The name of the employee placing the order |
<br /><br />
### How to run the service
You can run the service by creating a database in MySQL with following details -
**NAME= Northstar_project**
**USER= testuser**
**PASSWORD= TestPwd@123**
or alternatively you can set the details you want in the settings file.

Next commands -
1. Installing pipenv (package to segregate virtual environments) -
    >pip install pipenv
    >pipenv shell
    >pipenv install             (this is for installing all packages required by service)

2. To migrate all db changes use the following command -
    >python manage.py migrate

3. To run the service use the following command -
    >python manage.py runserver

4. To check the API Swagger Documentation -
    http://127.0.0.1:8000/swagger/