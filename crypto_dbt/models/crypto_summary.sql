SELECT id,
symbol,
current_price,
market_cap,
CASE WHEN price_change_percentage_24h > 0 THEN true
ELSE false
END AS is_positive_change,
extracted_at
FROM {{ source('public', 'crypto_prices') }}
