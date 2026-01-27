import os
import urllib.request
import dotenv
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

try:

    # Loading variables from the .env file
    dotenv.load_dotenv()

    # Retrieving credentials from environment variables
    __EMAIL_ADDRESS = os.getenv('EMAIL_USER')
    __EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

    url = "https://www.python.org/static/img/python-logo.png"

    msg = MIMEMultipart()
    msg['From'] = __EMAIL_ADDRESS
    msg['To'] = 'sammehta063@gmail.com'
    msg['Subject'] = 'Automated Email with Image Attachment'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(__EMAIL_ADDRESS, __EMAIL_PASSWORD)

    # Fetching the image from the URL
    response = urllib.request.urlopen(url)
    image_data = response.read()

    # Creating the HTML content with the embedded image
    html = f"""
            <html>
                <body>
                    <h1>This is an automated email with an image</h1>
                    <img src="cid:python_logo">
                </body>
            </html>
            """
    
    msg.attach(MIMEText(html, 'html'))

    image = MIMEImage(image_data)
    image.add_header('Content-ID', '<python_logo>')
    msg.attach(image)
    server.send_message(msg)

    server.quit()
    print("Email sent successfully with image attachment.")

except Exception as e:
    logging.error(f"Failed to send email: {e}")
    print(f"Failed to send email: {e}")