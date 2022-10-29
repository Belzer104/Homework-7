from setuptools import setup, find_namespace_packages

setup(
    name= "clean_folder",
    version= "0.0.1",
    author= "Illia",
    url= "hhttps://github.com/Belzer104",
    license= "MIT",
    packages= find_namespace_packages(),
    description = "Sorted file",
    long_description= open("README.md").read(),
    entry_points= {'console_scripts': ['clean-folder = clean_folder.clean:run_sort']}   
)