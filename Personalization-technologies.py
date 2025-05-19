import pandas as pd
from sklearn.cluster import KMeans

# --- Step 1: Unified Customer Data (CDP) ---
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'Email': ['a@ex.com', 'b@ex.com', 'c@ex.com', 'd@ex.com', 'e@ex.com'],
    'PagesViewed': [30, 5, 10, 15, 2],
    'Purchases': [5, 0, 1, 2, 0],
    'TotalSpent': [300, 0, 60, 150, 0]
})

# --- Step 2: AI-based Segmentation using Clustering ---
features = customers[['PagesViewed', 'Purchases', 'TotalSpent']]
kmeans = KMeans(n_clusters=3, random_state=42)
customers['Segment'] = kmeans.fit_predict(features)

# Rename segments for marketing clarity
segment_names = {
    0: 'High Value',
    1: 'New Visitor',
    2: 'Potential Buyer'
}
customers['SegmentName'] = customers['Segment'].map(segment_names)

# --- Step 3: Personalized Product Recommendations (rule-based for demo) ---
def recommend_products(segment):
    if segment == 'High Value':
        return 'Premium Plan, Exclusive Offers'
    elif segment == 'Potential Buyer':
        return 'Discounted Starter Kits, Demo Trial'
    else:
        return 'Welcome Guide, Signup Bonus'

customers['ProductRecommendation'] = customers['SegmentName'].apply(recommend_products)

# --- Step 4: Personalized Marketing Message ---
def generate_message(name, segment):
    if segment == 'High Value':
        return f"Hi {name}, thank you for being a loyal customer! Enjoy VIP rewards just for you."
    elif segment == 'Potential Buyer':
        return f"Hi {name}, you’re close to unlocking member perks! Grab a deal today."
    else:
        return f"Hi {name}, welcome! Here's a 10% discount to get started."

customers['MarketingMessage'] = customers.apply(
    lambda row: generate_message(row['Name'], row['SegmentName']), axis=1)

# --- Step 5: Next Best Experience Action ---
def next_best_action(segment):
    if segment == 'High Value':
        return 'Assign loyalty manager and send gift box'
    elif segment == 'Potential Buyer':
        return 'Send trial code and onboarding email'
    else:
        return 'Send welcome series and tutorial'

customers['NextBestAction'] = customers['SegmentName'].apply(next_best_action)
