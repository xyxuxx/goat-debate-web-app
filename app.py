# Import libraries
from unittest.mock import inplace

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

# Custom CSS for styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
        .stat-box {
            background-color: #0E1117;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin: 0.5rem;
            color: white;
        }
        .stat-box h1 {
            font-size: 3rem;
            margin: 0;
        }
        .stat-box p {
            font-size: 1.2rem;
            margin: 0;
        }
        .stat-box-messi {
            background-color: #26A69A;
        }
        .stat-box-ronaldo {
            background-color: #EC407A;
        }
    </style>
    """, unsafe_allow_html=True)

# Load dataframe and modifiction
df = pd.read_csv('./data/data.csv')
df = preprocessor.dataframe_modifier(df)

# Sidebar
st.sidebar.title('C.Ronaldo vs L.Messi')
st.sidebar.header('Club Career Analysis')

with st.sidebar:
    selected = option_menu(None, ['Overall', 'League', 'UEFA Champions League', 'Domestic Cup', 'Domestic Super Cup', 'Others Cup'],
        icons=['arrow-down-up', 'trophy', "trophy", 'trophy', 'trophy', 'trophy'],
        default_index=0,)

# Filtering Year
filter_year = helper.filter_year(df)
years = st.sidebar.selectbox('Select Year:', filter_year)

# Processing dataframe
df = preprocessor.preprocess(df, years)

# Overview of both players career
if selected == 'Overall':
    st.markdown("<h1 style='text-align: center;'>"
                    "Cristiano Ronaldo vs Lionel Messi"
                "</h1>"
                "<h2 style='text-align: center;'>"
                    "The GOAT Debate | Club Career"
                "</h2>", unsafe_allow_html=True)
    st.divider()
    st.markdown('The debate over who is the greatest footballer of all time (GOAT) between Lionel Messi and Cristiano Ronaldo has captivated football fans for over two decades. Their rivalry, characterized by their individual brilliance, consistency, and ability to perform on the biggest stages, has defined an era in football history. Both players have rewritten record books and pushed the boundaries of what is achievable on the field, setting new benchmarks in club football.')
    st.markdown('This project aims to explore and compare the club careers of Messi and Ronaldo using data collected between 10 July 2002 and 18 March 2023. Through this analysis, we hope to contribute a deeper understanding of their remarkable club careers and further fuel the ongoing debate about who is truly the GOAT.')

    st.divider()

    with st.container(border=True):
        cr_goals, lm_goals = helper.goals_per_year(df)

        cr_home_goals, lm_home_goals = helper.goals_home_and_away(df, 'H')
        cr_away_goals, lm_away_goals = helper.goals_home_and_away(df, 'A')

        cr_opponent, lm_opponent = helper.opponents_faced(df)


        # Club Goals
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Club Goals"
                    "</h2>", unsafe_allow_html=True)

        # Cristiano's stats
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>CR7</h1>
                        <p>Stats</p>
                    </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        # Messi's stats
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>LM10</h1>
                        <p>Stats</p>
                    </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

    # Quarter, Semi, Final Performance
    with st.container(border=True):
        cr_quarter, lm_quarter = helper.quarter_semi_final(df,'Quarter-Finals')
        cr_semi, lm_semi = helper.quarter_semi_final(df,'Semi-Finals')
        cr_final, lm_final = helper.quarter_semi_final(df,'Final')

        q_s_f_opponent_df = df[(df['Matchday'] == 'Quarter-Finals') | (df['Matchday'] == 'Semi-Finals') | (
                df['Matchday'] == 'Final')]
        cr_q_s_f_opponent, lm_q_s_f_opponent = helper.opponents_faced(q_s_f_opponent_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Final, Quarter Final and Semi Final Performance"
                    "</h2>", unsafe_allow_html=True)

        # Cristiano's stats
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>CR7</h1>
                        <p>Stats</p>
                    </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_quarter}</h1>
                    <p>Quarter Final</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_semi}</h1>
                    <p>Semi Final</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_final}</h1>
                    <p>Final</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_q_s_f_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)


        # Messi's stats
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>LM10</h1>
                        <p>Stats</p>
                    </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_quarter}</h1>
                    <p>Quarter Final</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_semi}</h1>
                    <p>Semi Final</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_final}</h1>
                    <p>Final</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_q_s_f_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)


    # Favourite Opponent
    with st.container(border=True):
        cr_fav_opponent, lm_fav_opponent = helper.favourite_opponent(df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Favourite Opponents"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_opponent)

        with col2:
            st.table(lm_fav_opponent)


    # Types of Goals
    with st.container(border=True):
        cr_goal_type, lm_goal_type = helper.type_of_goal(df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Types of Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_goal_type)

        with col2:
            st.table(lm_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_goal_pos, lm_goal_pos = helper.goal_by_position(df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_goal_pos)

        with col2:
            st.table(lm_goal_pos)


    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Goals per Minute"
                    "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30,10))
        plt.tight_layout()
        sns.histplot(df, x='Minute', hue='Player')
        plt.xticks(rotation=90)
        st.pyplot(fig)


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


