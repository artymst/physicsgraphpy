from setuptools import setup, find_packages

setup(
    name="physicsgraphpy",
    version="0.2.0",
    description="Beginner-friendly Python library for visualizing kinematics motion graphs",
    author="artymst",
    url="https://github.com/artymst/physicsgraphpy",  # Optional: your repo link
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
)
