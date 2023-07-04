import csv
import math
from sklearn.cluster import DBSCAN, MeanShift
from sklearn.metrics import accuracy_score

def calculate_range_azimuth_elevation(x, y, z):
    range = math.sqrt(x**2 + y**2 + z**2)
    azimuth = math.degrees(math.atan2(y, x))
    elevation = math.degrees(math.atan2(z, math.sqrt(x**2 + y**2)))
    return range, azimuth, elevation

# Read data from CSV file
filename = "object_data.csv"
data = []
true_labels = []
with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        obj_name = row[0]
        range = float(row[2])
        azimuth = float(row[3])
        elevation = float(row[4])
        data.append([range, azimuth, elevation])
        true_labels.append(obj_name)

# Perform DBSCAN clustering
epsilon = 1.0  # Maximum distance between two samples to be considered in the same neighborhood
min_samples = 3  # Minimum number of samples in a neighborhood to form a cluster
dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
dbscan_clusters = dbscan.fit_predict(data)

# Perform Mean Shift clustering
bandwidth = 2.0  # Bandwidth parameter for Mean Shift
mean_shift = MeanShift(bandwidth=bandwidth)
mean_shift_clusters = mean_shift.fit_predict(data)

# Calculate accuracies
dbscan_accuracy = accuracy_score(true_labels, dbscan_clusters)
mean_shift_accuracy = accuracy_score(true_labels, mean_shift_clusters)

print(f"DBSCAN Accuracy: {dbscan_accuracy:.4f}")
print(f"Mean Shift Accuracy: {mean_shift_accuracy:.4f}")
