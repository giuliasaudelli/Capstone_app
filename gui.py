import streamlit as st
import datetime
import config
import utils

st.title("PrediShown")


st.header("Appointment Information")

c1, c2 = st.columns(2)
with c1:
    appointment_date = st.date_input("***Date of the appointment:***",                              
                                datetime.date.today(),
                                format="DD/MM/YYYY"),
with c2:
    appointment_time = st.time_input("***Time of the appointment:***",
                                     datetime.time(8,00))
                                     

first_visit = st.toggle('***First visit***')

booking_date = st.date_input("***Booking date***",
                             datetime.date.today(),
                             format="DD/MM/YYYY",
                             key=2
                             )

lead_time = utils.check_date_validity(appointment_date, booking_date)
if lead_time < 0:
    st.error("The booking date needs to be before the appointment date", icon="🚨")
else:
    st.info(f"Lead time: {lead_time}")
    
    
c3, c4 = st.columns(2)
with c3:
    appointment_location = st.selectbox('***Location of the appointment:*** ',
                                    config.locations
                                    )
with c4:
    exam_type = st.selectbox('***Type of medical examination***',
                         sorted(config.exams))


priority = st.radio('***Priority level***',
                    config.priorities,
                    captions=['Urgent, within 24h',
                              'Short-term, within 10 days',
                              'Deferrable, within 30 days',
                              'Programmable, within 90 days'])


payment_method = st.selectbox('***Payment method***',
                              config.payment_methods)

st.header("Patient Information")

fiscal_code = st.text_input('***Fiscal code***',
                            value='',
                            max_chars=16,
                            )

is_valid = utils.check_fiscal_code(fiscal_code)
if is_valid:
    age = utils.get_age_form_fiscal_code(fiscal_code, appointment_date)
    sex = utils.get_sex_from_fiscal_code(fiscal_code)
    
    st.info(f"Age: {age}\n ")
    st.info(f"Sex: {sex}")
else:
    st.error("Fiscal Code not valid", icon="🚨")


if st.button('Submit', help='Click the button to comput the probability'):
    utils.save_data(appointment_date,
                    appointment_time,
                    first_visit,
                    booking_date, 
                    lead_time,
                    appointment_location, 
                    exam_type, 
                    priority, 
                    payment_method,
                    age,
                    sex)
    
    st.write('Data saved')
    
    st.write('Computing probability')
    utils.compute_probabilty()
        


