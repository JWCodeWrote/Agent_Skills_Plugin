# Redis

Use this reference when Redis is used for caching, rate limiting, queues, or session storage.

## Key Decisions

- Choose data model and key naming conventions.
- Set TTL policy and invalidation strategy.
- Decide on persistence mode and durability targets.
- Choose deployment mode: standalone, sentinel, or cluster.
- Define eviction policy based on workload.

## Performance Patterns

- Keep values small and compress large payloads.
- Use pipelining and batching to reduce round trips.
- Avoid hot keys with sharding or key tagging.
- Prefer server-side operations to reduce chatty reads.
- Use Lua scripts for atomic multi-step changes.

## Availability Patterns

- Use replicas and automatic failover for HA.
- Use Redis Cluster for horizontal scale and shard failover.
- Validate RTO and failover timing under load.
- Implement client-side retry with jitter and cap.

## Consistency and Correctness

- Treat cache as soft state and handle misses safely.
- Use versioned keys for invalidation with deployments.
- Use monotonic time for TTL in distributed systems.
- Avoid using Redis as the sole source of truth.

## Risks and Pitfalls

- Avoid unbounded memory growth without eviction.
- Avoid storing large blobs that increase fragmentation.
- Avoid blocking commands on large collections.
- Avoid single shared instance for all tenants.

## Signals to Watch

- Cache hit rate and eviction rate.
- Memory fragmentation and used memory.
- Command latency and slowlog.
- Replication lag and failover events.
