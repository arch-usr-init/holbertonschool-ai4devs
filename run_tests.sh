#!/bin/bash
echo "Running Python..."; python3 -m pytest multi_language_code_generator/test_reference.py
echo "Running JS..."; node multi_language_code_generator/reference_implementation.js
