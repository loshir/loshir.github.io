# memory_collection.py

MEMORY_COLLECTION = {
    "": {
        "start": 8758, 
        "end": 8800,
        "description": ""
    },
    
    "": {
        "start": 9200, 
        "end": 9250,
        "description": ""
    },
    
    "": {
        "start": 8900, 
        "end": 8930,
        "description": ""
    },
    
    "": {
        "start": 9000, 
        "end": 9040,
        "description": ""
    },
    
    "": {
        "start": 8820, 
        "end": 8850,
        "description": ""
    },
    
    "": {
        "start": 9100, 
        "end": 9130,
        "description": ""
    },
    
    "": {
        "start": 9300, 
        "end": 9340,
        "description": ""
    }
}

# Helper function to get a random memory
import random

def get_random_memory():
    memory_name = random.choice(list(MEMORY_COLLECTION.keys()))
    return memory_name, MEMORY_COLLECTION[memory_name]

def get_memory_by_name(name):
    return MEMORY_COLLECTION.get(name)

def get_all_memory_names():
    """Get list of all memory names"""
    return list(MEMORY_COLLECTION.keys())
