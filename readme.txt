To run this project in your computer, follow the steps below
-------------------------------------------------------------
Step 1. Make and activate virtual Environment in your computer
    In windows
    > virtualenv ecom
    > Scripts\activate
    In mac and linux
    $ python3 -m venv .venv
    $ source .venv/bin/activate

Step 2. Clone the project
    $ git clone https://github.com/TechAcademy-Azerbaijan/E-commerce-Sellshop-Omega
    $ cd sellshop
    if you do not have git in your computer, install it before and clone it again.

Step 3: Install dependencies 
    $ pip install -r requirements.txt

Step 4: Apply the migration if any
    $ python manage.py makemigrations
    $ python manage.py migrate

Step 5: You can now open project folder in your editor

Step 6: Run Development server
    $ python manage.py runserver