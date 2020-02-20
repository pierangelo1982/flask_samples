

crea virtualenv per python 3
```
virtualenv -p python3 env

source env/bin/activate
```

install requirements:
```
pip3 install -r requirements.txt
```

http://127.0.0.1:5000/home
```
{
  "message": "tutti mi possono vedere"
}
```

http://127.0.0.1:5000/login
```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlciIsImV4cCI6MTU4MjIzMjMwOH0.yaG71sw-Ldb47juRniChaZUKyu1zxVEtxjzhLmoZ4I8"
}
```
http://127.0.0.1:5000/dashboard?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlciIsImV4cCI6MTU4MjIzMjMwOH0.yaG71sw-Ldb47juRniChaZUKyu1zxVEtxjzhLmoZ4I8
```
{
  "message": "area riservata"
}
```