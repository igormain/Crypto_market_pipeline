# Crypto Market Pipeline

ETL pipeline for crypto market tracking data using Python, pandas, PostgreSQL, and dbt.

## Stack
- Python (pandas, SQLAlchemy)
- PostgreSQL (pgAdmin)
- SQL
- dbt

## Pipeline
- **Extract** - fetch top 50 cryptocurrencies via CoinGecko API, add `last_updated` and `extracted_at` columns
- **Transform** - remove rows with missing/zero prices, round percentage values
- **Load** - upload cleaned data to PostgreSQL via SQLAlchemy

## Data
CoinGecko API - Top 50 cryptocurrencies (real-time)
Source: https://www.coingecko.com/ru

## dbt Models
- `crypto_summary` - view with coin name, ticker, current price, market cap, and a price change flag (`is_positive_change`)

## How to run
1. Run ETL scripts in order:
python extract.py
python transform.py
python load.py
3. Run dbt model:
cd crypto_dbt
dbt run