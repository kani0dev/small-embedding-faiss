from faker import Faker 
from faker.providers import profile
import json, csv

fake = Faker()


class Factory:
        @staticmethod
        def generate_profile():

            name = fake.profile().get('name')
            sex = fake.profile().get('sex')
            job = fake.profile().get('job')
            message = fake.text()
            
            profile = {
                   "name" : name,
                   "sex" : sex, 
                   "job" : job, 
                   "message" : message
                }
            return profile


        @staticmethod
        def generate_profile_as_file(num_of_profiles = 10):
            profiles = []
            i =0 
            while i <= num_of_profiles: 
                profiles.append(Factory.generate_profile())
                i+=1

            with open('profiles.json','a') as file:
                    json.dump(profiles,file,indent=5)
                
            return profiles

