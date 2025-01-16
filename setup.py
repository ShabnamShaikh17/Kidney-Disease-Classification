import setuptools

with open("README.md", "r", encoding ="utf-8") as f:
long_description  = f.read()

__version__= "0.0.0"
REPO_NAME="Kidney-Disease-Classification"
AUTHOR_USER_NAME="ShabnamShaikh17"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL "shabnamshk017@gmail.com"
setuptools.setup(
name=SRC_REPO,
version=__version__,
author=AUTHOR_USER_NAME,
author_email = AUTHOR_EMAIL,
description = "A small python package for CNN app",
Long_description=long_description,
Long_description_content="text/markdown",

url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls={
    "bug tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
},
package_dir={"":"src"},
packages=setuptoools.find_packages(where="src")
)