#!/usr/bin/env python

import harborclient

host = "10.69.1.246"
user = "admin"
password = "Harbor12345"
protocol = "http"

client = harborclient.HarborClient(host, user, password)
client.set_project_private("library")