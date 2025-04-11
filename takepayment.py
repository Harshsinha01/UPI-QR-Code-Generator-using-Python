import qrcode

# Taking UPI ID and app choice as input
upi_id = input("Enter your UPI ID: ")
print("Select the payment app for which you want to generate the QR code:")
print("1. PhonePe")
print("2. Paytm")
print("3. Google Pay")
choice = input("Enter the number corresponding to your choice (1/2/3): ")

# Generating the URL based on the choice
if choice == "1":
    app_name = "PhonePe"
    payment_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
elif choice == "2":
    app_name = "Paytm"
    payment_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
elif choice == "3":
    app_name = "Google Pay"
    payment_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
else:
    print("Invalid choice. Exiting...")
    exit()

# Create and display the QR code for the selected app
qr_code = qrcode.make(payment_url)
print(f"Displaying QR code for {app_name}...")
qr_code.show()
