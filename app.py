import streamlit as st
import pyperclip

# Streamlit Page Config
st.set_page_config(page_title="Unit Converter", layout='centered')
st.title("🔄 Unit Converter")
st.write("Convert units easily")

# Conversion Data
unit_categories = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Foot": 3.28084},
    "Weight": {"Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274},
    "Temperature": "temperature",
    "Speed": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Mile/Hour": 2.23694},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400}
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

# UI Layout
category = st.selectbox("Select Category", list(unit_categories.keys()))

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"] if category == "Temperature" else list(unit_categories[category].keys())
from_unit = st.selectbox("Convert from", temperature_units)
to_unit = st.selectbox("Convert to", temperature_units)

value = st.number_input("Enter Value", min_value=0.0, step=0.1)

# Conversion Logic
if st.button("Convert"):
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = value * (unit_categories[category][to_unit] / unit_categories[category][from_unit])
    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    if st.button("Copy Result"):
        pyperclip.copy(f"{value} {from_unit} = {result:.4f} {to_unit}")
        st.toast("Copied to clipboard! ✅")

st.write("💡 Convert between different units instantly!")
