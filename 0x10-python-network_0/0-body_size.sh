#!/bin/bash
# This script will takes in a URL, sends a request to that URL
curl -s "$1" | wc -c
