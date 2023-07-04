import csv
import math

def calculate_range_azimuth_elevation(x, y, z):
    range = math.sqrt(x**2 + y**2 + z**2)
    azimuth = math.degrees(math.atan2(y, x))
    elevation = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
    return range, azimuth, elevation

# Assumed objects
objects = [
    {
        "name": "Cube",
        "points": [
            {"x": 1, "y": 1, "z": 1},
            {"x": 1, "y": 1, "z": -1},
            {"x": 1, "y": -1, "z": 1},
            {"x": 1, "y": -1, "z": -1},
            {"x": -1, "y": 1, "z": 1},
            {"x": -1, "y": 1, "z": -1},
            {"x": -1, "y": -1, "z": 1},
            {"x": -1, "y": -1, "z": -1},
        ]
    },
    {
        "name": "Sphere",
        "points": [
            {"x": 2, "y": 0, "z": 0},
            {"x": 0, "y": 2, "z": 0},
            {"x": 0, "y": 0, "z": 2},
        ]
    },
    {
        "name": "Cylinder",
        "points": [
            {"x": 1, "y": 0, "z": -2},
            {"x": 1, "y": 0, "z": -1.8},
            {"x": 1, "y": 0, "z": -1.6},
            {"x": 1, "y": 0, "z": -1.4},
            {"x": 1, "y": 0, "z": -1.2},
            {"x": 1, "y": 0, "z": -1},
            {"x": 1, "y": 0, "z": -0.8},
            {"x": 1, "y": 0, "z": -0.6},
            {"x": 1, "y": 0, "z": -0.4},
            {"x": 1, "y": 0, "z": -0.2},
            {"x": 1, "y": 0, "z": 0},
            {"x": 1, "y": 0, "z": 0.2},
            {"x": 1, "y": 0, "z": 0.4},
            {"x": 1, "y": 0, "z": 0.6},
            {"x": 1, "y": 0, "z": 0.8},
            {"x": 1, "y": 0, "z": 1},
            {"x": 1, "y": 0, "z": 1.2},
            {"x": 1, "y": 0, "z": 1.4},
            {"x": 1, "y": 0, "z": 1.6},
            {"x": 1, "y": 0, "z": 1.8},
        ]
    },
    # Add more objects here...
]

# Generate CSV file
filename = "object_data.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Object", "Point", "Range", "Azimuth", "Elevation"])  # Header row
    for obj in objects:
        for i, point in enumerate(obj['points']):
            range, azimuth, elevation = calculate_range_azimuth_elevation(point['x'], point['y'], point['z'])
            writer.writerow([obj['name'], i+1, range, azimuth, elevation])

print(f"CSV file '{filename}' generated successfully.")
