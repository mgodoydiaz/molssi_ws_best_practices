"""
Functions to measure molecules
"""
import numpy as np

from .measure import calculate_distance 
from .atom_data import atomic_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
   
    Parameters
    ----------
    symbols : list
        A list of elements.
   
    Returns
    -------
    mass : float
        The mass of the molecule"""
    
    suma = 0.
    for elemento in symbols:
       suma += atomic_weights[elemento]
    return suma

def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    The center of mass is weighted by each atom's weight.
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule. 

    Notes
    -----
    The center of mass is calculated with the formula
   
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    """
    M = calculate_molecular_mass(symbols)
    R = np.zeros(3)
    for i in range(len(coordinates)):
        r = coordinates[i]
        m = atomic_weights[symbols[i]]
        R+= r*m
    return R/M

