# Practical Worksheet 8

## Set Up Python Environment

![pip](images/pip.png)

## Run Hyperparameter Tuning Jobs

Create an IAM role to get access to the `SageMaker` service for hyperparameter tuning.

![role](images/role.png)

Create a bucket to to put the training data as well as the output from the training job.

![bucket](images/bucket.png)

Change bucket name in the session prepration cell.

![preparation](images/preparation.png)

Run the rest of the code cells then monitor the progress of the hyperparameter tuning job.

![jobs](images/jobs.png)
![sagemaker](images/sagemaker.png)
![status](images/status.png)

These are the hyperparameters of the best training job.

![hyperparameters](images/hyperparameters.png)

The output is stored in the same bucket by `SageMaker`.

![output](images/output.png)
