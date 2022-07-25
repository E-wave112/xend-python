import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="xend_python_sdk",
    version="0.1.6",
    description="The Xend Finance SDK arms python developers with the ability to build DeFi \
    applications with Xend Finance without needing to understand the complexities  \
    of the underlying blockchain or layer2 infrastructure.",
    author="Osagie Iyayi",
    packages=find_packages(),
    author_email="iyayiemmanuel1@gmail.com",
    url="https://github.com/E-wave112/xend-python",
    license="MIT",
    install_requires=["web3", "web3[tester]", "requests"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",
        # Specify which python versions that you want to support
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["python", "blockchain", "cryptocurrency", "layer2", "defi"],
    zip_safe=False,
)
