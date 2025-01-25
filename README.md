# Second Write Coding Assessment: Binary Code Parser
## Backend
cd into the backend repo
```
cd backend
```
### 1. Create .venv
Run the following commands to create and activate your virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
### 2. Install requirements
```
python3 -m pip install -r requirements.txt
```

### 3. Run the backend
```
cd app
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

## Frontend
cd into the frontend repo from the home directory `secondwrite`
```
cd frontend
```
### 1. Install dependencies
```
npm install
```
### 2. Run the frontend
```
npm run dev
```

## Pytest
Two simple tests for each endpoint (upload and download) are tested to ensure 200 response codes.
```
pytest backend/app/tests/tests.py
```

## Accessing the webpage
Your app should now be running on `localhost:3000`

The first screen allows you to upload binary files (.bin), which get parsed and uploaded to a sqlite database in the backend.
<img width="1470" alt="Screenshot 2025-01-24 at 10 37 47 PM" src="https://github.com/user-attachments/assets/f5bc97d5-72a4-46d2-a20b-d94d6f008eab" />

The second screen allows you to review the output by downloading the table from the backend into a json format, which gets displayed on the frontend and allows the user to download as a .json file.
<img width="1469" alt="Screenshot 2025-01-24 at 10 38 00 PM" src="https://github.com/user-attachments/assets/83633339-8420-4c6b-b774-eb956aa3e178" />

