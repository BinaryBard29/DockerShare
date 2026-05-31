FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf

COPY shared-files /usr/share/nginx/html

EXPOSE 80