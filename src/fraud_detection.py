import streamlit as st
import pandas as pd
import joblib

st.markdown("""
    <style>
        .stApp {
            background-color : gray;   
                                                                
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

model =joblib.load("fraud_detection_pipline.pkl")

st.title("Frauder catcher👮🔫??")
st.markdown("please provide the following transaction details if you frauder you must worry 🤫😎💪.")

st.divider()

transaction_type=st.selectbox("Transaction Type",["CASH_OUT","DEBIT","PAYMENT","TRANSFER"])
amount=st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance of sender Account",min_value=0.0,value=5000.0)
newbalanceOrig=st.number_input("New Balance of sender Account",min_value=0.0,value=4000.0)
oldbalanceDest=st.number_input("Old Balance of receiver Account",min_value=0.0,value=2000.0)
newbalanceDest=st.number_input("New Balance of receiver Account",min_value=0.0,value=3000.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig":newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }])
    prediction = model.predict(input_data)[0]

    st.subheader(f"prediction: '{int(prediction)}'")

    if prediction == 0 :
        st.success("Transaction is Legitimate you are safe😎😎💪 !!!!")
    else:st.error("catch you red handed frauder💥❌❌👮👮 !!!!")


