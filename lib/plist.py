#!/usr/bin/env python3


import re
from jinja2 import Template, Environment, FileSystemLoader
import os
import click


def read_env_file(env_file):
    with open(env_file) as f:
        lines = [
            l.strip()
            for l in f.read().split("\n")
        ]
    vars = [
        re.sub("^export +(.+)=.+", "\\1", line)
        for line in lines
        if re.match("^export ", line)
    ]
    return vars


def run(tpl_file, env_file, data={}):
    env = Environment(loader=FileSystemLoader("."), trim_blocks=False)
    template = env.get_template(tpl_file)
    vars = read_env_file(env_file)
    for v in vars:
        data[v] = os.environ[v]
    with open("/tmp/hoge.txt", "w") as f:
        f.write(str(data))
    return template.render(data)


@click.command()
@click.option("--env", "-e", required=True)
@click.option("--data", "-D", multiple=True)
@click.argument("template")
def main(env, data, template):
    data2 = {k:v for k,v in [d.split("=") for d in data]}
    ret = run(template, env, data2)
    print(ret)

if __name__ == "__main__":
    main()
