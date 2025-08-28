from setuptools import setup, find_packages

setup(
    name="python-boilerplate",
    version="0.1.0",
    description="Python boilerplate with uv.",
    author="Yan Santos",
    packages=find_packages(where="src"),
    package_dir={'': "src"},
    install_requires=[],
    python_requires=">=3.8", # Change accordingly to pyproject.toml
)
