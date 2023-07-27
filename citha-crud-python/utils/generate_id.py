import random
from datetime import datetime

def generate_id(length=6):
    digits = '0123456789'
    id = datetime.now().strftime('%Y%m%d')

    for _ in range(length):
        id += random.choice(digits)

    return id 
