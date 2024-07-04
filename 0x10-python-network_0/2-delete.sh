#!/bin/bash
#Sends a DELETE request to the URL provided as the first argument and shows the content of the response body
curl -s -X DELETE "${1}"
