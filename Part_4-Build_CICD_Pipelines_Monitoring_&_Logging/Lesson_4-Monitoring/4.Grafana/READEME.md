## Install and Configure Grafana for Prometheus
```bash
curl -LO https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_5.1.4_amd64.deb
sudo apt-get install -y adduser libfontconfig
sudo dpkg -i grafana_5.1.4_amd64.deb
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

Add 3000 port to inbound port