from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="binfile",
    version="0.9.0",
    description='A simple Python module for reading and writing "normal" datatypes'
    + "(such as U8, S64, null terminated strings etc.) from or to a file.",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="binary file datatype lowlevel",
    url="http://github.com/mheden/BinFile",
    author="Mikael Heden",
    author_email="mikael@heden.net",
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
