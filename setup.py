from setuptools import setup, find_packages
from os import getenv

setup(
    name='space-exploration-common-lib',
    version=getenv('VERSION', default='v0.0.4'),
    packages=find_packages(exclude=['tests']),
    package_dir={'space_exploration_common_lib': 'src/space_exploration_common_lib'},
    py_modules=[
        'space_exploration_common_lib.model',
        'space_exploration_common_lib.model.Duration',
        'space_exploration_common_lib.model.mission.ProjectMercury'
    ],
    python_requires='>=3.12, <4',
    include_package_data=True,
    install_requires=[
        'pydantic==2.7.1'
    ],
    author='Steven Hatch',
    author_email='stevegreghatch@gmail.com'
)
