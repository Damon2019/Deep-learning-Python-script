#!/usr/bin/env bash
echo "ubuntu" | sudo -S netstat -tlnp
cd /home/ubuntu
sudo ./jetson_clocks.sh
#ubuntu
sleep 2
cd /home/ubuntu/hf/all/tracker
sudo ./build/bin/tracking_demo

