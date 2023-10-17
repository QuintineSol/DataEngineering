# Health Insurance Cost Prediction

This project aims to predict health insurance costs using a machine learning model trained on a dataset that includes various factors such as age, sex, BMI, number of children, smoking habits, and region. The project also includes a web application that provides a user-friendly interface to make predictions based on the trained model.

## Introduction

The main objective of this project is to leverage the power of machine learning to accurately predict health insurance costs. By training a machine learning model on a dataset that contains relevant features, we can estimate insurance costs based on individual attributes. The model takes into account factors such as age, sex, BMI, number of children, smoking habits, and region to generate accurate predictions.

To make the prediction process accessible to users, we have developed a web application. The application provides a simple and intuitive interface where users can input their information and obtain an estimated insurance cost. The underlying machine learning model handles the prediction calculations, ensuring reliable results.

## How to Use

To use the Health Insurance Cost Prediction web application, follow these steps:

1. Visit the web application by clicking on the following link: [Health Insurance Cost Prediction](https://healthinsurancepred.streamlit.app/).

2. Once on the web application, you will see a user interface where you can enter the necessary information for the prediction.

3. Fill in the required fields:
   - **Age:** Slide the bar to select your age.
   - **Sex:** Choose your gender from the dropdown menu.
   - **BMI Value:** Enter your Body Mass Index (BMI) value.
   - **Number of Children:** Slide the bar to select the number of children you have.
   - **Smoker:** Select "Yes" if you are a smoker; otherwise, select "No."
   - **Region:** Choose your region from the dropdown menu.

4. After entering the information, click on the "Predict" button.

5. The application will process your input and display the predicted insurance amount based on the provided data.

Through the web application, users can conveniently obtain estimated health insurance costs by leveraging the power of machine learning.

## Dataset and Model

The web application utilizes a machine learning model that has been trained on the "insurance.csv" dataset. This dataset, located in the "dataset" folder of this repository, contains information about individuals' health insurance costs. By analyzing the patterns and relationships in the dataset, the machine learning model can make accurate predictions based on new input data.

The trained machine learning model is stored in the "insurance_pred" file, located in the "ML Model" folder. This model has been specifically developed and trained to handle health insurance cost prediction based on the provided dataset.

## Repository Structure

This repository has the following structure:

```
├── App
│   └── app.py
├── dataset
│   └── insurance.csv
├── ML Model
│   └── insurance_pred
├── README.md
└── requirements.txt
```

- `App/app.py`: The main script that runs the web application.
- `dataset/insurance.csv`: The dataset used for training the machine learning model.
- `ML Model/insurance_pred`: The trained machine learning model.
- `README.md`: The file you are currently reading.
- `requirements.txt`: The list of dependencies required to run the web application.

Feel free to explore the code and modify it according to your needs. If you encounter any issues or have suggestions for improvement, please create an issue on the repository.

## Prerequisites

To run this web application locally, you need to have the following dependencies installed:

- joblib==1.2.0
- streamlit==1.23.1
- scikit-learn
- pillow

You can install these dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).

Please verify if the updated content meets your requirements.

## SET UP THE PROJECT
STEP 1: start up your VM instance

STEP 2: open the SSH terminal

STEP 3: enter the following command
```bash
git clone https://github.com/QuintineSol/DataEngineering.git
```

IMPORTANT: each time you start your VM and want to run the project, it is important to enter the command
```bash
git pull
```
to get the latest version of the project from the remote repository.

## SET UP THE DOCKER CONTAINERS
STEP 1: create a container for prediction-ui
```bash
cd DataEngineering/prediction-ui
sudo docker build -t <username on Docker hub>/insurance-ui:0.0.1 .
sudo docker run -p 5001:5000 -e PREDICTOR_API=http://insurance-api:5000/insurance_predictor -d --name=insurance-ui <username on Docker hub>/insurance-ui:0.0.1
```
STEP 2: create a container for prediction-api
```bash
cd ../prediction-api
sudo docker build -t <username on Docker hub>/insurance-api:0.0.1 .
sudo docker run -p 5000:5000 -d --name=insurance-api <username on Docker hub>/insurance-api:0.0.1
```

STEP 3: create a virtual container network between the containers
```bash
sudo docker network create insurance-app-network
sudo docker network connect insurance-app-network insurance-api
sudo docker network connect insurance-app-network insurance-ui
```

STEP 4: create a container for training-api
```bash
cd ../training-api
sudo docker build -t <username on Docker hub>/insurance-train-api:0.0.1 .
sudo docker run -p 5002:5000 -v <your-host-path>/models:/usr/trainapp/models -d --name=insurance-train-api <username on Docker hub>/insurance-train-api:0.0.1
```
Note: you can find <your-host-path> by entering the followng commands
```bash
cd ../..
pwd
```
Please don't forget to go back to the training-api folder when creating the training-api container by entering the following commands
```bash
cd DataEngineerg/training-api
```

STEP 5: create a folder in the home directory of the VM called "models"

CHECK: entering the following commands
```bash
sudo docker images
```
should display the newly created docker images
```bash
sudo docker ps -a
```
should display the three running containers

## TEST THE PREDICTON-UI & PREDICTION-API
STEP 1: start the containers
```bash
sudo docker start insurance-ui
sudo docker start insurance-api
```

STEP 2: browse http://VM_external_ip:5001/checkinsurance

Note: don't forget to replace "VM_external_ip" with the correct external IP of your VM instance.
This IP address can be found where you started your VM instance.

STEP 4: enter some values 

STEP 5: press submit

CHECK: you should be redirected to another page containing the output of the model "The insurance amount is ...."

## TEST THE TRAINING-API
STEP 1: start the training-api container
```bash
sudo docker start insurance-train-api
```

STEP 2: open Insomnia

STEP 3: copy the training data from the github repository under the folder called 'data'

STEP 4: paste the data into Insomnia

STEP 5: change the URL to http://VM_external_ip:5002/training-api/model

STEP 6: click on 'Send'

## CI/CD PIPELINE - SETUP
STEP 1: go to Artifact Registry.

STEP 2: create a new repository called 'assignment1' and set the region to 'us-central1'.

## CI/CD PIPELINE - MANUAL TRIGGER
STEP 3: go to Cloud Build > Triggers.

STEP 4: click on 'connect repository'.

STEP 5: select the github repository of this project.

STEP 6: click 'create trigger'.
- name: 'manual'
- or in response to: manual invocation
- select the github repository of this project
- location: inline
- open editor and copy the content of cloud_build_ml_app under the folder cloub-build in this project
- add variable
   - variable 1: _LOCATION
   - value 1: us-central1
   - variable 2: _REPOSITORY
   - value 2: assignment1

STEP 7: click on 'run' and then on 'run trigger'.

STEP 8: go to 'Cloud Run'.

STEP 9: click on prediction-api and copy the URL at the top.

STEP 10: go back to prediction-ui and click on 'edit'.

STEP 11: under Environment Variables
- provide as value 1: <prediction-api-url>/insurance_predictor/

STEP 12: click on 'deploy'.

STEP 13: go to prediction-ui and copy the URL at the top.

STEP 14: browse <prediction-ui-url>/checkinsurance

## CI/CD PIPELINE - GITHUB PUSH
....

## CI/CD PIPELINE - BUCKETS

## SET UP MODEL REPOSITORY GOOGLE CLOUD
STEP 1: go to Cloud Storage > Buckets.

STEP 2: go to your model bucket (that was already created in the labs)

STEP 3: upload our model (in our github repo under the folder 'models') to this bucket

## TEST THE BASIC PREDICTION-UI & PREDICTION-API
STEP 1: start the prediction-ui by entering the following commands
```bash
cd DataEngineering/prediction-ui
python3 -m venv .insurance-ui.env
source .insurance-ui.env/bin/activate
pip install -r requirements.txt 
python3 app.py 
```
STEP 2: start the prediction-api by entering the following commands
```bash
cd DataEngineering/prediction-api
python3 -m venv .insurance-api.env
source .insurance-api.env/bin/activate
pip install -r requirements.txt 
python3 app.py 
```
STEP 3: browse http://VM_external_ip:5001/checkinsurance

Note: don't forget to replace "VM_external_ip" with the correct external IP of your VM instance.
This IP address can be found where you started your VM instance.

STEP 4: enter some values 

STEP 5: press submit

CHECK: you should be redirected to another page containing the output of the model "The insurance amount is ...."

Note: due to code changes, this basic testing doesn't work anymore.

## DOCKER CHEATSHEET
View the log of a container
```bash
sudo docker logs <docker_container_name>
```

View the created container images
```bash
sudo docker images
```

View the running containers
```bash
sudo docker ps -a
```

Delete all containers (including their images and the container network)
```bash
sudo docker system prune -a 
```