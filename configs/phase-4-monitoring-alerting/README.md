# Phase 4 Monitoring Configs 📁

This folder contains sanitized configuration files used for Phase 4 monitoring and alerting.

## Included configs

- `docker-compose.yml`
- `prometheus.yml`
- `alert.rules.yml`
- `alertmanager.yml`
- `blackbox.yml`
- Grafana datasource provisioning in `grafana/provisioning/datasources/prometheus.yml`

Grafana dashboard exports and dashboard provisioning files are not included in this repository.

## Notes

- The Grafana admin password in `docker-compose.yml` has been sanitized and replaced with `CHANGE_ME`.
- Internal lab IPs are left intact because they reflect the private LAN design of the homelab.
- These files represent the working Phase 4 monitoring stack used in the lab.

## Monitored endpoints

- `dns-primary`, `192.0.2.60`
- `dns-secondary`, `192.0.2.61`
- HA DNS VIP, `192.0.2.20`
