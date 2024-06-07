from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() #Gets the long description from Readme file

setup(
    name='ProjectName',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'ExampleOfLibrary',
    ],  # Add a comma here
    author='John Doe',
    author_email='JohnDoe@xyz.com',
    description='This is the short description',

    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
     project_urls={
           'Source Repository': 'https://github.com/A-Sharan1/' #replace with your github source
    }
)
