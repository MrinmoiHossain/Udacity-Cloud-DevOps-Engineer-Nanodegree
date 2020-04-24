```bash
sudo apt-get update
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo vim /etc/apt/sources.list
 > deb https://pkg.jenkins.io/debian-stable binary/

sudo apt-get install default-jdk -y
sudo apt-get update
sudo apt-get install jenkins -y
sudo systemctl status jenkins
```


* Source: https://pkg.jenkins.io/debian-stable/