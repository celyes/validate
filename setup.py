from setuptools import setup, find_packages

setup(
    name="checkr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.2.2",
        "setuptools>=59.6.0",
        "requests>=2.28.2",
        "ulid-py>=1.1.0",
        "validators>=0.20.0",
    ],
    author="Ilyes Chouia",
    author_email="celyes02@gmail.com",
    description="A simple package to validate data",
    url="https://github.com/celyes/validation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
