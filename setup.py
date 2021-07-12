import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gender_extractor",
    version="0.1.0",
    description="Extract the suspected gender given a name",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/wwydmanski/gender-extractor",
    author="Witold Wydmański",
    author_email="witold.wydmanski@uj.edu.pl",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gender_extractor"],
    include_package_data=True,
)
