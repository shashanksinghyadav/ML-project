from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # new line character will also get added
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
setup(
    name='mlproject',
    version='0.0.1',
    author='shashank',
    author_email='shashank.eee22@iitbhu.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)