import pandas as pd

# --- Step 1: Unified Customer Profile (CDP layer) ---
customers = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'Email': ['alice@example.com', 'bob@example.com', 'carol@example.com', 'dave@example.com'],
    'Phone': ['+1234567890', '+1234567891', '+1234567892', '+1234567893'],
    'LastVisit': ['2024-05-01', '2024-05-10', '2024-04-28', '2024-05-12'],
    'PagesViewed': [20, 5, 15, 2],
    'Purchases': [4, 0, 1, 0]
})

# --- Step 2: Segment Customers ---
def segment_customer(row):
    if row['Purchases'] >= 3:
        return 'Loyal'
    elif row['PagesViewed'] >= 10:
        return 'Interested'
    else:
        return 'New'

customers['Segment'] = customers.apply(segment_customer, axis=1)

# --- Step 3: Personalize Message Per Channel ---

# Email Messages
def email_message(name, segment):
    if segment == 'Loyal':
        return f"Hi {name}, thanks for being a top customer! Here's 20% off your next order."
    elif segment == 'Interested':
        return f"Hi {name}, we noticed your interest. Explore personalized picks!"
    else:
        return f"Hi {name}, welcome! Enjoy 10% off your first purchase."

# SMS Messages
def sms_message(name, segment):
    if segment == 'Loyal':
        return f"{name}, VIP alert! 20% off + free shipping!"
    elif segment == 'Interested':
        return f"{name}, we saved items just for you!"
    else:
        return f"{name}, get started with 10% off now."

# Push Notification Messages
def push_message(name, segment):
    if segment == 'Loyal':
        return "New arrivals just for you, loyal shopper!"
    elif segment == 'Interested':
        return "Finish your wishlist—limited time deals inside!"
    else:
        return "Welcome! Discover products tailored to you."

customers['EmailMsg'] = customers.apply(lambda r: email_message(r['Name'], r['Segment']), axis=1)
customers['SMSMsg'] = customers.apply(lambda r: sms_message(r['Name'], r['Segment']), axis=1)
customers['PushMsg'] = customers.apply(lambda r: push_message(r['Name'], r['Segment']), axis=1)

# --- Step 4: Simulate Sending ---
def simulate_sending(row):
    print(f"\n--- Sending to {row['Name']} ---")
    print(f"Email to {row['Email']}: {row['EmailMsg']}")
    print(f"SMS to {row['Phone']}: {row['SMSMsg']}")
    print(f"Push Notification: {row['PushMsg']}")

customers.apply(simulate_sending, axis=1)
