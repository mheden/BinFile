from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="binfile",
    version="0.9.0",
    description="<TODO>",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent" "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Lindenmayer l-system lsystem",
    url="http://github.com/mheden/BinFile",
    author="Mikael Heden",
    author_email="mikael@heden.net",
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
