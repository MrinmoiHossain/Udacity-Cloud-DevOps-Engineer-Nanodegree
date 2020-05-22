```bash
cd makeCoinChange/
ls
source venv/bin/activate
which python
which python3
pip3 install ipython
ipython
```

```ipython
!pip3 install requests 
import requests                                                              
url = "https://njt9zvmti2.execute-api.us-east-1.amazonaws.com/default/cloud9-makeCoinChange-makeCoinChange-1PMT5VNAN4SAA"                                         request = requests.post(url, json={"amount":1.45})                                   request                                                                              request.json()
```