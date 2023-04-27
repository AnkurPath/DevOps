from fastapi import FastAPI
from controller import configuration
from bson.objectid import ObjectId
from schematics.models import Model
from schematics.types import EmailType,StringType




class Customer(Model):
    cust_id = ObjectId()
    cust_email = EmailType(required=True)
    cust_name = StringType(required=True)


# An instance of class User
newuser = Customer()

# funtion to create and assign values to the instanse of class Customer created
def create_user(email, username):
    newuser.cust_id = ObjectId()
    newuser.cust_email  = email
    newuser.cust_name = username
    return dict(newuser)


app=FastAPI()


@app.get('/')
def test_func():
    return {"message":"this is test func"}


#Signup endpoint with Post Method

@app.post("/signup/{email}/{username}")
def addUser(email,username:str):
    user_exists=False
    data=create_user(email,username)
    # Covert data to dict so it can be easily inserted to MongoDB
    dict(data)
    # print(data)

    # Check if an email exists from the colection of users

    if configuration.db.users.find({'cust_email':data['cust_email']}).count()>0:
        user_exists=True
        print("Customer Exists")
        return {"message": "User  Exists"}

    # Checks if an email exists from the collection of users
    elif user_exists == False:
        configuration.db.users.insert_one(data)
        return  {"message":"User Created","email": data['cust_email'], "name": data['cust_name']}