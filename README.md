# **Interview Scheduling API**

This project is a Django-based API that allows candidates and interviewers to register their availability and enables HR managers to fetch schedulable interview slots based on their availability.

---

## **Setup Instructions**


### **Steps to Run Locally**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iamarjunc/Interview-Scheduling-API
   cd Interview-Scheduling-API 
2. **Create and activate a virtual environment**:

3. **Install dependencies**:
    ```bash
   pip install -r requirements.txt
4. **Run migrations:**
    ```bash
   python manage.py makemigrations 
   python manage.py migrate
5. **Start the development server:**
    ```bash
   python manage.py runserver
6. **Access the API:**<br>
   Base URL :  [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## **Endpoints**

### 1. Register a User

#### a) Register a Candidate
- **URL**: `/api/users/`
- **Method**: `POST`
- **Payload**:  
   ```json
   {
     "name": "Arjun C",
     "role": "candidate"
   }
#### b) Register an Interviewer
- **URL**: `/api/users/`
- **Method**: `POST`
- **Payload**:  
   ```json
   {
     "name": "John Doe",
     "role": "interviewer"
   }
### 2. Register Availability

- #### a) Set Availability for a Candidate
    - **URL**: `/api/availability/`
    - **Method**: `POST`
    - **Payload**:  
         ```json
        {
            "user": 1,
            "date": "2024-11-24",
            "start_time": "10:00:00",
            "end_time": "14:00:00"
        }
    - **Response**:
         ```json
        {
            "message": "Availability registered successfully!"
        }
- #### b) Set Availability for an Interviewer
    - **URL**: `/api/availability/`
    - **Method**: `POST`
    - **Payload**:  
        ```json
        {
            "user": 2,
            "date": "2024-11-24",
            "start_time": "11:00:00",
            "end_time": "12:00:00"
        }
    - **Response**:
         ```json
        {
            "message": "Availability registered successfully!"
        }
### 3. Get Schedulable Slots
- **URL**: `/api/schedule/`
- **Method**: `GET`
- **Query Parameters**:
    - `candidate_id`: Candidate's user ID
    - `interviewer_id`: Interviewer's user ID
- **Example** - http://127.0.0.1:8000/api/schedule/?candidate_id=1&interviewer_id=2
- **Response**:
    ```json
    {        
        "slots": [
            ["10:00", "11:00"],
            ["11:00", "12:00"]
        ]
    }


## **Suggestions**
   - **User Authentication & Authorization**: Implementing authentication (using JWT) to ensure that only authorized users can access the scheduling system. HR managers could have admin rights to view and create schedules, while candidates and interviewers would have restricted access to only their own schedules.
   - **Calendar Integration**: Integrating with external calendar services (like Google Calendar or Outlook) to allow users to automatically sync their availability and schedule interviews directly from the platform. This would also help avoid overbooking and ensure that interviewers and candidates are notified of upcoming interviews.
   - **Advanced Slot Filtering**: Allowing HR managers to filter available slots based on specific criteria like preferred times, meeting duration, or urgency, could help in quick scheduling. Implementing more advanced search options could speed up the process of finding available slots.
