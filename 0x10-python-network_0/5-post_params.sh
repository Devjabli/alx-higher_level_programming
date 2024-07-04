#!/bin/bash
#Sends a POST request to the specified URL and shows the content of the response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "${1}"
