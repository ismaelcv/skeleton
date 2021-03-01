from setuptools import setup, find_packages

base_dependencies = ["click >= 7.1.2",
                     'fastapi',
                     'uvicorn']
dev_dependencies = [
    "pytest",
    "logging"
]

setup(
    name="skeleton",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="Ismael Cabral",
    install_requires=base_dependencies,
    extras_require={
        "dev": dev_dependencies,
    },
    entry_points={
        'console_scripts': [
            'skeleton = package1.cli:main'
        ]
    }

)



# setup.py vs requirements.txt
# where should we define requirements
#
# - In setup.py we define lenient, minimum version requirements
# - If(!) we have requirements, we define exact working requirements
# - requirements.txt is useful when we make docker images, for that I typically use pip-compile

