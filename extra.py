import random 
import os

def get_random_file(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files: return None
    random_file = random.choice(files)
    return random_file