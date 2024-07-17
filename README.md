# replicator-quiz-demo

1. Environment Setup:
   - Install the latest version of Android Studio from the official website.
   - Ensure you have the Java Development Kit (JDK) installed on your system.

2. Clone the Repository:
   ```
   git clone https://github.com/your-username/quiz-app-couchbase-lite.git
   cd quiz-app-couchbase-lite
   ```

3. Open the Project:
   - Launch Android Studio.
   - Select "Open an Existing Project" and navigate to the cloned repository.

4. Configure Gradle:
   - Once the project is opened, Android Studio will automatically sync the Gradle files.
   - If prompted, update to the latest Gradle version.

5. Check Dependencies:
   - Open the `app/build.gradle` file.
   - Ensure the following dependencies are included:
     ```gradle
     dependencies {
         implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
         implementation "androidx.core:core-ktx:$core_ktx_version"
         implementation "androidx.appcompat:appcompat:$appcompat_version"
         implementation "com.couchbase.lite:couchbase-lite-android:$couchbase_lite_version"
         // Add other necessary dependencies
     }
     ```

6. Set Up Couchbase Lite:
   - In the `DatabaseManager.kt` file, ensure the database initialization is correct.
   - Check that the database name and collection names are properly set.
   - Ensure you setup App Services setup in Capella. After getting the connection string and the user created in App Services fill out the following in `DatabaseManager.kt` file:
    - In line 114
     ```
         url = URI(
            "urlAddress" \\ Add the connection string URL Address here 
        )
     ```
    - In line 133
      ```
         config.setAuthenticator(BasicAuthenticator("username", "password".toCharArray())) // Replace the username and password with the user details you havr created
      ```

7. Prepare the Questions:
   - Verify that the `questions.json` file in the `assets` folder contains the quiz questions.
   - Make sure the JSON structure matches the expected format in the app.

8. Configure the Android Emulator:
   - In Android Studio, go to Tools > AVD Manager.
   - Create a new virtual device or use an existing one (preferably with API level 29 or higher).

9. Build the Project:
   - Click on Build > Make Project to compile the code.
   - Resolve any build errors that may occur.

10. Run the Application:
    - Before running the Android application, run the Python server separately.
    - Open another terminal window, and navigate to the python-server directory
    ```
    cd python-server
    ```
    - The requirements.txt file in the python-server directory lists the necessary dependencies. Install them using pip:
    ```
    pip install -r requirements.txt
    ```
    - The ```app.py``` file has the logic for the AlexNet model to generate embeddings for an image passed by the Kotlin app. Now run the app. 
    ```
    python app.py
    ```
    - Now let's head back to our Android app
    - Select the emulator or connect a physical Android device.
    - Click on the "Run" button (green play icon) in Android Studio.
    - Wait for the app to install and launch on the device.

12. Using the App:
    - When the app launches, you'll see the main screen.
    - Enter your username when prompted.
    - The app will likely ask for camera permissions for image recognition.
    - Take a photo or select an image to determine the quiz category.
    - Answer the quiz questions as they appear.
    - After completing the quiz, view your score and check the leaderboard.

13. Debugging:
    - If you encounter any issues, check the Logcat in Android Studio for error messages.
    - Pay attention to any Couchbase-related logs for database operations.

14. Testing Synchronization (if implemented):
    - If the app includes synchronization features, ensure you have the Capella App Services properly setup.
    - Configure the replication URL in the app's settings or `DatabaseManager.kt`.
    - Test synchronization by running the app on multiple devices or emulators.

15. Customization:
    - To modify questions, edit the `questions.json` file.
    - To change the UI, look for XML layout files in the `res/layout` directory.
    - To adjust app behavior, modify the Kotlin files in the `app/src/main/java/com/example/quizappbycouchbase/` directory.

Remember to handle any required permissions, such as internet access or file system access, in the `AndroidManifest.xml` file. Also, ensure that you're complying with any licensing requirements for Couchbase Lite and other libraries used in the project.
