#!/bin/bash
# This script akes in a URL and displays all HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
