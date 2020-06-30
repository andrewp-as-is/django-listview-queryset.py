import setuptools

setuptools.setup(
    name='django-listview-queryset',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
