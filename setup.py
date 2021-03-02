import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Video2Pics", # Replace with your own username
    version="0.0.1",
    author="Prem Kumar KM",
    author_email="premkumar_km@yahoo.co.in",
    description="Generate the pictures from the Video file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/premkumarkm/Video2Pics.git",
    project_urls={
        "Bug Tracker": "https://github.com/premkumarkm/Video2Pics.git",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)