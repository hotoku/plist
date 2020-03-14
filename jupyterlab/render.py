import os
import plist
import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="render")
    parser.add_argument("tmp")
    parser.add_argument("env")
    args = parser.parse_args()

    ret = plist.run(args.tmp, args.env)
    print(ret)
