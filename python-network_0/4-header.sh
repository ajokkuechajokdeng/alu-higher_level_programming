#!/bin/bash
# Take in a URL as an argument sned a get request and display the body of the response
curl -sG "$1" -H "X-School-User-Id: 98"
