## import the libraries
import streamlit as st
from PIL import Image
import joblib
import numpy as np

## loading the ann model
mul_reg = joblib.load('eu_wage_model.h5')

## creat a function of prediction
def wage_prediciton(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)

    prediction = mul_reg.predict(input_reshape)
    print(prediction)

    # predict
    if (prediction > 0):
        return prediction
    else: 
        return prediction

    
def main():
    ## set page configuration 
    st.set_page_config(page_title='EU Employee Wage Estimator', layout='wide')

    ## add image
    image = Image.open(r'EU.jpg')
    st.image(image, use_column_width=False)

    ## add page title and content
    st.title('EU Employee Wage Estimator Using Linear Regression')
    st.write('Enter your demographic information to get estimated employee wage')
    
    ## variable inputs
    FULL = st.number_input('Is the expected contract type full-time? Otherwise, part-time | yes or no | yes = 1 and no = 0:',min_value=0,max_value=1 ,step=1)
    MARRIED = st.number_input("Is the person married? | yes or no | yes = 1 and no = 0:",min_value=0, step=1, max_value=1)
    PH010 = st.number_input("Rate the person's health on a scale from 1 to 5 | 1 = Very good, 2 = Good, 3 = Fair, 4 = Bad and 5 = Very Bad:",min_value=1, step=1, max_value=5)
    PH020 = st.number_input('Does the person suffer from any chronic (long-standing) illness or condition? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PE040 = st.number_input('Highest education level attained | 1 = Pre-primary education, 2 = Primary education, 3 = Lower secondary education, 4 = Secondary education, 5 = Post-secondary non tertiary education, 6 = First stage of tertiary education and 7 = Second stage of tertiary education:',min_value=1, step=1, max_value=7)
    PB150 = st.number_input('Is the person male? Otherwise, female | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_AT = st.number_input('Is the person working in Austria? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_BE = st.number_input('Is the person working in Belgium? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_CY = st.number_input('Is the person working in Cyprus? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_EE = st.number_input('Is the person working in Estonia? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_EL = st.number_input('Is the person working in Greece? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_ES = st.number_input('Is the person working in Spain? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_FI = st.number_input('Is the person working in Finland? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_FR = st.number_input('Is the person working in France? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_IT = st.number_input('Is the person working in Italy? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_LU = st.number_input('Is the person working in Luxembourg? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_MT = st.number_input('Is the person working in Malta? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_NL = st.number_input('Is the person working in Netherlands? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_SI = st.number_input('Is the person working in Slovenia? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    PB020_SK = st.number_input('Is the person working in Slovakia? | yes or no | yes = 1 and no = 0:',min_value=0, step=1, max_value=1)
    
    ## code for prediction
    predict = ''

    # button for prediction
    if st.button('Predict'):
        predict = wage_prediciton([FULL,MARRIED,PH010,PH020,PE040,PB150,PB020_AT,PB020_BE,PB020_CY,PB020_EE,PB020_EL,PB020_ES,PB020_FI,PB020_FR,PB020_IT,PB020_LU,PB020_MT,PB020_NL, PB020_SI,PB020_SK])

    st.success(predict)

if __name__ == '__main__':
    main()
