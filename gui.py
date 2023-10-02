import streamlit as st
import datetime
import config
import utils
import panel as pn
from PIL import Image


prob=0
prob_age=0
prob_hour=3
prob_lead_time=0
prob_priority=0
prob_payment_method=0

image = Image.open('C:\\Users\\Tesista\\Documents\\Capstone_app\\capstone.jpg')



st.markdown("# _:orange[PrediShown]_")

#st.title("_:orange[PrediShown]_")
#st.set_page_config(page_title='PrediShown')

# pn.extension()

# template = pn.template.FastListTemplate(
#     sidebar=["# Sidebar Column"],
#     main=["# Main Column"],
#     header=["# Header Column"],
#     sidebar_width=800
# )

# template.servable()

st.header("Appointment Information")
st.image(image,width=100)
c1, c2 = st.columns(2)
with c1:
    appointment_date = st.date_input("***Date of the appointment:***",                              
                                datetime.date.today(),
                                format="DD/MM/YYYY"),
with c2:
    appointment_time = st.time_input("***Time of the appointment:***",
                                     datetime.time(8,00))
    if appointment_time<datetime.time(9,00) and appointment_time>=datetime.time(7,30):
        prob_hour=1.5
    elif appointment_time<datetime.time(13,00) and appointment_time>=datetime.time(15,00):
        prob_hour=1.5
    elif appointment_time<datetime.time(17,30) and appointment_time>=datetime.time(18,30):
        prob_hour=1.5
    #st.write(prob_hour)

                                     

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


if lead_time<90 and lead_time>=0:
    prob_lead_time=3
elif lead_time<180 and lead_time>=91:
    prob_lead_time=2.5
elif lead_time<270 and lead_time>=181:
    prob_lead_time=2
elif lead_time>=270:
    prob_lead_time=0

#st.write(prob_lead_time)
    
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
if priority == 'U':
    prob_priority=3
elif priority == 'S':
    prob_priority=2.8
elif priority == 'D':
    prob_priority=2.5
elif priority == 'P':
    prob_priority=2
#st.write(prob_priority)

payment_method = st.selectbox('***Payment method***',
                              config.payment_methods)

if payment_method == 'S.S.N.':
    prob_payment_method=3
elif payment_method == 'Fondi Plus':
    prob_payment_method=2.8
elif payment_method == 'Solventi assimilati':
    prob_payment_method=2.8
elif payment_method == 'CDI check':
    prob_payment_method=2.5

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
    age=30

if age<18 and age>=0:
    prob_age=3
elif age<30 and age>=19:
    prob_age=2.5
elif age<65 and age>=31:
    prob_age=3
elif age>=65:
    prob_age=2.8

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
    
    st.write('Computing probability ...')
    prob=round((prob_hour+prob_payment_method+prob_age+prob_lead_time+prob_priority)/15*100)
    utils.compute_probabilty(prob)
    st.progress(prob)



