# Python - Rabbitmq - Mongodb

> Example using language Python handling queue rabbitmq and save-to mongodb

### Install environment
    + Python [Python](https://www.python.org/downloads) v2.7 to run.
    + Rabbitmq [Rabbit](https://www.rabbitmq.com/download.html)
    + Mongodb [Mongodb](https://www.mongodb.com) v3.4 to run.

- Install Extensions
```sh
$ sudo pip install pymongo
$ sudo pip install pika
```

### Config environment
- Rabbitmq
```sh
RABBIT_HOST = '127.0.0.1'
RABBIT_PORT = 5672
RABBIT_USER = 'guest'
RABBIT_PASS = 'guest'
RABBIT_VHOST = '/'
```
- Mongodb 
```sh
MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_DB   = 'db_sample'
```

### Use
- Send task to queue rabbitmq
```sh
$ python action.py sendqueue 
```

- Action queue from rabbitmq
```sh
$ python action.py progressqueue 
```
