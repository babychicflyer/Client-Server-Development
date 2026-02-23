# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username=None, password=None): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # Connection Variables 
        # 
        USER = username if username else 'aacuser'
        PASS = password if password else 'KellyReinersman'
        HOST = 'localhost' 
        PORT = 27017
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    def get_next_record_number(self):
        """
        Get the next available record number for use in the create method
        Returns:
            int: The next sequential record number
        """
        try:
            last_record = self.database.animals.find_one(
                sort = [("record_number", -1)]
            )
            if last_record and "record_number" in last_record:
                return last_record["record_number"]+1
            else: 
                return 1
        except Exception as e:
            print(f"An error occurred while getting next record number: {e}")
            return 1

    def create(self, data):
        """
        Insert a document into the collection
        Args:
            data (dict): A dictionary containing key/values pairs to insert
        Returns:
            bool: True if successful insert, False otherwise
        """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"An error occurred during insert: {e}")
                return False
        else:
            raise Exception("Nothing to save, data parameter is empty")

    def read(self, query):
        """
        Query documents from the collection using find()
        Args:
            query (dict): A dictionary containing key/value pairs to search for
        Returns:
            list: A list of documents matching the query, or empty list if none
        """
        if query is not None:
            try:
                cursor = self.collection.find(query)
                results = list(cursor)
                return results
            except Exception as e:
                print(f"An error occurred during query: {e}")
                return []
        else:
            raise Exception("Query parameter cannot be empty") 
    
    def update(self, query, update_data):
        """
        Update document(s) in the collection
        Args:
            query (dict): A dictionary containing key/value pairs to identify document(s) to update
            update_data (dict): A dictionary containing key/value pairs to update
        Returns:
            int: The number of documents modified
        """
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Query and update_data parameters cannot be empty")

    def delete(self, query):
        """
        Delete document(s) from the collection
        Args:
            query (dict): A dictionary containing key/value pairs to identify document(s) to delete
        Returns:
            int: The number of documents deleted
        """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            raise Exception("Query parameter cannot be empty")