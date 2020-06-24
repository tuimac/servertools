from setuptools import setup, find_packages
import os
import shutil

# Setuptools
setup(
    name="httptracker",
    version="1.0.0",
    url="https://github.com/tuimac/httptracker",
    author="tuimac",
    author_email="tuimac.devadm01@gmail.com",
    license="LICENSE.md",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.4",
       	"Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Software Distribution"
    ],
    description="Tools of tracing http requests.",
    python_requires=">=3.4.0",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "django>=3.0.0",
        "djangorestframework",
        "django-filter",
        "django-cors-headers",
        "setuptools"
    ],
    packages=["httptracker"],
    entry_points={
        "console_scripts": [
            "httptracker=httptracker.main:main"
        ]
    }
)
