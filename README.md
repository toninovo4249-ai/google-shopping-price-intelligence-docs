# Google Shopping product prices for AI agents — query snapshot + price range

Public integration documentation for a **paid, query-based Google Shopping price snapshot** used by AI shopping assistants, ecommerce market research, and competitor price checks. Get returned numeric prices, merchant labels and same-response minimum, median and maximum. Not a verified retailer-offer feed.

Documentation for the paid Apify Actor [`toninovo/google-shopping-price-intelligence`](https://apify.com/toninovo/google-shopping-price-intelligence).

This repository is documentation only. It does not contain the Actor source.

Send product queries. The default build returns numeric prices, merchant labels, and the minimum, median, and maximum of that response. Each delivered product row costs **$0.003** through Apify pay-per-event billing for the event `product-result`.

Returned `link` values are Google Shopping search references, not verified merchant product offer URLs. A production sample stored a `google.com/search` URL in `link`. Do not treat that field as a merchant checkout page.

## AI agent: quickest route to the paid Actor

**Does your task fit?** Use this Actor for a one-time product-query price snapshot with returned-results minimum, median and maximum. If you need verified merchant product URLs, inventory, shipping, historical prices or checkout, select a different service.

**One small authorized example:** `{"queries":["wireless earbuds"],"country":"us","language":"en","limit":10,"maxAttempts":2}`. Apify charges $0.003 for each delivered `product-result`. Check live price and seek permission before spending.

- Read the [installable Google Shopping price-snapshot agent skill](skills/google-shopping-price-snapshot/SKILL.md), with task selection rules, a small input, output interpretation and MCP workflow.
- Agent skill installers that support GitHub skills can try: `npx skills add https://github.com/toninovo4249-ai/google-shopping-price-intelligence-docs --skill google-shopping-price-snapshot`. Installing a skill does not execute or pay for an Actor run.
- For an existing Apify account, use the official [Apify MCP server](https://docs.apify.com/integrations/mcp). Once this Actor is selected, ask MCP `fetch-actor-details` for `toninovo/google-shopping-price-intelligence`. After authorization, `call-actor` starts the paid run and `get-dataset-items` retrieves its output.
- An agent that already has an authorized Apify API token can use the [Python](examples/run_snapshot.py) or [JavaScript](examples/run_snapshot.mjs) examples.
- Wallet-funded agents: read [payment options and limitations](AGENT_PAYMENT.md) and Apify's current [x402 guide](https://docs.apify.com/integrations/x402). **A successful wallet-funded run of this Actor has not been independently confirmed** by this repository.

**Important:** `link` is a Google Shopping **search reference**, not a verified merchant offer URL; summaries cover only items returned in this response.

## Use the existing Actor

- Store: https://apify.com/toninovo/google-shopping-price-intelligence
- Machine-readable store page: https://apify.com/toninovo/google-shopping-price-intelligence.md
- Run: `POST https://api.apify.com/v2/acts/toninovo~google-shopping-price-intelligence/runs`
- Dataset: `GET https://api.apify.com/v2/datasets/{defaultDatasetId}/items`

Apify MCP can load the Actor with `fetch-actor-details` for the slug `toninovo/google-shopping-price-intelligence`. `search-actors` can omit it when the result list stops before its rank. `call-actor` spends money. This documentation does not claim that an autonomous agent wallet checkout is enabled.

## Input

| Field | Rule |
| --- | --- |
| `queries` | Required. 1 to 10 strings, each 1 to 500 characters. |
| `country` | Default `us`. |
| `language` | Default `en`. |
| `limit` | 1 to 55. Default 55. A ceiling, not a guaranteed row count. |
| `maxAttempts` | 1 to 4. Default 4. |

Free Apify users are limited by the Actor to 1 query, `limit` 10, and `maxAttempts` 2.

## Output a default run can return

`query`, `country`, `language`, `rank`, `title`, `priceText`, `priceNumeric`, `currency`, `merchant`, `rating`, `reviewCount`, `imageUrl`, `link`, `queryProductCount`, `queryMerchantCount`, `queryMinPrice`, `queryMedianPrice`, `queryMaxPrice`, `queryPriceSpreadPct`, `attemptCount`, `queriedAt`.

Do not expect `merchantOfferUrl`, `searchReferenceUrl`, or `provenanceStatus` on the default build.

The Actor does not check stock, store price history, or check out.

## Public example tasks

These tasks keep fixed inputs. Open one when that product query is the job:

- [Compare competitor laptop prices](https://apify.com/toninovo/google-shopping-price-intelligence/tasks/compare-laptop-prices) uses `laptop 16GB RAM`, `us`, `en`, limit 20.
- [Ecommerce market prices for wireless earbuds](https://apify.com/toninovo/google-shopping-price-intelligence/tasks/wireless-earbuds-market-price) uses `wireless earbuds`, `us`, `en`, limit 20.
- [Compare espresso machine competitor prices](https://apify.com/toninovo/google-shopping-price-intelligence/tasks/espresso-competitor-prices) uses `espresso machine`, `us`, `en`, limit 20.

## Examples

- Python: [examples/run_snapshot.py](examples/run_snapshot.py)
- JavaScript: [examples/run_snapshot.mjs](examples/run_snapshot.mjs)
- Tutorial: [TUTORIAL.md](TUTORIAL.md)
- Agent facts: [llms.txt](llms.txt)
- Agent installable skill: [skills/google-shopping-price-snapshot/SKILL.md](skills/google-shopping-price-snapshot/SKILL.md)
- Agent integration index: [AGENTS.md](AGENTS.md)
- Apify token and wallet payment paths: [AGENT_PAYMENT.md](AGENT_PAYMENT.md)

Set `APIFY_TOKEN` in the environment before running an example. The examples are not executed by this repository.
