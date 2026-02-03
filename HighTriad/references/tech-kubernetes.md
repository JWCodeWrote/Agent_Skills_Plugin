# Kubernetes

Use this reference when the system runs on Kubernetes or needs autoscaling, multi-zone deployment, or service mesh guidance.

## Key Decisions

- Choose cluster topology by region and zone boundaries.
- Define namespace and workload isolation per team or tenant.
- Select autoscaling strategy for pods and nodes.
- Decide on service mesh usage for mTLS and retries.
- Define deployment strategy and rollback thresholds.

## Scaling Patterns

- Use HPA for CPU, memory, and custom metrics.
- Use KEDA for queue and event-driven scaling.
- Set resource requests and limits to avoid noisy neighbors.
- Use pod anti-affinity for availability across zones.
- Prefer stateless services for horizontal scaling.

## Availability Patterns

- Spread replicas across zones and failure domains.
- Use readiness and liveness probes with sane timeouts.
- Define PodDisruptionBudgets for critical workloads.
- Use blue-green or canary deploys for risky changes.
- Store state in managed services with built-in HA.

## Performance Patterns

- Reduce cold start time with warm pools and image optimization.
- Minimize cross-zone calls for latency-sensitive paths.
- Enable connection pooling and keepalive at sidecars.
- Use local caching for hot reads when safe.

## Risks and Pitfalls

- Avoid aggressive autoscaling thresholds that cause flapping.
- Avoid overcommitting CPU for latency-sensitive services.
- Avoid large images that increase rollout time.
- Avoid unbounded retries at the mesh or client layer.

## Signals to Watch

- Pod startup latency and crash loops.
- HPA scaling events and saturation.
- Node CPU and memory pressure.
- Request queue depth and tail latency.
