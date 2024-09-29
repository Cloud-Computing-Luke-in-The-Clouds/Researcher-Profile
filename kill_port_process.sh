#!/bin/bash

# Check if a port number is provided
if [ $# -eq 0 ]; then
    echo "Please provide a port number."
    echo "Usage: $0 <port_number>"
    exit 1
fi

PORT=$1

# Find the process ID using the port
PID=$(sudo lsof -t -i:$PORT)

# Check if a process was found
if [ -z "$PID" ]; then
    echo "No process found using port $PORT"
    exit 0
fi

# Kill the process
echo "Killing process $PID on port $PORT"
sudo kill -9 $PID

# Check if the kill was successful
if [ $? -eq 0 ]; then
    echo "Process successfully killed"
else
    echo "Failed to kill the process"
fi