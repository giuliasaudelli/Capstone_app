import streamlit as st
import datetime

#test

st.title("PrediShown")

st.date_input("data della visita", datetime.date(2019, 7, 6))


st.toggle('Prima visita')

st.date_input("data di prenotazione", datetime.date(2019, 7, 6))

st.time_input('ora della visita', datetime.time(8, 45))

option1 = st.selectbox(
    'sede della visita',
    ('Saint Bon', 'Navigli', 'Bicocca', 'Rho'))

option2 = st.selectbox(
    'sesso',
    ('Femmina', 'Maschio'))

title = st.text_input('Codice Fiscale', 'SDLGLI99M488A')

option3 = st.selectbox(
    'Tipo di esame',
    ('testacollo', 'torace'))

start_color, end_color = st.select_slider(
    'grado di urgenza',
    options=['1', '2', '3', '4'],
    value=('1', '4'))

option4 = st.selectbox(
    'metodo di pagamento',
    ('S.S.N.', 'Fondi Plus', 'Solventi assimilati', 'CDI check'))
