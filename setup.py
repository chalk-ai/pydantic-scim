import re
from codecs import open
from os import path

from setuptools import find_packages, setup


def read(name: str) -> str:
    repo_root = path.abspath(path.dirname(__file__))
    with open(path.join(repo_root, name)) as f:
        return f.read()


def get_version() -> str:
    version_file = "_version.py"
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", read(version_file), re.M)
    assert match is not None, f"Unable to find version string in {version_file}"
    return match.group(1)


setup(
    version=get_version(),
    name="pydantic-scim",
    author="Chalk AI, Inc.",
    description="Pydantic types for SCIM",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.8.0",
    url="https://chalk.ai",
    packages=find_packages(exclude=("tests",)),
    install_requires=read("requirements.txt").splitlines(),
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
)
