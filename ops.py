import click
from eth_account import Account
import requests

FAUCET_SERVER_URL = "https://your-faucet-server.com"

@click.group()
def cli():
    pass

@cli.command()
@click.option('--event-code', prompt='Event code', help='Unique event code for the faucet')
def create_faucet(event_code):
    # Generate ephemeral account
    acct = Account.create()
    print(f"Send testnet ETH to this address: {acct.address}")
    
    # Send event code and private key to faucet server
    response = requests.post(f"{FAUCET_SERVER_URL}/create_faucet", json={
        "event_code": event_code,
        "private_key": acct.key.hex()
    })
    if response.ok:
        print("Faucet created successfully.")
    else:
        print("Error creating faucet:", response.text)

@cli.command()
@click.option('--address', prompt='Your wallet address', help='Your wallet address to receive ETH')
@click.option('--event-code', prompt='Event code', help='Event code to claim from')
def claim(address, event_code):
    # Request faucet drip
    response = requests.post(f"{FAUCET_SERVER_URL}/claim", json={
        "address": address,
        "event_code": event_code
    })
    if response.ok:
        print("Claim successful! Check your wallet.")
    else:
        print("Claim failed:", response.text)

if __name__ == '__main__':
    cli()
