from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.3.3',
    description='Clean folders',
    url='https://github.com/manu/DZ_7',
    author='Manushyna Nataliia',
    author_email='nataliia.manushyna@gmail.com',
    license='',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})