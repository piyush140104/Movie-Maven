# it is a small project so we dont need helper function else we helper function
# when u define local packets u have to define these things
from setuptools import setup

# why we do that
# if u want this project as packets so you can easily deploy on pypyi website u can host on pypyi
with open("README.md","r",encoding="utg-8") as fh:
    long_description=fh.read()
    
AUTHOR_NAME='Piyush Gupta'
SRC_REPO='src'
# we use streamlit u can also use flask we create web application using streamlit
LIST_OF_REQUIREMENTS=['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='piyush7988658764@gmail.com',
    description='A small example package for movies recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)
    
    