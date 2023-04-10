import streamlit as st
import pandas as pd


# Create a function to display the data based on column index and column titles
def display_data(df, df_title, column_index):
    # Get the question title
    
    question_title = df_title[df_title.columns[column_index]][0]
    
    # Create a container for the question
    question_container = st.container()
   
    
    # Add the question text to the container with formatting
    with question_container:
        if column_index in range(10,14) :
            pass
        else:
            st.markdown(f"<h4 style='text-align: left; color: #008080;'>{question_title}</h4>", unsafe_allow_html=True)
    
    # Check if the value contains a URL
    value = df.iloc[0, column_index]
    if isinstance(value, str) and 'http' in value:
        
        # Display the image
        st.image(value)
    elif column_index == 9:
        # Get the GPS coordinates
        gps = df.iloc[0, i]
        gps = gps.split(' ')
        lat = float(gps[0])
        lon = float(gps[1])
              
        map_data = {"lat": [lat], "lon": [lon]}
        # Display a map with a pin at the specified coordinates
        st.map(map_data, zoom=6)
    elif column_index in range(10,14,1):
        # Do nothing
        pass 
    else:
        # Display the text value
        # st.write(value)
        # if value is nan print no answer
        if pd.isna(value):
            st.write(f"<h5 style='text-align: left; color: dark-blue;'>No Answer</h5>", unsafe_allow_html=True)
        else:
            st.write(f"<h5 style='text-align: left; color: dark-blue;'>{value}</h5>", unsafe_allow_html=True)

# Load the CSV data
df = pd.read_csv('fc_status.csv')
df_title = df[0:1]
# df_title = df_title[0]

# Get the unique values for province, district, and tehsil
provinces = df['province'].unique()
districts = []
tehsils = []

# Create a sidebar with dropdowns to filter the data
province = st.sidebar.selectbox('Select Province', provinces)
districts = df[df['province'] == province]['district'].unique()
district = st.sidebar.selectbox('Select District', districts)
tehsils = df[(df['province'] == province) & (df['district'] == district)]['tehsil'].unique()
tehsil = st.sidebar.selectbox('Select Tehsil', tehsils)

# Filter the data based on user selection
df_filtered = df[(df['province'] == province) & (df['district'] == district) & (df['tehsil'] == tehsil)]

# Create a button to display the data
if st.sidebar.button('Show Data'):
    # Get the dataframe without the first row
    # df_data = df_filtered.iloc[1:]
    
    # Loop through the columns and display the data
    for i in range(len(df_filtered.columns)):
        display_data(df_filtered, df_title, i)
