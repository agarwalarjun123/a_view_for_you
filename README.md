# A view for you

Context
A Django app that provides the details of nearby and popular landscapes with photographs, user reviews and filter tags.

PreRequisite
1. python3.7
2. elasticsearch Instance (Copy CA certificate to root Directory)
3. MySQL Instance (For Production, For Development Project runs with sqlite3) 

Setup
The first step is to clone the repository
```bash
git clone https://github.com/agarwalarjun123/a_view_for_you.git
cd a_view_for_you
```

Secondly, install the dependencies
```bash
python3 -m virtual venv
source venv/bin/activate
pip install -r requirements.txt
```

Setup Environment Variables
```bash
touch .env
cat test.env >> .env
```
Note: modify .env to use correct elasticsearch hosted credentials and mysql credentials (For ENV=PRODUCTION).

Collect Static Content
```bash
python3 manage.py collectstatic
```


Setup DB
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Add Landscape Data Collated
```bash
python3 populate.py
python3 es_sync.py 
```

To run the project
```bash
python3 manage.py runserver
```
## Walkthrough
###### Homepage
Navigate to ```http://127.0.0.1:8000/```
Here you can see the most popular landscapes, among with the searching tool.
For registered users it will suggest landscapes that may be of interest based on their previous reviews and location.

###### Landscape details
This view is available when you click on a landscape card.
It contains basic information such as landscape’s description, location, access, opening hours, fees, food, etc.

###### Add landscape review
On each Landscape details, there is an option to add a review. Once clicked on the option, you will be able to comment according to a visit, adding tags, rating and pictures.

###### Profile
Navigate to ```http://127.0.0.1:8000/profile/```
Here it is display basic personal information; includes landscapes visited, comments made and the amount of likes and reviews made.

###### Login
This option is able by clicking on the Login button on the home page or navigating to ```http://127.0.0.1:8000/auth/login/```.
For thism two options are available: to login with email and password or to select an authomatic google login.

###### Sign up
This option is able by clicking on the Login button on the home page or navigating to ```http://127.0.0.1:8000/auth/register/```.
You will be able to register entering a picture, username, email and password

