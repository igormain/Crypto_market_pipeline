
def transform(df):
    df = df[~df['current_price'].isna()]
    df = df[df['current_price'] > 0]
    df['price_change_percentage_24h'] = df['price_change_percentage_24h'].round(2)
    return df