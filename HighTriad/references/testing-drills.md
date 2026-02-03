# Testing and DR Drills

Use this reference when defining validation plans for high concurrency, high performance, and high availability.

## Load Testing

Define test at expected peak with p95/p99 targets.
Measure throughput, latency percentiles, and error rate.
Validate resource saturation and autoscaling response.

## Stress Testing

Push beyond peak to identify breaking points.
Validate backpressure, rate limiting, and queue behavior.
Confirm graceful degradation over hard failure.

## Soak Testing

Run sustained load for hours or days.
Detect memory leaks, cache churn, and slow growth issues.
Verify steady-state latency and error budgets.

## Chaos Testing

Inject dependency failures and network partitions.
Test retry, timeout, and circuit breaker behavior.
Validate RTO and recovery paths.

## DR Drills

Test backup restore and data replay workflows.
Measure failover time and validate RPO.
Validate runbooks and on-call procedures.

## Success Criteria

Meet SLOs under peak and degraded conditions.
Recover within RTO and stay within RPO.
Keep error budget burn within acceptable thresholds.
