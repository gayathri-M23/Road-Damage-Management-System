# Road Damage Management System

## Project Overview

The Road Damage Management System is a smart platform designed to help citizens report road damages such as potholes, cracks, and damaged road surfaces. The system allows users to submit complaints with location details and images of the damaged roads. Authorities can monitor reported issues, assign repair tasks, track maintenance progress, and update the status of repairs. This system improves road safety and ensures timely maintenance of road infrastructure.

## Problem Statement

Road damages such as potholes, cracks, and surface deterioration are major causes of accidents, traffic congestion, and vehicle damage. Traditional reporting methods are often slow, manual, and lack proper tracking mechanisms, leading to delays in road repairs. There is a need for an efficient digital system that enables citizens to report road damages quickly and helps authorities manage repair activities effectively.

## Objectives

* Provide an easy platform for reporting road damages.
* Maintain a centralized database of road damage reports.
* Enable authorities to monitor and manage repair activities.
* Reduce delays in road maintenance and repairs.
* Improve road safety for drivers and pedestrians.
* Track and monitor the status of reported issues.

## Scope of the Project

* User registration and login.
* Road damage reporting with images.
* Location-based complaint submission.
* Complaint verification and management.
* Repair task assignment and tracking.
* Status updates and notifications.
* Report generation for maintenance activities.

## Module List

### 1. User Authentication Module

* User Registration
* Login and Logout
* Profile Management

### 2. Road Damage Reporting Module

* Report Road Damage
* Upload Damage Images
* Enter Location Details
* Submit Complaints

### 3. Complaint Management Module

* View Submitted Complaints
* Verify Damage Reports
* Assign Priority Levels

### 4. Repair Management Module

* Assign Repair Teams
* Update Repair Status
* Monitor Maintenance Progress

### 5. Tracking and Notification Module

* Track Complaint Status
* Receive Status Updates
* View Repair Progress

### 6. Admin Module

* Manage Users
* Manage Complaints
* Generate Reports
* Monitor System Activities

## Technology Stack

### Front End

* HTML
* CSS
* JavaScript
* Bootstrap

### Back End

* Python
* Flask

### Database

* SQLite / MySQL

## Database Table List

### Users

| Field Name   | Type         |
| ------------ | ------------ |
| user_id      | INT (PK)     |
| name         | VARCHAR(100) |
| email        | VARCHAR(100) |
| password     | VARCHAR(100) |
| phone_number | VARCHAR(15)  |

### Road_Damage_Reports

| Field Name  | Type         |
| ----------- | ------------ |
| report_id   | INT (PK)     |
| user_id     | INT (FK)     |
| location    | VARCHAR(255) |
| damage_type | VARCHAR(100) |
| description | TEXT         |
| image_path  | VARCHAR(255) |
| report_date | DATE         |
| status      | VARCHAR(50)  |

### Repair_Details

| Field Name      | Type         |
| --------------- | ------------ |
| repair_id       | INT (PK)     |
| report_id       | INT (FK)     |
| assigned_team   | VARCHAR(100) |
| start_date      | DATE         |
| completion_date | DATE         |
| repair_status   | VARCHAR(50)  |

### Notifications

| Field Name        | Type     |
| ----------------- | -------- |
| notification_id   | INT (PK) |
| user_id           | INT (FK) |
| message           | TEXT     |
| notification_date | DATE     |

### Admin

| Field Name | Type         |
| ---------- | ------------ |
| admin_id   | INT (PK)     |
| admin_name | VARCHAR(100) |
| email      | VARCHAR(100) |
| password   | VARCHAR(100) |

## Expected Outcome

The system will provide a faster and more efficient way to report and manage road damages. It will improve communication between citizens and authorities, reduce repair delays, and contribute to safer roads and better transportation infrastructure.

## Future Enhancements

* AI-based pothole detection using image processing.
* GPS-enabled automatic location detection.
* Mobile application support.
* Real-time notifications and alerts.
* Smart City integration.
* Analytics dashboard for road maintenance planning.

## Author

**Gayathri**

First Year Student project
