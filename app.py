# Install Streamlit by running this command in the terminal: "pip install streamlit"
import streamlit as st

st.set_page_config(page_title="Simple Unit Converter", page_icon="🔄")
st.title("🔄 Simple Unit Converter")

# Length Converter
st.header("📏 Length Converter")

length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Feet": 3.28084}
length_input = st.number_input("Enter length:", min_value=0.0)
length_from = st.selectbox("Convert from:", list(length_units.keys()))
length_to = st.selectbox("Convert to:", list(length_units.keys()))

if st.button("Convert Length"):
    result = length_input * (length_units[length_to] / length_units[length_from])
    st.success(f"{length_input} {length_from} = {result:.2f} {length_to}")

# Temperature Converter
st.header("🌡 Temperature Converter")

temp_input = st.number_input("Enter temperature:")
temp_from = st.selectbox("Convert from:", ["Celsius", "Fahrenheit"])
temp_to = st.selectbox("Convert to:", ["Celsius", "Fahrenheit"])

def convert_temp(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius":
        return (value * 9/5) + 32  
    else:
        return (value - 32) * 5/9  

if st.button("Convert Temperature"):
    temp_result = convert_temp(temp_input, temp_from, temp_to)
    st.success(f"{temp_input}° {temp_from} = {temp_result:.2f}° {temp_to}")

# Footer
st.write("---")
st.write("Made with ❤️ by Tarfeeha Hussain")
