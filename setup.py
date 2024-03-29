from setuptools import find_packages, setup

setup(
    name='Flask_Demo',
    version='1.1.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'werkzeug', 'click', 'flask_bootstrap', 'pytest'
    ],
)
