FROM openresty/openresty:1.13.6.2-bionic

EXPOSE 80

COPY server.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf

COPY ./app /local/www/app
