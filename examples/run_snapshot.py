"""Call the paid Actor toninovo/google-shopping-price-intelligence. Docs example only."""

import os

from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    raise SystemExit("Set APIFY_TOKEN before running.")

client = ApifyClient(token)
run = client.actor("toninovo/google-shopping-price-intelligence").call(
    run_input={
        "queries": ["wireless earbuds"],
        "country": "us",
        "language": "en",
        "limit": 10,
        "maxAttempts": 2,
    },
    max_total_charge_usd=0.10,
)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(
        item.get("title"),
        item.get("priceNumeric"),
        item.get("currency"),
        item.get("merchant"),
        item.get("link"),
        item.get("queryMinPrice"),
        item.get("queryMedianPrice"),
        item.get("queryMaxPrice"),
    )
