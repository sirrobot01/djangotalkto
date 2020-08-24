from setuptools import setup

setup(
    name="django-talkto",
    version=0.1,
    description="A Django app to talk to APIs.",
    long_description="file: README.md",
    url="https://www.biodun.dev/",
    author="Akere Mukhtar",
    author_email="akeremukhtar10@gmail.com",
    license="BSD-3-Clause",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "httpx",
        "django"
    ],
    extras_require={
        'rest': ["djangorestframework"]
    }
)
