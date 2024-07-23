from setuptools import setup, find_packages

setup(
    name='Dignity',
    version='1.0.0',
    description='A programming language designed for large, conplex projects that need simpler code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dylan Do',
    author_email='dodylan190@gmail.com',
    url='https://github.com/Weno-Inc/Dignity',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, for example:
        # 'somepackage>=1.2.3',
    ],
    entry_points={
        'console_scripts': [
            'dignity=dignity.run_dignity:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache 2.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
)
