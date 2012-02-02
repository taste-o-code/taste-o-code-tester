#/bin/sh

nohup pyres_web --dsn=localhost:6379 --port=8080 &
nohup pyres_web --dsn=localhost:6380 --port=8081 &