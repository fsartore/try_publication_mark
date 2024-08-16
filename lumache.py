"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    This function defines a rule that ensures a task is scheduled 
    for the exact number of days specified by self.task_days for 
    a given index i in the model m.
    
    :param self: Reference to the current instance of the class.
    :param m: The model containing the activity variables.
    :param i: The index for the task.
    :returns: True if the sum of days scheduled for task i equals self.task_days, False otherwise.
    :rtype: bool
    
    The return equation is:
    \[
    \sum_{j} m.x[i, j] == self.task_days
    \]
    """
    return ["shells", "gorgonzola", "parsley"]

