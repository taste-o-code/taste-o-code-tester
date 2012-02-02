#/bin/bash
PYTHONTPATH='../' nohup pyres_worker -f $HOME/logs/pyres_worker.log --port=6380 submissions &