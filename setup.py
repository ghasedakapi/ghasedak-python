import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ghasedak",
    version="0.1.4",
    author="Dariush Abbasi",
    author_email="poshtehani@gmail.com",
    description="Ghasedak sms webservice api wrapper for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/ghasedakapi/ghasedak-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)