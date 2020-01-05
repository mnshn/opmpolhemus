import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opmpolhemus-paulmoonshine",  # Replace with your own username
    version="0.0.1",
    author="pdl",
    author_email="p.delange@uky.edu",
    description="coreg of opms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulmoonshine/opmpolhemus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
