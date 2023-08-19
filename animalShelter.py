#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:33:51 2023

@author: blakekemp_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32411
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)  # data should be a dictionary 
                return True
            else:
                raise ValueError("Nothing to save because data parameter is empty")
        except Exception as e:
            raise Exception("Error while creating document: " + str(e))

    # Create method to implement the R in CRUD.
    def read(self, data):
        try:
            if data is not None:
                result = self.collection.find(data)  # Perform the read operation using the find method of the specified collection (self.collection).
                return list(result)  # Return the result as a list
            else:
                raise ValueError("Cannot perform read operation because data parameter is empty")
        except Exception as e:
            raise Exception("Error while reading document: " + str(e))

    # Create method to implement the U in CRUD.
    def update(self, query, update_data):
        try:
            if query is not None and update_data is not None:
                result = self.collection.update_many(query, {'$set': update_data})  # Update multiple documents matching the query with the specified update_data
                return result.modified_count  # Return the number of objects modified in the collection
            else:
                raise ValueError("Cannot perform update operation because query or update_data parameter is empty")
        except Exception as e:
            raise Exception("Error while updating document: " + str(e))

    # Create method to implement the D in CRUD.
    def delete(self, data):
        try:
            if data is not None:
                result = self.collection.delete_many(data)  # Delete multiple documents matching the data
                return result.deleted_count  # Return the number of objects removed from the collection
            else:
                raise ValueError("Cannot perform delete operation because data parameter is empty")
        except Exception as e:
            raise Exception("Error while deleting document: " + str(e))