from setuptools import setup, find_packages

setup(
    name="smb3-split-offsetter",
    version="1.0.0",
    description=("Offset livesplit splits in SMB3"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="smb3-split-offsetter",
    author="narfman0",
    author_email="narfman0@blastedstudios.com",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
)
