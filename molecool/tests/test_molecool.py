"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np
import pytest
import sys

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

def test_calculate_distance():
    """Test that calculates distance, calculates what we expect"""

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1
    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance


@pytest.mark.xfail
def test_calculate_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])


    expected_angle = 120
    
    calculated_angle = molecool.calculate_angle(r1,r2,r3,degrees=True)
    
    assert expected_angle==calculated_angle
    
@pytest.mark.skip()
def test_calculate_angle_60():
    r4 = np.array([0,0,-1])
    r5 = np.array([0,1,0]) 
    r6 = np.array([1,0,0])
    
    expected_angle2= 60
    
    calculated_angle2 = molecool.calculate_angle(r4,r5,r6,degrees=True)
    
    assert expected_angle2 == pytest.approx(calculated_angle2,abs=1e-2)

def test_build_bond_list():
    coordinates = np.array([ 
        [1,1,1],
        [2.4,1,1],
        [-0.4,1,1],
        [1,1,2.4],
        [1,1,-0.4]
    ])
    bonds = molecool.build_bond_list(coordinates)
    assert len(bonds)==4

    for bond_length in bonds.values():
        assert bond_length ==1.4

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert center_of_mass.all() == expected_center.all()

@pytest.mark.parametrize("r1 ,r2, r3, expected_angle",[
    (np.array([1,0,0]), np.array([0,0,0]),np.array([0,1,0]),90),
    (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]),60),
])

def test_calculate_angle_many(r1,r2,r3,expected_angle):
    calculated_angle = molecool.calculate_angle(r1,r2,r3,degrees=True)
    assert pytest.approx(calculated_angle) == expected_angle