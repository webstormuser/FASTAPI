from pydantic import BaseModel

# Define a Pydantic model named 'Address'.
# This model represents the structure for an address.
class Address(BaseModel):
    # 'city' field: Type-hinted as a string.
    city: str
    # 'state' field: Type-hinted as a string.
    state: str
    # 'pin' field: Type-hinted as a string (e.g., postal code).
    pin: str

# Define a Pydantic model named 'Patient'.
# This model represents the structure for patient information,
# and it includes a nested 'Address' model.
class Patient(BaseModel):
    # 'name' field: Type-hinted as a string.
    name: str
    # 'gender' field: Type-hinted as a string with a default value of 'Female'.
    # If not provided during instantiation, 'gender' will default to 'Female'.
    gender: str = 'Female'
    # 'age' field: Type-hinted as an integer.
    age: int
    # 'address' field: This field is of type 'Address' (the Pydantic model defined above).
    # This demonstrates Pydantic's ability to handle nested models,
    # ensuring the 'address' data also conforms to the 'Address' schema.
    address: Address

# Create a dictionary containing data for an Address.
address_dict = {'city': 'Jalgaon', 'state': 'Maharashtra', 'pin': '425001'}

# Instantiate the 'Address' model. Pydantic validates 'address_dict' against the 'Address' schema.
address1 = Address(**address_dict)

# Create a dictionary containing data for a Patient.
# Notice that 'gender' is not included here, so the default value 'Female' from the model will be used.
# The 'address' key's value is the 'address1' (Address model instance) created above.
patient_dict = {'name': 'Ashwini', 'age': 35, 'address': address1}

# Instantiate the 'Patient' model.
# Pydantic validates 'patient_dict' against the 'Patient' schema,
# which includes validating the nested 'address' object.
patient1 = Patient(**patient_dict)

# Convert the Pydantic model instance 'patient1' into a Python dictionary.
# exclude_unset=True: This argument tells model_dump() to only include fields
# that were explicitly set when the model instance was created,
# excluding fields that took their default values.
# In this case, 'gender' has a default value ('Female') and was not explicitly set in 'patient_dict',
# so it will be excluded from the resulting dictionary 'temp'.
temp = patient1.model_dump(exclude_unset=True)

# Print the resulting dictionary.
# This will show 'name', 'age', and 'address', but 'gender' will be absent.
print(temp)
# Print the type of 'temp', which will be <class 'dict'>.
print(type(temp))