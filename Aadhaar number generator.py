import random

def generate_uid():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

def find_valid_uid():
    while True:
        uid = generate_uid()
        result = validate_uid(uid)
        if result == 0:
            return uid

# Find a valid UID
valid_uid = find_valid_uid()
print("Valid UID:", valid_uid)
