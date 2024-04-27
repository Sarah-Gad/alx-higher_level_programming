#!/bin/bash
# This script sends a GET request to the URL with a  header variable
curl -sH "X-School-User-Id: 98" "$1"
