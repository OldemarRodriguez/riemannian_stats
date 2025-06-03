
---

#  Contributing Guide

Thank you for your interest in contributing to **Riemannian STATS**! All contributions are welcome, code improvements, bug reports, documentation enhancements, or feature suggestions.

---

## 🧩 How You Can Contribute

### 🐞 Reporting Issues

One of the simplest and most valuable ways to help is reporting bugs or issues.

* Check the [existing issues](https://github.com/OldemarRodriguez/riemannian_stats/issues) to avoid duplicates.
* Clearly describe the problem and how to reproduce it.
* Include details like Python version, operating system, and any error messages.

You can open a new issue [here](https://github.com/OldemarRodriguez/riemannian_stats/issues/new).

---

### 📚 Improving Documentation

Good documentation is crucial. If you spot anything unclear or outdated, feel free to contribute!

#### Steps to contribute docs:

1. Fork the repository.
2. Make changes to the documentation inside the `/docs` directory.
3. Submit a pull request with a clear explanation of your improvements.

#### 🛠️ Build the documentation locally:

You need **Sphinx** and the **Furo theme**:

```bash
pip install sphinx furo
```

Then build the docs:

```bash
cd docs
sphinx-build -b html source html
```

Open `docs/html/index.html` in a browser to view the result.

---

### 🧠 Contributing Code

Code contributions, bug fixes, new features, refactors, are very welcome.

#### Workflow:

1. **Fork** the repository.

2. **Clone** it:

   ```bash
   git clone https://github.com/OldemarRodriguez/riemannian_stats.git
   ```

3. **Create a feature branch**:

   ```bash
   git checkout -b feature/my-new-feature
   ```

4. Make your changes and commit:

   ```bash
   git commit -am "Add my-new-feature"
   ```

5. **Push to your fork**:

   ```bash
   git push origin feature/my-new-feature
   ```

6. Open a **pull request** with a clear summary of your changes.

---

## 🧼 Code Style & Testing

### 🎨 Code Formatting

Use [Black](https://github.com/psf/black) to keep code consistent:

```bash
pip install black
black .
```

### ✅ Run Tests

Please make sure all tests pass before submitting:

```bash
python -m unittest discover tests
```

Or if you prefer `pytest`:

```bash
pytest tests
```

---

## 🔍 Pull Request Reviews

Maintainers will review your pull request and may suggest improvements. Don’t hesitate to ask questions, feedback is part of the process!

---

## ❓ Questions?

Feel free to open an issue or reach out. We’re happy to help and grateful for your contribution!

