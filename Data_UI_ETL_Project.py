# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import json
# import plotly.express as px
#
#
# #Display the the header
# st.header("Pandas Data to PSQL Database Connection ")
# # Reading the Csv File
# csv_loc = st.text_input('Enter CSV File Location')
# if len(csv_loc)>0:
#     df_csv=pd.read_csv(csv_loc)
#     df_csv.columns = df_csv.columns.str.replace(" ","")
#     st.write(df_csv)
# else:
#     st.write("Enter the location for the CSV Path")
#
# #Readin the Json File
# json_loc = st.text_input('Enter Json  File Location')
# if len(json_loc)>0:
#     with open(json_loc,'r') as f:
#         data = json.loads(f.read())
#         df_nested_list = pd.json_normalize(data, record_path =['objects'])
#         st.write(df_nested_list)
# else:
#     st.write("Enter the location for the Json Path")
#
# #Reading the Excel File
# excel_loc = st.text_input('Enter Excel File Location')
# if len(excel_loc)>0:
#     df_excel=pd.read_excel(excel_loc)
#     df_excel.columns = df_excel.columns.str.replace(" ","")
#     st.write(df_excel)
# else:
#     st.write("Enter the location for the Excel Path")
#
# if len(df_nested_list)>=0:
#     df = pd.concat([df_nested_list,df_csv,df_excel],axis=0)
#     df.drop(columns = 'ID',inplace = True)
#     df.reset_index(inplace=True,drop = True)
#     df.rename(columns = {'Newcolumn':'Company'}, inplace = True)
#     st.header("Combined Data from all the Three file types")
#     st.write(df)
# else:
#     st.write("Input the Data")
#
#
# st.header("EDA for the given Data")
#
# st.write(df.describe(include="object"))
#
# fig = px.pie(hole=0.2,
# labels=df.JobTitle.values,
# names = df.JobTitle.unique(),
# )
# st.header("Donut Chart")
# st.plotly_chart(fig)

# --------------------------------------------------------------------------------------


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import plotly.express as px

#Display the the header
st.header("Pandas Data to PSQL Database Connection ")
# Reading the Csv File
csv_loc = st.text_input('Enter CSV File Location')
if len(csv_loc)>0:
    df_csv=pd.read_csv(csv_loc)
    df_csv.columns = df_csv.columns.str.replace(" ","")
    st.write(df_csv)
else:
    st.write("Enter the location for the CSV Path")

#Readin the Json File
json_loc = st.text_input('Enter Json  File Location')
try:
    if len(json_loc)>0:
        with open(json_loc,'r') as f:
            data = json.loads(f.read())
            df_nested_list = pd.json_normalize(data, record_path =['objects'])
            st.write(df_nested_list)
    else:
        st.write("Enter the location for the Json Path")
except:
    df_nested_list = pd.read_json(json_loc)
    st.write(df_nested_list)

#Reading the Excel File
excel_loc = st.text_input('Enter Excel File Location')
if len(excel_loc)>0:
    df_excel=pd.read_excel(excel_loc)
    df_excel.columns = df_excel.columns.str.replace(" ","")
    st.write(df_excel)
else:
    st.write("Enter the location for the Excel Path")

if len(df_nested_list)>=0:
    df = pd.concat([df_nested_list,df_csv,df_excel],axis=0)
    # df.drop(columns = 'ID',inplace = True)
    # df.reset_index(inplace=True,drop = True)
    # df.rename(columns = {'Newcolumn':'Company'}, inplace = True)
    st.header("Combined Data from all the Three file types")
    st.write(df)
else:
    st.write("Input the Data")


st.header("EDA for the given Data")

st.write(df.describe(include="object"))
# df=df.sort_values("")
fig = px.bar(df,x='ID',y='JobTitle',
labels=df.ID.unique
)
st.header("Donut Chart")
st.plotly_chart(fig)
