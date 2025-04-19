# Project Motion CHP

## Overview
This project is a user behavior tracking application that captures mouse movements, key presses, and user details. It calculates cursor speed and typing speed to determine if the user is a human or a robot. The data is saved in multiple formats (CSV, Excel, JSON) and a comparison report is generated.

## Features
- Tracks mouse movements and key presses.
- Calculates cursor speed and typing speed.
- Saves user data and behavior data in CSV, Excel, and JSON formats.
- Generates a comparison report.
- Provides a GUI for user input using Tkinter.

## New Features (Updated April 19, 2025)

- **Session Tracking**: Added functionality to track the duration of user sessions.
- **Enhanced Behavior Metrics**: Improved calculation of cursor speed and typing speed, and added metrics like mouse clicks and key presses.
- **Export for Machine Learning**: Users can now export behavior data as a dataset (`ml_behavior_dataset.csv`) for machine learning purposes.
- **Improved Data Saving**: Enhanced data saving to include history and ensure unique user IDs.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required Python packages:
   ```bash
   pip install pandas
   ```

## Setting Up a Virtual Environment

To ensure a clean and isolated environment for the project, it is recommended to use a virtual environment.

1. Navigate to the project directory:
   ```bash
   cd path/to/project-motion-chp
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the `main.py` file:
   ```bash
   python main.py
   ```
2. Fill in the user details in the GUI and click "Save User" to save individual user data.
3. Click "Save All Data" to save all user and behavior data and generate a comparison report.

### Updated Usage

1. **Session Tracking**:
   - The application now tracks session duration automatically.
   - Session duration is included in the behavior data.

2. **Export Dataset**:
   - Use the "Export Dataset" button in the GUI to save behavior data for machine learning.
   - The dataset is saved as `ml_behavior_dataset.csv`.

3. **Enhanced Data Saving**:
   - User and behavior data are saved with unique IDs.
   - History is appended to existing files without overwriting.

## How the Code Works

1. **Mouse and Keyboard Tracking**:
   - The application tracks mouse movements and key presses using event bindings in the Tkinter GUI.
   - Mouse movements are stored with their coordinates and timestamps.
   - Key presses are recorded with their timestamps.

2. **Behavior Analysis**:
   - Cursor speed is calculated based on the distance and time between consecutive mouse movements.
   - Typing speed is calculated based on the number of key presses and the total time taken.
   - A heuristic determines if the user is a human or a robot based on these metrics.

3. **Data Saving**:
   - User details and behavior data are saved in CSV, Excel, and JSON formats.
   - A comparison report is generated summarizing the behavior analysis.

4. **GUI**:
   - The application provides a user-friendly interface for entering user details and saving data.

## Running the Application

1. Ensure the virtual environment is activated.
2. Run the `main.py` file:
   ```bash
   python main.py
   ```
3. Interact with the GUI to input user details and save data.
4. Use the "Save All Data" button to save all collected data and generate the comparison report.

## Output Files
- `user_data.csv`, `user_data.xlsx`, `user_data.json`: Contain user details.
- `behavior_data.csv`, `behavior_data.xlsx`, `behavior_data.json`: Contain behavior data.
- `comparison_report.txt`: Contains a summary of user behavior analysis.
- `ml_behavior_dataset.csv`: Contains behavior data formatted for machine learning.

## Logging
Logs are saved in the console to track application events and errors.