# BulkTRX

BulkTRX is a Python-based utility for efficiently checking TRX and TRC20 token balances across multiple accounts on the TRON blockchain. It supports input from both TRON addresses and private keys, streamlining the process for users and developers managing multiple wallets.

## Features

- **Dual Input Compatibility**: Accepts both TRON addresses and private keys from a single input file.
- **Batch Processing**: Enables the simultaneous balance checking of numerous accounts.
- **API Rate Limit Compliance**: Designed to respect TRON API's rate limits, preventing overuse penalties.
- **Real-Time Feedback**: Provides progress updates and summaries directly in the console.
- **Error Logging**: Outputs invalid entries to a separate file for easy correction and reprocessing.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.6 or Higher**: Your system must have Python 3.6 or a higher version installed.
- **Python Development Headers**: For compiling certain Python extensions, you need to have Python development headers installed.
  ```bash
  sudo apt-get install python3.9-dev
  ```
- **Required Libraries**:
- `requests`: A library for making HTTP requests. Install it using:
  ```
  pip install requests
  ```
- `tronapi`: A Python API for interacting with Tron (TRX). Install it using:
  ```
  pip install tronapi
  ```
  Note: Installing `tronapi` might require additional dependencies such as `pysha3`, which in turn may require Python development headers to be installed on your system.
- **Tronscan API Key**: You will need a Tronscan API Key for some functionalities. Obtain it from [Tronscan](https://tronscan.org).

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
