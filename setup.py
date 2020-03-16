from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="polytope-sampling",
    version="0.1",
    author="David Walz",
    description="Uniform sampling subject to linear constraints",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DavidWalz/polytope-sampling",
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=["numpy", "scipy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering",
    ],
)
