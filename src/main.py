#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A module that generates code from a prompt
"""

__author__ = "Brian Koech"
__copyright__ = "None"
__credits__ = ["Brian Koech"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Brian Koech"
__email__ = "info@libranconsult.com"
__status__ = ""

# Import modules
from prompt_genius.ai_runner import generate_images

# Run the code generator

if __name__ == "__main__":
    CODE_PROMPT = (
        "You are a graphics designer. Generate a logo for a company called 'Piety Health' which offers care and nursing support to the disability sector in Australia"
    )

    code = generate_images(CODE_PROMPT)  # type: ignore
    print(code)
