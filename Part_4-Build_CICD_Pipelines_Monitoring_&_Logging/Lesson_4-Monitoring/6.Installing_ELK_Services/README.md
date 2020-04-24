## ELK Installaion
```bash
git clone https://github.com/elastic/ansible-elasticsearch
cd ansible-elasticsearch/
cat README.md
vim main.yaml
- name: Elasticsearch with custom configuration
  hosts: localhost
  roles:
    - role: elastic.elasticsearch

mkdir -p roles/elastic.elasticsearch
ls
mv defaults/ docs/ files/ filter_plugins/ handlers/ helpers/ meta/ tasks/ templates/ test/ vars/ roles/elastic.elasticsearch/
vim inventory
localhost ansible_connection=local

ansible-playbook -i inventory main.yaml
netstat -pnltu
```

## Install and Configure Kibana
```
sudo apt-get install kibana
sudo apt-get install nginx
sudo vim /etc/nginx/sites-enabled/default
echo "kibanaadmin:`openssl passwd -apr1`" | sudo tee -a /etc/nginx/htpasswd.users
sudo vim /etc/kibana/kibana.yml
elasticsearch.username
elasticsearch.password

systemctl start elasticsearch
systemclt start kibana
```

