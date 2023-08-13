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
from prompt_genius.ai_runner import generate_code

# Run the code generator

if __name__ == "__main__":
    CODE_PROMPT = (
        "Write a python function that takes a String"
        "as input and returns the number of vowels in the string."
    )

    code = generate_code(CODE_PROMPT)  # type: ignore
    print(code)
