import pandas as pd

try:
    # csv = open('ddmmyyy_verge.csv', 'w')
    csvv= "ddmmyyy_verge.csv"
    without_header = "temp.csv"
    df_state = pd.read_csv('ddmmyyy_verge.csv')
    df_state.drop_duplicates(subset=['URL','Headline','Author','Date'], inplace=True, keep='first')
    df_state.to_csv(csvv, index=False)
    df_state.to_csv(without_header, index=False, header=None)

except (RuntimeError, TypeError, NameError):
    pass