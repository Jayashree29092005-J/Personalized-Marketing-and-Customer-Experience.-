import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load customer data
# Example data structure
data = {
    'Name': ['Alice', 'Bob', 'Carol'],
    'Email': ['alice@example.com', 'bob@example.com', 'carol@example.com'],
    'LastPurchase': [45, 120, 5],  # Days ago
    'Segment': ['Active', 'Lapsed', 'New']
}

df = pd.DataFrame(data)

# Email content templates
templates = {
    'Active': "Hi {name}, thank you for being a loyal customer! Check out our latest offers.",
    'Lapsed': "Hi {name}, we miss you! Here's a 20% discount to welcome you back.",
    'New': "Hi {name}, welcome! Here's how to get started with your first purchase."
}

# Email sending function
def send_email(to_email, subject, message):
    from_email = "your_email@example.com"
    from_password = "your_password"  # Use environment variables in production

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        # Use Gmail's SMTP server for demonstration (adjust for your provider)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")

# Automate email sending
for _, row in df.iterrows():
    personalized_msg = templates[row['Segment']].format(name=row['Name'])
    send_email(row['Email'], "Your Personalized Offer", personalized_msg)
