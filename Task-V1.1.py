import time
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Global variable to control program exit
exitFlag = [False]

# Function to handle keypress events
def on_key(event):
    if event.key == 'q' or event.key == 'Q':
        exitFlag[0] = True
        print("Exiting program...")
        

# Function for simulating the data stream
def dataStreamSimulation():
    print("Data Stream Simulation started...\nPlease wait...")
    while not exitFlag[0]:
        # Seasonal data with noise using sin function
        seasonal_component = np.sin(np.linspace(0, 2 * np.pi, 100))
        noise = np.random.normal(0, 0.2, 100)
        data_stream = seasonal_component + noise

        # Looping through the data stream
        for value in data_stream:
            if exitFlag[0]:
                break
            yield value
            time.sleep(0.22)  # Simulate real-time stream delay

# Function for visualizing the data stream and printing anomalies in CLI
def detect(data_stream, window_size=50, padding=0.1):
    fig, ax = plt.subplots()  # Create a plot figure
    x_data, y_data = [], []  # Initialize the x and y data lists
    buffer = []  # Initialize the buffer list

    # Initialize the IsolationForest model
    model = IsolationForest(contamination=0.02)

    # Initialize axis limits
    min_y, max_y = float('inf'), float('-inf')

    # Set up the keypress event handler
    fig.canvas.mpl_connect('key_press_event', on_key)

    # Function to update the graph with new data and anomalies
    def update_graph():
        ax.clear()
        ax.plot(x_data, y_data, label='Data Stream', color='blue')

        # Plot anomalies
        anomalies = model.predict(buffer)
        anomaly_indices = [i for i, anomaly in enumerate(anomalies) if anomaly == -1]

        # Plot anomalies in red
        for i, (x, y, anomaly) in enumerate(zip(x_data, y_data, anomalies)):
            if anomaly == -1:
                ax.scatter(x, y, color='red', label='Anomaly' if i == 0 else "", zorder=5)

        # Add some padding to the y-axis limits
        y_padding = (max_y - min_y) * padding
        ax.set_ylim(min_y - y_padding, max_y + y_padding)


        # Adding a note to press Q to quit and stop the program 
        ax.text(0.5, 1.05, "Press 'Q' to quit", transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='center', color='black')

        ax.legend()
        plt.pause(0.01)

        # Print anomaly details to the console
        if anomaly_indices:
            print(f"Anomalies detected at indices: {anomaly_indices}")
            for idx in anomaly_indices:
                print(f"Time: {x_data[idx]}, Value: {y_data[idx]:.4}")

    # looping through the data stream
    for idx, data_point in enumerate(data_stream):
        if exitFlag[0]:
            break

        # adding new data to the buffer
        x_data.append(idx)
        y_data.append(data_point)
        buffer.append([data_point])

        # Update axis limits
        min_y = min(min_y, data_point)
        max_y = max(max_y, data_point)

        # limit the size of x_data and y_data to the window size
        if len(x_data) > window_size:
            x_data.pop(0)
            y_data.pop(0)

        if len(buffer) >= window_size:
            # Fit the model on the buffer and predict anomalies
            model.fit(buffer)
            buffer = buffer[-window_size:]  # Keep only the latest window_size data

            # Update the graph with new data and anomalies
            update_graph()

# Define variable stream to be the data stream and call the detect function
stream = dataStreamSimulation()
detect(stream)
