import random

# Define tolerance ranges for quality control
TOLERANCES = {
    "length": (9.8, 10.2),   # in cm
    "width": (4.8, 5.2),     # in cm
    "weight": (95, 105)      # in grams
}

# Simulate item measurements
def generate_item(id):
    return {
        "id": id,
        "length": round(random.uniform(9.5, 10.5), 2),
        "width": round(random.uniform(4.5, 5.5), 2),
        "weight": round(random.uniform(90, 110), 2)
    }

# Quality control function
def check_item_quality(item):
    results = {}
    for key, (min_val, max_val) in TOLERANCES.items():
        value = item[key]
        results[key] = min_val <= value <= max_val
    return results

# Run quality control check on a batch of items
def run_quality_control(batch_size=10):
    passed = 0
    for i in range(batch_size):
        item = generate_item(i + 1)
        qc_results = check_item_quality(item)
        if all(qc_results.values()):
            passed += 1
            status = "PASSED"
        else:
            status = "FAILED"
        print(f"Item {item['id']}: {status} - {item}, QC: {qc_results}")
    print(f"\nTotal Passed: {passed}/{batch_size}")

# Run the example
run_quality_control(10)
