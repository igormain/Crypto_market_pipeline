from sqlalchemy import create_engine

def load(df):
    engine = create_engine('postgresql://postgres:1234@localhost:54321/crypto_db')
    df.to_sql('crypto_prices', engine, if_exists='replace', index = False, chunksize=10000)
    print(f'Loaded {len(df)} rows')