# Phase 6.5 Screenshot Checklist

## RustDesk / VM Hardening Screenshots

Screenshot folder:

~~~text
screenshots/phase-6.5/
~~~

Existing RustDesk screenshots remain part of this phase.

## Docker Management / Portainer Screenshots

Screenshot folder:

~~~text
screenshots/phase-6.5/docker-management-portainer/
~~~

Role labels replace filenames that contain machine identifiers. Existing images are unchanged.

| File or evidence label | Description |
|---|---|
| 01 proxmox container admin host vm summary screenshot | container-admin-host VM summary |
| 02 proxmox container admin host network mac address screenshot | Proxmox virtual NIC MAC source |
| 03 container admin host dhcp lease validation screenshot | container-admin-host reserved IP validation |
| 04 container admin host network validation screenshot | Gateway, DNS, and internet validation |
| `05-docker-installed-validation.png` | Docker and Docker Compose validation |
| `06-portainer-server-running.png` | Portainer Server container running |
| `07-portainer-initial-login.png` | Portainer UI available |
| 08 container admin host ufw status screenshot | container-admin-host firewall status |
| 09 portainer agent metrics host running screenshot | Agent running on metrics-host |
| 10 metrics host agent firewall rule screenshot | Agent firewall rule |
| 11 portainer metrics host environment online screenshot | metrics-host online in Portainer |
| `12-portainer-monitoring-containers-visible.png` | Monitoring containers visible |
| `13-portainer-access-over-lan.png` | Portainer reachable over LAN |
| `14-portainer-access-over-tailscale-subnet-route.png` | Portainer reachable remotely over Tailscale |
| 15 proxmox backup container admin host screenshot | container-admin-host backup completed |

## Before Publishing

Follow the [public safety checklist](../public-safety-checklist.md) for redaction rules.
