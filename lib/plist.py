import re
from jinja2 import Template, Environment, FileSystemLoader
import os


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


def run(tpl_file, env_file):
    env = Environment(loader=FileSystemLoader("."), trim_blocks=False)
    template = env.get_template(tpl_file)
    vars = read_env_file(env_file)
    data = {}
    for v in vars:
        data[v] = os.environ[v]
    with open("/tmp/hoge.txt", "w") as f:
        f.write(str(data))
    return template.render(data)
