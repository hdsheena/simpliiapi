# new version to pypi (pip install twine):
# rm -rf dist && python setup.py sdist && python -m twine upload dist/*
import os
import setuptools

readme = os.path.join(os.path.dirname(__file__), "README.md")
with open(readme, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpliiapi",
    description="a screen-scraping API for Mint.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="2.15",
    packages=["simpliiapi"],
    license="The MIT License",
    author="Michael Rooney",
    author_email="mrooney.simpliiapi@rowk.com",
    url="https://github.com/simpliiapi/simpliiapi",
    install_requires=[
        "configargparse",
        "oathtool",
        "pandas>=1.0",
        "requests",
        "selenium>=4.3.0,<5.0.0",
        "selenium-requests>=2.0.3",
        "xmltodict",
        "keyring",
    ],
    python_requires=">=3.6",
    entry_points=dict(
        console_scripts=[
            "simpliiapi = simpliiapi.cli:main",
        ],
    ),
)
