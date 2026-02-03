---
name: hightriad
description: Design and review systems for high concurrency, high performance, and high availability. Use when planning architecture, scaling strategies, SLOs/SLIs, load testing, resilience, failover, capacity planning, caching, data access optimization, or incident-readiness for production systems.
---

# HighTriad

Build professional, production-grade system designs that balance high concurrency, high performance, and high availability.

## Core Workflow

1. **Clarify requirements**
Collect workload shape, critical paths, and failure tolerance.
Ask for absolute targets: RPS/QPS, p95/p99 latency, peak traffic, growth rate, error budget, RTO/RPO, data consistency needs.

2. **Define SLIs/SLOs**
Choose 3 to 5 primary SLIs and map them to explicit SLOs.
Prefer latency percentiles, availability, throughput, and freshness over averages.

3. **Model the system**
Sketch request flow and identify bottlenecks across compute, network, storage, and dependency call chains.
Enumerate concurrency boundaries: queues, pools, locks, partitions, and external rate limits.

4. **Design for scale**
Select scaling axis: horizontal, vertical, data partitioning, or event-driven async.
Define partitioning keys, load balancing strategy, and caching boundaries.

5. **Design for performance**
Minimize critical path length, reduce tail latency, and cut remote calls.
Choose data access patterns, indexing, caching tiers, and compression tradeoffs.

6. **Design for availability**
Add redundancy, fault isolation, and graceful degradation.
Define failover paths, health checks, circuit breakers, and data durability strategy.

7. **Validate with tests**
Create load, stress, soak, and chaos test plans aligned to SLOs.
Plan rollback and mitigation steps for regression risk.

8. **Operationalize**
Define observability, alerting, runbooks, and capacity review cadence.
Prepare incident response playbooks and on-call readiness.

## Reference Map

- Read `references/tech-kubernetes.md` when the system runs on Kubernetes or needs autoscaling, multi-zone placement, or service mesh guidance.
- Read `references/tech-redis.md` when using Redis for caching, rate limiting, queues, or session storage.
- Read `references/tech-postgresql.md` when PostgreSQL is the primary datastore or when designing replicas, partitioning, and indexing.
- Read `references/tech-kafka.md` when using Kafka for event streaming, async pipelines, or decoupling services.
- Read `references/tech-nginx.md` when edge routing, TLS termination, or L7 load balancing is required.
- Read `references/industry-finance.md` for trading, payments, or regulated workloads.
- Read `references/industry-ecommerce.md` for flash sales, promotions, and cart/checkout workloads.
- Read `references/industry-iot.md` for device fleets, bursty telemetry, or edge connectivity constraints.
- Read `references/industry-realtime.md` for chat, gaming, or real-time collaboration systems.
- Read `references/templates.md` when the user needs architecture, SLO, or capacity plan templates.
- Read `references/testing-drills.md` when load testing, chaos testing, or DR drills are requested.

## Concurrency Design Checklist

- Define concurrency target by peak RPS and concurrent users.
- Bound resource usage with worker pools, queues, and backpressure.
- Partition workload by tenant, shard key, or request type.
- Use async I/O for network and storage operations.
- Limit shared-state contention with sharding or lock-free structures.
- Apply rate limiting at edge and internal dependencies.
- Protect downstream services with bulkheads and timeouts.

## Performance Design Checklist

- Reduce critical path by collapsing or parallelizing remote calls.
- Minimize p99 latency contributors: cold starts, GC pauses, locks, slow queries.
- Add caching with explicit invalidation rules.
- Use read replicas or materialized views for read-heavy workloads.
- Choose data formats and compression based on CPU vs bandwidth tradeoff.
- Optimize queries with indexes and selective projections.
- Warm pools and caches for predictable latency.

## Availability Design Checklist

- Eliminate single points of failure with redundancy across zones.
- Use health checks and automated failover.
- Separate control plane and data plane failure domains.
- Support graceful degradation for non-critical features.
- Define RTO/RPO per subsystem and validate with DR drills.
- Ensure idempotency for retries and at-least-once delivery.
- Protect data with backups, versioning, and restore verification.

## Validation Plan

- Run load tests to p95/p99 targets at expected peak.
- Run stress tests beyond peak to validate backpressure behavior.
- Run soak tests to surface memory leaks and queue buildup.
- Run chaos tests on dependencies and network partitions.
- Validate auto-scaling and failover timing against RTO.

## Deliverables

- Architecture diagram with data flow and failure domains.
- SLI/SLO document with error budgets and alert thresholds.
- Capacity plan with scaling triggers and cost projections.
- Risk register with mitigations and rollback plans.
- Test plan covering load, stress, soak, and chaos.
- Operational runbook with on-call actions and dashboards.

## Red Flags

- SLOs not defined or only averages tracked.
- Unbounded queues or unlimited fiber/thread spawning.
- Single shared database without partitioning plan at scale.
- No clear rollback or mitigation plan for deploys.
- No chaos testing or failover verification.

## Output Template

Provide a concise plan with headings in this order:
1. Targets (SLIs/SLOs, RTO/RPO)
2. Workload model (traffic shape, hotspots, dependencies)
3. Architecture (flow, scaling axis, partitions)
4. Performance (critical path, caching, data access)
5. Availability (redundancy, failover, degradation)
6. Validation (tests and success criteria)
7. Ops (observability, runbooks, incident response)
