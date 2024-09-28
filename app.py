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
    selected = option_menu(None, ['Overall', 'League', 'UEFA Champions League', 'Domestic Cup', 'Domestic Super Cup', 'Other Cups'],
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
    st.markdown('This project aims to explore and compare the club careers of Messi and Ronaldo using data collected between `10 July 2002 and 18 March 2023`. Through this analysis, we hope to contribute a deeper understanding of their remarkable club careers and further fuel the ongoing debate about who is truly the GOAT.')

    st.divider()

    # Overall analysis
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

        st.divider()
        fig = plt.figure(figsize=(6, 5))
        sns.countplot(df, y='Competition', hue='Player')
        plt.title('Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)


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

        st.divider()
        fig = plt.figure(figsize=(7, 4))
        sns.countplot(q_s_f_opponent_df, y='Competition', hue='Player')
        plt.title('Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # El Classico Goals
    h2h_match_df = df[(((df['Club'] == 'Real Madrid') | (df['Club'] == 'FC Barcelona')) & (
                (df['Opponent'] == 'Real Madrid') | (df['Opponent'] == 'FC Barcelona')))]
    with st.container(border=True):
        cr_h2h_match_goal = len(h2h_match_df[h2h_match_df['Player'] == 'Cristiano Ronaldo'])
        lm_h2h_match_goal = len(h2h_match_df[h2h_match_df['Player'] == 'Lionel Messi'])
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "El Clásico Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{cr_h2h_match_goal}</h1>
                        <p>Ronaldo Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{lm_h2h_match_goal}</h1>
                        <p>Messi Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(8, 2))
        ax = sns.countplot(h2h_match_df, y='Venue', hue='Player')

        plt.title('El Clásico Goals per Competition')
        plt.xlabel('No of Goals')
        plt.xticks(np.arange(0, 20, step=5))
        st.pyplot(fig)


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

    # Most goals in a single match
    with st.container(border=True):
        cr_most_goal, lm_most_goal = helper.goals_in_single_match(df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Most Goals in a Single Match"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_most_goal)
        with col2:
            st.table(lm_most_goal)


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
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)

# League goal analysis
if selected == 'League':
    # League Goals
    with st.container(border=True):
        league_df = df[(df['Competition'] == 'Liga Portugal') | (df['Competition'] == 'Premier League') | (
                df['Competition'] == 'LaLiga') | (df['Competition'] == 'Serie A') | (
                       df['Competition'] == 'Ligue 1') | (df['Competition'] == 'Saudi Pro League')]
        cr_league_goals, lm_league_goals = helper.goals_per_year(league_df)

        cr_home_league_goals, lm_home_league_goals = helper.goals_home_and_away(league_df, 'H')
        cr_away_league_goals, lm_away_league_goals = helper.goals_home_and_away(league_df, 'A')

        cr_league_opponent, lm_league_opponent = helper.opponents_faced(df)

        # Club Goals
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "League Goals"
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
                    <h1>{len(cr_league_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_league_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_league_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_league_opponent}</h1>
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
                    <h1>{len(lm_league_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_league_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_league_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_league_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(7, 4))
        sns.countplot(league_df, y='Competition', hue='Player')
        plt.title('League Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Europe's Top 5 League Goals
    with st.container(border=True):
        et5_league_df = df[(df['Competition'] == 'Premier League') | (
                df['Competition'] == 'LaLiga') | (df['Competition'] == 'Serie A') | (
                       df['Competition'] == 'Ligue 1')]
        cr_et5_league_goals, lm_et5_league_goals = helper.goals_per_year(et5_league_df)

        cr_et5_home_league_goals, lm_et5_home_league_goals = helper.goals_home_and_away(et5_league_df, 'H')
        cr_et5_away_league_goals, lm_et5_away_league_goals = helper.goals_home_and_away(et5_league_df, 'A')

        cr_et5_league_opponent, lm_et5_league_opponent = helper.opponents_faced(et5_league_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Europe's Top 5 League Goals"
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
                    <h1>{len(cr_et5_league_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_et5_home_league_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_et5_away_league_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_et5_league_opponent}</h1>
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
                    <h1>{len(lm_et5_league_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_et5_home_league_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_et5_away_league_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_et5_league_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(7, 4))
        sns.countplot(et5_league_df, y='Competition', hue='Player')
        plt.title("Europe's Top 5 League Goals per Competition")
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # LaLiga Goals
    with st.container(border=True):
        laliga_df = df[(df['Competition'] == 'LaLiga')]
        cr_laliga_goals, lm_laliga_goals = helper.goals_per_year(laliga_df)

        cr_laliga_home_goals, lm_laliga_home_goals = helper.goals_home_and_away(laliga_df, 'H')
        cr_laliga_away_goals, lm_laliga_away_goals = helper.goals_home_and_away(laliga_df, 'A')

        cr_laliga_opponent, lm_laliga_opponent = helper.opponents_faced(laliga_df)

        # Club Goals
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "LaLiga Goals"
                    "</h2>", unsafe_allow_html=True)

        # Cristiano's stats
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown("""<div class="stat-box stat-box-ronaldo">
                            <h1>CR7</h1>
                            <p>Stats</p>
                    </div>
                    """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class="stat-box stat-box-ronaldo">
                                <h1>{len(cr_laliga_goals)}</h1>
                                <p>Total Goals</p>
                            </div>
                        """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{len(cr_laliga_home_goals)}</h1>
                        <p>Home Goals</p>
                    </div>
                    """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{len(cr_laliga_away_goals)}</h1>
                        <p>Away Goals</p>
                    </div>
                """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{cr_laliga_opponent}</h1>
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
                        <h1>{len(lm_laliga_goals)}</h1>
                        <p>Total Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{len(lm_laliga_home_goals)}</h1>
                        <p>Home Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{len(lm_laliga_away_goals)}</h1>
                        <p>Away Goals</p>
                    </div>
                """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{lm_laliga_opponent}</h1>
                        <p>Scored Against</p>
                    </div>
                """, unsafe_allow_html=True)

        st.divider()
        sorted_laliga_df = laliga_df.copy()
        sorted_laliga_df['Matchday'] = pd.to_numeric(sorted_laliga_df['Matchday'])
        sorted_laliga_df = sorted_laliga_df.sort_values(by='Matchday')
        fig = plt.figure(figsize=(8, 8))
        sns.countplot(sorted_laliga_df, y='Matchday', hue='Player')
        plt.title("LaLiga Goals per Matchday")
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # El Classico Goals
    h2h_league_match_df = df[(((df['Club'] == 'Real Madrid') | (df['Club'] == 'FC Barcelona')) & (
                (df['Opponent'] == 'Real Madrid') | (df['Opponent'] == 'FC Barcelona')) & (
                    df['Competition'] == 'LaLiga'))]
    with st.container(border=True):
        cr_h2h_league_match_goal = len(h2h_league_match_df[h2h_league_match_df['Player'] == 'Cristiano Ronaldo'])
        lm_h2h_league_match_goal = len(h2h_league_match_df[h2h_league_match_df['Player'] == 'Lionel Messi'])
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "LaLiga: El Clásico Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{cr_h2h_league_match_goal}</h1>
                        <p>Ronaldo</p>
                    </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{lm_h2h_league_match_goal}</h1>
                        <p>Messi</p>
                    </div>
                """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(8, 2))
        sns.countplot(h2h_league_match_df, y='Venue', hue='Player')
        plt.title("El Clásico League Goals per Venue")
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Favourite Opponent
    with st.container(border=True):
        cr_fav_league_opponent, lm_fav_league_opponent = helper.favourite_opponent(league_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Favourite League Opponents"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_league_opponent)

        with col2:
            st.table(lm_fav_league_opponent)

    # Most goals in a single match
    with st.container(border=True):
        cr_league_most_goal, lm_league_most_goal = helper.goals_in_single_match(league_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Most Goals in a Single League Match"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_league_most_goal)
        with col2:
            st.table(lm_league_most_goal)

    # Types of Goals
    with st.container(border=True):
        cr_league_goal_type, lm_league_goal_type = helper.type_of_goal(league_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Types of League Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_league_goal_type)

        with col2:
            st.table(lm_league_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_league_goal_pos, lm_league_goal_pos = helper.goal_by_position(league_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise League Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_league_goal_pos)

        with col2:
            st.table(lm_league_goal_pos)

    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Goals per Minute in League"
                    "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30, 10))
        plt.tight_layout()
        sns.histplot(league_df, x='Minute', hue='Player')
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)

# UCL goals analysis
if selected == 'UEFA Champions League':
    # UCL goals
    with st.container(border=True):
        ucl_df = df[(df['Competition'] == 'UEFA Champions League')]
        cr_ucl_goals, lm_ucl_goals = helper.goals_per_year(ucl_df)

        cr_home_ucl_goals, lm_home_ucl_goals = helper.goals_home_and_away(ucl_df, 'H')
        cr_away_ucl_goals, lm_away_ucl_goals = helper.goals_home_and_away(ucl_df, 'A')

        cr_ucl_opponent, lm_ucl_opponent = helper.opponents_faced(ucl_df)

        # UCL Goals
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "UEFA Champions League Goals"
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
                    <h1>{len(cr_ucl_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_ucl_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_ucl_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_ucl_opponent}</h1>
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
                    <h1>{len(lm_ucl_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_ucl_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_ucl_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_ucl_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(7, 4))
        sns.countplot(ucl_df, y='Matchday', hue='Player')
        plt.title('UEFA Champions League Goals per Matchday')
        plt.xlabel('No of Goals')
        st.pyplot(fig)



    # El Classico Goals
    h2h_ucl_match_df = df[(((df['Club'] == 'Real Madrid') | (df['Club'] == 'FC Barcelona')) & (
                (df['Opponent'] == 'Real Madrid') | (df['Opponent'] == 'FC Barcelona')) & (
                                          df['Competition'] == 'UEFA Champions League'))]
    with st.container(border=True):
        cr_h2h_ucl_match_goal = len(h2h_ucl_match_df[h2h_ucl_match_df['Player'] == 'Cristiano Ronaldo'])
        lm_h2h_ucl_match_goal = len(h2h_ucl_match_df[h2h_ucl_match_df['Player'] == 'Lionel Messi'])
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "UEFA Champions League: El Clásico  Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                        <div class="stat-box stat-box-ronaldo">
                            <h1>{cr_h2h_ucl_match_goal}</h1>
                            <p>Ronaldo Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                        <div class="stat-box stat-box-messi">
                            <h1>{lm_h2h_ucl_match_goal}</h1>
                            <p>Messi Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(12, 1))
        sns.countplot(h2h_ucl_match_df, y='Venue', hue='Player')
        plt.title('UEFA Champions League El Clásico Goals per Venue')
        plt.xlabel('No of Goals')
        plt.xticks(np.arange(1,3,step=1))
        st.pyplot(fig)

    # Favourite Opponent
    with st.container(border=True):
        cr_fav_ucl_opponent, lm_fav_ucl_opponent = helper.favourite_opponent(ucl_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Favourite UEFA Champions League Opponents"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_ucl_opponent)

        with col2:
            st.table(lm_fav_ucl_opponent)

    # Most goals in a single match
    with st.container(border=True):
        cr_ucl_most_goal, lm_ucl_most_goal = helper.goals_in_single_match(ucl_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                            "Most Goals in a Single UEFA Champions League Match"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_ucl_most_goal)
        with col2:
            st.table(lm_ucl_most_goal)

    # Types of Goals
    with st.container(border=True):
        cr_ucl_goal_type, lm_ucl_goal_type = helper.type_of_goal(ucl_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Types of UEFA Champions League Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_ucl_goal_type)

        with col2:
            st.table(lm_ucl_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_ucl_goal_pos, lm_ucl_goal_pos = helper.goal_by_position(ucl_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise UEFA Champions League Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_ucl_goal_pos)

        with col2:
            st.table(lm_ucl_goal_pos)

    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Goals per Minute in UEFA Champions League"
                        "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30, 10))
        plt.tight_layout()
        sns.histplot(ucl_df, x='Minute', hue='Player')
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)

# Domestic Cup Analysis
if selected == 'Domestic Cup':
    # Domestic Cup Goals
    with st.container(border=True):
        dc_df = df[(df['Competition'] == 'Copa del Rey') | (df['Competition'] == 'Coppa Italia') | (
                df['Competition'] == 'FA Cup') | (df['Competition'] == 'EFL Cup')]
        cr_dc_goals, lm_dc_goals = helper.goals_per_year(dc_df)

        cr_home_dc_goals, lm_home_dc_goals = helper.goals_home_and_away(dc_df, 'H')
        cr_away_dc_goals, lm_away_dc_goals = helper.goals_home_and_away(dc_df, 'A')

        cr_dc_opponent, lm_dc_opponent = helper.opponents_faced(dc_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Domestic Cup Goals"
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
                    <h1>{len(cr_dc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_dc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_dc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_dc_opponent}</h1>
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
                    <h1>{len(lm_dc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_dc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_dc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_dc_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(10,5))
        sns.countplot(dc_df, y='Competition', hue='Player')
        plt.title('Domestic Cup Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Copa Del Ray Goals
    with st.container(border=True):
        cdl_df = df[(df['Competition'] == 'Copa del Rey')]
        cr_cdl_goals, lm_cdl_goals = helper.goals_per_year(cdl_df)

        cr_home_cdl_goals, lm_home_cdl_goals = helper.goals_home_and_away(cdl_df, 'H')
        cr_away_cdl_goals, lm_away_cdl_goals = helper.goals_home_and_away(cdl_df, 'A')

        cr_cdl_opponent, lm_cdl_opponent = helper.opponents_faced(cdl_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                            "Copa Del Ray Goals"
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
                            <h1>{len(cr_cdl_goals)}</h1>
                            <p>Total Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col3:
             st.markdown(f"""
                        <div class="stat-box stat-box-ronaldo">
                            <h1>{len(cr_home_cdl_goals)}</h1>
                            <p>Home Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                        <div class="stat-box stat-box-ronaldo">
                            <h1>{len(cr_away_cdl_goals)}</h1>
                            <p>Away Goals</p>
                        </div>
                    """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                        <div class="stat-box stat-box-ronaldo">
                            <h1>{cr_cdl_opponent}</h1>
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
                            <h1>{len(lm_cdl_goals)}</h1>
                            <p>Total Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                        <div class="stat-box stat-box-messi">
                            <h1>{len(lm_home_cdl_goals)}</h1>
                            <p>Home Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                        <div class="stat-box stat-box-messi">
                            <h1>{len(lm_away_cdl_goals)}</h1>
                            <p>Away Goals</p>
                        </div>
                    """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                        <div class="stat-box stat-box-messi">
                            <h1>{lm_cdl_opponent}</h1>
                            <p>Scored Against</p>
                        </div>
                    """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(10, 5))
        sns.countplot(cdl_df, y='Matchday', hue='Player')
        plt.title('Domestic Cup Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Copa del Rey: El Clásico Goals
    h2h_cdl_match_df = df[(((df['Club'] == 'Real Madrid') | (df['Club'] == 'FC Barcelona')) & (
                (df['Opponent'] == 'Real Madrid') | (df['Opponent'] == 'FC Barcelona')) & (
                    df['Competition'] == 'Copa del Rey'))]
    with st.container(border=True):
        cr_h2h_cdl_match_goal = len(h2h_cdl_match_df[h2h_cdl_match_df['Player'] == 'Cristiano Ronaldo'])
        lm_h2h_cdl_match_goal = len(h2h_cdl_match_df[h2h_cdl_match_df['Player'] == 'Lionel Messi'])
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Copa del Rey: El Clásico Goals"
                    "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                    <div class="stat-box stat-box-ronaldo">
                        <h1>{cr_h2h_cdl_match_goal}</h1>
                        <p>Ronaldo Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                    <div class="stat-box stat-box-messi">
                        <h1>{lm_h2h_cdl_match_goal}</h1>
                        <p>Messi Goals</p>
                    </div>
                """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(8, 2))
        sns.countplot(h2h_cdl_match_df, y='Venue', hue='Player')
        plt.title('Copa del Rey El Clásico Goals per Venue')
        plt.xlabel('No of Goals')
        plt.xticks(np.arange(1,5,step=1))
        st.pyplot(fig)

    # Favourite Opponent
    with st.container(border=True):
        cr_fav_dc_opponent, lm_fav_dc_opponent = helper.favourite_opponent(dc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Favourite Domestic Cup Opponents"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_dc_opponent)

        with col2:
            st.table(lm_fav_dc_opponent)

    # Most goals in a single match
    with st.container(border=True):
        cr_dc_most_goal, lm_dc_most_goal = helper.goals_in_single_match(dc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                            "Most Goals in a Single Domestic Cup Match"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dc_most_goal)
        with col2:
            st.table(lm_dc_most_goal)

    # Types of Goals
    with st.container(border=True):
        cr_dc_goal_type, lm_dc_goal_type = helper.type_of_goal(dc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Types of Domestic Cup Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dc_goal_type)

        with col2:
            st.table(lm_dc_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_dc_goal_pos, lm_dc_goal_pos = helper.goal_by_position(dc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise Domestic Cup Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dc_goal_pos)

        with col2:
            st.table(lm_dc_goal_pos)

    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Goals per Minute in Domestic Cup"
                        "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30, 10))
        plt.tight_layout()
        sns.histplot(dc_df, x='Minute', hue='Player')
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)

# Domestic Super League analysis
if selected == 'Domestic Super Cup':
    # Domestic Super Cup goals
    with st.container(border=True):
        dsc_df = df[(df['Competition'] == 'Supercopa de España') | (df['Competition'] == 'Supercoppa Italiana') | (df['Competition'] == 'Trophée des Champions')]
        cr_dsc_goals, lm_dsc_goals = helper.goals_per_year(dsc_df)

        cr_home_dsc_goals, lm_home_dsc_goals = helper.goals_home_and_away(dsc_df, 'H')
        cr_away_dsc_goals, lm_away_dsc_goals = helper.goals_home_and_away(dsc_df, 'A')

        cr_dsc_opponent, lm_dsc_opponent = helper.opponents_faced(dsc_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Domestic Super Cup Goals"
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
                    <h1>{len(cr_dsc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_dsc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_dsc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_dsc_opponent}</h1>
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
                    <h1>{len(lm_dsc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_dsc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_dsc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_dsc_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(10, 5))
        sns.countplot(dsc_df, y='Competition', hue='Player')
        plt.title('Domestic Super Cup Goals per Competition')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Supercopa de España Goals
    with st.container(border=True):
        sde_df = df[(df['Competition'] == 'Supercopa de España')]
        cr_sde_goals, lm_sde_goals = helper.goals_per_year(sde_df)

        cr_home_sde_goals, lm_home_sde_goals = helper.goals_home_and_away(sde_df, 'H')
        cr_away_sde_goals, lm_away_sde_goals = helper.goals_home_and_away(sde_df, 'A')

        cr_sde_opponent, lm_sde_opponent = helper.opponents_faced(sde_df)

        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Supercopa de España Goals"
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
                    <h1>{len(cr_sde_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_sde_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_sde_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_sde_opponent}</h1>
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
                    <h1>{len(lm_sde_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_sde_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_sde_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_sde_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(dsc_df, y='Matchday', hue='Player')
        plt.title('Supercopa de España Goals per Matchday')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Supercopa de España El Clásico Goals
    h2h_sde_match_df = df[(((df['Club'] == 'Real Madrid') | (df['Club'] == 'FC Barcelona')) & (
                (df['Opponent'] == 'Real Madrid') | (df['Opponent'] == 'FC Barcelona')) & (
                                       df['Competition'] == 'Supercopa de España'))]
    with st.container(border=True):
        cr_h2h_sde_match_goal = len(h2h_sde_match_df[h2h_sde_match_df['Player'] == 'Cristiano Ronaldo'])
        lm_h2h_sde_match_goal = len(h2h_sde_match_df[h2h_sde_match_df['Player'] == 'Lionel Messi'])
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Supercopa de España: El Clásico Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                        <div class="stat-box stat-box-ronaldo">
                            <h1>{cr_h2h_sde_match_goal}</h1>
                            <p>Ronaldo Goals</p>
                        </div>
                    """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                        <div class="stat-box stat-box-messi">
                            <h1>{lm_h2h_sde_match_goal}</h1>
                            <p>Messi Goals</p>
                        </div>
                    """, unsafe_allow_html=True)
        st.divider()
        fig = plt.figure(figsize=(8, 2))
        sns.countplot(dsc_df, y='Venue', hue='Player')
        plt.title('Supercopa de España El Clásico Goals per Venue')
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Favourite Opponent
    with st.container(border=True):
        cr_fav_dsc_opponent, lm_fav_dsc_opponent = helper.favourite_opponent(dsc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Favourite Domestic Super Cup Opponents"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_dsc_opponent)

        with col2:
            st.table(lm_fav_dsc_opponent)

    # Most goals in a single match
    with st.container(border=True):
        cr_dsc_most_goal, lm_dsc_most_goal = helper.goals_in_single_match(dsc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                            "Most Goals in a Single Domestic Super Cup Match"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dsc_most_goal)
        with col2:
            st.table(lm_dsc_most_goal)

    # Types of Goals
    with st.container(border=True):
        cr_dsc_goal_type, lm_dsc_goal_type = helper.type_of_goal(dsc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Types of Domestic Super Cup Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dsc_goal_type)

        with col2:
            st.table(lm_dsc_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_dsc_goal_pos, lm_dsc_goal_pos = helper.goal_by_position(dsc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise Domestic Super Cup Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_dsc_goal_pos)

        with col2:
            st.table(lm_dsc_goal_pos)

    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Goals per Minute in Domestic Super Cup"
                        "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30, 10))
        plt.tight_layout()
        sns.histplot(dsc_df, x='Minute', hue='Player')
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)

# Other Cups goals analysis
if selected == 'Other Cups':
    # Other Cups Goals
    with st.container(border=True):
        oc_df = df[(df['Competition'] == 'UEFA Champions League Qualifying') | (df['Competition'] == 'FIFA Club World Cup') | (df['Competition'] == 'UEFA Super Cup') | (df['Competition'] == 'Europa League')]
        cr_oc_goals, lm_oc_goals = helper.goals_per_year(oc_df)

        cr_home_oc_goals, lm_home_oc_goals = helper.goals_home_and_away(oc_df, 'H')
        cr_away_oc_goals, lm_away_oc_goals = helper.goals_home_and_away(oc_df, 'A')

        cr_oc_opponent, lm_oc_opponent = helper.opponents_faced(oc_df)

        # Domestic Cup Goals
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                    "Other Cups' Goals"
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
                    <h1>{len(cr_oc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_home_oc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{len(cr_away_oc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-ronaldo">
                    <h1>{cr_oc_opponent}</h1>
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
                    <h1>{len(lm_oc_goals)}</h1>
                    <p>Total Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_home_oc_goals)}</h1>
                    <p>Home Goals</p>
                </div>
            """, unsafe_allow_html=True)

        with col4:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{len(lm_away_oc_goals)}</h1>
                    <p>Away Goals</p>
                </div>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
                <div class="stat-box stat-box-messi">
                    <h1>{lm_oc_opponent}</h1>
                    <p>Scored Against</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        fig = plt.figure(figsize=(8, 5))
        sns.countplot(oc_df, y='Competition', hue='Player')
        plt.title("Other Cups' Goals per Competition")
        plt.xlabel('No of Goals')
        st.pyplot(fig)

    # Favourite Opponent
    with st.container(border=True):
        cr_fav_oc_opponent, lm_fav_oc_opponent = helper.favourite_opponent(oc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Favourite Other Cups' Opponents"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_fav_oc_opponent)

        with col2:
            st.table(lm_fav_oc_opponent)

    # Most goals in a single match
    with st.container(border=True):
        cr_oc_most_goal, lm_oc_most_goal = helper.goals_in_single_match(oc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                            "Most Goals in a Single Other Cups' Match"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_oc_most_goal)
        with col2:
            st.table(lm_oc_most_goal)

    # Types of Goals
    with st.container(border=True):
        cr_oc_goal_type, lm_oc_goal_type = helper.type_of_goal(oc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Types of Other Cups' Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_oc_goal_type)

        with col2:
            st.table(lm_oc_goal_type)

    # Position-wise Goals
    with st.container(border=True):
        cr_oc_goal_pos, lm_oc_goal_pos = helper.goal_by_position(oc_df)
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Position-wise Other Cups' Goals"
                        "</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.table(cr_oc_goal_pos)

        with col2:
            st.table(lm_oc_goal_pos)

    # Goals per 90 minute
    with st.container(border=True):
        st.markdown("<h2 style='text-align: center; margin:1rem;'>"
                        "Goals per Minute in Other Cups"
                        "</h2>", unsafe_allow_html=True)
        fig = plt.figure(figsize=(30, 10))
        plt.tight_layout()
        sns.histplot(oc_df, x='Minute', hue='Player')
        plt.ylabel('No of Goals')
        plt.xticks(rotation=90)
        st.pyplot(fig)


