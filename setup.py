import os
import typing
from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'


def get_requirements(file_name: str) -> typing.List[str]:
    """_summary_:This functions will return the list of requirements 

    Args:
        file_name (str): _description_: name of file from we want to get requirements

    Returns:
        typing.List[str]: _description_: List of requirements
    """
    requirements = []
    with open(file_name, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            """_summary_: This will remove -e . from requirements when setup.py is called directly"""

            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    description="complete end to end ml projects",
    author="Mangaldeep",
    author_email="mangaldeep95.ms@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
