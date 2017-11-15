#!/usr/bin/env python

import sys, csv

f = open(sys.argv[1])

rows = csv.DictReader(f.readlines())

fields = ['id','x','y','z']
out = csv.DictWriter(sys.stdout, fieldnames=fields)
seen = []
for row in rows:
    id = row['id']
    for field in fields[1:]:
        row[field] = abs( int(row[field]) )

    if id in seen:
        seen.append(id)
        print("Found duplicate: {}".format(row['id']), file=sys.stderr)
        continue

    out.writerow(row)
