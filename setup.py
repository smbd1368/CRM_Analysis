from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CRM_Analysis",
    version="0.2.0",  # Increment this version number
    author="mohamad davoodi",
    author_email="mohamadbagherdavoodi@gmail.com",
    description="A package for Customer Relationship Management (CRM) analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smbd1368/CRM_Analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.0",
        "scikit-learn>=0.24.0",
    ],
)
