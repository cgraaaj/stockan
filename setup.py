from setuptools import setup
from pip._internal.req import parse_requirements


def readme():
    with open("README.md") as f:
        return f.read()

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(ir.req) for ir in install_reqs]
setup(
    name="stockan",
    version="0.0.1",
    description="StockMarketStategiesAnalyzer",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    author="Rajvel govindarajan",
    author_email="cgr.6713@gmail.com",
    keywords="Stockan",
    license="MIT",
    packages=["stock_analyzer",'nsetools'],
    install_requires=reqs,
    include_package_data=True,
)