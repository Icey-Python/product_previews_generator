import pandas as pd
import random
from datetime import datetime, timedelta
from review_bodies import review_bodies
from product_review_titles import review_titles
from products import products

names = ["Karen Wong", "Alex Liu", "Sarah Park", "James Kim",
         "Linda Lee", "David Choi", "Emily Chen", "John Wang"]
email_domains = ["@example.com", "@shop.com", "@mail.com"]

# Function to generate random dates


def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


# Initialize start and end date for the random date range
start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 12, 31)

# Create a list to hold all review data
data = []
# Generate 10-20 reviews per product
for product_id, product in enumerate(products, start=1):
    # Create a unique product code
    product_code = f"ATO{str(product_id).zfill(3)}"
    num_reviews = random.randint(15, 20)

    for _ in range(num_reviews):
        # Randomize review details
        title = random.choice(review_titles[product])
        body = random.choice(review_bodies[product])
        rating = random.randint(1, 5)
        review_date = random_date(start_date, end_date).strftime("%Y-%m-%d")
        reviewer_name = random.choice(names)
        reviewer_email = f"{reviewer_name.split()[0][0].lower()}.{reviewer_name.split()[
            1].lower()}{random.choice(email_domains)}"
        product_url = f"https://shop.com/products/{
            product.lower().replace(' ', '-').replace('/', '-')}"
        picture_urls = [f"https://cdn.shopify.com/review-images/{
            product_code}-{i+1}.jpg" for i in range(random.randint(1, 3))]

        # Append each review as a dictionary
        data.append({
            "title": title,
            "body": body,
            "rating": rating,
            "review_date": review_date,
            "reviewer_name": reviewer_name,
            "reviewer_email": reviewer_email,
            "product_url": product_url,
            "picture_urls": str(picture_urls),
            "product_id": product_code,
            "product_handle": product
        })

# Create DataFrame
df = pd.DataFrame(data)
df.drop_duplicates('body')
# Save DataFrame to Excel
df.to_excel("product_reviews.xlsx", index=False)

# save to csv
df.to_csv("product_reviews.csv", index=False)
print("Files created successfully with product review data.")
