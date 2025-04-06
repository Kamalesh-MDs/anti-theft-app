import cv2

cam = cv2.VideoCapture(0)
ret, frame = cam.read()

if ret:
    cv2.imwrite("Proof.jpg",frame)
    print("Image saved.")
else:
    print("Failed to capture image." )
cam.release()

import requests

# Get public IP
ip = requests.get("https://api.ipify.org").text
print("Your IP Address:", ip)

# Get location using IP
response = requests.get(f"https://ipapi.co/{ip}/json/")
print("Full location response:")
print(response.text)  # <-- ADD THIS LINE

location_data = response.json()

city = location_data.get("city", "Unknown")
region = location_data.get("region", "Unknown")
country = location_data.get("country_name", "Unknown")

print(f"Location: {city}, {region}, {country}")


import smtplib
from email.message import EmailMessage

def send_email():
    EMAIL_ADDRESS = "kkamal69391@gmail.com"  # your gmail
    EMAIL_PASSWORD = "upif mpdh ktla dpch"  # app password (no spaces!)

    msg = EmailMessage()
    msg['Subject'] = '🚨 Theft Alert Detected!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # send to yourself

    msg.set_content(f"""
ALERT: Suspicious activity detected!

📍 Location: {city}, {region}, {country}
🌐 IP Address: {ip}
Check the attached image for proof.
    """)

    with open("proof.jpg", "rb") as f:
        img_data = f.read()
        msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename='proof.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("✅ Email sent!")

# Call the function
send_email()
