#!/bin/bash
# This script takes in a URL as ana rgument, sends a GET request to it, & displays the body of the response
curl -sH "X-School-User-Id: 98" "${1}"
