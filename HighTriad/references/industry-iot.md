# IoT Systems

Use this reference for large device fleets, bursty telemetry, and intermittent connectivity.

## Key Decisions

- Define device identity, auth, and rotation strategy.
- Choose ingestion protocol and gateway topology.
- Define data retention and downsampling policy.
- Decide on edge buffering and offline behavior.

## Performance Patterns

- Use batch ingestion with backpressure control.
- Partition by device or region for scale.
- Use time-series storage for telemetry.
- Separate command/control from telemetry pipelines.

## Availability Patterns

- Support offline caching on devices or gateways.
- Use regional ingestion endpoints for locality.
- Isolate noisy devices with per-tenant limits.
- Provide fallback firmware update channels.

## Risks and Pitfalls

- Avoid single global broker for all devices.
- Avoid tight coupling between ingestion and analytics.
- Avoid unbounded device reconnect storms.

## Signals to Watch

- Device connect rate and reconnect spikes.
- Ingestion backlog and processing lag.
- Firmware update success rate and rollback events.
