# Classroom Management System

## Team Info
- Naman Manish Trivedi ([@namanmanish](https://github.com/namanmanish))
- K V Sumanth Reddy ([@sumanthreddy07](https://github.com/sumanthreddy07))


#### Install components
```bash
sudo apt-get update
sudo apt-get install python-pip 
```

#### Setting up Virtual Environment and Install Requirements
```bash
sudo pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```
## Running the server
```bash
cd roombooking
python manage.py runserver
In your web browser go to localhost:8000/user/sign_up
```
## Running the tests
```bash
cd roombooking
python manage.py test book
```
## Faculty scenarios
* A new user can signup and if already a user he/she can login
* Any authanticated user can create a new room booking
* User can view his past bookings and can edit or delete the bookings which are not yet done

## Manager scenarios
* A new user can signup as a manager and if already a user he/she can login
* Any authenticated manager can view all the room bookings, details of the customers and the vacancy status of all the room
* Manager can create new time slots and define the maximum days for an advance booking
* Manager can add a new room
* Manager can delete or edit time slots but the changes to be done only after 'n' days here 'n' is the maximum days for an advance booking
* Manager can edit or delete the time slots only once a day
* These restictions are allpied by keeping in mind the bookings which are already created when these time slots existed
* Due to this different dates may have different time slots
* Faculty, while creating a new booking will choose the date and the time slot will dynamically loaded on the basis of the date chosen

## API
Have created API for creating a new time slot<br/>
url : 'book/api'<br/>
<b>GET</b><br/>
responsedataformat : json<br/>
data : Array of dictionaries containing all the time slots<br/>
<b>POST</b><br/>
requestdataformat : json (as raw data in body of request)<br/>
sample : {"int_time":some_value,"end_time":some_value}<br/>
responsedataformat : json (the object which is created)<br/>

