import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
df['iso_a3'] = df['iso_a3'].str.lower()

def get_big_mac_price_by_year(year, country_code):
    year = 2006
    country_code = "can"
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')"
    df_result = df.query(query_text)
    mean_dollar_value = df_result['dollar_price'].mean()
    rounded_mean = round(mean_dollar_value, 2)
    return rounded_mean

def get_big_mac_price_by_country(country_code):
    country_code = "jpn"
    query_text = f"(iso_a3 == '{country_code}')"
    df_result = df.query(query_text)
    mean_dollar_value = df_result['dollar_price'].mean()
    rounded_mean = round(mean_dollar_value, 2)
    return rounded_mean

def get_the_cheapest_big_mac_price_by_year(year):
    year = 2016
    country_code = "ven"
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_text)
    min_value = df_result['dollar_price'].min()
    rounded_min_value = round(min_value,2)
    return rounded_min_value

def get_the_most_expensive_big_mac_price_by_year(year):
    year = 2006
    country_code = "nor"
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_text)
    max_value = df_result['dollar_price'].max()
    rounded_max_value = round(max_value,2)
    return rounded_max_value

if __name__ == "__main__":
    year = 2006
    country_code = "can"
    print(get_big_mac_price_by_year(year, country_code))
    print(get_big_mac_price_by_country(country_code))
    print (f"Venezuela(VEN): {get_the_cheapest_big_mac_price_by_year(year)}")
    print (f"Norway(NOR): {get_the_most_expensive_big_mac_price_by_year(year)}")