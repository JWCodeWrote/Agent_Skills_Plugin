# Finance Systems

Use this reference for trading, payments, ledgering, or regulated financial workloads.

## Key Decisions

- Define consistency requirements per transaction type.
- Specify audit trail and data retention obligations.
- Define RTO/RPO targets by ledger criticality.
- Choose cryptographic and key management standards.

## Performance Patterns

- Separate read models for analytics and reporting.
- Use write-ahead logging and immutable ledgers.
- Prioritize low-latency paths for critical trades.
- Isolate batch processing from real-time flows.

## Availability Patterns

- Use active-active or warm-standby for core ledgers.
- Validate end-to-end failover with replay safety.
- Implement idempotency keys for payment requests.
- Provide manual override workflows for incidents.

## Compliance and Security

- Enforce least privilege and segregation of duties.
- Encrypt data in transit and at rest.
- Record all changes with non-repudiation controls.

## Risks and Pitfalls

- Avoid cross-region synchronous writes on low-latency paths.
- Avoid implicit rounding or precision loss.
- Avoid retry storms on payment gateways.

## Signals to Watch

- Settlement latency and reconciliation error rate.
- Duplicate or failed transaction rate.
- Audit log completeness and delivery lag.
