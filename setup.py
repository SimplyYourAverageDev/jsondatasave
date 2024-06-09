from setuptools import setup, find_packages

VERSION = '1.6'
DESCRIPTION = 'Facilitating the process to store JSON data'

# Reading the long description from README.md
with open("README.md", 'r', encoding='utf-8') as r:
    long_description = r.read()

# Setting up
setup(
    name="jsondatasave",
    version=VERSION,
    author="YourAverageDev",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SimplyYourAverageDev/jsondatasave",  # Your GitHub project URL
    project_urls={
        "Bug Tracker": "https://github.com/SimplyYourAverageDev/jsondatasave/issues",
        "Documentation": "https://github.com/SimplyYourAverageDev/jsondatasave#readme",
    },
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'JSON', 'Data Storage'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Specifying the license as an OSI approved license
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",  # It's good practice to specify which Python versions are supported
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",  # Assuming support up to Python 3.11
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT"
)