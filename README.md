
# OptimismFaucet - Superchain Faucet

The **OptimismFaucet** project provides a Superchain Faucet that allows developers to obtain free testnet ETH tokens for testing and development on multiple Optimism testnet chains.

---

## Overview

- Supports testnet ETH distribution for various Optimism chains including:
  - OP Sepolia
  - Base Sepolia
  - PGN Sepolia
  - Zora Sepolia
  - Other OP Chains in the Superchain ecosystem
- Enables developers to test smart contracts and dApps without spending real ETH.
- Uses enhanced authentication methods including onchain identity and social authentication to prevent abuse.
- Allows claiming up to 1 testnet ETH per day, significantly more than traditional faucets.
- Built with Python.

---

## Features

- Fast and reliable faucet for Optimism testnets.
- Supports multiple chains within the Optimism Superchain.
- Onchain identity verification (e.g., via Optimist NFT) for increased claim limits.
- Social authentication via GitHub also supported.
- Open source under the MIT License.

---

## How to Use

1. Connect your wallet (e.g., MetaMask) to the Superchain Faucet interface.
2. Authenticate using onchain identity (Optimist NFT) or social login.
3. Request testnet ETH for your desired Optimism testnet chain.
4. Receive testnet tokens instantly to your wallet.
5. Use tokens to deploy and test smart contracts or dApps on Optimism testnets.

---

## Getting Started

To run or contribute to the faucet:

1. Clone the repository:
   ```
   git clone https://github.com/tm-0430/OptimismFaucet.git
   ```
2. Install dependencies (Python required):
   ```
   pip install -r requirements.txt
   ```
3. Configure environment variables and API keys as needed.
4. Run the faucet service:
   ```
   python ops.py
   ```

---

## Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---
