import streamlit as st
import pickle
import pandas as pd

from PIL import Image
im = Image.open("pascal-meier-of2bV2tO3CA-unsplash.jpg")
st.image(im, width = 600, caption = "GD")

df = pd.read_csv('model_son.csv')

html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Churn Prediction ML App (Demo) </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.sidebar.title('Churn Probability of a Single Customer')

if st.checkbox("Churn Probability of Randomly Selected Customers"):
    st.markdown("## How many customers to be selected randomly?")
    nr = st.selectbox("Please select the number of customers", [1, 10, 20, 30, 40, 50, 100])
    if st.button("Analyze"):
        st.success(f"The Churn Probability of Randomly Selected {nr} Customers")
        st.dataframe(df.sample(n = nr))

if st.checkbox("Top Customers to Churn"):
    st.markdown("## How many customers to be selected?")
    nr2 = st.selectbox("Please select the number of customers", [1, 10, 20, 30, 40, 50, 100])
    if st.button("Show"):
        st.success(f"Top {nr2} Customers to Churn")
        st.dataframe(df.sort_values("Churn Probability", axis=0, ascending=False).head(nr2))    
    
if st.checkbox("Top Loyal Customers"):
    st.markdown("## How many customers to be selected?")
    nr3 = st.selectbox("Please select the number of customers", [1, 10, 20, 30, 40, 50, 100])
    if st.button("Get"):
        st.success(f"Top {nr3} Loyal Customers")
        st.dataframe(df.sort_values("Churn Probability", axis=0, ascending=True).head(nr3))
    

    
tenure=st.sidebar.slider("Number of months the customer has stayed with the company (tenure)", 1, 72, step=1)
MonthlyCharges=st.sidebar.slider("The amount charged to the customer monthly", 0,100, step=5)
TotalCharges=st.sidebar.slider("The total amount charged to the customer", 0,5000, step=10)
Contract=st.sidebar.selectbox("The contract term of the customer", ('Month-to-month', 'One year', 'Two year'))
OnlineSecurity=st.sidebar.selectbox("Whether the customer has online security or not", ('No', 'Yes', 'No internet service'))
InternetService=st.sidebar.selectbox("Customer’s internet service provider", ('DSL', 'Fiber optic', 'No'))
TechSupport=st.sidebar.selectbox("Whether the customer has tech support or not", ('No', 'Yes', 'No internet service'))


def single_customer():
    my_dict = {"tenure" :tenure,
        "OnlineSecurity":OnlineSecurity,
        "Contract": Contract,
        "TotalCharges": TotalCharges ,
        "InternetService": InternetService,
        "TechSupport": TechSupport,
        "MonthlyCharges":MonthlyCharges}
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample

columns = ['tenure', 'MonthlyCharges', 'TotalCharges', 'OnlineSecurity_No',
       'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
       'InternetService_DSL', 'InternetService_Fiber optic',
       'InternetService_No', 'TechSupport_No',
       'TechSupport_No internet service', 'TechSupport_Yes',
       'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year']

df_h = single_customer()
df_h = pd.get_dummies(df_h).reindex(columns = columns, fill_value = 0)

model = pickle.load(open("model_son.pkl", "rb"))

from decimal import Decimal

if st.sidebar.button("Submit"):
    result = (model.predict_proba(df_h))[0]
    st.sidebar.success(f"Churn Probability of Selected Customer is {(result)*100} %")  
    