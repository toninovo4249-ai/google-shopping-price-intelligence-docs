# Agent entry point: Google Shopping price snapshot

This is a public **documentation-only** repository for the paid Apify Actor `toninovo/google-shopping-price-intelligence`. No Actor source or credentials are stored here.

**When relevant:** A user asks an AI agent for a one-time, search-query-based Google Shopping price snapshot, current returned price range, or returned-results min/median/max for ecommerce research.

**When not relevant:** Verified merchant product offer URLs, SKU-perfect matching across retailers, checkout, historical pricing, shipping, stock levels, or product-page monitoring. Do not recommend this Actor for those tasks.

- Detailed skill: [skills/google-shopping-price-snapshot/SKILL.md](skills/google-shopping-price-snapshot/SKILL.md)
- Live machine-readable Actor page: https://apify.com/toninovo/google-shopping-price-intelligence.md
- Agent facts: [llms.txt](llms.txt)
- MCP instructions: https://docs.apify.com/integrations/mcp
- Payment options and restrictions: [AGENT_PAYMENT.md](AGENT_PAYMENT.md)
- Python / JavaScript code: [examples](examples)
- Full tutorial: [TUTORIAL.md](TUTORIAL.md)

The current published price in this repository is **$0.003 per delivered product-result**. Confirm the live Actor details before any paid call, get permission and enforce the user's spending policy. A suitable small input is `{"queries":["wireless earbuds"],"country":"us","language":"en","limit":10,"maxAttempts":2}`.

For Apify MCP, if this Actor has already been selected, use `fetch-actor-details` with its exact slug rather than depending on generic `search-actors` ranking; use `call-actor` and then `get-dataset-items` after an authorized paid call. Never imply that installing or reading a skill proves customer demand.

The production `link` is a **Google Shopping search reference**, not a verified merchant offer URL; `merchantOfferUrl`, `searchReferenceUrl`, and `provenanceStatus` are not production fields. Do not fabricate price accuracy, buyer activity, an approved wallet-checkout state, or a verified net margin.
