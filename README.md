# Hospital management system (HMS)
This project is a comprehensive application for managing a hospital. It includes various functionalities for managing patient and doctor information, scheduling shifts, booking appointments, and tracking payment statuses.
# Features
### 1. Patient Information Management
<img width="960" height="540" src="https://raw.githubusercontent.com/Farbod0o/Hospital-Management-System/main/Screenshots/Patient%20Registration.png">


* **Register Patient Information:** 
Allows registering new patient details including name, age, gender, contact number, and medical information.
* **Update Patient Information:** Capability to edit and update existing patient details.
* **Search and Display Patient Information:**
Search patients by name, hospital number, or other attributes and display their information.
### 2. Doctor Information Management
<img width="960" height="540" src="https://raw.githubusercontent.com/Farbod0o/Hospital-Management-System/main/Screenshots/Search%20for%20doctors.png">

* **Register Doctor Information:** Allows registering new doctor details including name, specialty, contact number, and medical license number.
* **Update Doctor Information:** Capability to edit and update existing doctor details.
* **Search and Display Doctor Information:** Search doctors by name, specialty, or other attributes and display their information.
### 3. Shift Scheduling for Doctors
<img width="960" height="540" src="https://raw.githubusercontent.com/Farbod0o/Hospital-Management-System/main/Screenshots/list%20of%20shifts.png">

* **Define Shifts:** Ability to define work shifts for doctors based on days of the week and working hours.
* **Display Shift Schedules:** Display each doctor's shift schedule for better planning and management.
### 4. Appointment Booking for Patients
<img width="960" height="540" src="https://github.com/Farbod0o/Hospital-Management-System/blob/main/Screenshots/Book%20Appointments.png?raw=true">

* **Book Appointments:** Patients can book appointments based on the available shifts of doctors.
* **Track Appointments:** Capability for patients to track and view their booked appointments.
### 5. Payment Tracking
* **Record Payments:** Record and manage payments made by patients.
* **Track Payment Status:** Display the status of payments and track unpaid amounts.

## Installation
### 1. Clone the repository and install dependencies:

```bash
git clone github.com/Farbod0o/Hospital-Management-System
cd HMS
pip install -r requirements.txt
```
### 2. Configure the Database and Initial Settings:
* Edit the *'da.py'* file to configure the database settings and other configurations.

### 3.Run the Application:
```
 python app.py 
```

## Usage
* **User Interface:** Patients and doctors and admins can interact with the system through a user-friendly interface to manage their respective information and tasks.
## Contributing

We welcome contributions to enhance this project. To contribute, please follow these steps:

* Fork the repository.
* Create a new branch with your changes.
* Commit your changes and push to the branch.
* Open a Pull Request.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the `LICENSE` file for more details.
