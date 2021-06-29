from setuptools import setup, find_packages

setup(
    name='django-sage-encrypt',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    version='0.0.1',
    license='GNU',
    description='encrypt PostgreSQL database',
    author='Sage Team',
    author_email='mail@sageteam.org',
    url='https://github.com/sageteam-org/django-sage-encrypt',
    download_url='https://github.com/sageteam-org/django-sage-encrypt/archive/refs/tags/0.1.tar.gz',
    keywords=['django', 'python', 'encrypt', 'PostgreSQL', 'postgres'],
    install_requires=[
        'Django',
    ]
)
