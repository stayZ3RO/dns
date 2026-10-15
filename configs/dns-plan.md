# DNS Configuration Plan: Phase 2 Baseline (2026-04-06)

This historical plan was first recorded on 2026-04-06, before Phase 3 added HA DNS and Unbound. See [CURRENT-STATUS.md](../CURRENT-STATUS.md) for the Project 1 closeout state.

## Primary DNS

192.168.68.10 (Pi-hole)

---

## Future HA DNS

192.168.68.20 (Virtual IP)

---

## Upstream DNS

Cloudflare (1.1.1.1)

---

## Design

* All clients receive DNS via DHCP
* Pi-hole acts as centralized DNS resolver
* DNS traffic is logged and filtered

---

## Notes

* No secondary DNS to prevent bypass
* DNS enforced at router level
