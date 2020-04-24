sudo apt-get install ansible python3-pip
sudo pip3 install tox

## Installation Prometheus
```bash
git clone https://github.com/cloudalchemy/ansible-prometheus.git
cd ansible-prometheus/
mkdir -p roles/cloudalchemy.prometheus
mv defaults/ handlers/ meta/ molecule/ tasks/ templates/ vars/ roles/cloudalchemy.prometheus/
ls roles/cloudalchemy.prometheus/
vim main.yaml
---
- hosts: all
  roles:
  - cloudalchemy.prometheus
  vars:
    prometheus_targets:
      node:
      - targets:
        - localhost:9100
        labels:
          env: demosite

vim inventory
localhost ansible_connection=local

ansible-playbook -i inventory main.yaml
```

## Prometheus: Node Exporter – Install and Config – Ubuntu
```bash
sudo useradd node_exporter -s /sbin/nologin
curl -LO https://github.com/prometheus/node_exporter/releases/download/v0.18.1/node_exporter-0.18.1.linux-amd64.tar.gz
tar xzf node_exporter-0.18.1.linux-amd64.tar.gz
cd node_exporter-0.18.1.linux-amd64/
sudo mv node_exporter /usr/local/bin
sudo vim /etc/systemd/system/node_exporter.service
	[Unit]
	Description=Node Exporter
	After=network.target

	[Service]
	User=node_exporter
	Group=node_exporter
	Type=simple
	ExecStart=/usr/local/bin/node_exporter

	[Install]
	WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl restart node_exporter
sudo systemctl status node_exporter


sudo vim /etc/prometheus/prometheus.yml
(at the end)
  - job_name: 'node_exporter_metrics'
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9100']


sudo systemctl restart prometheus
sudo systemctl status prometheus
```