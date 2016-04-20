#!/usr/bin/env python
# encoding: utf-8

s = str("date: invalid date ‘2324-23-02 03:03:00‘")
# s = s.encode("UTF-8")
if s.find("invalid") == -1:
  print "No 'is' here!"
else:
  print "Found 'invalid' in the string."