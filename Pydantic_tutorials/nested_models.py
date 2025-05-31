from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address # This field is an instance of the Address model

# Create a dictionary for Address data
address_dict = {'city': 'Jalgaon', 'state': 'Maharashtra', 'pin': '425001'}

# Instantiate the Address model with the dictionary data
address1 = Address(**address_dict)

# Create a dictionary for Patient data.
# The 'address' key here holds the already instantiated Address object.
patient_dict = {'name': 'Ashwini', 'gender': 'female', 'age': 35, 'address': address1}

# Instantiate the Patient model with the dictionary data.
# Pydantic will validate all fields, including the nested 'address' model.
patient1 = Patient(**patient_dict)

# Convert the Pydantic model instance 'patient1' into a Python dictionary.
# By calling model_dump() without arguments, all fields will be included.
temp = patient1.model_dump() # Corrected line: Removed the incomplete 'include='

print(type(temp)) # This will now print <class 'dict'>
print(temp) # You can also print the dictionary to see its content