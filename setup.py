from setuptools import setup, find_packages

__version__ = '0.0.4'
__author__ = 'Paul de Lange'
__email__ = 'p.delange@uky.edu'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="opmpolhemus",
    version=__version__,
    author=__author__,
    author_email=__email__,
    license='MIT',
    description="sensor locations of opms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulmoonshine/opmpolhemus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy>=1.13'],
    python_requires='>=3.6',
)
