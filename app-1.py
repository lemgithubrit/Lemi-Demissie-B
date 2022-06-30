import streamlit as st 
#header
st.set_page_config(page_title="Wabepage", page_icon=":tada:", layout="wide")
st.title("Engineering Properties of Ethiopian Grains Crops")
st.write("Five major cereals (Teff, Wheat, Maize, Sorghum and Barley)")
st.write("-----------") 
#subheader
with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
      st.header("Available Data")   
st.subheader("A.Physical Properties ")
st.write("(Size, Shape, Roundness,  Sphercity, Volume, Bulk Density, Solid Density, Porosity, Shrinkage, Color and Appearance and Moisture Content)")
import streamlit as st
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Bulk Desinty': [20, 20, 30, 40,50],
  'Angle of Repose':[10, 20, 40, 50,60],
  'Porocity': [10, 20, 40, 50,70],
  'Roundness': [10, 20, 40, 50,60],
  'Coeffincient of Resistuttion': [1, 2, 3, 4,5],
  'Coefficient of Friction': [10, 20, 30, 40,50],
  'Roundness':[10, 20, 40, 50,60],
  'Sphericity': [10, 20, 40, 50,55]
})
st.table(df)
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
st.subheader("B.Flow Properties ")  
import streamlit as st
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Segregation': [20, 20, 30, 40,50],
  'Velocity':[10, 20, 40, 50,60],
  'Impact Force': [10, 20, 40, 50,70],
  'Funel Flow': [10, 20, 40, 50,60],
  'Silo Dicharge': [1, 2, 3, 4,5]
}) 
st.table(df)  
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
st.subheader("C.Segregation Properties ")  
import streamlit as st
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Segregation': [245, 2098, 300, 450,550],
  'Velocity':[10, 210, 420, 540,620],
  'Impact Force': [130, 240, 460, 560,720],
  'Funel Flow': [180, 280, 420, 510,630],
  'Silo Dicharge': [122, 233, 356, 456,511]
}) 
st.table(df) 
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
#sidenes 
st.sidebar.title("Option")
text=st.sidebar.text_area("Write Comment Here")
st.write(text)
button1=st.sidebar.button("Submit Text")
date = st.sidebar.date_input("Text Here")
uploaded_files=st.sidebar.file_uploader("Chose a csv file",accept_multiple_files=True)
for uploaded_file in uploaded_files:
      bytes_data=uploaded_file.read()
      st.write("filename:",uploaded_file.name)
      st.write(bytes_data)
#add file
st.write("##")
st.write("---") 
st.subheader("Registration")
frist,second,last=st.columns(3)
frist.text_input("Frist Name")
second.text_input("Middle Name")
last.text_input("Last Name")
email,mob=st.columns([3,1])
email.text_input("Email")
mob.text_input("Mob Number")
user,pw,pw2=st.columns(3)
user.text_input("Username")
pw.text_input("password",type="password")
pw2.text_input("Retype your password",type="password")
button1=st.button("Submit")
st.write("---") 
st.write('Developer Lemi Demissie PhD student at Adama Science and Technology University')


