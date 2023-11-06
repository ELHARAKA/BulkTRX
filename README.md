# BulkTRX

BulkTRX is a simple yet powerful script designed to facilitate the batch checking of TRX and token balances for multiple addresses on the TRON network.

## Features

- Batch processing: Check balances for multiple addresses in one go.
- Rate limiting: Respects the TRON API's rate limit for optimal performance without hitting the limit.
- Ease of use: Simple setup process and user-friendly interface.

## Getting Started

To use BulkTRX, you need to have the following prerequisites set up:

- Python 3.6 or higher
- The `requests` library for making HTTP requests
- The `tronapi` library to interact with the TRON blockchain

Additionally, you'll need a free API key from Tronscan.

### Installation

1. **Install Python libraries**:
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

* Note: Ensure addresses are listed one per line in `addr.txt` before running the script.
* To check TRX balances, simply run the script without any arguments:

```bash
python3 BulkTRX.py
```

* To check token balances, add --token followed by the contract address.

```bash
python3 BulkTRX.py --token=<TOKEN_CONTRACT_ADDRESS>
```

* The script tracks progress in the terminal and upon completion, lists found balances, also saved in `found.txt`.

## Contributing

Contributions make the open-source community an incredible place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

## License

Distributed under the MIT License.
