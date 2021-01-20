import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ibm-functions",
    version="0.0.1",
    author="davetropeano",
    author_email="davetropeano.com",
    description="orchestraion and state wrapper for IBM Cloud Functions",
    long_description=long_description,
    url="https://github.com/davetropeano/ibm-functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
