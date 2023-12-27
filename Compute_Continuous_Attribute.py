# II. Compute Gini Index of Continuous Attribute.
# 1) Compute Gini Index using the given split values: 55, 65, 72, 80, 87, 92, 97, 100, 122, 172,230
# 2) Which threshold value provides the best split?

import numpy as np

# Given split values
split_values = [55, 65, 72, 80, 87, 92, 97, 100, 122, 172, 230]
classes = ['C0', 'C1']  # Assuming two classes

# Calculate Gini Index for each split
best_gini_index = float('inf')
best_threshold = None

for threshold in split_values:
    left_class_counts = [0, 0]  # Class counts for the left subset
    right_class_counts = [0, 0]  # Class counts for the right subset
    left_total = 0
    right_total = 0

    # Count the occurrences of each class in the left and right subsets
    for value in split_values:
        if value <= threshold:
            index = 0
        else:
            index = 1
        for class_index, class_label in enumerate(classes):
            if class_label == 'C0':
                left_class_counts[class_index] += 1
                left_total += 1
            else:
                right_class_counts[class_index] += 1
                right_total += 1

    # Calculate Gini Index for the split
    left_gini = 1 - np.sum((np.array(left_class_counts) / left_total) ** 2)
    right_gini = 1 - np.sum((np.array(right_class_counts) / right_total) ** 2)
    total_gini = (left_total / len(split_values)) * left_gini + (right_total / len(split_values)) * right_gini

    # Update the best threshold if a lower Gini Index is found
    if total_gini < best_gini_index:
        best_gini_index = total_gini
        best_threshold = threshold

# Print the Gini Index for each split and the best threshold
print("Gini Index for each split:")
for index, threshold in enumerate(split_values):
    print(f"Threshold: {threshold} - Gini Index: {best_gini_index}")

print("\nBest Threshold:", best_threshold)