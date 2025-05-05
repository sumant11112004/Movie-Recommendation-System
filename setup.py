from setuptools import setup 

with open("REDME.md", "r", encoding= "utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'Sumant Kumar'
SRC_REPO = 'src'
LIST_of_Requirement= ['streamlit']

setup(
    
    name = SRC_REPO,
    version = '0.0.1',
    author= AUTHOR_NAME,
    author_email='sumantkumar11112004@gmail.com',
    description='A simple python package to make a simple web app for movie recommendation system',
    long_description= long_description,
    long_description_content_type='text/markdown',
    package =[SRC_REPO],
    python_requires = '>=3.10',
    install_requires = LIST_of_Requirement,

)
