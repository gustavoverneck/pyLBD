import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from src.setup import log

'''
    This is still a work in progress. The idea is to import a .stl file and scale it to fit a grid.
'''

def load_stl_file(file_path):
    """Loads an .stl file and returns the vertices and model information."""
    log("Importing .stl file.")
    model_mesh = mesh.Mesh.from_file(file_path)
    vertices = model_mesh.vectors.reshape(-1, 3)  # Reshape the vertices to a Nx3 array
    return vertices

def scale_and_dimensionalize(vertices, grid_shape=(10, 10, 10), target_dimension=2, position=(0, 0, 0), scale=1, rotation_angle=0):
    """
    Adjusts the model to fit into a grid of size nx by ny by nz, changes its position, allows scaling, and rotates the model.

    - `vertices`: Vertices of the STL model (Nx3 array).
    - `grid_shape`: Size of the grid (nx, ny, nz).
    - `target_dimension`: Desired dimensionality (1, 2, or 3).
    - `position`: New position of the object within the grid.
    - `scale`: Scale factor for the object (default is 1, which fits the object perfectly).
    - `rotation_angle`: Angle in degrees to rotate the model (default is 0).
    """
    log("Dimensionalizing, scaling and rotating .stl object.")
    # Dimensionalize model
    if target_dimension == 1:
        # Keeps only one coordinate (x)
        vertices = vertices[:, 0].reshape(-1, 1)
    elif target_dimension == 2:
        # Keeps only two coordinates (x, y)
        vertices = vertices[:, :2]
    elif target_dimension == 3:
        #  Keeps all three coordinates (x, y, z)
        vertices = vertices[:, :3]
    else:
        log("ValueError: target_dimension must be 2.")
        raise ValueError("target_dimension must be 2.")

    # Get the minimum and maximum coordinates of the model
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    model_size = max_coords - min_coords

    # Get the grid size
    nx, ny, nz = grid_shape

    # Calculate the scale factor
    scale_factors = np.array([nx, ny, nz])[:target_dimension] / model_size
    scale_factor = min(scale_factors)  # Maintains the proportion in the adjustment

    # Apply the user-defined scale
    scale_factor *= scale

    # Scale the model
    vertices_scaled = (vertices - min_coords) * scale_factor

    # Calculate the offset
    offset = np.array([nx, ny, nz])[:target_dimension] / 2 - (model_size * scale_factor) / 2
    vertices_transformed = vertices_scaled + offset + np.array(position)[:target_dimension]

    # Rotate the model around its center
    if rotation_angle != 0:
        rotation_angle_rad = np.deg2rad(rotation_angle)
        if target_dimension == 2:
            rotation_matrix = np.array([
                [np.cos(rotation_angle_rad), -np.sin(rotation_angle_rad)],
                [np.sin(rotation_angle_rad), np.cos(rotation_angle_rad)]
            ])
        elif target_dimension == 3:
            rotation_matrix = np.array([
                [np.cos(rotation_angle_rad), -np.sin(rotation_angle_rad), 0],
                [np.sin(rotation_angle_rad), np.cos(rotation_angle_rad), 0],
                [0, 0, 1]
            ])
        # Translate vertices to the center, rotate, then translate back
        center = np.mean(vertices_transformed, axis=0)
        vertices_transformed = np.dot(vertices_transformed - center, rotation_matrix) + center

    return vertices_transformed

