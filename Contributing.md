
---

# Contributing Guide

---

Thank you for your interest in contributing to the **riemann_stats_py** project! Contributions of all types are welcome—code improvements, bug reports, documentation enhancements, and feature suggestions.

## How to Contribute

### Reporting Issues

Reporting issues or bugs is one of the simplest ways to help improve the project.

- Check the [existing issues](https://github.com/yourusername/riemann_stats_py/issues) first to avoid duplication.
- Clearly describe the issue and steps to reproduce it, if possible.
- Include relevant details like Python version, operating system, and error messages.

You can open a new issue [here](https://github.com/yourusername/riemann_stats_py/issues/new).

### Contributing Documentation

Good documentation is vital. Improvements to clarity, completeness, or readability are especially helpful.

To contribute documentation:

1. Fork the repository.
2. Make your changes to documentation files (typically located in the `/docs` folder or docstrings within the code).
3. Submit a pull request (PR) clearly explaining your documentation improvements.

#### Building Documentation Locally

To build documentation locally:

```shell
pip install -r docs_requirements.txt
sphinx-build -b html docs docs/_build
```

You can view the built documentation by opening `docs/_build/index.html` in a browser.

### Contributing Code

Contributions in the form of code enhancements, bug fixes, and new features are encouraged!

Follow these steps:

1. **Fork** the repository to your GitHub account.
2. **Clone** the repository locally:

```shell
git clone https://github.com/yourusername/riemann_stats_py.git
```

3. **Create** a new branch for your changes:

```shell
git checkout -b feature/my-new-feature
```

4. Make your changes and commit them clearly.

```shell
git commit -am "Add my new feature"
```

5. **Push** your changes back to GitHub:

```shell
git push origin feature/my-new-feature
```

6. Submit a pull request clearly explaining your changes.

### Code Formatting

To maintain consistency, please format your code using [Black](https://github.com/psf/black) before submitting your pull request:

```shell
pip install black
black .
```

### Running Tests

Please ensure all existing unit tests pass and consider adding new tests for your changes:

```shell
python -m unittest discover tests
```

or using `pytest`:

```shell
pytest tests
```

## Pull Request Reviews

The maintainers will review your pull request and may suggest improvements. Communication and iteration are key—don’t hesitate to ask questions or discuss alternatives!

## Code of Conduct

We value a welcoming community and expect contributors to adhere to respectful and constructive communication. Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Feel free to open an issue or contact the maintainers if you have any questions. Your contributions and feedback are greatly appreciated!

