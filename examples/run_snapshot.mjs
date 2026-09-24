// Call the paid Actor toninovo/google-shopping-price-intelligence.
// npm install apify-client
import { ApifyClient } from "apify-client";

const token = process.env.APIFY_TOKEN;
if (!token) {
  throw new Error("Set APIFY_TOKEN before running.");
}

const client = new ApifyClient({ token });
const run = await client.actor("toninovo/google-shopping-price-intelligence").call(
  {
    queries: ["wireless earbuds"],
    country: "us",
    language: "en",
    limit: 10,
    maxAttempts: 2,
  },
  { maxTotalChargeUsd: 0.1 },
);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  console.log(
    item.title,
    item.priceNumeric,
    item.currency,
    item.merchant,
    item.link,
    item.queryMinPrice,
    item.queryMedianPrice,
    item.queryMaxPrice,
  );
}
