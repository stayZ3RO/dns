# Public-safety checklist

This repo is public. Before committing or publishing, check:

1. **Run the scanner:** `python3 scripts/check-public-safety.py`. It fails on MAC addresses, RFC 1918 addresses, unapproved public IPv4 addresses, tailnet (`100.64.0.0/10`) device addresses, and known internal machine names in tracked text. It also runs in CI (`docs-check.yml`). A justified exception goes in `.public-safety-allow`; exceptions must not preserve real lab addresses or internal machine names.
2. **Look at every screenshot yourself.** No scanner can read an image. Open each new or changed image and check for passwords, tokens, keys, MACs, real lab addresses, public IPs, account IDs, SSIDs, people's names (including room names), device serial numbers, and real internal hostnames. Replace address and hostname labels with documentation values before publishing a new or changed image.
3. **Never use blur or pixelation over a secret.** Pixelated text can be partly recovered. Cover it with a solid opaque box. Masked password dots also reveal the length; cover them too.
4. **Deleting a file does not delete it from history.** If a secret was ever committed, rotate it first; a history rewrite is optional and does not un-leak it.
5. **Use documentation addresses and generic roles.** Lab network examples must use the RFC 5737 ranges `192.0.2.0/24`, `198.51.100.0/24`, or `203.0.113.0/24`. Do not publish real internal machine names or SSH aliases. Use roles such as `dns-primary`, `dns-secondary`, `hypervisor`, or `backup-host`, and keep product names such as Pi-hole, Proxmox, Unbound, and Caddy. Loopback addresses, protocol constants, and well-known public DNS resolvers may remain where they explain the configuration.
