# this is awesome, you can run from gist!!
# streamlit run https://gist.githubusercontent.com/sirselim/eb2c8b0f693e2cf02e0a04434be4d098/raw
# author: Miles Benton
# created: 26th Nov 2019

# load streamlit
import streamlit as st
# To make things easier later, we're also importing useful packages. 
import numpy as np
import pandas as pd
import altair as alt
# define datasets
from vega_datasets import data

st.sidebar.title("About")

st.sidebar.info("This is a demo application written to help understand and test Streamlit.")

"""
# Exploring streamlit for interactive web apps using python
"""

"""
#### Note:
Once you have streamlit installed you can use it to run 'apps' (just python scripts really) locally, i.e.:

`streamlit run my_app.py`

...or, what I believe to be extremely awesome, you can run from URLs, including gists!! i.e. to run this exact 'app':

`streamlit run https://gist.githubusercontent.com/sirselim/eb2c8b0f693e2cf02e0a04434be4d098/raw`

If you add the above functionality with integrated gist features made available via VScode extensions (gistFS, vscode-gist) you get a very powerful way to directly test, share and collaborate on fully functional apps quite seemlessly.
Pretty niffty!
"""

"""
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

"""
## We can also draw charts

This is some basic markdown text that is being parsed by streamlit.
"""

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
## Maps

Maps as well...
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

"""
## Testing Altair
"""

st.code("""
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', 
    y='b', 
    size='c', 
    color='c',
    tooltip=['a', 'b', 'c']).interactive()

st.write(c)
""", language="python")

"""
It appears that if you have code blocks that are shown they are not evaluated...?
"""

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', 
    y='b', 
    size='c', 
    color='c',
    tooltip=['a', 'b', 'c']).interactive()

st.write(c)

"""
## Testing chart reveal behind checkbox
"""

source = data.cars()

if st.checkbox('Show Altair chart'):
    testChart = alt.Chart(source).mark_circle(size=60).encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(testChart)

"""
## Progress bars
"""

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'