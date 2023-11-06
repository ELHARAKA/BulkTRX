# BulkTRX
# Version: 1.0.0
# Developed by Fahd El Haraka ©
# Email: fahd@web3dev.ma
# Telegram: @thisiswhosthis
# Website: https://web3dev.ma
# GitHub: https://github.com/ELHARAKA

import os
import sys
import time
import requests
import concurrent.futures
from tronapi import Tron
from tronapi import HttpProvider

# Constants for API rate limiting
MAX_CALLS_PER_SECOND = 5
SLEEP_TIME = 1.0 / MAX_CALLS_PER_SECOND
start_time = time.time()

# Parse command line arguments for token contract
token_contract = None
for arg in sys.argv:
    if arg.startswith('--token='):
        token_contract = arg.split('=')[1]

# Initialize Tron API with the provided node details
full_node = HttpProvider('https://api.trongrid.io')
solidity_node = HttpProvider('https://api.trongrid.io')
event_server = HttpProvider('https://api.trongrid.io')

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)

def get_api_key():
    api_key_file = 'api.txt'
    api_key = None

    if os.path.isfile(api_key_file):
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
    else:
        api_key = input("First run, Enter your Tronscan API Key: ").strip()
        with open(api_key_file, 'w') as file:
            file.write(api_key)

    return api_key

API_KEY = get_api_key()

def get_trx_balance(address):
    time.sleep(SLEEP_TIME)
    balance_sun = tron.trx.get_balance(address)
    return balance_sun / 1_000_000

def get_token_balance(address, contract_address):
    time.sleep(SLEEP_TIME)
    url = f"https://apilist.tronscanapi.com/api/account/wallet?address={address}&asset_type=0"
    headers = {
        "TRON-PRO-API-KEY": API_KEY,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        balance = 0
        token_abbr = ""
        for token in result['data']:
            if token['token_id'] == contract_address:
                balance = float(token['balance'])
                token_abbr = token['token_abbr']
                return balance, token_abbr
    return 0, ""

def save_found_addresses(address, trx_balance, token_balance=None):
    with open('found.txt', 'a') as f:
        balance_info = f'{address} : TRX {trx_balance}'
        if token_balance is not None:
            balance_info += f', Token {token_balance}'
        f.write(balance_info + '\n')

def print_progress(count, total):
    elapsed_time = time.time() - start_time
    if count > 0:
        estimated_total_time = elapsed_time / (count / total)
        remaining_time = estimated_total_time - elapsed_time
    else:
        remaining_time = 0

    percent_complete = (count / total) * 100
    remaining_seconds = int(remaining_time % 60)
    remaining_minutes = int(remaining_time // 60)

    progress_text = f"\rProgress: ({count}/{total}) {percent_complete:.2f}% Complete - {remaining_minutes} min {remaining_seconds} sec left..."
    sys.stdout.write(progress_text)
    sys.stdout.flush()

def check_address(address):
    trx_balance = get_trx_balance(address)
    token_balance = None
    token_abbr = ""

    if token_contract:
        token_balance, token_abbr = get_token_balance(address, token_contract)
        if token_balance is None:
            token_balance = 0

    if trx_balance > 0 or (token_balance is not None and token_balance > 0):
        save_found_addresses(address, trx_balance, token_balance)
        return {'address': address, 'trx': trx_balance, 'token': token_balance, 'token_abbr': token_abbr}
    return None

def main():
    global start_time
    start_time = time.time()
    with open('addr.txt') as f:
        addresses = f.read().splitlines()

    total_addresses = len(addresses)
    found_balances = []

    chunks = [addresses[i:i + 4] for i in range(0, len(addresses), 4)]

    total_processed = 0

    for _, address_chunk in enumerate(chunks):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_address = {executor.submit(check_address, address): address for address in address_chunk}
            for future in concurrent.futures.as_completed(future_to_address):
                try:
                    balance_info = future.result()
                    if balance_info:
                        found_balances.append(balance_info)
                except Exception as exc:
                    address = future_to_address[future]
                    print(f"\n{address} generated an exception: {exc}")

        total_processed += len(address_chunk)
        print_progress(total_processed, total_addresses)

        time.sleep(1)

    sys.stdout.write("\rFinished checking all addresses. Check 'found.txt' file." + " " * 50 + "\n")
    sys.stdout.flush()

    if found_balances:
        print("Addresses with balances found:")
        for balance in found_balances:
            print(f"{balance['address']} : {balance['trx']} TRX, {balance['token']} {balance['token_abbr']}")

if __name__ == "__main__":
    main()
