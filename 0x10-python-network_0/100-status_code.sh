#!/bin/bash
# Standard comment placeholder, REMEBER TO CHANGE THIS OO!!!
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
