#build flask
 cd rest
 docker build -itag python_app:v1 .

# build nginx
 cd nginx
 docker build -itag nginx_server:v1 .

 docker compose up
