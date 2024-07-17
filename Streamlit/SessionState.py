import streamlit as st
import pandas as pd

#sreamlit framework
st.title("Learning StreamLit")

# here num_rows acts as global variable thats gonna maintain its state even after the application has restarted
if "num_rows" not in st.session_state:
    st.session_state['num_rows'] =2
    st.session_state['category']='year' 
    


df = pd.read_csv("Streamlit/annual-enterprise.csv")


increment = st.button('Show more columns')
if increment:
     st.session_state['num_rows']+=1

decrement = st.button('Show fewer columns')
if decrement:
     st.session_state['num_rows']-=1


st.table(df.head(st.session_state['num_rows']))
st.write(st.session_state['num_rows'])
########### Learn to use call backs ##################

types = ['year', 'units', "address"]

def handle_Click_via_button(newType):
     #st.write(f'newtype In handle click={newType}')
     st.session_state['category'] = newType

def handle_via_radio_button():
  st.session_state['category'] = type_col
   

st.selectbox(label='Select your column', options=st.session_state['category'])
type_col=st.radio(label ='what do u wana see in the select box',on_change=handle_via_radio_button,options=types, key='my_radio')


st.button('Change',on_click=handle_Click_via_button, args=[type_col])







