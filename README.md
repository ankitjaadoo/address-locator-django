# address-locator-django
This is a single page Django application which takes in an excel file containing different addresses as input and returns an updated excel file containing the addresses along with their respective latitudes and logitudes.

## Libraries/Frameworks used :

- Python==3.8.5
- attrs==20.3.0
- certifi==2020.12.5
- click==7.1.2
- click-plugins==1.1.1
- cligj==0.7.1
- Django==2.2.17
- et-xmlfile==1.0.1
- Fiona==1.8.18
- geographiclib==1.50
- geopandas==0.8.1
- geopy==2.1.0
- jdcal==1.4.1
- munch==2.5.0
- numpy==1.19.4
- openpyxl==2.5.1
- pandas==1.2.0
- pyproj==3.0.0.post1
- python-dateutil==2.8.1
- pytz==2020.5
- Shapely==1.7.1
- six==1.15.0
- sqlparse==0.4.1

## Instructions to run the project

# Run the following commands in your terminal (Mac)

1. git clone https://github.com/ankitjaadoo/address-locator-django.git
2. cd address-locator-django/
3. python3 -m venv .venv && source .venv/bin/activate (create and activate virtual environment)
4. pip3 install -r requirements.txt (download all required libraries)
5. django-admin manage.py makemigrations
6. django-admin manage.py migrate
7. django-admin manage.py runserver (launch the server)

# Run the following commands in your terminal (Windows)

1. git clone https://github.com/ankitjaadoo/address-locator-django.git
2. cd address-locator-django/
3. python3 -m venv .venv
4. .\env\Scripts\activate (activate virtual environment)
5. pip3 install -r requirements.txt (download all required libraries)
6. django-admin manage.py makemigrations
7. django-admin manage.py migrate
8. django-admin manage.py runserver (launch the server)


# Go to http://127.0.0.1:8000/ on your browser - you will see a File Upload option over there. Select the "addresses.xlsx" file attached with this folder and hit the Uplaod button. Next, you will be prompted with a message saying "Your File has been saved, do check inside your project folder!"