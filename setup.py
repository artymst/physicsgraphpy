from setuptools import setup, find_packages

setup(
    name="physicsgraphpy",
    version="0.2.0",
    description="Beginner-friendly Python library for kinematics, projectile motion, and motion graph animation",
    author="artymst",
    url="https://github.com/artymst/physicsgraphpy",
    packages=find_packages(),  # Automatically finds your physicsgraphpy subfolder as a package
    install_requires=[
        "matplotlib",
        "numpy"
    ],
    python_requires=">=3.7",
    license="MIT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Education"
    ]
)
