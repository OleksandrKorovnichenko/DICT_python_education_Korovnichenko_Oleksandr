import requests


# Function to get exchange rate from FloatRates API or cache
def get_exchange_rate(base, target):
    url = f'https://www.floatrates.com/daily/{base}.json'
    response = requests.get(url)
    data = response.json()
    rate = data[target.lower()]['rate']
    return rate


base_currency = input("Please enter your base currency code (e.g., USD): ")
# Save exchange rates for USD and EUR
usd_exchange_rate = get_exchange_rate(base_currency, 'USD')
eur_exchange_rate = get_exchange_rate(base_currency, 'EUR')

# Main program loop
while True:
    if not base_currency:
        break

    target_currency = input("Please enter the target currency code: ")
    amount = float(input("Please enter the amount of money you want to exchange: "))

    if target_currency == 'USD':
        print("Checking the cache...")
        print("It is in the cache!")
        exchange_rate = usd_exchange_rate
    elif target_currency == 'EUR':
        print("Checking the cache...")
        print("It is in the cache!")
        exchange_rate = eur_exchange_rate
    else:
        print("Checking the cache...")
        print("Sorry, but it is not in the cache!")
        exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate

        print(f"You received {converted_amount:.2f} {target_currency}.\n")

print("Program terminated.")
