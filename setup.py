import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PTC",
    version="0.0.1",
    author="Ismaël Lachheb",
    author_email="ismael.lachheb@protonmail.com",
    description="A cluster to assess cluster tendency of a datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject", #TOADD
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)