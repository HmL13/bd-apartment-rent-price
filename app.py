import streamlit as st
import pickle
import numpy as np

# Load the model and data columns
with open('bd_apartment_rent_price.pickle', 'rb') as file:
    model = pickle.load(file)

data_columns = ["beds", "bath", "area", "adabor", "aftab nagar", "agargaon", "badda", "bakalia", "banani", "banasree", "baridhara", "bashundhara r-a", "bayazid", "cantonment", "dakshin khan", "dhanmondi", "double mooring", "east nasirabad", "gulshan", "halishahar", "khilgaon", "khilkhet", "khulshi", "mirpur", "mohammadpur", "sholokbahar", "uttar khan", "uttara"]

# Capitalize the first letter of each location name
locations = [loc.title() for loc in data_columns[3:]]

# Streamlit app
st.set_page_config(page_title="Apartment Rent Price in Bangladesh", page_icon="🏠")

# Add CSS for background image and semi-transparent overlay
st.markdown(
    """
    <style>
    html, body {
        overflow: hidden;  /* Disable scrolling */
    }
    .stApp {
        background: url('https://cdn.discordapp.com/attachments/762960761378308096/1261288769231781981/image.png?ex=66926a34&is=669118b4&hm=dbe79c89969c8107c2b626b068ecb872644c781ff82a95d6eb6d4b3433a4f3e6&') no-repeat center center fixed;
        background-size: 100% 110%;
    }
    
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="overlay-box">', unsafe_allow_html=True)
st.title("Apartment Rent Price in Bangladesh")

# Input features
with st.form("rent_form"):
    area = st.number_input("Area (Square Feet)", min_value=500, max_value=5000, step=100)
    
    st.write("Bedroom")
    bedrooms = st.radio("", [1, 2, 3, 4, 5], index=2, horizontal=True, key="bedrooms_radio")

    st.write("Bathroom")
    bathrooms = st.radio("", [1, 2, 3, 4, 5], index=2, horizontal=True, key="bathrooms_radio")

    location = st.selectbox("Location", locations)

    submit_button = st.form_submit_button(label="Estimate Price")

# Create input array with zeros
input_data = np.zeros(len(data_columns))

# Assign the values to the appropriate indices
input_data[data_columns.index("beds")] = bedrooms
input_data[data_columns.index("bath")] = bathrooms
input_data[data_columns.index("area")] = area

# Match the selected location to its lowercase version in data_columns
selected_location = location.lower()
if selected_location in data_columns:
    input_data[data_columns.index(selected_location)] = 1

# Reshape input data to match the model's expected input
input_data = input_data.reshape(1, -1)

# Predict rent price
if submit_button:
    predicted_price = model.predict(input_data)
    st.subheader(f"{predicted_price[0]:,.0f} BDT")

st.caption("The predicted price might not be 100% accurate!")

# Footer
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)
st.markdown('<div style="text-align: center;">Created by HmL13</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)