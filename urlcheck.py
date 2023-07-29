#!/usr/bin/env python
#This code takes a URLs as input from a file and returns the status code of those URLs.

import requests as req

def urlread():
    try:
        filename = input("Please enter the file name: ")

        with open(filename, "r") as f:
            for url in f.readlines():
                resp = req.get(url.strip())
                code = resp.status_code
                print("Status code for " + url.strip() + ": " + str(code))
    except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))

urlread()
