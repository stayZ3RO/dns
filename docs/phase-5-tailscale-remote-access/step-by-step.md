# Phase 5: Step-by-Step Guide 🛠️

---

## Quick Navigation

| Page | Link |
|---|---|
| Phase Home | [README](README.md) |
| Overview | [overview.md](overview.md) |
| Step-by-Step Guide | [step-by-step.md](step-by-step.md) |
| Validation | [validation.md](validation.md) |
| Documentation Hub | [docs/](../README.md) |

---


## 📖 Purpose

This guide documents the implementation of secure remote access for the homelab using Tailscale.

Phase 5 builds on the completed HA DNS and monitoring stack and adds:

- secure remote connectivity
- private tailnet-based device access
- SSH administration over Tailscale
- off-site administration without router port forwarding

---

## ✅ Prerequisites

Before starting Phase 5, the following were already complete:

- HA DNS with dual Pi-hole nodes
- monitoring and alerting with Prometheus and Grafana
- Alertmanager Discord notifications
- local SSH access to both Pi nodes on the home network
- Windows desktop and laptop available as remote admin endpoints
- Tailscale account created

---

## 1. Create the Tailscale Tailnet 🌐

Tailscale was selected as the Phase 5 remote access platform.

### Tasks completed

1. created or signed in to a Tailscale account
2. allowed Tailscale to create the private tailnet
3. opened the Tailscale admin console
4. prepared the first device for enrollment

### Validation

- admin console loaded successfully
- tailnet was available for device enrollment
- Tailscale prompted to add the first device

![Tailscale first device setup](../../screenshots-redacted/phase-5/01-tailscale-first-device-setup.png)

![Tailnet before devices were added](../../screenshots-redacted/phase-5/02-tailscale-machines-empty-state.png)

---

## 2. Add the Windows Desktop 💻

The Windows desktop was added to the tailnet first.

### Tasks completed

1. installed Tailscale on the Windows desktop
2. signed in with the same Tailscale account
3. confirmed the device appeared in the Machines list

### Validation

- Windows desktop successfully joined the tailnet
- Tailscale assigned the device a private tailnet address

![Windows desktop added to tailnet](../../screenshots-redacted/phase-5/03-windows-desktop-added-to-tailnet.png)

---

## 3. Add the Second Windows Admin Device 🖥️

A second Windows device was added as another admin endpoint.

### Tasks completed

1. installed Tailscale on the second Windows device
2. signed in with the same Tailscale account
3. confirmed the device appeared in the Machines list

### Validation

- second Windows device successfully joined the tailnet
- both Windows admin devices appeared in the Tailscale console

![Second Windows admin device added to tailnet](../../screenshots-redacted/phase-5/04-second-windows-device-added-to-tailnet.png)

---

## 4. Install Tailscale on dns-primary 📡

Tailscale was installed on `dns-primary`.

### Tasks completed

1. SSH’d locally into `dns-primary`
2. installed Tailscale using the Linux install script
3. ran `sudo tailscale up`
4. authenticated the device through the Tailscale login link
5. confirmed the device appeared in the Tailscale admin console

### Validation commands

```bash
tailscale ip
tailscale status
hostname
```

### Validation

- `dns-primary` joined the tailnet successfully
- `dns-primary` received a Tailscale IP address
- `dns-primary` appeared in `tailscale status`
- `dns-primary` appeared in the admin console

[Tailscale installation started on dns-primary](../../screenshots-redacted/phase-5/)

[dns-primary authenticated and visible in Tailscale status](../../screenshots-redacted/phase-5/)

[dns-primary visible in Tailscale admin console](../../screenshots-redacted/phase-5/)

---

## 5. Install Tailscale on dns-secondary 📡

The same Tailscale process was repeated on `dns-secondary`.

### Tasks completed

1. SSH’d locally into `dns-secondary`
2. installed Tailscale using the Linux install script
3. ran `sudo tailscale up`
4. authenticated the device through the Tailscale login link
5. confirmed the device appeared in the Tailscale admin console

### Validation commands

```bash
tailscale ip
tailscale status
hostname
```

### Validation

- `dns-secondary` joined the tailnet successfully
- `dns-secondary` received a Tailscale IP address
- `dns-secondary` appeared in `tailscale status`
- `dns-secondary` appeared in the admin console

[Tailscale installation and authentication on dns-secondary](../../screenshots-redacted/phase-5/)

[dns-secondary authenticated and visible in Tailscale status](../../screenshots-redacted/phase-5/)

---

## 6. Confirm All Core Devices in the Tailnet ✅

After both Raspberry Pi nodes were added, the Tailscale admin console showed the core devices in the tailnet.

### Devices visible

- Windows desktop
- second Windows admin device
- `dns-primary`
- `dns-secondary`

### Validation

- all expected devices appeared in the Tailscale Machines list
- each device had a Tailscale IP address
- both Pi nodes were online

![All core devices visible in the tailnet](../../screenshots-redacted/phase-5/10-all-core-devices-visible-in-tailnet.png)

---

## 7. Enable Tailscale SSH on Both Pi Nodes 🔐

Tailscale SSH was enabled on both Raspberry Pi nodes.

### Commands used

On `dns-primary`:

```bash
sudo tailscale set --ssh
```

On `dns-secondary`:

```bash
sudo tailscale set --ssh
```

### Validation

- command completed successfully on `dns-primary`
- command completed successfully on `dns-secondary`
- both nodes were prepared for SSH access through the tailnet

[Tailscale SSH enabled on dns-primary](../../screenshots-redacted/phase-5/)

[Tailscale SSH enabled on dns-secondary](../../screenshots-redacted/phase-5/)

---

## 8. Confirm SSH Service on Both Pi Nodes 🧪

The local SSH service was checked on both Raspberry Pi nodes.

### Commands used

```bash
sudo systemctl status ssh
```

### Validation

- SSH service was enabled on `dns-primary`
- SSH service was active and running on `dns-primary`
- SSH service was enabled on `dns-secondary`
- SSH service was active and running on `dns-secondary`

[SSH service active on dns-primary](../../screenshots-redacted/phase-5/)

[SSH service active on dns-secondary](../../screenshots-redacted/phase-5/)

---

## 9. Test Tailnet Connectivity from the Admin Device 📡

Basic connectivity was tested from the admin endpoint.

### Validation commands

```bash
tailscale ping dns-primary
tailscale ping dns-secondary
```

### Implementation note

During testing, running `tailscale` commands from Ubuntu WSL on the Windows admin machine showed a separate unauthenticated Tailscale context.

The cleaner approach was to use the Windows Tailscale client as the authenticated admin endpoint instead of trying to manage a separate WSL Tailscale identity.

![Tailscale ping validation from admin device](../../screenshots-redacted/phase-5/15-tailscale-ping-validation-from-admin-device.png)

---

## 10. Validate Remote Administration Model 📶

The final validation confirmed that remote administration could be performed through the private Tailscale path instead of public SSH exposure.

### Result

- admin endpoints were inside the tailnet
- both Pi nodes were inside the tailnet
- SSH services were active on both Pi nodes
- no router port forwarding was required
- no public SSH exposure was needed

---

## 🏁 Result

Phase 5 completed the secure remote access layer for the homelab by adding:

- private tailnet-based connectivity
- both Raspberry Pi nodes added to Tailscale
- both admin endpoints added to Tailscale
- SSH service validation on both Pi nodes
- Tailscale SSH enabled on both Pi nodes
- a remote admin path that does not depend on public SSH exposure
