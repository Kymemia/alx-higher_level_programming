#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
[ $# -lt 2 ] && echo "Usage: $0 <URL> <filename>" && exit 1 curl -s "$1" -d "@2" -X POST -H "Content-Type: application/json"
