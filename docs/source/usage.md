# Usage

## Installation

To install lumache:

```console
(.venv) $ pip install lumache
```

## Creating recipes

To create a recipe, you can use the {py:func}`lumache.get_random_ingredients` function. This function returns a list of random ingredients.


```{eval-rst}
.. autofunction:: lumache.get_random_ingredients
```

Sometime, an {py:exc}`lumache.InvalidKindError` error will be raised

```{eval-rst}
.. autoexception:: lumache.InvalidKindError
```