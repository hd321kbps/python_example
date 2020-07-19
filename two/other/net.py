#!/usr/bin/python3
# -*- coding: utf-8 -*-

import http.client

conn = http.client.HTTPConnection("www.igormarchuk.ru")
conn.request("Get", "/")

resp = conn.getresponse()

print(resp.read())