#/usr/bin/bash

mongo admin --host localhost --port 27017 -u $MONGO_INIT_USERNAME -p $MONGO_INIT_PASSWORD --eval "
db.createUser({user: '$DB_USERNAME', pwd:'$DB_PASSWORD', roles:[{role: 'readWrite', db:'website'}]});"