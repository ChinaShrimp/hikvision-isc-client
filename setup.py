import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hikvision-isc-client", # Replace with your own username
    version="0.0.1",
    author="Lyon Liang",
    author_email="ll_nwpu@163.com",
    description="Client to interact with Hikvision iSC platform using open API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChinaShrimp/hikvision-isc-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
)