# 📱 UPI QR Code Generator

A simple Python script to generate **QR codes for UPI payments** using popular apps like **PhonePe**, **Paytm**, and **Google Pay**.

With this tool, users can generate and display a QR code linked to their UPI ID that can be scanned to receive payments easily.

---

## ⚙️ Features

- Supports **PhonePe**, **Paytm**, and **Google Pay**
- Generates a valid `upi://pay` URL
- Displays a scannable QR code
- Customizable UPI ID and app selection

---

## 💻 Prerequisites

- Python 3.x
- `qrcode` library (install via pip)

### Install the required package:

bash
- `pip install qrcode[pil]`

## 🚀 How to Use
1. Run the Script
bash
`python generate_upi_qr.py`

2. Input Details
- Enter your UPI ID (e.g., username@bank)
- Choose the desired payment app (PhonePe, Paytm, or Google Pay)

3. QR Code Display
- A scannable QR code will be displayed
- Anyone can scan it via the selected UPI app to send payments

## 🔒 Disclaimer
- Always verify QR codes before using them for payments.
- This tool is for personal or demonstration purposes only.

## 🙌 Acknowledgments
- qrcode Python library
- UPI deep linking standards by NPCI
