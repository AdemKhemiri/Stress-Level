import json
import matplotlib.pyplot as plt

# Load data from JSON file
with open('output/stress_data.json', 'r') as json_file:
    data = json.load(json_file)

# Extract relevant data for plotting (modify this based on your JSON structure)
blink_stress = [entry['blink_stress'] for entry in data['frames']]
eyebrow_stress = [entry['eyebrow_stress'] for entry in data['frames']]
lip_stress = [entry['lip_stress'] for entry in data['frames']]
final_stress = [entry['final_stress'] for entry in data['frames']]

# Plotting without explicit frame numbers
plt.figure(figsize=(10, 6))

plt.plot(blink_stress, label='Blink Stress Level', linestyle='-')
plt.plot(eyebrow_stress, label='Eyebrows Stress Level', linestyle='-')
plt.plot(lip_stress, label='lip Stress Level', linestyle='-')
plt.plot(final_stress, label='final Stress Level', linestyle='-')

plt.xlabel('Frame Index')
plt.ylabel('Stress Level')
plt.title('Stress Analysis Over Time')
plt.legend()
plt.grid(True)
plt.show()
