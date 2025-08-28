# Python boilerplate with uv

A starting template for Python projects, built from scratch using uv package manager.

## Pre-requisites ⚙️
- [uv](https://github.com/astral-sh/uv) installed.

## How to start 🛠️

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yanrdgs-dev/python-boilerplate.git
    cd python-boilerplate
    ```
2. **Create and activate the virtual environment:** 
    ```bash
    uv venv
    source .venv/bin/activate # use `.venv\Scripts\activate on Windows.
    ```

3. **Install the dependencies:**
    ```bash
    uv pip install -r requirements-dev.txt
    uv pip install -e .
    ```

4. **Install your own dependencies:**
    ```bash
    uv pip install <package_name>
    ```

5. **Code your packages in `src/template_package` and write your tests in `tests/`.**

## How to use 🖥️
- **Run all tests:**
    ```bash
    pytest
    ```

- **Format all codes:**
    ```bash
    black .
    ```

- **Code quality (linting)**
    ```bash
    flake8 .
    ```