import streamlit as st
import joblib
import time
def main():
    html_temp='''cd
    <head><title>Insurance</title></head>
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-aling:center>Health Insurance Cost Prediction
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = joblib.load('insurance_pred') # load the model
    
    p1 = st.slider("Enter Your Age", 18, 100)
    
    s1 = st.selectbox("Sex", ("Male", "Female"))
    if s1 == "Male":
        p2 = 1
    else:
        p2 = 0

    p3 = st.number_input("Enter Your BMI Value")
    p4 = st.slider("Enter Number of Children", 0, 4) 
    
    s2 = st.selectbox("Smoker", ("Yes", "No"))
    if s2 == "Yes":
        p5 = 1
    else:
        p5 = 0
        

    s3 = st.selectbox("Region", ('southwest', 'southeast', 'northwest', 'northeast'))
    if s3=='southwest':
        p6=1
    elif s3=='southeast':
        p6=2
    elif s3=='northwest':
        p6=3
    elif s3=='northeast':
        p6=4
    
    if st.button('Predict'):
        prediction = model.predict([[p1, p2, p3, p4, p5, p6]])
        with st.spinner("Processing..."):
            time.sleep(1)
        st.success('Insurance Amount is {} '.format(round(prediction[0], 2)))    
    
if __name__ == '__main__':
    main()

