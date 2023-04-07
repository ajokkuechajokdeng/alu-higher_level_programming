#!/bin/bash
# Receiving content and displaying content length information
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
