# Import libraries
import streamlit as st
from streamlit_option_menu import option_menu

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

# Streamlit page config
st.set_page_config(
    page_title='GOAT-Debate',
    page_icon='./img/favicon.png',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Importing module
import preprocessor, helper

# Load dataframe and modifiction
df = pd.read_csv('./data/data.csv')
df = preprocessor.dataframe_modifier(df)

# Sidebar
st.sidebar.title('C.Ronaldo vs L.Messi')
st.sidebar.header('GOAT-Debate | Club Career')

with st.sidebar:
    selected = option_menu(None, ["Overall", "League", "UEFA Champions League", 'Domestic Cup', 'Domestic Super Cup', 'Others Cup'],
        icons=['arrow-down-up', 'trophy', "trophy", 'trophy', 'trophy', 'trophy'],
        default_index=0,)

filter_year = helper.filter_year(df)
years = st.sidebar.selectbox('Select Year:', filter_year)

# Processing dataframe
df = preprocessor.preprocess(df, years)

if selected == 'Overall':
    pass
if selected == 'League':
    pass
if selected == 'UEFA Champions League':
    pass
if selected == 'Domestic Cup':
    pass
if selected == 'Domestic Super Cup':
    pass
if selected == 'Others Cup':
    pass


