import re
from setuptools import setup, find_packages


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(project + '/_version.py').read())
    return result.group(1)


with open("readme.md", "r") as fh:
    long_description = fh.read()

PROJECT_NAME = "template_python"

setup(
    name="template_python",
    version=get_property('__version__', PROJECT_NAME),
    author="Jordan Schupbach",
    author_email="jordan.schupbach@montana.edu",
    description="A template python project package",
    keywords="python, template",
    long_description=open('readme.md').read(),
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordans1882/template-python",
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",  # TODO... edit this license... consider freedom
    include_package_data=True,
    package_data={'': ['_assets/example_images/*.png']},
    # TODO: Add install_requires field?
)
