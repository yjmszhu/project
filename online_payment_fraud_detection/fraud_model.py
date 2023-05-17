## import the libraries
import streamlit as st
from PIL import Image
import pickle
import numpy as np

## loading the ann model
with open('fraud_model.pickle', 'rb') as file:
    model_KNN = pickle.load(file)

## creat a function of prediction
def fraud_prediciton(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)

    prediction = model_KNN.predict(input_reshape)
    print(prediction)
    
    # predict
    if (prediction[0] == 0):
        return 'The online payment is not likely to be a fraud.' # 0
    else: 
        return 'The online payment is likely to be a fraud.' # 1
    
def main():
    ## set page configuration 
    st.set_page_config(page_title='Online Payment Fraud Detector', layout='wide')

    ## add image
    image = Image.open(r'fraud_app.jpg')
    st.image(image, use_column_width=False)

    ## add page title and content
    st.title('Online Payment Fraud Detector Using K-Nearest Neighbors Algorithm')
    st.write('Enter your online payment information to get fraud risk evaluation')
    
    ## variable inputs
    step = st.number_input('Time length of online payment by hours:',min_value=0, step=1)
    amount = st.number_input('Amount of online payment:',min_value=0.00, step=0.01)
    oldbalanceOrg = st.number_input('Balance of sender before the transaction:',min_value=0.00, step=0.01)
    oldbalanceDest = st.number_input('Balance of recipient before the transaction:',min_value=0.00, step=0.01)
    type_CASH_IN = st.number_input('Is it a cash-in transaction | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    type_CASH_OUT = st.number_input('Is it a cash-out transaction | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    type_PAYMENT = st.number_input('Is it a payment transaction | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    type_TRANSFER = st.number_input('Is it a transfer transaction | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)

    ## code for prediction
    predict = ''

    # button for prediction
    if st.button('Predict'):
        predict = fraud_prediciton([step,amount,oldbalanceOrg,oldbalanceDest,type_CASH_IN,type_CASH_OUT,type_PAYMENT,type_TRANSFER])

    st.success(predict)

if __name__ == '__main__':
    main()
