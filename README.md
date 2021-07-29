Using a flask app with nginx and uswig to send OSC commands to a PD patch - jsut the very first steps.

## Followed this tutorial:

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

## There is problem with the ownership of the socket file:

sudo tail /var/log/nginx/error.log:

    2021/07/29 16:04:22 [crit] 3737#3737: *4 connect() to unix:/home/pi/flask/hvc2/flasktest.sock failed (13: Permission denied) while connecting to upstream,    client: 127.0.0.1, server: hvc.berlin, request: "GET / HTTP/1.1", upstream: "uwsgi://unix:/home/pi/flask/hvc2/flasktest.sock:", host: "127.0.0.1"


It is solved only temporarely by running (after starting the service):

    sudo chown www-data:www-data flasktest.sock

And added to service:

    PrivateTmp=true

