[![Build Status](https://travis-ci.org/OCHIENGDAVIS/pols-with-datastructures.svg?branch=develop)](https://travis-ci.org/OCHIENGDAVIS/pols-with-datastructures)  [![Maintainability](https://api.codeclimate.com/v1/badges/8c94e63cb24e332dd416/maintainability)](https://codeclimate.com/github/OCHIENGDAVIS/pols-with-datastructures/maintainability) [![Coverage Status](https://coveralls.io/repos/github/OCHIENGDAVIS/pols-with-datastructures/badge.svg?branch=develop)](https://coveralls.io/github/OCHIENGDAVIS/pols-with-datastructures?branch=develop)

# POLITICO
Politico is an application that enables citizens give their mandate to politicians running for different government offices while building trust in the process through transparency. It has the following functionalities :


- Admin (electoral body) can create a political party
- Admin (electoral body can delete a political party)
- Admin (electoral body) can create different political offices
- Users can vote for only one politician per political office
-  Users can see the results of election 

# How to install and run the App

- Clone the repository using this URL `git clone git@github.com:OCHIENGDAVIS/pols-with-datastructures.git`
- `CD` into the cloned repo
- Create a virtual environment  using python 3.7 `virtualenv env  --python=python3.7`
- Activate the virtaul environment `source env/bin/activate` on Linux/Mac or `source env/Scripts/activate` on windows
- Install the requirements `pip install -r requirements.txt`
- Run the application server using the command ` python run.py `

# Running Tests

- Do `pytest --cov=app `

# Endpoints

| Endpoint       | Functionality         | 
| ------------- |:-------------
| POST localhost:5000/api/v1/parties    | Create a political party |
| GET localhost:5000/api/v1/parties/<party_id>     | Fetch a particular political party record   |
| GET localhost:5000/api/v1/parties | Fetch all political parties records      |
| PATCH localhost:5000/api/v1/parties/<party_id>/name | Edit the name of a political party      |
| DELETE localhost:5000/api/v1/parties/<party_id>  | Delete a specific political party    |
| POST localhost:5000/api/v1/offices | Create a political office     |
| GET localhost:5000/api/v1/offices | Fetch all political offices records      |
| GET localhost:5000/api/v1/offices<office_id> | Fetch a specific  political office records      |

# Heroku Application

[Acces the app here](https://pols-with-datastructures.herokuapp.com/api/v1/parties)


# Authors

Davis Ochieng



