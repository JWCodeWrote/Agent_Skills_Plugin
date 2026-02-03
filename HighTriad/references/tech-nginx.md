# Nginx

Use this reference when handling edge routing, TLS termination, or L7 load balancing.

## Key Decisions

- Choose TLS termination location and cert rotation flow.
- Define upstream health checks and failover behavior.
- Configure timeouts and keepalive for upstreams.
- Choose rate limiting strategy and scope.
- Decide on caching behavior for static and API responses.

## Performance Patterns

- Enable keepalive for upstream connections.
- Use HTTP/2 and TLS session resumption.
- Enable gzip or brotli for text responses.
- Offload static assets to CDN where possible.
- Tune worker processes and connections to CPU cores.

## Availability Patterns

- Use multiple ingress replicas and anycast or L4 load balancing.
- Set sensible retry and failover thresholds.
- Avoid long timeouts that tie up workers.
- Use circuit breaker logic at the edge when possible.

## Security Patterns

- Enforce TLS versions and strong ciphers.
- Use request size limits and header sanity checks.
- Apply WAF or bot protection for abuse cases.

## Risks and Pitfalls

- Avoid global rate limits that block critical traffic.
- Avoid unlimited request bodies on upload paths.
- Avoid misconfigured timeouts that amplify retries.

## Signals to Watch

- Upstream error rate and timeout rate.
- Edge latency and TLS handshake time.
- Rate limit hits and block counts.
