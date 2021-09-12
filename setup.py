from setuptools import find_packages, setup

base_dependencies = [
    "pandas>=1.2.4",
    "scikit-learn>=0.24.2",
    "seaborn>=0.11",
    "python-dateutil>=2.8.1",
]


additional_dependencies = {
    "dev": [
        "black>=20",
        "pre-commit>=2.15.0",
        "pytest>=6.2.1",
        "pylint>=2.7.4",
        "fire>=0.4.0",
    ],
    # # don't want to install this on your VM since it's shipped with Databricks connect
    # "ci": ["pyspark"],
}


setup(
    name="skeleton",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="Ismael Cabral",
    install_requires=base_dependencies,
    extras_require=additional_dependencies,
    entry_points={"console_scripts": ["skeleton = package1.cli:main"]},
)


# setup.py vs requirements.txt
# where should we define requirements
#
# - In setup.py we define lenient, minimum version requirements
# - If(!) we have requirements, we define exact working requirements
# - requirements.txt is useful when we make docker images, for that I typically use pip-compile
