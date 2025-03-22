import streamlit as st

st.title("Unit Converter 🔄")
st.write("Convert different units easily!")

# 1️⃣ Length Conversion
st.header("📏 Length Converter")
length_input = st.number_input("Enter value (meters)", min_value=0.0, format="%.2f")

# Dropdown for conversion choice
length_unit = st.selectbox("Convert to:", ["Feet", "Inches", "Kilometers", "Miles"])

# Conversion logic
if length_unit == "Feet":
    result = length_input * 3.28084
elif length_unit == "Inches":
    result = length_input * 39.3701
elif length_unit == "Kilometers":
    result = length_input / 1000
elif length_unit == "Miles":
    result = length_input * 0.000621371

st.write(f"Converted Value: {result:.2f} {length_unit}")


# 2️⃣ Weight Conversion
st.header("⚖️ Weight Converter")
weight_input = st.number_input("Enter value (kg)", min_value=0.0, format="%.2f")

# Dropdown for conversion choice
weight_unit = st.selectbox("Convert to:", ["Grams", "Pounds", "Ounces"])

# Conversion logic
if weight_unit == "Grams":
    result = weight_input * 1000
elif weight_unit == "Pounds":
    result = weight_input * 2.20462
elif weight_unit == "Ounces":
    result = weight_input * 35.274

st.write(f"Converted Value: {result:.2f} {weight_unit}")

# 3️⃣ Temperature Conversion
st.header("🌡️ Temperature Converter")
temp_input = st.number_input("Enter value (Celsius)", format="%.2f")

# Dropdown for conversion choice
temp_unit = st.selectbox("Convert to:", ["Fahrenheit", "Kelvin"])

# Conversion logic
if temp_unit == "Fahrenheit":
    result = (temp_input * 9/5) + 32
elif temp_unit == "Kelvin":
    result = temp_input + 273.15

st.write(f"Converted Value: {result:.2f} {temp_unit}")

# 4️⃣ Time Conversion
st.header("⏳ Time Converter")
time_input = st.number_input("Enter value (seconds)", min_value=0.0, format="%.2f")

# Dropdown for conversion choice
time_unit = st.selectbox("Convert to:", ["Minutes", "Hours"])

# Conversion logic
if time_unit == "Minutes":
    result = time_input / 60
elif time_unit == "Hours":
    result = time_input / 3600

st.write(f"Converted Value: {result:.2f} {time_unit}")

# 5️⃣ Speed Conversion
st.header("🚀 Speed Converter")
speed_input = st.number_input("Enter value (km/h)", min_value=0.0, format="%.2f")

# Dropdown for conversion choice
speed_unit = st.selectbox("Convert to:", ["m/s", "mph"])

# Conversion logic
if speed_unit == "m/s":
    result = speed_input / 3.6
elif speed_unit == "mph":
    result = speed_input * 0.621371

st.write(f"Converted Value: {result:.2f} {speed_unit}")