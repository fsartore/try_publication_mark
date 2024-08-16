# Usage

## Installation

To install lumache:

```console
(.venv) $ pip install lumache
```

## Creating recipes

To create a recipe, you can use the <a href="https://github.com/fsartore/try_publication_mark/blob/main/lumache.py#L18-L26" target="_blank">`lumache.get_random_ingredients`</a> function. This function returns a list of random ingredients.

```{math}
\begin{aligned}
    \min  \quad  &\sum_{i \in P} \sum_{y \in Y } \delta_y C_{i,y}^I a_{i,y}+
    \sum_{i \in P}\sum_{y \in Y} \delta_y C_{i,y}^F (b_{i,y} + a_{i,y} - r_{i,y}) +\\
    &\sum_{i \in P}\sum_{y \in Y} \sum_{h \in H} \delta_y w_h C^V_{i,y,h} q_{i,y,h} 
\end{aligned}
```

```{eval-rst}
.. autofunction:: lumache.get_random_ingredients
```

Sometime, an {py:exc}`lumache.InvalidKindError` error will be raised

```{eval-rst}
.. autoexception:: lumache.InvalidKindError
```