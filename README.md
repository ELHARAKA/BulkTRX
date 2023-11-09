# BulkTRX

BulkTRX is a Python-based utility for efficiently checking TRX and TRC20 token balances across multiple accounts on the TRON blockchain. It supports input from both TRON addresses and private keys, streamlining the process for users and developers managing multiple wallets.

## Features

- **Dual Input Compatibility**: Accepts both TRON addresses and private keys from a single input file.
- **Batch Processing**: Enables the simultaneous balance checking of numerous accounts.
- **API Rate Limit Compliance**: Designed to respect TRON API's rate limits, preventing overuse penalties.
- **Real-Time Feedback**: Provides progress updates and summaries directly in the console.
- **Error Logging**: Outputs invalid entries to a separate file for easy correction and reprocessing.

## Prerequisites

- Python 3.6 or higher
- `requests` library
- `tronapi` library
- Tronscan API key

## Installation

- **Install the required Python libraries**:
   Run the following command to install the necessary Python libraries:

   ```bash
   pip install requests tronapi
   ```
### Obtain a Tronscan API Key

1. Visit [Tronscan](https://tronscan.org) and sign up for an account if you haven't already.
2. Navigate to the API Key section and generate a new API key.

### Configure your API key

- On the first run of the script, it will prompt you to enter your Tronscan API Key.
- Alternatively, you can manually create a file named `api.txt` in the same directory as the script and paste your API key there.

## Usage

* Prepare an input file named wallets.txt with TRON addresses or private keys, each on a new line.
* Run BulkTRX:

```bash
python3 BulkTRX.py
```

* To check balances for a specific token, use the `--token` argument

```bash
python3 BulkTRX.py --token=<TOKEN_CONTRACT_ADDRESS>
```

* Found balances will be saved in `found.txt`. Addresses or keys that could not be processed will be logged in `invalid.txt`.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **highly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

## License

Distributed under the MIT License.
