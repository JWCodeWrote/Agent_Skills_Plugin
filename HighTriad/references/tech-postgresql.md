# PostgreSQL

Use this reference when PostgreSQL is the primary datastore or the system needs strong consistency with relational queries.

## Key Decisions

- Choose primary key and partitioning strategy early.
- Define read vs write scaling approach.
- Decide on connection pooling and pool sizing.
- Select replication mode and lag tolerance.
- Define backup and restore objectives.

## Performance Patterns

- Create indexes for high-selectivity queries.
- Avoid N+1 query patterns and large result sets.
- Use prepared statements and query caching.
- Use partitioning for large time-series tables.
- Schedule VACUUM and analyze to prevent bloat.

## Availability Patterns

- Use primary-replica setup with automatic failover.
- Isolate writes to a single primary to avoid conflicts.
- Validate failover scripts and promotion timing.
- Use PITR and verify restores regularly.

## Concurrency Patterns

- Use optimistic locking for hot rows.
- Reduce lock contention with smaller transactions.
- Avoid long-running transactions in OLTP paths.
- Use SKIP LOCKED for work queues.

## Risks and Pitfalls

- Avoid unbounded connection counts on the primary.
- Avoid missing indexes on hot paths.
- Avoid large transactions that block vacuum.
- Avoid cross-region synchronous writes for low-latency paths.

## Signals to Watch

- p95/p99 query latency by endpoint.
- Replication lag and WAL volume.
- Connection pool saturation.
- Lock waits and deadlocks.
