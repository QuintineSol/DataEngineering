## Machine Learning Model

This project used the following machine learning model: https://github.com/Kajal03g/HealthInsuranceAmountPrediction/blob/main. It predicts health insurance costs based on age, sex, BMI, number of children, smoking habits and region of residence (in America). 

## Repository Structure

This repository has the following structure:

```
.
├── README.md
├── cloud-build
│   ├── cloud_build_pipeline_executor.json
│   ├── cloud_build_pipeline_run.json
│   ├── cloud_build_pred_api.json
│   └── cloud_build_pred_ui.json
├── data
│   └── train_data.json
├── models
│   └── insurance_pred
├── prediction-api
│   ├── Dockerfile
│   ├── app.py
│   ├── insurance_pred
│   ├── insurance_predictor.py
│   └── requirements.txt
├── prediction-ui
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates
│       ├── input_form_page.html
│       └── response_page.html
├── requirements.txt
├── synchronizer
│   ├── data_upload.txt
│   ├── model_upload.txt
│   └── upload_training_data.bash
├── training-api
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── resources
│       └── model_trainer.py
└── training-pipeline
    ├── components
    │   ├── insurance_predictor_training_pipeline.yaml
    │   ├── pipeline.ipynb
    │   └── training-pipeline.png
    └── pipeline_executor
        ├── Dockerfile
        ├── pipeline_executor.py
        └── requirements.txt
```

## How to use

The following guideline explain step-by-step how to set up the project. 

Note: it is assumed that all exercises/tasks from the labs were finished. Therefore, if this is not the case, please do this first.

STEP 1: Go to Google Cloud > Artifact Registry.

STEP 2: Create a new repository called 'assignment1' and set the region to 'us-central1'.

STEP 3: Go to Cloud Build > Triggers.

STEP 4: Create the following CI/CD triggers.

1. Prediction-API
- Name: build-prediction-api
- Region: us-central1
- Event: push to a branch
- Repository: QuintineSol/DataEngineering
- Branch: main
- Included files filter (glob): prediction-api/**   and   synchronizer/model_upload.txt
- Type: Cloud Build configuration file (yaml or json)
- Location: Repository
- Cloud Build configuration file location: cloud-build/cloud_build_pred_api.json
- Variable 1: _LOCATION      Value 1: us-central1
- Variable 2: _REPOSITORY    Value 2: assignment1

2. Prediction-UI
- Name: build-prediction-ui
- Region: us-central1
- Event: push to a branch
- Repository: QuintineSol/DataEngineering
- Branch: main
- Included files filter (glob): prediction-ui/**   and   synchronizer/model_upload.txt
- Type: Cloud Build configuration file (yaml or json)
- Location: Repository
- Cloud Build configuration file location: cloud-build/cloud_build_pred_ui.json
- Variable 1: _LOCATION      Value 1: us-central1
- Variable 2: _REPOSITORY    Value 2: assignment1

3. Pipeline Executor
- Name: build-pipeline-executor
- Region: us-central1
- Event: push to a branch
- Repository: QuintineSol/DataEngineering
- Branch: main
- Included files filter (glob): training-pipeline/pipeline_executor/**
- Type: Cloud Build configuration file (yaml or json)
- Location: Repository
- Cloud Build configuration file location: cloud-build/cloud_build_pipeline_executor.json
- Variable 1: _LOCATION      Value 1: us-central1
- Variable 2: _REPOSITORY    Value 2: assignment1

4. Execute Pipeline
- Name: execute-pipeline
- Region: us-central1
- Event: push to a branch
- Repository: QuintineSol/DataEngineering
- Branch: main
- Included files filter (glob): synchronizer/data_upload.txt     and     training-pipeline/components/**
- Type: Cloud Build configuration file (yaml or json)
- Location: Repository
- Cloud Build configuration file location: cloud-build/cloud_build_pipeline_run.json
- Variable 1: _LOCATION      Value 1: us-central1
- Variable 2: _REPOSITORY    Value 2: assignment1

STEP 5: Run the pipeline executor trigger (trigger 3 in the step above).

STEP 6: Open a Google Cloud Shell.

STEP 7: Enter the following commands
```bash
git clone https://github.com/QuintineSol/DataEngineering.git
cd DataEngineering/synchronizer
bash upload_training_data.bash <github-user-name> <github-token>
```

STEP 8: Go to Cloud Build > History.

This should display the running pipeline.

STEP 9: Go to Vertex AI > Pipelines.

STEP 10: Click on the running pipeline to view its progress.

STEP 11: When the pipeline is finished, go back to Cloud Build > History. This should now display the building of prediction-API and prediction-UI.

STEP 12: When the building of prediction-API and prediction-UI is finished, go to Cloud Run.

STEP 13: Click on prediction-api and copy the URL at the top.

STEP 14: Go back to prediction-ui and click on 'edit'.

STEP 15: Under Environment Variables
- provide as value 1: <prediction-api-url>/insurance_predictor/

STEP 16: Go to the bottom and click on 'deploy'.

STEP 17: Go to prediction-ui and copy the URL at the top.

STEP 18: Browse <prediction-ui-url>/checkinsurance

STEP 19: Enter values and click on 'submit'.

This should redirect the user to a response page displaying the predict insurance costs.

The guidelines above only use a subset of the created triggers. The remainder of the triggers can be tested by changing the content of the prediction-api, prediction-ui, training-pipeline/pipeline_executor or training-pipeline/components in the github repository.

## Docker Cheatsheet (this was used during development)
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