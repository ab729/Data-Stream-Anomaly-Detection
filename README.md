# Efficient Data Stream Anomaly Detection

## 1. Introduction

### 1.1 Purpose
The purpose of this repository is to provide a detailed overview of the approach developed for Efficient Data Stream Anomaly Detection. This document covers the objectives, design, implementation, testing, and deployment processes associated with the software.

### 1.2 Scope
This report covers the following aspects:
- Description of the software/system
- Design and architecture
- Implementation details
- Testing methodologies

### 1.3 Audience
This document is intended for the ******* **** ****** Team.

## 2. Scripts Overview

### 2.1 Scripts Description
The Python code uses three main libraries:
1. **Matplotlib**: For visualizing the process.
2. **NumPy & Pandas**: For data analysis and dealing with datasets.
3. **Scikit-learn**: For implementing ML algorithms.

### 2.2 Objectives
Simulating real-time sequences of floating-point numbers could represent various metrics such as financial transactions or system metrics.

## 3. Design and Architecture

### 3.1 Script Architecture
The solution was designed to approach anomaly detection through testing two main algorithms:
- **Statistical Approach**: Using the Moving Average algorithm that relies on the mean and standard deviation of the data stream. Given the data's susceptibility to drift and seasonal variations, the implementation was adjusted accordingly.
- **Machine Learning Approach**: Using the IsolationForest algorithm, training the Isolation Forest model on a portion of the normal data stream. As new data comes in, the model flags points that seem anomalous.

### 3.2 Design Considerations
The statistical approach struggles with concept drift and seasonal variations. Decomposing the time series into seasonal and trend components is essential for obtaining more efficient results.

### 3.3 Component Design
The script consists of two main functions:
- `dataStreamSimulation()`: Generates seasonal data with noise using NumPy’s `sin` method.
- `detect()`: Detects and visualizes anomalies in the data stream.

## 4. Implementation

### 4.1 Development Environment
- **Programming Language**: Python 3.12.0
- **Frameworks and Libraries**:
  - **scikit-learn**: Used for the IsolationForest algorithm, a key part of the anomaly detection mechanism.
  - **NumPy**: For generating synthetic data streams and numerical operations.
  - **matplotlib**: To visualize the data streams and detected anomalies.
  - **Pandas**: For structuring and handling datasets more effectively.
- **Tools**:
  - **Code Editor**: Visual Studio Code, chosen for its rich ecosystem of extensions for Python development and lightweight workflow.
  - **Version Control**: Git, to manage changes.
  - **Virtual Environment**: `venv` for isolating the project dependencies from other Python environments.

### 4.2 Integration
- **Modular Approach**: Each component of the system (data stream, detection, and visualization) is developed as a standalone module. This approach allows for easy debugging and maintenance.
- **Real-time Processing**: The system processes data as it is received, leveraging Python’s generator functions for the stream and efficient updating with Matplotlib.

## 5. Testing

### 5.1 Testing Strategy
The testing strategy involved applying the script to an external CSV dataset containing 500 financial transactions to finalize the approach selection.

### 5.2 Test Cases and Results
The test results for both algorithms are recorded and detailed below.

## 6. Conclusion

### 6.1 Summary
Given the test results, the Statistical Approach provides acceptable results for high deviation values but fails with medium and lower values. Despite being faster and consuming fewer computational resources, the Machine Learning approach using the IsolationForest algorithm was chosen for its more accurate and efficient results. After validation and testing contamination parameter was set to 2% or 0.02

---

