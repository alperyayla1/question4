import pandas as pd
df = pd.read_csv("C:/Users/alper/Downloads/country_vaccination_stats (1).csv")
country_grouped_df = df.groupby("country")

for country, group in country_grouped_df:

    if pd.isna(group['daily_vaccinations']).all():

        group['daily_vaccinations'].fillna(0, inplace=True)
        df.loc[group.index, 'daily_vaccinations'] = group['daily_vaccinations']
    else:


        min_value = group['daily_vaccinations'].min()

        group['daily_vaccinations'].fillna(min_value, inplace=True)
        df.loc[group.index, 'daily_vaccinations'] = group['daily_vaccinations']


df.to_csv('updated_data1.csv', index=False)

