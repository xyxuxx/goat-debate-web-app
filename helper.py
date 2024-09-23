# Filtering function of years
def filter_year(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Calender Year')
    return years