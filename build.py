#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default
import platform
import os

os.environ['CONAN_USERNAME'] = os.environ.get('CONAN_USERNAME','conanos')

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    items = []
    for item in builder.items:
        # skip mingw cross-builds
        if platform.system() == "Windows":
            if item.settings["compiler"] != "Visual Studio":
                continue
            if not item.options["libffi:shared"]:
                continue
        items.append(item)

    builder.items = items

    builder.run()
