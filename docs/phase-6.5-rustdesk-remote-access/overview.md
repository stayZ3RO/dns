# Phase 6.5 Overview: RustDesk Remote Access & VM Hardening 🔐

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


## 📌 Purpose

Phase 6.5 prepares the lab for project closeout by validating remote access, VM hardening, monitoring maintenance, and backup readiness.

This is the final technical hardening phase before closing Project 1 and moving future routing/switching/VLAN work into a separate project.

---

## 🧠 Why This Phase Matters

Before changing the network path in a future project, the lab needed:

- reliable remote access
- hardened SSH access
- LAN-only remote desktop
- controlled monitoring storage growth
- clean VM naming
- enough disk headroom
- verified backups

---

## 🧩 Final Architecture

| Component | Host | IP |
|---|---|---:|
| Proxmox Host | `hypervisor` | `192.0.2.80` |
| Omada Controller | CT 180 | `192.0.2.10` |
| Docker Monitoring | VM 281 | `192.0.2.81` |
| RustDesk Server | VM 183 | `192.0.2.83` |

---

## 🔐 RustDesk Server

| Item | Value |
|---|---|
| VM Name | `remote-access-host` |
| VM ID | `183` |
| IP Address | `192.0.2.83` |
| OS | Debian |
| Runtime | Docker Compose |
| Containers | `rustdesk-hbbs`, `rustdesk-hbbr` |
| Firewall | UFW LAN-only |

---

## 📊 Docker Monitoring VM

| Item | Value |
|---|---|
| Old VM Name | `container-services-host` |
| New VM Name | `metrics-host` |
| VM ID | `281` |
| IP Address | `192.0.2.81` |
| Disk | `50GB` |
| Docker logs | `10MB x 3 files` |
| Prometheus retention | `30d` / `10GB` |
| Portainer component | Agent only |

---

## 🧭 Portainer Design

| Host | Component |
|---|---|
| `metrics-host` | Portainer Agent |
| Future `container-app-host` VM | Portainer Server |

This keeps monitoring focused and reserves application hosting for a separate VM.

---

## ✅ Result

The lab has validated remote access, monitoring hardening, Docker retention, disk expansion, and backup readiness.

This phase supports closing out the HA DNS / core infrastructure foundation project.
