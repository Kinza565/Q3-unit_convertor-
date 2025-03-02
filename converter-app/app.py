import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    conversions = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084}
    return value if from_unit == to_unit else value * (conversions[to_unit] / conversions[from_unit])


def convert_weight(value, from_unit, to_unit):
    conversions = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462}
    return value if from_unit == to_unit else value * (conversions[to_unit] / conversions[from_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversions = {
        ("Celsius", "Fahrenheit"): (value * 9/5) + 32,
        ("Fahrenheit", "Celsius"): (value - 32) * 5/9,
        ("Celsius", "Kelvin"): value + 273.15,
        ("Kelvin", "Celsius"): value - 273.15,
        ("Fahrenheit", "Kelvin"): (value - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): (value - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), value)


# Custom CSS Styling
st.markdown("""
    <style>
        body { background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%); font-family: 'Poppins', sans-serif; }
        .stButton>button { background-color: #ff5e57; color: white; border-radius: 30px; padding: 14px; transition: 0.3s; }
        .stButton>button:hover { background-color: #ff1c00; }
        .stTextInput>div>input, .stSelectbox>div>div>input { border: 1px solid #ff5e57; border-radius: 30px; padding: 14px; }
        .stAlert, .stSuccess { padding: 12px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("""<h1 style='text-align: center; color: #ff5e57;'>🔢 Unit Converter</h1>""", unsafe_allow_html=True)
st.markdown("""<h3 style='text-align: center;'>Convert Length, Weight, or Temperature with Ease</h3>""", unsafe_allow_html=True)

# Conversion Categories
category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])
categories = {"Length": ["Meters", "Kilometers", "Miles", "Feet"], "Weight": ["Kilograms", "Grams", "Pounds"], "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]}

from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])
value = st.number_input("Enter Value", min_value=0.0 if category != "Temperature" else -273.15, format="%.2f", step=0.01)

if value <= 0 and category != "Temperature":
    st.error("Please enter a positive value greater than zero.")

if "results" not in st.session_state:
    st.session_state.results = []

if st.button("Convert"):
    result = {
        "Length": convert_length,
        "Weight": convert_weight,
        "Temperature": convert_temperature
    }[category](value, from_unit, to_unit)

    result_text = f"✅ {value} {from_unit} = **{result:.4f} {to_unit}**"
    st.success(result_text)
    st.session_state.results.append(result_text)

if st.session_state.results:
    st.markdown("### 🔄 Conversion History")
    for res in st.session_state.results[-5:]:
        st.write(res)

st.markdown("""<div style='text-align: center; color: #888;'>Made with ❤️ by Kinza Khan</div>""", unsafe_allow_html=True)
