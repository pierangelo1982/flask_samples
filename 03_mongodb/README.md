

install requirements
```
pip install -r requirements.txt
```

docker mongodb
```
docker run -d --name flask-mongo \
    -e MONGO_INITDB_ROOT_USERNAME=mongoadmin \
    -e MONGO_INITDB_ROOT_PASSWORD=mypassword \
    -p 27017:27017 \
    mongo
```