import setuptools

setuptools.setup(
    name                            = "tutorial-resource",
    description                     = "Training models with scikit-learn in orquestra.",
    url                             = "https://github.com/luisguiserrano/tutorial-resource",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {"" : "python"},
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "pandas",
        "sklearn",
        "numpy",
   ],
)
