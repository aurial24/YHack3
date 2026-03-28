# Setting up and Running the Frontend (React Native Expo)

## 1. Install dependencies

   ```bash
   npm install
   ```

## 2. Start the app

   ```bash
   npx expo start
   ```

In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

You can start developing by editing the files inside the **app** directory. This project uses [file-based routing](https://docs.expo.dev/router/introduction).



# Setting up the Backend (FASTAPI)

## 1. Go into the backend folder

   ```bash
   cd backend
   ```

## 2. Create a Python virtual environment (keeps your packages isolated)

   ```bash
   python -m venv venv
   ```

## 3. Activate the virtual environment
### On Mac/Linux:

   ```bash
   source venv/bin/activate
   ```
### On Windows (Command Prompt):

   ```bash
   venv\Scripts\activate
   ```

## 4. Install FastAPI and Uvicorn (the server that runs FastAPI)

   ```bash
   pip install fastapi uvicorn
   ```

# Running the Backend

   ```bash
   uvicorn main:app --reload
   ```