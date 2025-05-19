import pandas as pd

# ----- Step 1: Ingest and unify customer data (CDP) -----

# CRM data
crm_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'Email': ['alice@example.com', 'bob@example.com', 'carol@example.com', 'dave@example.com'],
    'SignupDate': ['2023-01-01', '2023-03-12', '2023-06-15', '2023-08-01']
})

# Website interaction data
web_data = pd.DataFrame({
    'CustomerID': [1, 2, 3, 5],
    'LastVisit': ['2024-05-10', '2024-05-08', '2024-05-12', '2024-05-14'],
    'PagesViewed': [15, 7, 3, 8]
})

# Purchase history data
purchase_data = pd.DataFrame({
    'CustomerID': [1, 3, 4],
    'TotalSpent': [350, 80, 150],
    'LastPurchaseDate': ['2024-04-30', '2024-05-05', '2024-05-10']
})

# Support tickets data
support_data = pd.DataFrame({
    'CustomerID': [2, 3, 4],
    'TicketsRaised': [1, 3, 0],
    'LastTicketDate': ['2024-05-01', '2024-04-25', None]
})

# Merge all data into unified CDP profile
cdp = crm_data.merge(web_data, on='CustomerID', how='outer') \
              .merge(purchase_data, on='CustomerID', how='outer') \
              .merge(support_data, on='CustomerID', how='outer')

# Fill missing values
cdp.fillna({
    'Name': 'Unknown',
    'Email': 'Unknown',
    'SignupDate': 'N/A',
    'LastVisit': 'N/A',
    'PagesViewed': 0,
    'TotalSpent': 0,
    'LastPurchaseDate': 'N/A',
    'TicketsRaised': 0,
    'LastTicketDate': 'N/A'
}, inplace=True)

# ----- Step 2: Segment customers -----

def segment_customer(row):
    if row['TotalSpent'] > 300:
        return 'VIP'
    elif row['PagesViewed'] > 10 and row['TotalSpent'] > 50:
        return 'Engaged Buyer'
    elif row['PagesViewed'] > 5:
        return 'Interested'
    elif row['TicketsRaised'] > 2:
        return 'Support Priority'
    else:
        return 'New or Low Engagement'

cdp['Segment'] = cdp.apply(segment_customer, axis=1)

# ----- Step 3: Generate personalized marketing messages -----

def marketing_message(row):
    if row['Segment'] == 'VIP':
        return f"Hi {row['Name']}, thank you for being a VIP customer! Enjoy exclusive offers just for you."
    elif row['Segment'] == 'Engaged Buyer':
        return f"Hi {row['Name']}, thanks for your interest! Here's 15% off your next purchase."
    elif row['Segment'] == 'Interested':
        return f"Hi {row['Name']}, check out our new arrivals tailored for you."
    elif row['Segment'] == 'Support Priority':
        return f"Hi {row['Name']}, we’re here to help! Your satisfaction is our priority."
    else:
        return f"Hi {row['Name']}, welcome! Explore our products and enjoy your shopping."

cdp['MarketingMessage'] = cdp.apply(marketing_message, axis=1)

# ----- Step 4: Simulate personalized customer experience (e.g., next best action) -----

def next_best_action(row):
    if row['Segment'] == 'VIP':
        return "Assign personal account manager and send VIP gift."
    elif row['Segment'] == 'Support Priority':
        return "Prioritize support response and offer compensation."
    elif row['Segment'] == 'Engaged Buyer':
        return "Send personalized product recommendations."
    elif row['Segment'] == 'Interested':
        return "Send discount coupon to encourage purchase."
    else:
        return "Send welcome onboarding content."

cdp['NextBestAction'] = cdp.apply(next_best_action,axis=1)
