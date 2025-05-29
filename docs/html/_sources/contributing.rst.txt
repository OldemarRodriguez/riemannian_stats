Source Code and Contributors
============================

The source code for the **Riemannian STATS** package is publicly available on GitHub:

GitHub Repository
-----------------

🔗 **GitHub Repository**:
`https://github.com/OldemarRodriguez/riemannian_stats.git <https://github.com/OldemarRodriguez/riemannian_stats.git>`_

You can visit the repository to:

- Access the complete source code
- Report issues or suggest improvements
- Fork the project and contribute

Contributing Guide
------------------

Thank you for your interest in contributing to the **Riemannian STATS** project! Contributions of all types are welcome—code improvements, bug reports, documentation enhancements, and feature suggestions.

How to Contribute
~~~~~~~~~~~~~~~~~

Reporting Issues
^^^^^^^^^^^^^^^^

Reporting issues or bugs is one of the simplest ways to help improve the project.

- Check the `existing issues <https://github.com/OldemarRodriguez/riemannian_stats/issues>`_ first to avoid duplication.
- Clearly describe the issue and steps to reproduce it, if possible.
- Include relevant details like Python version, operating system, and error messages.

You can open a new issue `here <https://github.com/OldemarRodriguez/riemannian_stats/issues/new>`_.

Contributing Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Good documentation is vital. Improvements to clarity, completeness, or readability are especially helpful.

To contribute documentation:

1. Fork the repository.
2. Make your changes to documentation files (located in the ``/docs`` directory).
3. Submit a pull request (PR) clearly explaining your documentation improvements.

Building Documentation Locally
""""""""""""""""""""""""""""""

To build documentation locally:

.. code-block:: shell

    pip install -r docs_requirements.txt
    sphinx-build -b html docs/ docs/html/

You can view the built documentation by opening ``docs/html/index.html`` in a browser.

Contributing Code
^^^^^^^^^^^^^^^^^

Contributions in the form of code enhancements, bug fixes, and new features are encouraged!

Follow these steps:

1. **Fork** the repository to your GitHub account.
2. **Clone** the repository locally:

   .. code-block:: shell

       git clone https://github.com/OldemarRodriguez/riemannian_stats.git

3. **Create** a new branch for your changes:

   .. code-block:: shell

       git checkout -b feature/my-new-feature

4. Make your changes and commit them clearly:

   .. code-block:: shell

       git commit -am "Add my-new-feature"

5. **Push** your changes back to GitHub:

   .. code-block:: shell

       git push origin feature/my-new-feature

6. Submit a pull request clearly explaining your changes.

Code Formatting
^^^^^^^^^^^^^^^

To maintain consistency, please format your code using `Black <https://github.com/psf/black>`_ before submitting your pull request:

.. code-block:: shell

    pip install black
    black .

Running Tests
^^^^^^^^^^^^^

Please ensure all existing unit tests pass and consider adding new tests for your changes:

Using unittest:

.. code-block:: shell

    python -m unittest discover tests

Or using ``pytest``:

.. code-block:: shell

    pytest tests

Pull Request Reviews
^^^^^^^^^^^^^^^^^^^^

The maintainers will review your pull request and may suggest improvements. Communication and iteration are key—don’t hesitate to ask questions or discuss alternatives!

Questions?
^^^^^^^^^^

Feel free to open an issue or contact the maintainers if you have any questions. Your contributions and feedback are greatly appreciated!

Contributors
------------

This package is developed and maintained by:

- **Oldemar Rodríguez Rojas** – `oldemar.rodriguez@ucr.ac.cr <mailto:oldemar.rodriguez@ucr.ac.cr>`_
- **Jennifer Lobo Vásquez** – `jennifer.lobo.vasquez@gmail.com <mailto:jennifer.lobo.vasquez@gmail.com>`_

We welcome contributions from the community!
If you are interested in contributing, please open an issue or submit a pull request on GitHub.

Thank you to everyone who supports and improves **Riemannian STATS**.
