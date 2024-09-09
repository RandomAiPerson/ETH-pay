import streamlit as st

# Streamlit UI
st.title("ETH Payment App")

# Input recipient address
recipient_address = st.text_input("Recipient Address", "")

# Slider for ETH amount
eth_amount = st.slider("Select amount of ETH to send", 0.01, 5.0, step=0.01)

# Button to generate payment link
if st.button("Generate Payment Link"):
    if recipient_address:
        # Generate the payment URL for MetaMask
        transaction_url = f"ethereum:{recipient_address}?value={int(eth_amount * 10**18)}"

        # Show the payment link
        st.write(f"Send {eth_amount} ETH to {recipient_address}")
        st.write(f"Payment URL (MetaMask): [Click here to pay](https://metamask.io)")

        # Alternatively, show the raw transaction URL
        st.write(f"Ethereum payment URL: `{transaction_url}`")

        st.info("Copy and paste this URL into MetaMask or scan it using a wallet app to complete the payment.")
    else:
        st.error("Please enter a valid recipient address.")
