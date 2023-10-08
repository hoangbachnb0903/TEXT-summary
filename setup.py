import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'TEXTOOL-summary'
AUTHOR_USERNAME = 'DEV_HoangNT'
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = 'hoangnt12092@gmail.com'

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description=" a small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    project_urls ={
        "BugTracker":f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    }
    package_dir={"":"src"},
    packages=setuptools.findpackages(where="src")
)
