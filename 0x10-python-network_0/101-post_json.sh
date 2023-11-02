#!/bin/bash
# Standard comment placeholder, REMEBER TO CHANGE THIS OO!!!
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
