import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ADPClientKit",
    version="2025.2.18",
    author="Adrian Albrecht",
    author_email="adriandevprojects@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/adriandevprojects/ADPClientKit",
    license="GPL-3.0",
    description="AdrianDevProjects ClientKit SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
)