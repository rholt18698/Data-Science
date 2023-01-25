#!/usr/bin/env python3
proto = ["ssh", "http", "https"] #Proto list
print(proto)
print(proto[1])  # print http
proto.extend("dns") # this line will add d, n, and s
print(proto)



