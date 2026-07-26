#!/usr/bin/python3
# filter for filterdiff
# to look into .pyc details
# requires  zypper in python3-xdis

import sys
import trace
import xdis.load

tracer = trace.Trace(
        trace = 1,
        count = 0
        )

def main():
    m = xdis.load.load_module(sys.argv[1])
    #print(m)


tracer.run('main()')
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")
