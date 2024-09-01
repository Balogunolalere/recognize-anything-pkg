from setuptools import setup, find_packages

setup(
    name='recognize_anything',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'timm',
        'transformers',
        'fairscale',
        'pycocoevalcap'
    ],
    entry_points={
        'console_scripts': [
            'recognize_anything=recognize_anything.inference_ram:main',
        ],
    },
    package_data={
        'recognize_anything': [
            'datasets/*',
            'images/*',
            'ram/configs/*',
            'ram/data/*',
            'ram/models/*',
            'ram/utils/*'
        ]
    },
)
