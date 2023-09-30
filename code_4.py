import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    country_code = country_code.upper()
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')"
    df_result = df.query(query_text)
    mean_dollar_value = df_result['dollar_price'].mean()
    rounded_mean = round(mean_dollar_value, 2)
    return rounded_mean

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query_text = f"(iso_a3 == '{country_code}')"
    df_result = df.query(query_text)
    mean_dollar_value = df_result['dollar_price'].mean()
    rounded_mean = round(mean_dollar_value, 2)
    return rounded_mean

def get_the_cheapest_big_mac_price_by_year(year):
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_text)
    index_min_value = df_result['dollar_price'].idxmin()
    min_value = df_result.loc[index_min_value]
    rounded_min_value = f"{min_value['name']}({min_value['iso_a3']}): {round(min_value['dollar_price'],2)}"
    return rounded_min_value

def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_text)
    index_max_value = df_result['dollar_price'].idxmax()
    max_value = df_result.loc[index_max_value]
    rounded_max_value = f"{max_value['name']}({max_value['iso_a3']}): {round(max_value['dollar_price'],2)}"
    return rounded_max_value

if __name__ == "__main__":
    year = 2006
    country_code = 'can'
    print(get_big_mac_price_by_year(year, country_code))
    print(get_big_mac_price_by_country(country_code))
    print(get_the_cheapest_big_mac_price_by_year(year))
    print(get_the_most_expensive_big_mac_price_by_year(year))