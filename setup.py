from setuptools import setup, find_packages
setup(
    name='ghenv',
    version='1.0.0',
    packages=find_packages(),
    long_description_content_type="text/markdown",
    py_modules=['cli', 'main'],
    python_requires=">=3.10.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'certifi==2022.12.7',
        'cffi==1.15.1',
        'charset-normalizer==3.1.0',
        'Deprecated==1.2.13',
        'idna==3.4',
        'pycparser==2.21',
        'PyGithub==1.58.0',
        'PyJWT==2.6.0',
        'PyNaCl==1.5.0',
        'requests==2.28.2',
        'urllib3==1.26.14',
        'wrapt==1.15.0',
    ],
    entry_points={
        'console_scripts': [
            'ghenv=cli:main'
        ]
    },
)