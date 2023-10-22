## Machine Learning Model

The project uses the following machine learning model: https://github.com/Kajal03g/HealthInsuranceAmountPrediction/blob/main. It predicts health insurance costs based on age, sex, BMI, number of children, smoking habits and region of residence (in America). 

## Repository Structure

The repository has the following structure:

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

The following guidelines explain how to set up the project step-by-step. It is assumed that labs 0 to 5 were finished. If this is not the case, please do this first.

STEP 1: Go to Google Cloud > Artifact Registry.

STEP 2: Create a new repository called 'assignment1' and set the region to 'us-central1'.

STEP 3: Go to the remote github repository.

STEP 4: Download the 'parameters-insurance-pipeline.json' under training-pipeline > components.

STEP 5: In this file, enter your values for 'project-id', 'data_bucket' and 'model_repo'.

STEP 6: Go to Google Cloud > Cloud Storage.

STEP 7: Upload your version of the parameters-insurance-pipeline.json file to your data bucket.

STEP 8: Go to Cloud Build > Triggers.

STEP 9: Create the following CI/CD triggers.

1. Prediction-API
- Name: build-prediction-api
- Region: us-central1
- Event: push to a branch
- Repository: QuintineSol/DataEngineering
- Branch: main
- Included files filter (glob): prediction-api/**   and   synchronizer/model_upload.txt
- Type: Cloud Build configuration file (yaml or json)
- Location: Inline
    - Click 'open editor'.
    - Copy the content of cloud-build/cloud_build_pred_api.json from the github repo
    - Change 'models_de2023_qjsol' to the name of your model bucket
    - Click 'Done'
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
- Location: Inline
    - Click 'open editor'.
    - Copy the content of cloud-build/cloud_build_pipeline_run.json from the github repo
    - Change 'data_de2023_qjsol' to the name of your data bucket
    - Change 'temp_de2023_qjsol' to the name of your temp bucket
    - Click 'Done'
- Variable 1: _LOCATION      Value 1: us-central1
- Variable 2: _REPOSITORY    Value 2: assignment1

STEP 10: Run the pipeline executor trigger (trigger 3 in the step above).

STEP 11: Open a Google Cloud Shell.

STEP 12: Enter the following commands
```bash
git clone https://github.com/QuintineSol/DataEngineering.git
cd DataEngineering/synchronizer
bash upload_training_data.bash <github-user-name> <github-token>
```

STEP 13: Go to Cloud Build > History.

This should display that the building/running of the pipeline is in progress.

STEP 14: Go to Vertex AI > Pipelines.

STEP 15: Click on the running pipeline to view its progress.

STEP 16: When the pipeline is finished, go back to Cloud Build > History. 

This should now display the building of the prediction-API and prediction-UI.

STEP 17: When the building of prediction-API and prediction-UI is finished, go to Cloud Run.

STEP 18: Click on prediction-api and copy the URL at the top.

STEP 19: Go back to prediction-ui and click on 'edit'.

STEP 20: Under Environment Variables
- provide as value 1: <prediction-api-url>/insurance_predictor/

STEP 21: Go to the bottom and click on 'deploy'.

STEP 22: Go to prediction-ui and copy the URL at the top.

STEP 23: Browse <prediction-ui-url>/checkinsurance

STEP 24: Enter values and click on 'submit'.

This should redirect you to a response page displaying the predicted insurance costs.

The guidelines above only use a subset of the created triggers. The remainder of the triggers can be tested by changing the content of the folders prediction-api, prediction-ui, training-pipeline/pipeline_executor or training-pipeline/components in the github repository. Since this has been tested already, please don't do this now.

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