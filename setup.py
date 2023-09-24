from setuptools import setup
from typing import List



def get_requirements_list()->list[str]:
    """
    Description: This function is going to return list of requirements
    mentioned in requirements.txt file

    return: This funtion is going to retun a list which contain name of
    libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()
# Declaring varaiables for setup functions

PROJECT_NAME = "housing-price-predictor"
VERSION = '0.0.1'
AUTHOR = "Srinath Laka"
DESCRIPTION = "This a project of prediction model of house prices"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

setup(
name = PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description = DESCRIPTION,
packages= PACKAGES,
install_requires = get_requirements_list()

)

if __name__ ==  "main":
    print(get_requirements_list)