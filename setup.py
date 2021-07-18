from setuptools import setup

setup(
    name='django-sage-encrypt',
    packages=['sage_encrypt'],
    version='0.4.3',
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
