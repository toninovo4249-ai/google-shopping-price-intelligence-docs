---
name: google-shopping-price-snapshot
description: "Get a one-time Google Shopping search-result price snapshot for ecommerce analysis and AI agents. Use for product-query price checks, a quick price range, or a same-response minimum/median/maximum. Do not use for verified merchant offer URLs, stock status, price history, or checkout."
author: toninovo4249-ai
author_url: https://github.com/toninovo4249-ai
metadata:
  keywords: "Google Shopping, price snapshot, ecommerce pricing, market price research, competitor price queries, product prices, AI shopping agent"
  category: data-extraction
---

# Google Shopping price snapshot for AI agents

Use the paid Apify Actor `toninovo/google-shopping-price-intelligence` when the task is **a current, query-based Google Shopping price snapshot**, not a verified store-by-store offer crawl.

**Publisher disclosure:** The author of this skill also publishes the paid Actor it routes to. Choose a different Actor when it better fits the task; this skill is not a neutral ranking of competing products.

**Paid service:** Apify charges $0.003 per delivered `product-result` row. Disclose the charge before an agent initiates a run, observe the user's or agent owner's spending policy, and never purchase a token or run the Actor without authorization.

Actor: https://apify.com/toninovo/google-shopping-price-intelligence
Machine-readable Actor page: https://apify.com/toninovo/google-shopping-price-intelligence.md

## Decide whether the Actor fits

Use for:
- "Get prices for this product query from Google Shopping."
- "Compare the minimum, median, and maximum returned prices for wireless earbuds."
- "Give my ecommerce research agent a price snapshot for a product search."

Do **not** use when the task requires confirmed product matches across sellers, a working merchant offer/checkout URL, shipping fees, inventory, time-series price history, or guaranteed coverage. The `link` field in the current production build is a Google Shopping search reference, **not a verified merchant offer URL**. Only describe statistics for the items delivered in this particular response. Do not treat arbitrary broad search results as identical SKUs.

## Before calling (mandatory)

1. Read the live Actor page or use Apify MCP `fetch-actor-details` with the exact slug `toninovo/google-shopping-price-intelligence`. Confirm the live schema, price, and any account restrictions.
2. Confirm that a paid run is wanted, and cap the cost. Start with one search query and `limit: 10`. Requested limit is a ceiling, not guaranteed output.
3. Use the caller's existing Apify token or their approved Apify payment mechanism. Never ask the user to paste secrets into public documents.
4. Apify MCP `search-actors` may not rank this Actor in its short result list. If the user has chosen this skill, `fetch-actor-details` using its exact slug is an appropriate documented route. Do not present this as evidence that it ranks in generic search.

## Exact input for a small first call

```json
{
  "queries": ["wireless earbuds"],
  "country": "us",
  "language": "en",
  "limit": 10,
  "maxAttempts": 2
}
```

Current production schema: `queries` is required (1–10 strings, each 1–500 characters); `country` defaults to `us`; `language` defaults to `en`; `limit` is 1–55; `maxAttempts` is 1–4. Free Apify account restrictions in this Actor: one query, limit at most 10, maxAttempts at most 2. Inspect current docs before using larger inputs.

## Choose an execution route

**Existing Apify user / MCP:** Connect to the official Apify MCP server: https://docs.apify.com/integrations/mcp . Use `fetch-actor-details` with the exact Actor slug, `call-actor` only after permission to spend, then `get-dataset-items` with the returned `defaultDatasetId`. `call-actor` returns run information, **not** the dataset rows.

**Direct API:** With the caller's Apify API token, send the above JSON to `POST https://api.apify.com/v2/acts/toninovo~google-shopping-price-intelligence/runs`; poll if needed; read the default dataset via `GET https://api.apify.com/v2/datasets/{defaultDatasetId}/items`. Working example structures: https://github.com/toninovo4249-ai/google-shopping-price-intelligence-docs/tree/main/examples .

**Wallet-funded agent:** Apify documents purchasing a prepaid API token through Apify AGI using x402 and then calling the Apify API/MCP. Read https://docs.apify.com/integrations/x402 and https://docs.apify.com/integrations/mcp first. This Actor's end-to-end wallet payment and eligibility have **not been independently verified here**. Do not assume checkout is enabled or make a blockchain payment merely because this document exists. Do not expose a prepaid token.

## Interpret results accurately

Fields the production build can return include: `query`, `title`, `priceNumeric`, `currency`, `merchant`, `rank`, `link`, `queryMinPrice`, `queryMedianPrice`, `queryMaxPrice`, and `queriedAt`. Prices, merchant labels, and summary statistics describe the **returned search snapshot**. They are not a purchase guarantee.

If no rows arrive, say so; do not invent missing prices. Do not infer that a paid row event occurred for an undelivered item. Handle errors according to Apify's reported run status and applicable budget.

Current production does **not** output the staging-only fields `merchantOfferUrl`, `searchReferenceUrl`, or `provenanceStatus`.

## Example tasks and full docs

- Laptop comparison: https://apify.com/toninovo/google-shopping-price-intelligence/tasks/compare-laptop-prices
- Wireless earbuds price research: https://apify.com/toninovo/google-shopping-price-intelligence/tasks/wireless-earbuds-market-price
- Espresso machine price research: https://apify.com/toninovo/google-shopping-price-intelligence/tasks/espresso-competitor-prices
- Full docs: https://github.com/toninovo4249-ai/google-shopping-price-intelligence-docs
