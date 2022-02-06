from setuptools import find_packages, setup

setup(
    name="hdebug",
    version="0.0.0",
    description="Hypothesis debugging with vscode",
    python_requires=">=3.9",
    packages=find_packages(exclude=["tests"]),
    package_data={
        "": ["py.typed"],
    },
    install_requires=["hypothesis==6.36.1"],
    extras_require={
        "dev": [
            "autoflake~=1.4",
            "black~=21.10b0",
            "build~=0.7",
            "isort~=5.9",
            "flake8~=4.0",
            "flake8-annotations~=2.7",
            "flake8-colors~=0.1",
            "pytest~=6.2",
        ]
    },
)
