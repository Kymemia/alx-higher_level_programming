#!/bin/bash
# This script takes in a URL, sends a request to it, & displays the size of the body in response
curl -s "${1}" | wc -c
