#!/usr/bin/env python3

import sys
import os
import subprocess

def run():
    in_name = sys.argv[1]
    pre, ext = os.path.splitext(in_name)
    out_name = pre + ".pdf"
    template = None
    with open(in_name, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("template"):
                parts = line.split(":", 2)
                if len(parts) > 1:
                    template = parts[1].strip()
                    break
    print("compiling '{}' to '{}' using template '{}'".format(in_name, out_name, template))
    # subprocess.run(['pandoc', '--template=/home/kratenko/PycharmProjects/brief/brief/templates/'+template, in_name, '-o', out_name])
    subprocess.run(['pandoc', in_name, '-s', '-o', out_name, '--template='+template])


if __name__ == '__main__':
    run()
