import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclustertend",
    version="1.4.0",
    author="Ismaël Lachheb",
    author_email="ismael.lachheb@protonmail.com",
    description="A package to assess cluster tendency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lachhebo/pyclustertend", 
    keyword = ["cluster tendency", "clustering", "cluster", "machine learning",
                "hopkins", "VAT"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
