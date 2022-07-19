"""
Module for work with resources
"""


def path(relative_path):
    """
    Get path to resource file
    """
    import tests
    from pathlib import Path
    return (
        Path(tests.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
