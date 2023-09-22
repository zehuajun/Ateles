#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generate(option):
    import os
    from importlib import import_module
    with import_module("lib.load_config") as load_config:
        config_root = load_config.root(lang["no_file_exists"])
        if option["debug"]:
            print(lang["config_loaded"] + " " + os.path.abspath(".") + "config.yaml")
        config_theme = load_config.theme(config_root["theme"],lang["error_no_theme_config"])
        if option["debug"]:
            print(lang["config_loaded"] + " " + config_root["theme"]).replace("__init__.py", "") + "config.yaml")
            


