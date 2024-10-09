import requests

def get_exchange_rate(base_currency, target_currency):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    response = requests.get(url, params={'apikey': api_key})
    data = response.json()
    
    if response.status_code == 200:
        return data['rates'].get(target_currency)
    else:
        print(f"Failed to fetch exchange rate: {data.get('description')}")

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (e.g., USD, EUR, GBP): ").upper()
    to_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    else:
        print("Failed to perform conversion.")

if __name__ == "__main__":
    main()
