from setuptools import setup, find_packages
from os import path
from typing import Optional, List
import re


here = path.abspath(path.dirname(__file__))

def get_package_name(line: str) -> Optional[str]:
    package_name_version_pattern = re.compile(r"[a-zA-Z0-9\-]*==[\d\.]*")
    matched_string = package_name_version_pattern.match(line)
    return matched_string if matched_string is None else matched_string.group(0)

def fetch_installable_packages(packages: List[str]) -> List[str]:
    return list(filter(lambda element: element, map(get_package_name, f.readlines())))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt")) as f:
    requirements = fetch_installable_packages(f.readlines())

with open(path.join(here, "requirements-dev.txt")) as f:
    requirements_dev = fetch_installable_packages(f.readlines())

setup(
    name='algostructures',
    version='0.1.0',
    description='A simple python wrapper around datastructures and algorithms implemented in C',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    # url='https://github.com/tanayseven/algostructures-c',
    author='Tanay PrabhuDesai',
    author_email='tanayseven@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='sample setuptools development algorithms datastructures',
    package_dir={'': 'algostructures'},
    packages=find_packages(where='algostructures/'),  # Required
    python_requires='>=3.7, <4',
    install_requires=requirements,
    extras_require={
        "dev": requirements_dev
    },

    # TODO: Add binary files here
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # TODO: Add this
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/tanayseven/algostructures-c/issues',
        'Say Thanks!': 'https://saythanks.io/to/algostructures-c',
        'Source': 'https://github.com/tanayseven/algostructures-c/',
    },
)