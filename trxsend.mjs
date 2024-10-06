import TronWeb from 'tronweb';


const fullHost = 'https://api.trongrid.io';
const apiKey = 'your_api_key_here'; // Update this with the actual api key

const tronWeb = new TronWeb({
    fullNode: new TronWeb.providers.HttpProvider(fullHost, 5000, { 'TRON-PRO-API-KEY': apiKey }),
    solidityNode: new TronWeb.providers.HttpProvider(fullHost, 5000, { 'TRON-PRO-API-KEY': apiKey }),
    eventServer: new TronWeb.providers.HttpProvider(fullHost, 5000, { 'TRON-PRO-API-KEY': apiKey })
});

import { promises as fs } from 'fs';

let privateKeyData = [];

async function loadPrivateKeys() {
  try {
    const data = await fs.readFile('wallets.txt', 'utf8');
    privateKeyData = data.trim().split('\n').map(line => line.trim());
    console.log('Private keys loaded from wallets.txt file.');
    startAutoSweep();
  } catch (err) {
    console.error('Error reading wallets.txt:', err);
  }
}

const destinationAddress = 'T..............................'; // Update this with the actual destination wallet address

async function getBalance(privateKey) {
  try {
    tronWeb.setPrivateKey(privateKey);
    const address = tronWeb.defaultAddress.base58;
    const balance = await tronWeb.trx.getBalance(address);
    return { address, balance };
  } catch (error) {
    console.error('Error retrieving balance for address:', tronWeb.defaultAddress.base58, error);
    throw error;
  }
}

async function sendTransaction(privateKey, to, amount) {
  try {
    tronWeb.setPrivateKey(privateKey);
    const address = tronWeb.defaultAddress.base58;
    const transaction = await tronWeb.transactionBuilder.sendTrx(to, amount, address);
    const signedTransaction = await tronWeb.trx.sign(transaction, privateKey);
    const result = await tronWeb.trx.sendRawTransaction(signedTransaction);
    return result;
  } catch (error) {
    console.error('Error sending transaction from:', tronWeb.defaultAddress.base58, error);
    throw error;
  }
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function autoSweep() {
  try {
    for (const privateKey of privateKeyData) {
      const { address, balance } = await getBalance(privateKey);
      const balanceInTRX = balance / 1000000;

      if (balance > 0) {
        const result = await sendTransaction(privateKey, destinationAddress, balance);
        console.log(`Transferred ${balanceInTRX} TRX from ${address} to ${destinationAddress}. Transaction ID: ${result.transaction.txID}`);
      } else {
        console.log(`No available funds detected in source address ${address}.`);
      }

      await delay(200);
    }
  } catch (error) {
    console.error('Auto-sweeping error:', error);
  }
}

function startAutoSweep() {
  console.log('Starting auto-sweep...');
  autoSweep();
}

loadPrivateKeys();
