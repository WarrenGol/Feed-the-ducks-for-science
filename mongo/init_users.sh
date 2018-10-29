#/usr/bin/bash

mongo admin --host localhost --port 27017 -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD --eval "
db.createUser({user: '$DB_USERNAME', pwd:'$DB_PASSWORD', roles:[{role: 'readWrite', db:'website'}]});"
