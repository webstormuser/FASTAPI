from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

# Define a Pydantic model named 'Patient' that inherits from BaseModel.
# This model will define the structure and validation rules for patient data.
class Patient(BaseModel):
    # 'name' field: Type-hinted as a string. Pydantic will validate this.
    name: str
    
    # 'email' field:
    # - EmailStr is a Pydantic type that automatically validates if the string is a valid email address.
    email: EmailStr
    
    # 'age' field: Type-hinted as an integer. Pydantic will coerce/validate this.
    age: int
    
    # 'weight' field: Type-hinted as a float, representing weight in kilograms.
    weight: float # kg
    
    # 'height' field: Type-hinted as a float, representing height in meters.
    height: float # mtr
    
    # 'married' field: Type-hinted as a boolean.
    married: bool
    
    # 'allergies' field:
    # - List[str] specifies that it must be a list containing only strings.
    allergies: List[str]
    
    # 'contact_details' field:
    # - Dict[str, str] specifies that it must be a dictionary where both keys and values are strings.
    contact_details: Dict[str, str]

    # 'bmi' is a computed field.
    # @computed_field decorator marks this method as a property that will be
    # computed when the model instance is created or accessed.
    # @property decorator allows accessing 'bmi' as an attribute (e.g., patient.bmi)
    # rather than a method (patient.bmi()).
    # -> float indicates that this computed field will return a float.
    @computed_field
    @property
    def bmi(self) -> float:
        # Calculate Body Mass Index (BMI) using the weight and height attributes of the patient.
        # The formula is weight / (height^2).
        # round() is used to round the BMI to two decimal places.
        bmi = round(self.weight / (self.height**2), 2)
        return bmi

# Define a function to update and display patient data.
# It takes an argument 'patient' which is type-hinted as a 'Patient' object.
# Pydantic ensures that the 'patient' object passed here conforms to the Patient model's structure.
def update_patient_data(patient: Patient):
    # Access and print various attributes of the validated patient object.
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    # Access and print the computed 'bmi' field.
    print('BMI', patient.bmi)
    print('updated')

# Create a dictionary with sample patient information.
# Pydantic will automatically validate and coerce types (e.g., 'age' from string to int)
# when creating the Patient instance.
patient_info = {
    'name': 'Ashwini',
    'email': 'abc@icici.com',
    'age': '65', # Pydantic will convert this string to an integer
    'weight': 75.2,
    'height': 1.72,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '2353462', 'emergency': '235236'}
}

# Create an instance of the 'Patient' model using the 'patient_info' dictionary.
# During this step, Pydantic performs all validations and instantiates the object.
# If any data does not conform to the model's rules, a ValidationError will be raised.
patient1 = Patient(**patient_info)

# Call the function to process and display the validated patient data.
update_patient_data(patient1)