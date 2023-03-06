#!/bin/bash
# cd dds && ./workplace/scripts/run_implementation.sh

cleanup() {
	sudo killall flask
	sudo killall python
}
# run cleanup() on these signals
# TODO: it seems that this is not working for ctrl-C SIGINT
trap cleanup SIGINT SIGTERM EXIT

killall flask
killall python

# I am using miniconda3 on my chameleon machine, set up conda for this script
source /home/cc/miniconda3/etc/profile.d/conda.sh
conda activate dds

# start DDS servers in background
data_port=$(( 10000 + 1 ))
rm -rf server_temp/*
rm -rf server_temp-cropped/*

echo "concierge -- INFO -- Starting DDS Server @ :${data_port}"
FLASK_APP=../backend/backend.py flask run --port=${data_port} > /tmp/null & 

sleep 2

# start DDS clients in background, the last one in foreground
# the DDS client will also start the gRPC Pipeline server
python entrance.py