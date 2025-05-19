import pandas as pd

# Simulated web form data
web_form_data = pd.DataFrame({
    'customer_id': [101, 102],
    'name': ['Alice Johnson', 'Bob Smith'],
    'email': ['alice@example.com', 'bob@example.com'],
    'signup_date': ['2025-01-10', '2025-02-15']
})

# Simulated CRM data
crm_data = pd.DataFrame({
    'customer_id': [101, 102],
    'last_contacted': ['2025-05-01', '2025-05-10'],
    'loyalty_tier': ['Gold', 'Silver']
})

# Simulated transaction data
transactions = pd.DataFrame({
    'customer_id': [101, 101, 102],
    'purchase_date': ['2025-05-01', '2025-05-05', '2025-05-08'],
    'amount': [120.50, 89.99, 45.00]
})

# Aggregate transaction data
transaction_summary = transactions.groupby('customer_id').agg(
    total_spent=pd.NamedAgg(column='amount', aggfunc='sum'),
    total_orders=pd.NamedAgg(column='amount', aggfunc='count')
).reset_index()

# Merge all data
merged_data = web_form_data.merge(crm_data, on='customer_id', how='left')
merged_data = merged_data.merge(transaction_summary, on='customer_id', how='left')

# Display final integrated dataset
print("Integrated Customer Data:")
print(merged_data)
