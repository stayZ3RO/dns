# Project Closeout: HA DNS & Core Infrastructure Foundation

## Summary

This repository is complete as the first major home infrastructure project.

It documents a resilient foundation for DNS, monitoring, alerting, secure remote access, virtualization, and service hosting.

---

## Completed Capabilities

- Network baseline and ISP migration documentation
- Pi-hole DNS filtering and query visibility
- Dual-node HA DNS with Keepalived VIP failover
- Gravity Sync replication between Pi-hole nodes
- Local recursive DNS with Unbound
- Prometheus and Grafana monitoring
- Alertmanager alert routing
- Discord alert delivery
- Tailscale secure remote administration
- Proxmox infrastructure host
- Omada Controller LXC
- Docker monitoring VM
- Monitoring migration from gaming PC to Linux VM
- RustDesk self-hosted remote access
- Docker log rotation
- Prometheus retention controls
- Portainer Agent preparation
- Proxmox backup validation

---

## Final Project 1 State (Historical Snapshot)

This was the Project 1 layout at closeout, before the managed-router and later UniFi cutovers. It is not a current host map. Omada is retired, monitoring now runs on VM 294, and the current network core is documented in [netlab](https://github.com/stayZ3RO/netlab).

```text
AT&T Fiber / ONT
  ↓
AT&T Gateway with IP Passthrough
  ↓
Deco Mesh Router
  ↓
Home LAN - 192.168.68.0/24
  ├── HA DNS VIP - 192.168.68.20
  ├── ashpi-1 - 192.168.68.60
  ├── ashpi-2 - 192.168.68.61
  ├── Proxmox Host - 192.168.68.80
  ├── Docker Monitoring VM - 192.168.68.81
  ├── RustDesk Server VM - 192.168.68.83
  └── Omada Controller LXC - 192.168.68.10
```

---

## Why The Project Ends Here

The HA DNS and infrastructure foundation are complete.

The next step at closeout was a managed routing, switching, and VLAN segmentation project. That work has its own [netlab repository](https://github.com/stayZ3RO/netlab). Its router and switch cutovers are complete; VLAN segmentation remains planned.

---

## Moved to Separate Project

The follow-up project records the completed ER605/Omada cutover, the 2026-09-27 UniFi UDM Pro and USW-24-PoE refresh, and planned VLAN and firewall work:

- ER605 live router cutover (historical)
- managed switch as the core switch (historical)
- Deco AP mode migration (complete)
- VLAN segmentation
- inter-VLAN firewall policy
- trusted, lab, IoT, and guest isolation
- SSID-to-VLAN mapping (planned; wireless hardware support to be confirmed)

---

## Final Result

This project demonstrates practical infrastructure work across networking, Linux, DNS, monitoring, alerting, virtualization, secure access, documentation, and operational validation.
