followed this tutorial:

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

problem:

sudo tail /var/log/nginx/error.log:

2021/07/29 16:04:22 [crit] 3737#3737: *4 connect() to unix:/home/pi/flask/hvc2/flasktest.sock failed (13: Permission denied) while connecting to upstream, client: 127.0.0.1, server: hvc.berlin, request: "GET / HTTP/1.1", upstream: "uwsgi://unix:/home/pi/flask/hvc2/flasktest.sock:", host: "127.0.0.1"


solved only temporarely by :

sudo chown www-data:www-data flasktest.sock

and added to service:

PrivateTmp=true

