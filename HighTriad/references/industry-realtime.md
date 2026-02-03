# Real-time Systems

Use this reference for chat, gaming, collaboration, and low-latency streaming.

## Key Decisions

- Choose transport: WebSocket, gRPC stream, or UDP.
- Define session and presence model.
- Decide on state ownership and conflict resolution.
- Define fan-out strategy and room partitioning.

## Performance Patterns

- Minimize hop count in the critical path.
- Use regional edge nodes for latency reduction.
- Batch small messages when safe.
- Use delta updates instead of full state sync.

## Availability Patterns

- Fail over sessions with state checkpointing.
- Use sticky routing for session affinity.
- Limit blast radius with shard isolation.
- Degrade non-critical features under load.

## Risks and Pitfalls

- Avoid centralized presence services at scale.
- Avoid large room fan-out without batching.
- Avoid unbounded per-connection memory.

## Signals to Watch

- Message delivery latency and loss rate.
- Concurrent session count by region.
- Fan-out queue depth and drop rate.
