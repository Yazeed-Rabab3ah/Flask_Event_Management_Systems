# Event Management System

## Overview
This is a simple **Event Management System** built with **Flask**, **SQLAlchemy**, **HTML**, **CSS**, and **JavaScript**. The system allows users to **create**, **read**, **update**, and **delete** event information. It features a clean interface for managing events, including event titles, descriptions, and locations.

---

## Features
- **Create Event**: Add new events with title, description, and location.
- **Read Event**: View the details of all events.
- **Update Event**: Edit event information.
- **Delete Event**: Remove an event from the system.
- **Responsive UI**: The frontend is styled using HTML and CSS for a simple and clean design.
- **User Confirmation**: Delete events with a confirmation prompt for better user experience.

---

## Technologies Used
- **Flask**: Web framework used to build the backend.
- **SQLAlchemy**: ORM (Object Relational Mapper) for interacting with the database.
- **HTML/CSS**: Markup and styling for the frontend.
- **JavaScript**: For interactive components like confirmation before deleting events.

---

## Installation

### Prerequisites
Ensure you have **Python 3.x** installed. You will also need **pip** to install the required dependencies.

### Step-by-Step Installation

1. **Clone the Repository**  
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/event-management-system.git
   ```

2. **Create a Virtual Environment**  
   Navigate to the project directory and create a virtual environment:
   ```bash
   cd event-management-system
   python -m venv venv
   ```

3. **Activate the Virtual Environment**  
   For Windows:
   ```bash
   venv\Scripts\activate
   ```
   For macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install Dependencies**  
   Install the required Python dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**  
   After the dependencies are installed, run the Flask app:
   ```bash
   flask run
   ```

   The app should now be running at `http://127.0.0.1:5000/`.

---
  
### Managing Events
- **Create Event**: Go to the "Create Event" page to add a new event with details like title, description, and location.
- **View Events**: The homepage will list all events with options to view, edit, or delete them.
- **Update Event**: Edit event details by selecting the event and modifying its information.
- **Delete Event**: Remove an event by clicking the delete button and confirming the action.

---
