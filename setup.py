import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Text_summarization_kaggleX"
AUTHOR_USER_NAME = "kunaltembhare003"
SRC_REPO = "textSummarizer"
AUTHEOR_EMAIL  = "kunaltembhare003@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHEOR_EMAIL,
    description="Text Summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kunaltembhare003/Text_summarization_kaggleX",
    project_urls={
        "Bug Tracker": "https://github.com/kunaltembhare003/Text_summarization_kaggleX/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)


