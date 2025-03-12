import streamlit as st
import pandas as pd


# st.markdown("<h1 style='text-align: center;'>🔄 Unit Converter App</h1>", unsafe_allow_html=True)
# st.text("Here you can convert your one  unit value to an other unit value")

import streamlit as st
# A package that handles units and unit conversions.
from pint import UnitRegistry

# Initialize 
ureg = UnitRegistry()

# Tittle
st.markdown("<h1 style='text-align: center;'>🔄 Simple Unit Converter App</h1>", unsafe_allow_html=True)

# Create dictionary store Unit i their categories like Length to cover -> meter, kilo meter, mile 
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch", "centimeter", "millimeter"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"]
}

# Choose Category Type  for Unit Conversions
category = st.selectbox("Select Units Type:", list(unit_categories.keys()))

# Getting unit Inputs
from_unit = st.selectbox("From:", unit_categories[category])
to_unit = st.selectbox("To:", unit_categories[category])

#  Value Input from User like 10, from meter to centimeter
value = st.number_input(f"Enter Value in {from_unit}", min_value=0.00, format="%.2f")

# Conversion Section
if st.button("Convert"):
    try:
        if category == "Temperature":
            
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                # if units are same like ....  meter to meter conversion
                result = value  
        else:
            # Use UnitRegistration() package for other conversions
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        #  Displaying Result here
        st.success(f"✅{value} {from_unit} = {result:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")

