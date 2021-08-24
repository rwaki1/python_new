import os, json
import pandas as pd
from hamcrest.library import collection
import unittest


def data_load(self):
    studentsList = []
    file_names = ['a.json']

    #for file_name in file_names:
        with open(file_names) as f:
            studentDict = json.loads(file_names)
            print(studentDict)
            studentsList.append(file_names)
            print("Printing each JSON Decoded Object")
            for student in studentsList:
                print(student["firstName"], student["lastName"], student["gender"], student["age"],student["address"]["streetAddress"]["city"]["state"]["postalCode"],student["phoneNumbers"]["type"]["number"])
            #file_data = json.load(f)  # load data from JSON to dict
            #for k, v in file_data.items():  # iterate over key-value pairs
                #collection.insert_one(v)  # your collection object here