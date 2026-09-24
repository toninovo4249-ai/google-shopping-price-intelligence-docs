# Payment routes for AI agents

The existing paid Apify Actor is **toninovo/google-shopping-price-intelligence**.
Public Actor facts and live price: https://apify.com/toninovo/google-shopping-price-intelligence.md

## Recommended first route: an existing Apify token

An AI application with a user-authorized Apify account and token can call the current production Actor directly or through the official Apify MCP server. Billing is by the Actor's `product-result` event, published as **$0.003 per delivered product row** at the time these docs were written. Re-check the live Actor page before paying.

A small starter input is:

```json
{"queries":["wireless earbuds"],"country":"us","language":"en","limit":10,"maxAttempts":2}
```

For direct API clients, use the official Apify API and the Python/JavaScript examples in this repo. For MCP, connect through https://docs.apify.com/integrations/mcp , call `fetch-actor-details` with the exact slug, authorize the cost, then `call-actor` and `get-dataset-items`.

## Alternative route: an agent with a funded wallet

Official docs: https://docs.apify.com/integrations/x402 and https://docs.apify.com/integrations/mcp .

Apify describes a wallet-funded path in which an agent uses x402 to purchase a **prepaid Apify API token through Apify AGI**, then uses that token to access the Apify API or MCP. Apify's documentation currently says the minimum prepaid purchase is $1 in USDC on Base, unused prepaid credit expires after 14 days, and unused balance is nonrefundable. Wallet setup may need an authenticated email inbox, USDC, and a small amount of ETH. Check the **current official documentation**: this integration is experimental and its terms can change.

**Important:** This repo does not demonstrate a settled x402 purchase or a wallet-funded run of our Actor. Eligibility, regional availability, fees, and the exact payment route must be checked at execution time. The official docs distinguish prepaid Apify AGI access from per-request direct agentic payment eligibility. Do not claim our Actor has a verified direct x402 checkout.

1. Confirm whether the intended payment route supports this Actor with Apify's current public eligibility/selection rules.
2. Obtain human or delegated payment authorization, including a spending limit.
3. Follow Apify's official wallet and prepaid token workflow; do **not** publish wallet secrets or prepaid tokens.
4. Use the resulting approved token to call the Actor with the small JSON input above.
5. Read the run's default dataset and report delivered rows and actual charges when the account makes them available. Do not claim a successful payment merely because the API examples are published.

## Fit and result limits

The current production output is **Google Shopping search-result price data**, with numerical prices, merchant labels, and same-response minimum/median/maximum statistics. The `link` field is a Google Shopping search reference, not a verified merchant product offer. Avoid this Actor when a buyer needs actual product offers with confirmed merchant URLs, checkout, stock, shipping or historical price movements.

These instructions help an agent integrate; they are **not** evidence of external paid demand or proven net profit.
