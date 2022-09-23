from setuptools import find_packages, setup

setup(
    name="pythia",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
