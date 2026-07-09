from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fingerchips",
    version="1.0.0",
    author="SSA-66",
    description="FingerChips - A Python project for finger chips related functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SSA-66/FingerChips_In_Python",
    py_modules=["American", "Chinese", "Indian", "Korean", "french"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
