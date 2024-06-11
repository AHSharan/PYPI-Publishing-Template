# PyPI Publishing Template

This repository contains a template and detailed instructions for publishing your Python package to PyPI. Follow the steps below to get your package live on PyPI.org.

## Steps to Publish Your Package to PyPI

### 1. Prepare Your Project

1. Ensure your project contains the necessary files:
   - `setup.py`
   - `README.md`
   - Any other required files (e.g., `LICENSE`, `.gitignore`)

2. Download the template and edit the files (Refer to the link given in resource section for the video explanation):
    

### 2. Create an Account on PyPI

1. Go to [PyPI.org](https://pypi.org/account/register/) and create an account.

### 3. Get Your PyPI API Token

1. Log in to your PyPI account.
2. Go to your account settings.
3. Navigate to the "API tokens" section.
4. Click on "Add API token".
5. Provide a name for your token and specify the desired scope (e.g., "Entire account").
6. Click "Add token".
7. Copy the generated token and keep it secure.

### 4. Build Your Package

1. Make sure you have the latest versions of `setuptools` and `wheel` installed:
    ```bash
    pip install --upgrade setuptools wheel
    ```

2. Build your package:
    ```bash
    python setup.py sdist bdist_wheel
    ```

### 5. Install Twine

1. Install Twine if you haven't already:
    ```bash
    pip install twine
    ```

### 6. Upload Your Package

1. Use Twine to upload your package to PyPI:
    ```bash
    twine upload dist/*
    ```

2. When prompted, enter your username (or `__token__` for token-based authentication) and your API token as the password.

### 7. Verify Your Upload

1. Check your package on [PyPI.org](https://pypi.org/) to ensure it has been uploaded successfully.

## Template Files

- `setup.py`: Contains metadata and configuration for your package.
- `README.md`: Your project's readme file (this file).
- Additional files like `LICENSE` and `.gitignore` as needed.

For more information and to download the template, visit the [GitHub repository](https://github.com/A-Sharan1/PYPI-Publishing-Template).

## Resources

- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
- [PyPI Documentation](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Youtube Video](https://youtu.be/6NnnRDTOObw)

Happy publishing!
