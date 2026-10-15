# IP Address Plan

## Network Range

192.0.2.0/24

---

## Core Infrastructure

Router (Deco): 192.0.2.1
Primary Pi-hole: 192.0.2.10
Secondary Pi-hole: 192.0.2.11
Virtual IP (VIP): 192.0.2.20

---

## DHCP Range

192.0.2.100 to 192.0.2.200

---

## Notes

* Static IPs reserved for infrastructure components
* DHCP used for client devices
* DNS routed through Pi-hole
