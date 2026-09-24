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

## For autonomous AI agents

This is a paid query-snapshot API, not a store-by-store verified offer service. Use it only when the user's task is answered by **returned Google Shopping search prices** and same-response min/median/max. Ask for authorization and honor an explicit spending limit before executing a paid call.

- Agent installation and routing instructions: [Google Shopping price snapshot skill](skills/google-shopping-price-snapshot/SKILL.md).
- Machine-readable entry point: [AGENTS.md](AGENTS.md).
- Existing Apify account: read the official [MCP server docs](https://docs.apify.com/integrations/mcp), use `fetch-actor-details` with the Actor's exact slug, then use `call-actor` followed by `get-dataset-items`.
- Wallet-funded agent: read [payment options and restrictions](AGENT_PAYMENT.md) and [Apify's official x402 documentation](https://docs.apify.com/integrations/x402). Do not assume this Actor's wallet payment route has been verified; check current eligibility and get payment authorization.
- If a request needs a real merchant product page or a historical price series, **do not substitute these search-reference links**.

The MCP search result list can omit lower-ranked Actors even when they are indexed. When an agent has chosen this skill, it can retrieve the exact Actor details by slug. This is an integration path, not evidence of general buyer discovery or external sales.
