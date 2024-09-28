import pandas as pd

# Modification function of dataframe
def dataframe_modifier(df):
    years = []
    for i in df['Date'].str.split('/'):
        years.append(i[2])
    years = pd.DataFrame(years)
    years = years.rename(columns={0: 'Year'})
    df = df.join(years, how='outer')
    return df

# Preprocessing function of dataframe
def preprocess(df, year):
    df['Competition'] = df['Competition'].replace(['Supercopa', 'Italy Cup', 'Troph�e des Champions', 'Champions League'], ['Supercopa de España', 'Coppa Italia', 'Trophée des Champions', 'UEFA Champions League'])
    df['Matchday'] = df['Matchday'].replace(['final', 'last 16'],['Final', 'Round of 16'])
    df['Opponent'] = df['Opponent'].replace(['CÃ³rdoba CF', 'Sporting GijÃ³n', 'FC ZÃ¼rich', 'MalmÃ¶ FF', 'Borussia MÃ¶nchengladbach', 'GrÃªmio Foot-Ball Porto Alegrense', 'Deportivo de La CoruÃ±a', 'Deportivo de La Coruaa'],['Córdoba CF', 'Sporting de Gijón', 'FC Zürich', 'Malmö FF', 'Borussia Mönchengladbach','Grêmio Foot-Ball Porto Alegrense', 'Deportivo de La Coruña', 'Deportivo de La Coruña'])
    df['Type'].fillna('Not Reported in Data', inplace=True)
    df['Playing_Position'].fillna('Not Reported in Data', inplace=True)
    if year == 'All Time':
        new_df = df
    if year != 'All Time':
        new_df = df[df['Year'] == year]
    return new_df