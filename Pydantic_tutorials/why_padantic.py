from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Define a Pydantic model named 'Patient' that inherits from BaseModel.
# This model will define the structure and validation rules for patient data.
class Patient(BaseModel):
    # 'name' field:
    # - Annotated[str, ...] indicates type hints with Pydantic's Field metadata.
    # - Field provides validation and documentation:
    #   - max_length=50: Ensures the name is no longer than 50 characters.
    #   - title: Provides a short, human-readable title.
    #   - description: Offers a longer explanation.
    #   - examples: Provides example values for documentation.
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Sameer', 'Ashwini'])]
    
    # 'email' field:
    # - EmailStr is a Pydantic type that automatically validates if the string is a valid email address.
    email: EmailStr
    
    # 'linkedin_url' field:
    # - AnyUrl is a Pydantic type that automatically validates if the string is a valid URL.
    linkedin_url: AnyUrl
    
    # 'age' field:
    # - int specifies the type as integer.
    # - Field(gt=0, lt=120) enforces that age must be greater than 0 and less than 120.
    age: int = Field(gt=0, lt=120)
    
    # 'weight' field:
    # - Annotated[float, ...] indicates type hints with Field metadata.
    # - Field(gt=0, strict=True) enforces:
    #   - gt=0: Weight must be greater than 0.
    #   - strict=True: Ensures the input type is exactly float, preventing implicit conversions (e.g., from int).
    weight: Annotated[float, Field(gt=0, strict=True)]
    
    # 'married' field:
    # - Annotated[bool, ...] indicates type hints with Field metadata.
    # - Field(default=None, description='...') sets a default value of None if not provided
    #   and provides a description.
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    
    # 'allergies' field:
    # - Optional[List[str]] means it can be a list of strings or None.
    # - Field(default=None, max_length=5) sets a default of None and allows max 5 items in the list.
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    
    # 'contact_details' field:
    # - Dict[str, str] specifies that it must be a dictionary where both keys and values are strings.
    contact_details: Dict[str, str]
    
# Define a function to update patient data.
# It takes an argument 'patient' which is type-hinted as a 'Patient' object.
# Pydantic will ensure 'patient' conforms to the Patient model's structure.
def update_patient_data(patient: Patient):
    # Access and print specific attributes of the validated patient object.
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

# Create a dictionary with patient information.
# CORRECTED: 'allergies' is now a list of strings.
patient_info = {'name':'Ashwini', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1225', 'age': '30', 'weight': 58,'allergies':['eating banana'],'contact_details':{'phone':'2353462'}}

# Create an instance of the 'Patient' model using the 'patient_info' dictionary.
# Pydantic validates the data against the 'Patient' model's rules during instantiation.
# If validation fails, it will raise an error.
patient1 = Patient(**patient_info)

# Call the function to update patient data, passing the validated 'patient1' object.
update_patient_data(patient1)