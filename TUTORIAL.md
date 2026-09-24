# Call the paid Google Shopping price Actor

Use the existing Actor `toninovo/google-shopping-price-intelligence`:

https://apify.com/toninovo/google-shopping-price-intelligence

Pass `queries`, and optionally `country`, `language`, `limit`, and `maxAttempts`. Read the run's default dataset. Apify charges **$0.003** for each delivered `product-result`. A row that is not delivered is not a `product-result`.

Read `priceNumeric`, `currency`, `merchant`, and `link`. Also read `queryMinPrice`, `queryMedianPrice`, and `queryMaxPrice` from that same response. `link` is a Google Shopping search reference. A production sample stored a `google.com/search` URL in that field. Do not present it as a verified merchant offer URL.

Python: [examples/run_snapshot.py](examples/run_snapshot.py). JavaScript: [examples/run_snapshot.mjs](examples/run_snapshot.mjs).

```python
from apify_client import ApifyClient
import os

client = ApifyClient(os.environ["APIFY_TOKEN"])
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
items = client.dataset(run["defaultDatasetId"]).list_items().items
```

If you already know the slug, ask Apify MCP for `fetch-actor-details` before `call-actor`. `search-actors` may leave this Actor off a short result list. `call-actor` spends money and does not replace reading the dataset.

Free Apify accounts stay at one query and 10 products. `maxAttempts` stops at 4. Run the Actor again later if you need another snapshot. It does not store the previous price.

Public tasks with fixed inputs:

- https://apify.com/toninovo/google-shopping-price-intelligence/tasks/compare-laptop-prices
- https://apify.com/toninovo/google-shopping-price-intelligence/tasks/wireless-earbuds-market-price
- https://apify.com/toninovo/google-shopping-price-intelligence/tasks/espresso-competitor-prices
