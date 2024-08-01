import streamlit as st
import pandas as pd

# Title and description
st.title("Simple Streamlit App")
st.write("This is a simple example of a Streamlit app.")

# Adding a sidebar
st.sidebar.title("Sidebar")
option = st.sidebar.selectbox(
    'Select a number',
    list(range(1, 11))
)

# Display the selected option
st.write(f'You selected: {option}')

# Dataframe display
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})
st.write("Here's a simple dataframe:")
st.write(df)

# Plotting a chart
st.line_chart(df)

# Adding a button
if st.button('Say hello'):
    st.write('Hello!')