"""
Module for work with resources
"""


def path(relative_path):
    """
    Get path to resource file
    """
    import test
    from pathlib import Path
    return (
        Path(test.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )
