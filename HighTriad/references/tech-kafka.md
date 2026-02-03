# Kafka

Use this reference when Kafka is used for event streaming, async pipelines, or service decoupling.

## Key Decisions

- Choose partition key for ordering and scalability.
- Define retention and compaction policies.
- Choose delivery semantics and idempotency strategy.
- Decide on schema governance and evolution.
- Define retry, DLQ, and replay strategy.

## Performance Patterns

- Size partitions to match consumer parallelism.
- Batch producers and tune linger and batch size.
- Keep message payloads compact.
- Use compression for bandwidth efficiency.
- Co-locate producers and brokers when possible.

## Availability Patterns

- Use replication factor aligned to failure domains.
- Use ISR monitoring for broker health.
- Validate leader election timing under load.
- Test consumer group rebalances during failures.

## Correctness Patterns

- Use idempotent producers for at-least-once.
- Use transactional producers for exactly-once where needed.
- Store offsets only after processing completes.
- Ensure consumers are idempotent for retries.

## Risks and Pitfalls

- Avoid too few partitions for bursty workloads.
- Avoid very large messages that block batching.
- Avoid unbounded topic growth without retention.
- Avoid tight retry loops without backoff.

## Signals to Watch

- Consumer lag per group.
- Broker disk usage and ISR size.
- Produce and fetch latency.
- Rebalance frequency and duration.
