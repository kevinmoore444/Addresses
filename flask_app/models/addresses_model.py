from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Address:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM addresses;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_addresses = []
        for one_row in results:
            this_address_instance = cls(one_row)
            all_addresses.append(this_address_instance)
        return all_addresses


    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO addresses (email)
            VALUES (%(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    


    @staticmethod
    def validator(potential_address):
        is_valid = True
        if not EMAIL_REGEX.match(potential_address['email']): 
            is_valid = False
            flash("Invalid email address!")
        return is_valid