import re
import config
import streamlit as st
import json
import random

def check_fiscal_code(fiscal_code):
    '''
    check if the fiscal code inserted is valid
    '''
    pattern = re.compile(config.fiscal_code_pattern)
    match = bool(pattern.match(fiscal_code))
    return match



def get_age_form_fiscal_code(fiscal_code, appointment_date):
    '''
    Given the fiscal code and appointment date estimate the patient age
    (not precise)
    '''
    MIN_AGE_MRI = 6
    
    year = int(fiscal_code[6:8])
    year_options = [1900 + year , 2000 + year]
    
    age_options = [appointment_date[0].year -i for i in year_options]
    
    if age_options[1] < MIN_AGE_MRI:
        return age_options[0]
    
    return age_options[1]

    
def get_sex_from_fiscal_code(fiscal_code):
    '''
    Given a fiscal code return the sex 
    '''
    number = int(fiscal_code[9:11])
    
    if number < 32:
        return "Male"
    return "Female"


def check_date_validity(appointment_date, booking_date):
    '''
    Check if the booking date is before the appointment date
    '''
    time_distance = appointment_date[0] - booking_date
    days_distance = time_distance.days
    
    return days_distance
        

def save_data(appointment_date,
              appointment_time,
              first_visit,
              booking_date, 
              lead_time,
              appointment_location, 
              exam_type, 
              priority, 
              payment_method,
              age,
              sex):
    '''
    Save data in a json file
    '''
    d = {
        'appointment_date': appointment_date[0],
        'appointment_time': appointment_time,
        'first_visit': first_visit,
        'booking_date': booking_date,
        'lead_time': lead_time,
        'appointment_location': appointment_location,
        'exam_type': exam_type,
        'priority': priority,
        'payment_method': payment_method,
        'age': age,
        'sex': sex
    }
    
    with open("data.json", "w") as outfile:
        json.dump(d, outfile, indent=4, sort_keys=True,  default=str)
        
def compute_probabilty(probabilità):
    '''
    Load the data and compute the probability
    (for the moment is random)
    '''
    with open("data.json", "r") as f:
        data = json.load(f)
        
    #st.markdown(f'# Probability: {probabilità} %')