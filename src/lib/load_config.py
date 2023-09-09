#!/usr/bin/env python
# -*- coding: utf-8 -*-

# root()函数用来打开根配置文件并返回配置，函数仅接受一个变量lang，为语言配置中的 no_file_exists 键值
import sys


def root(lang):
    import yaml

    if os.path.exists("config.yaml"):
        with open("config.yaml", "r") as tmp:
            config_root = yaml.load(tmp)
    else:
        print(lang + " config.yaml")
        sys.exit(1)
    return config_root


# theme()函数用来打开主题配置文件并返回配置，函数仅接受2个变量config_root_theme和lang，config_root_theme为根配置文件中的theme键值，lang为语言配置中的 error_no_theme_config 键值
def theme(config_root_theme, lang):
    import yaml
    import os

    if (
        config_root_theme.split("-")[0] == "ateles"
        and config_root_theme.split("-")[1] == "theme"
    ):
        import inspect

        with open(
            inspect.getfile(config_root_theme).replace("__init__.py", "")
            + "config.yaml",
            "r",
        ) as tmp:
            config_theme = yaml.load(tmp)
    elif os.path.exists("config." + config_root_theme + ".yaml"):
        with open("config." + config_root_theme + ".yaml", "r") as tmp:
            config_theme = yaml.load(tmp)
    elif os.path.exists("themes/" + config_root_theme + "/config.yaml"):
        with open("themes/" + config_root_theme + "/config.yaml", "r") as tmp:
            config_theme = yaml.load(tmp)
    else:
        print(lang)
        sys.exit(1)
    return config_theme
