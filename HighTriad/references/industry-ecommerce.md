# E-commerce Systems

Use this reference for flash sales, promotions, search/browse, and cart/checkout workloads.

## Key Decisions

- Define inventory consistency and oversell policy.
- Choose cart persistence model and TTL strategy.
- Define SLA for checkout latency and payment success.
- Decide on cache invalidation for price and stock.

## Performance Patterns

- Cache catalog and pricing with short TTLs.
- Precompute search indexes and facets.
- Use queue-based order processing post-checkout.
- Serve static assets via CDN with cache busting.

## Availability Patterns

- Degrade gracefully by disabling non-critical features.
- Isolate checkout from recommendation services.
- Use circuit breakers on payment providers.
- Maintain fallback pricing and inventory views.

## Risks and Pitfalls

- Avoid single inventory lock for all SKUs.
- Avoid long checkout transactions that lock stock.
- Avoid coupling checkout to downstream analytics.

## Signals to Watch

- Add-to-cart to checkout conversion rate.
- Inventory update lag and stock mismatch rate.
- Payment failure rate by provider.
