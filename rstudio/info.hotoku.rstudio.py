import os
import plist
import sys


if __name__ == "__main__":
    ret = plist.run("info.hotoku.rstudio.jinja.plist",
                    "../.envrc")
    print(ret)
