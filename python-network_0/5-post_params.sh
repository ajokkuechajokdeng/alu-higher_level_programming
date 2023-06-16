#!/bin/bash
# Takes in a URL sends a POST request to passes in URL displays the body of the reponse
curl -sHX -d "email=test@gmail.com&subject=I will always be here for PLD" POST "$1"
