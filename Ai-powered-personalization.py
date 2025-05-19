import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Sample user-product interaction data
data = {
    'User': ['Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave'],
    'Product': ['Laptop', 'Phone', 'Phone', 'Tablet', 'Laptop', 'Tablet', 'Phone'],
    'Rating': [5, 3, 4, 4, 4, 5, 2]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a user-product matrix
user_product_matrix = df.pivot_table(index='User', columns='Product', values='Rating').fillna(0)

# Normalize data (optional but helps with similarity)
scaler = StandardScaler()
normalized_matrix = scaler.fit_transform(user_product_matrix)

# Compute cosine similarity between users
user_similarity = cosine_similarity(normalized_matrix)

# Create a similarity DataFrame
similarity_df = pd.DataFrame(user_similarity, index=user_product_matrix.index, columns=user_product_matrix.index)

# Function to recommend products
def recommend_products(target_user, top_n=2):
    similar_users = similarity_df[target_user].sort_values(ascending=False)[1:]  # Exclude self
    recommendations = {}

    for user, similarity_score in similar_users.items():
        user_ratings = user_product_matrix.loc[user]
        for product, rating in user_ratings.items():
            if user_product_matrix.loc[target_user, product] == 0:  # if target user hasn't rated
                if product not in recommendations:
                    recommendations[product] = 0
                recommendations[product] += rating * similarity_score

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [product for product, score in sorted_recommendations[:top_n]]

# Example usage
print("Recommendations for Alice:", recommend_products('Alice'))
