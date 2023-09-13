import streamlit as st
import datetime

st.title("PrediShown")

st.date_input("Date of the medical appointment", datetime.date(2019, 7, 6))


st.toggle('First visit')

st.date_input("Reservation date", datetime.date(2019, 7, 6))

st.time_input('Appointment time', datetime.time(8, 45))

option1 = st.selectbox(
    'Location of the medical centre',
    ('--- SELECT ---', 'Saint Bon', 'Navigli', 'Bicocca', 'Rho'))

option2 = st.selectbox(
    'Gender',
    ('--- SELECT ---', 'Female', 'Male'))

title = st.text_input('Fiscal code', '---INSERT HERE---')

option3 = st.selectbox(
    'Type of medical examination',
    ('--- SELECT ---', 'Spine', 'Thorax', 'Limbs'))

start_color, end_color = st.select_slider(
    'Emergency degree',
    options=['1', '2', '3', '4'],
    value=('1', '4'))

option4 = st.selectbox(
    'Payment method',
    ('--- SELECT ---', 'S.S.N.', 'Fondi Plus', 'Solventi assimilati', 'CDI check'))
