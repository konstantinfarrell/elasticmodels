import sys
from setuptools import find_packages, setup

setup(
    name='elasticmodels',
    version='0.1.0',
    install_requires=['elasticsearch<2.0.0','elasticsearch-dsl<2.0.0'],
    packages=find_packages(),
    long_description=open('README.md').read(),
    author='Matt Johnson',
    extras_require={
        'dev': [
            "mock",
            "model_mommy",
            "coverage",
            "django" + ("<1.7" if sys.version_info[:2] < (2, 7) else "")
        ],
    }
)
