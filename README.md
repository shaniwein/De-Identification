# De-Identification

This is a simple api that receives a patient's record and returns it de-identified.
Developed in Python2.7 in a Linux environment.

**Running the API:**
1. Edit the environment vars in the setup.sh script with the relevant paths (if running on Linux, you can leave the defaults).
2. Run the setup.sh script from inside the project directory (if running on Windows, manually execute the relevant steps in the scripts).
3. After the setup, the api should start running automatically.

**How To Use It?**
Once the API is running, send a request to http://127.0.0.1:5000/de_identify with the parameter _record=patient record json_
