import streamlit as st
from web3 import Web3

# Initialize Web3
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Use your Infura project ID
web3 = Web3(Web3.HTTPProvider(infura_url))

# Streamlit UI
st.title("ETH Payment App")

# Input fields
recipient_address = st.text_input("Recipient Address", "")
sender_private_key = st.text_input("Sender Private Key", "", type="password")
eth_amount = st.slider("Select amount of ETH to send", 0.01, 5.0, step=0.01)

# Display current balance (optional)
if st.button("Check Balance"):
    if web3.isAddress(recipient_address):
        balance = web3.eth.get_balance(recipient_address)
        st.write(f"Recipient balance: {web3.fromWei(balance, 'ether')} ETH")
    else:
        st.error("Invalid recipient address")

# Send ETH transaction
if st.button("Send ETH"):
    if web3.isAddress(recipient_address) and sender_private_key:
        try:
            sender_address = web3.eth.account.from_key(sender_private_key).address
            nonce = web3.eth.getTransactionCount(sender_address)
            
            # Build transaction
            tx = {
                'nonce': nonce,
                'to': recipient_address,
                'value': web3.toWei(eth_amount, 'ether'),
                'gas': 21000,
                'gasPrice': web3.toWei('50', 'gwei'),
            }

            # Sign and send the transaction
            signed_tx = web3.eth.account.sign_transaction(tx, sender_private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

            # Transaction hash
            st.success(f"Transaction successful! TX Hash: {web3.toHex(tx_hash)}")
        except Exception as e:
            st.error(f"Error sending transaction: {str(e)}")
    else:
        st.error("Invalid recipient address or private key")

