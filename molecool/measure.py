"""
Functions related to measurements.
"""

import numpy as np


def calculate_angle(
    rA: np.ndarray, rB: np.ndarray, rC: np.ndarray, degrees: bool = False
) -> float:
    """Calculate the angle between three points.

    Parameters
    ----------
    rA, rB, rC: np.ndarray
        The coordinates of each point.

    degrees: bool, optional
        Indicates whether the answer should be in degrees (True) or radians (False)

    Returns
    -------
    theta: float
        The angle created by the three points.
    """

    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


def calculate_distance(rA: np.ndarray, rB: np.ndarray) -> float:
    """Calculate the distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinates of each point.

    Returns
    -------
    distance : float
        The distance between the two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """

    d = rA - rB
    dist = np.linalg.norm(d)
    return dist
