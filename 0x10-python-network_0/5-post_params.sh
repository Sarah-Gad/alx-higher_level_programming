#!/bin/bash
# This script sends a POST request to the passed URL
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
