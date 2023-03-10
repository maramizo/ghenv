from setuptools import setup, find_packages
setup(
    name='ghenv',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['cli', 'main'],
    python_requires=">=3.10.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        x for x in open('requirements.txt').read().split('\n') if x
    ],
    entry_points={
        'console_scripts': [
            'ghenv=cli:main'
        ]
    }
)