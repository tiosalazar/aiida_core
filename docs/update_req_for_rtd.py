#!/usr/bin/env python
"""
Whenever the requirements in ../setup_requirements.py are updated,
run also this script to update the requirements for Read the Docs.
"""
import sys, os
sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0],os.pardir))

import setup_requirements

required_packages = sorted(setup_requirements.install_requires)

# Required version
req_for_rtd_lines = ['Sphinx>=1.5']

for package in required_packages:
    # To avoid that it requires also the postgres libraries
    if package.startswith('psycopg2'): 
        continue
    # Would need to install with process-dependency-links
    if package.startswith('plum'): 
        continue    
    req_for_rtd_lines.append(package)

req_for_rtd = "\n".join(sorted(req_for_rtd_lines))

basename = 'requirements_for_rtd.txt'

with open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 
                       basename), 'w') as f:
    f.write(req_for_rtd)

print "File '{}' written.".format(basename)





