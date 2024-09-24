import numpy as np
import pandas as pd

# Filtering function of years
def filter_year(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Calender Year')
    return years

# Goals per year
def goals_per_year(df):
    cr_goals_year = df[df['Player'] == 'Cristiano Ronaldo']
    lm_goals_year = df[df['Player'] == 'Lionel Messi']

    return cr_goals_year, lm_goals_year

# Home and Away goals
def goals_home_and_away(df, venue):
    if venue == 'H':
        cr_goals = df[(df['Player'] == 'Cristiano Ronaldo') & (df['Venue'] == 'H')]
        lm_goals = df[(df['Player'] == 'Lionel Messi') & (df['Venue'] == 'H')]
    if venue == 'A':
        cr_goals = df[(df['Player'] == 'Cristiano Ronaldo') & (df['Venue'] == 'A')]
        lm_goals = df[(df['Player'] == 'Lionel Messi') & (df['Venue'] == 'A')]
    return cr_goals, lm_goals

# Opponents Faced
def opponents_faced(df):
    cr_opponent = df[df['Player'] == 'Cristiano Ronaldo']['Opponent'].nunique()
    lm_opponent = df[df['Player'] == 'Lionel Messi']['Opponent'].nunique()

    return cr_opponent, lm_opponent

# Quarter, Semi, Final goal
def quarter_semi_final(df, matchday):
    if matchday == 'Quarter-Finals':
        cr_md_goal = len(df[(df['Player'] == 'Cristiano Ronaldo') & (df['Matchday'] == 'Quarter-Finals')])
        lm_md_goal = len(df[(df['Player'] == 'Lionel Messi') & (df['Matchday'] == 'Quarter-Finals')])
    if matchday == 'Semi-Finals':
        cr_md_goal = len(df[(df['Player'] == 'Cristiano Ronaldo') & (df['Matchday'] == 'Semi-Finals')])
        lm_md_goal = len(df[(df['Player'] == 'Lionel Messi') & (df['Matchday'] == 'Semi-Finals')])
    if matchday == 'Final':
        cr_md_goal = len(df[(df['Player'] == 'Cristiano Ronaldo') & (df['Matchday'] == 'Final')])
        lm_md_goal = len(df[(df['Player'] == 'Lionel Messi') & (df['Matchday'] == 'Final')])
    return cr_md_goal, lm_md_goal

# Type of goal
def type_of_goal(df):
    cr_goal_type = df[df['Player'] == 'Cristiano Ronaldo']['Type'].value_counts().reset_index().rename(
        columns={'Type': 'Type of Goal', 'count': 'Goals'})
    lm_goal_type = df[df['Player'] == 'Lionel Messi']['Type'].value_counts().reset_index().rename(
        columns={'Type': 'Type of Goal', 'count': 'Goals'})
    cr_goal_type.index = np.arange(1, len(cr_goal_type)+1)
    lm_goal_type.index = np.arange(1, len(lm_goal_type)+1)

    return cr_goal_type, lm_goal_type

# Goal by Position
def goal_by_position(df):
    cr_goal_pos = df[df['Player'] == 'Cristiano Ronaldo']['Playing_Position'].value_counts().reset_index().rename(
        columns={'Playing_Position': 'Position', 'count': 'Goals'})
    lm_goal_pos = df[df['Player'] == 'Lionel Messi']['Playing_Position'].value_counts().reset_index().rename(
        columns={'Playing_Position': 'Position', 'count': 'Goals'})
    cr_goal_pos.index = np.arange(1, len(cr_goal_pos)+1)
    lm_goal_pos.index = np.arange(1, len(lm_goal_pos)+1)

    return cr_goal_pos, lm_goal_pos

# Favourite Opponent
def favourite_opponent(df):
    cr_fav_opponent = df[df['Player'] == 'Cristiano Ronaldo']['Opponent'].value_counts().head(10).reset_index().rename(
        columns={'Opponent':'Team', 'count':'Goals'})
    lm_fav_opponent = df[df['Player'] == 'Lionel Messi']['Opponent'].value_counts().head(10).reset_index().rename(
        columns={'Opponent':'Team', 'count':'Goals'})

    cr_fav_opponent.index = np.arange(1, len(cr_fav_opponent)+1)
    lm_fav_opponent.index = np.arange(1, len(lm_fav_opponent)+1)

    return cr_fav_opponent, lm_fav_opponent
