# Phase 5.5 Validation: Tailscale Subnet Router

## Local VM Validation

Commands used:

~~~bash
hostname
ip -br addr
ip route
ping -c 4 192.0.2.1
ping -c 4 192.0.2.20
ping -c 4 1.1.1.1
getent hosts tailscale.com
~~~

Expected results:

| Check | Expected Result |
|---|---|
| Hostname | `subnet-router` |
| IP address | `192.0.2.84` |
| Gateway | `192.0.2.1` |
| Pi-hole VIP | Reachable |
| Internet | Reachable |
| DNS | Resolves successfully |

## Tailscale Validation

Commands used:

~~~bash
tailscale status
tailscale ip -4
sysctl net.ipv4.ip_forward
~~~

Expected results:

| Check | Expected Result |
|---|---|
| Tailscale status | VM online |
| Tailscale IP | Assigned |
| IP forwarding | Enabled |
| Advertised route | `192.0.2.0/24` |

## LAN Reachability from Subnet Router

Commands used:

~~~bash
ping -c 4 192.0.2.1
ping -c 4 192.0.2.20
ping -c 4 192.0.2.60
ping -c 4 192.0.2.61
ping -c 4 192.0.2.80
ping -c 4 192.0.2.81
ping -c 4 192.0.2.83
~~~

Validated targets:

| Address | Service |
|---|---|
| `192.0.2.1` | Gateway |
| `192.0.2.20` | Pi-hole HA DNS VIP |
| `192.0.2.60` | dns-primary |
| `192.0.2.61` | dns-secondary |
| `192.0.2.80` | Proxmox |
| `192.0.2.81` | metrics-host / Grafana |
| `192.0.2.83` | RustDesk VM |

## Remote Client Validation

Remote Tailscale clients were tested from outside the home Wi-Fi network.

Validated remote LAN access:

| Service | Address |
|---|---|
| Pi-hole | `http://192.0.2.20/admin` |
| Proxmox | `https://192.0.2.80:8006` |
| Grafana | `http://192.0.2.81:3000` |
| Omada Controller | `https://192.0.2.10` |
| RustDesk VM | `192.0.2.83` |

## RustDesk Validation

RustDesk clients continue to use the LAN IP configuration:

| Setting | Value |
|---|---|
| ID Server | `192.0.2.83:21116` |
| Relay Server | `192.0.2.83:21117` |
| API Server | blank |

Remote Tailscale clients can reach the RustDesk VM through the subnet route instead of requiring the RustDesk VM's Tailscale IP.

## Result

Remote LAN access was validated through Tailscale subnet routing with no public port forwarding.
