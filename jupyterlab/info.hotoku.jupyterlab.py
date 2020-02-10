import os
from jinja2 import Template, Environment, FileSystemLoader
import plist


def run():
    env = Environment(loader=FileSystemLoader("."), trim_blocks=False)
    template = env.get_template("info.hotoku.jupyterlab.jinja.plist")
    vars = [
        "HOTOKU_PLIST_DESTPATH",
        "HOTOKU_PLIST_DOCKER",
        "HOTOKU_PLIST_JUPYTERLAB_EXEPATH",
        "HOTOKU_PLIST_JUPYTERLAB_WORKDIR",
        "HOTOKU_PLIST_JUPYTERLAB_LOGOUT",
        "HOTOKU_PLIST_JUPYTERLAB_LOGERR",
        "HOTOKU_PLIST_JUPYTERLAB_PORT"
    ]
    data = {}
    for v in vars:
        data[v] = os.environ[v]
    print(template.render(data))


if __name__ == "__main__":
    run()
