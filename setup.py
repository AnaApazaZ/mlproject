from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e."

def get_requiremets(file_path:str)->List[str]:
    '''
    this function will return rewuirements
    '''
    requiremets = []
    with open(file_path) as file_obj:
        requiremets = file_obj.readlines()
        requiremets=[req.replace("\n","") for req in requiremets]

        if HYPHEN_E_DOT in requiremets:
            requiremets.remove(HYPHEN_E_DOT)
    return requiremets

setup(
    name="mlproject",
    version="0.0.1",
    author="Ana Apaza",
    author_email="anapapazaz@gmail.com",
    packages=find_packages(),
    install_requires=get_requiremets('requirements.txt')
)