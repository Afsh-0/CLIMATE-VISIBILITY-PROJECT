from setuptools import setup, find_packages

setup(
    name="CIMATE_VISIBILITY_PROJECT",
    version="1.0.0",
    author="Afsha",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "joblib",
        "pyyaml"
    ]
)