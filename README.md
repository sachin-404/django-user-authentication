# User Authentication

This repository houses the code for a powerful user authentication app built on the Django web framework. The primary purpose of this application is to provide a secure and seamless login experience for users, enabling them to access restricted areas of any website or application. This app offers a simple and intuitive user registration process. New users can quickly create an account by providing their desired username and password. Upon successful registration, their information is securely stored in the database for future login verification. With the robust features and user-friendly interface, this authentication app can be easily integrate into any Django project.

## Run Locally

### A. Running Using Docker Image
Running the containerized application is incredibly easy. With just two commands, you can pull the Docker image and run the container without worrying about any missing dependencies (no more "it works on my machine" moments!).

To run the app using the Docker image, ensure Docker is installed on your device. If Docker is not installed, please refer to the official Docker documentation for the installation process.

1. Open the terminal on your device and pull the Docker image using the following command:
```
docker pull sachin404/django-authentication
```

2. Run the following command to start the container:
```
docker run sachin404/django-authentication
```
3. Open your browser and visit `http://127.0.0.1:8000/` to access the app's homepage.

### B. Running Using the GitHub Repository

To run the app directly from the GitHub repository, follow these steps:

1. Open the terminal on your device and clone the repository using the following command:
```
git clone https://github.com/sachin-404/django-user-authentication.git
```
2. Open the project in your preferred IDE (such as VS Code) and set up a virtual environment by running the following command:
```
python3 -m venv venv
```
> **Note** : If you are using Windows, replace `python3` with `python`."

3. Activate the virtual environment

- For Linux/Mac:
```
source venv/bin/activate
```

- For Windows:
```
venv/Scripts/activate
```
4. Install all the dependencies by running the following command:
```
pip3 install -r requirements.txt
```

5. Perform migrations by running the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
6. Finally, run the following command to start the server:
```
python3 manage.py runserver
```
7. Open your browser and visit `http://127.0.0.1:8000/` to access the app's homepage.

![Homepage](https://github.com/sachin-404/django-user-authentication/assets/96824004/eec1ed70-d6df-4d3f-8009-ac2ab34c02d2)

## Feedback
Feedbacks are always welcome! If you encounter any issues or have suggestions for enhancing the app, please drop me message on [Twitter](https://twitter.com/sachin_404).
