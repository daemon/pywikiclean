import setuptools


setuptools.setup(
    name="wikiclean",
    version="0.0.1",
    author="Ralph Tang",
    author_email="r33tang@uwaterloo.ca",
    description="Python port of lintool's tool for converting Wikipedia markup to plaintext.",
    url="https://github.com/daemon/pywikiclean",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
