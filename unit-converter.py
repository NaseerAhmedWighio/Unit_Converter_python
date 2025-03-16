import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversations={
        "Meters_Kilometers": 0.001,
        "Kilometers_Meters": 1000,
        "Grams_Kilograms": 0.001,
        "Kilograms_Grams": 1000
    }

    key = f"{unit_from}_{unit_to}" 

    if key in conversations:
        conversion = conversations[key]
        return value * conversion
    else:
        return "Conversion not found"
    
st.title("Unit Converter")

value = st.number_input("Enter the value")
unit_from= st.selectbox("Convert from:",["Meters","Kilometers","Gram","Kilograms"])
unit_to= st.selectbox("Convert to:",["Meters","Kilometers","Grams","Kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Total {unit_to}: {result}")