#
#=======================================================
# Title: Assignment 9.2 Querying and Creating Documents
# Author: Professor Krasso
# Modified by: Gustavo Roo Gonzalez
# Date: 16 December 2021
# Description: Querying and Creating Documents
#=======================================================
#

# Imports
from pymongo import MongoClient
import pprint
import datetime

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# Create new User document
user = {
    "first_name": "Buzz",
    "last_name": "Lightyear",
    "email": "buzz@pixar.com",
    "employee_id": "9876543",
    "date_created": datetime.datetime.utcnow()
}

# Insert new user document
user_id = db.users.insert_one(user).inserted_id

# Output auto-generated user_id
print(user_id)

# Query users collection with find_one() method
pprint.pprint(db.users.find_one({"employee_id": "9876543"}))