#build flask
 cd rest
 docker build --tag python_app:v1 .

# build nginx
 cd nginx
 docker build --tag nginx_server:v1 .

 docker compose up
