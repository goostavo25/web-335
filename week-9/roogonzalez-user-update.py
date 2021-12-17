#
#=======================================================
# Title: Assignment 9.3 Updating and deleting documents
# Author: Professor Krasso
# Modified by: Gustavo Roo Gonzalez
# Date: 16 December 2021
# Description: Updating and deleting documents
#=======================================================
#

# Imports
from pymongo import MongoClient
import pprint

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# Update user email from users collection using the update_one() method
db.users.update_one(
    {"employee_id": "9876543"},
    {
        "$set": {
            "email": "groogonzalez@my365.bellevue.edu"
        }
    }
)

# Query the users collection using find_one() method
pprint.pprint(db.users.find_one({"employee_id": "9876543"}))