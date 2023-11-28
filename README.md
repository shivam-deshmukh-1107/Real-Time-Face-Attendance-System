# Real-Time Face Attendance System

## Introduction

The Real-Time Face Attendance System is a computer vision project that leverages facial recognition technology to automate attendance tracking. The system integrates with a real-time database, providing instant updates on students' attendance records. This project includes webcam integration, face recognition, a graphical interface, encoding generation, and seamless interaction with Firebase for real-time data storage.

## Features

- **Real-time Face Recognition:** Utilizes the OpenCV and face_recognition libraries to perform real-time face recognition through a webcam.
- **Graphical Interface:** Provides a user-friendly graphical interface to display system status, attendance information, and detected faces.
- **Encoding Generation:** Generates facial encodings for known students and stores them, facilitating efficient face recognition.
- **Firebase Integration:** Connects seamlessly with Firebase Realtime Database for storing and updating student data and attendance records.
- **Attendance Limitation:** Implements a 30-second delay between consecutive attendance markings to prevent rapid entries.
- **Image Storage:** Stores student images in a Firebase storage bucket, linked to respective student IDs.

## Getting Started

### Prerequisites

- Python 3.6 or later
- OpenCV
- Face Recognition
- cv zone
- Firebase Admin SDK

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/real-time-face-attendance-system.git
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Obtain Firebase credentials (serviceAccountKey.json) and update the configuration in main.py and database_input.py.

### Usage

1. Run the main script:
    ```bash
   python main.py
    ```
2. Follow the on-screen instructions to mark attendance.

### Project Structure


- `main.py`: Main script for webcam integration, face recognition, and real-time database interaction.
- `database_input.py`: Script to initialize and add sample data to the Firebase Realtime Database.
- `encode_generator.py`: Script to generate facial encodings and store them.

### Contributing
Contributions are welcome! Feel free to open issues or pull requests for any improvements or bug fixes.
