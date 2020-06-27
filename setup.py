from setuptools import setup, find_packages

setup(
    name='kocrawl',
    version='0.2',
    description='Korean web crawler collections',
    author='Hyunwoong Ko',
    author_email='gusdnd852@naver.com',
    url='https://github.com/Kochat-framework/kocrawl',
    install_requires=['numpy', 'beautifulsoup4', 'requests'],
    packages=find_packages(exclude=[]),
    keywords=['crawler', 'korean crawler', 'kochat'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
