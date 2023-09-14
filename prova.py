import streamlit as st
import datetime

#test

st.title("PrediShown")

st.date_input("Date of the medical appointment", datetime.date(2019, 7, 6))


firstvisit=st.toggle('First visit')

reservation_date=st.date_input("Reservation date", datetime.date(2019, 7, 6))

appointment_time=st.time_input('Appointment time', datetime.time(8, 45))

medicalcenter = st.selectbox(
    'Location of the medical centre',
    ('--- SELECT ---', 'Saint Bon', 'Navigli', 'Bicocca', 'Rho'))

gender = st.selectbox(
    'Gender',
    ('--- SELECT ---', 'Female', 'Male'))

fiscalcode = st.text_input('Fiscal code', '--- INSERT HERE ---')

examination_type = st.selectbox(
    'Type of medical examination',
    ('--- SELECT ---', 'Spine', 'Thorax', 'Limbs'))

start_color, end_color = st.select_slider(
    'Priority level',
    options=['U', 'B', 'D', 'P'],
    value=('U', 'B'))

st.caption('Legend:')
st.caption(' U - Urgent, within 24h')
st.caption('S - Short-term, within 10 days')
st.caption('D - Deferrable, within 30 days')
st.caption('P - Programmable, within 90 days')

payment_method = st.selectbox(
    'Payment method',
    ('--- SELECT ---', 'S.S.N.', 'Fondi Plus', 'Solventi assimilati', 'CDI check'))

