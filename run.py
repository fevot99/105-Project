import streamlit as st
import pandas as pd

# Title and description
st.title("ITI105 App")
st.write("This is a simple example of a ITI105 app.")

# Adding a sidebar
st.sidebar.title("Sidebar")
option = st.sidebar.selectbox(
    'Enter the number of Songs',
    list(range(1, 11))
)

# Display the selected option
st.write(f'The number of Songs elected: {option}')

# Dataframe display
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': ['Song 1', 'Song 2', 'Song 3', 'Song 4']
})
st.write("Here's the Recommended Song and Artist Name:")
st.write(df)

# Plotting a chart
st.line_chart(df)

# Adding a button
if st.button('Say hello'):
    st.write('Hello!')
