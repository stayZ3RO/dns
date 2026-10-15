# Phase 6.5 Diagrams: RustDesk Remote Access & VM Hardening 🗺️

---

## Quick Navigation

| Page | Link |
|---|---|
| Phase Home | [README](README.md) |
| Overview | [overview.md](overview.md) |
| Step-by-Step Guide | [step-by-step.md](step-by-step.md) |
| Validation | [validation.md](validation.md) |
| Diagrams | [diagrams.md](diagrams.md) |
| Documentation Hub | [docs/](../README.md) |

---


## Final Pre-Cutover Service Layout

```text
Proxmox Host - 192.0.2.80
├── CT 180: network-controller - 192.0.2.10
├── VM 183: remote-access-host - 192.0.2.83
│   ├── rustdesk-hbbs
│   ├── rustdesk-hbbr
│   └── UFW LAN-only firewall
└── VM 281: metrics-host - 192.0.2.81
    ├── Grafana
    ├── Prometheus
    ├── Alertmanager
    ├── Blackbox Exporter
    └── Portainer Agent
```

---

## RustDesk Access Flow

```text
Laptop / Gaming PC / Phone
        ↓
RustDesk Client
        ↓
remote-access-host - 192.0.2.83
        ├── hbbs
        └── hbbr
```

---

## Docker Management Plan

```text
Future container-app-host VM - 192.0.2.82
└── Portainer Server
    ↓
metrics-host VM - 192.0.2.81
└── Portainer Agent - 9001
```

---

## Project Boundary

This phase closes the remote access and VM hardening work for Project 1.

Network segmentation, VLANs, and the managed router/switch production cutover will be handled in a separate project.
