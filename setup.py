import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
        name="lambdata-dylan0stewart",
        version= "0.1.4",
        author= "dylan0stewart",
        description= " a collection of data science helper functions",
        long_description= LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/dylan0stewart/lambdataDCS",
        packages=setuptools.find_packages(),
        python_requires=">=3.5",
        install_requires= REQUIRED,
        classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]
        )

