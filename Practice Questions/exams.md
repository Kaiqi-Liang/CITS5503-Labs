# Exams

## 2021

### Question 1 (20 points)

The creative designers of a marketing and video editing company in Melbourne use a commercial web-based application for converting videos to different formats. In addition, one of the main advantages of this software is the ability to publish those videos in popular social media networks such as YouTube, Instagram, Twitter, etc. This allows the user to convert and edit a video and then publish the same video at the same time to all different social media that the user selects in the software. This is particularly useful for marketing campaigns were usually a video is published in different social media networks. In the past, before using that software they used to spend around 5-10 hours to convert a single video to different formats, resolutions, etc. and upload them to all different social media. Now using this software this process is reduced to only 45mins to 1 hour. Since they started using this software, they have to pay a monthly subscription fee of 25.000 AUD per month or around 300.000 AUD per year regardless of the number of videos they process per year. Despite all the benefits from this software, the CTO of the company believes they should pay a software developer to replicate this web-based software instead of keep paying those high fees. While he knows building software is expensive, he also believes there must be a way of designing this new software to reduce the cost and make it profitable in the long term. You as a Software Developer and Cloud Computing expert are hired for this task.

#### 1.1 (10 points)

You initially think on using EC2 instances for processing. Briefly explain what other AWS technologies you would use to replicate the web-based software functionalities and what architecture you would use to satisfy the needs of the client using such technologies.

    1. Use Load Balancer to balance the load of the EC2 instances.
    2. Use S3 to store the different formats of the videos.
    3. Use Amplify (Mobile Hub) to develop and deploy the web app.
    4. Use Elastic Transcoder to convert videos to different formats.

    Use a client/server architecture where the Load Balancer and the EC2 instances behind it acting as the server, and the application is the client.

#### 1.2 (10 points)

The company currently creates on average 50 videos per month and it’s not likely to increase the demand of clients for the next couple of years. Take also into account that there are less than 20 people that will be using the system. Discuss how you could change the previous solution using now a full serverless architecture and what benefits and disadvantages would have this new architecture over the previous architecture using EC2 instances.

Move the processing code from EC2 to Lambda and add an API Gateway to implement this Serverless architecture.

    Benefits:

    1. Lambda provides simplicity and less complexity over EC2.
    2. No need to manage server infrastructure so that developers can focus on the business problem they are trying to solve.
    3. More economic as payment is as per the throughput, Lambda charges on the number of function calls as opposed to EC2 charges on the hours even when the machines are idle.
    4. Less coupling as different components are well separated and communicate through an API.

    Disadvantages:

    1. Less customisable and flexible as AWS decides the infrastructure therefore less control.
    2. Serverless Architecture executes commands and functions on temporarily created containers. So if a client performs few tasks on your app, the serverless architecture will create a temporary box and will destroy it as soon as the client is done performing tasks, this results in delays which are also known as cold start.
    3. Serverless platforms can be overloaded which opens up a lot of security concerns such as Denial of Service attacks.

### Question 2 (20 points)

A professor in Computer Science at UWA has data from all labs, mid-term exam and final exam marks for the last two years of every student in csv format. He first noticed that in previous years those students that did very well in the labs and mid-term exam for a particular unit got at least 70% marks in the final exam. This year, the professor only has access to the labs and mid-term exam marks in csv format. However, he thinks he can predict the outcome of the final exam for students before marking the final exam.

#### 2.1 (10 points)

How would you use AWS technologies to prove (or disprove) his theory and help the professor predicting the marks for the current students this year?

    1. Upload the csv file of the marks for the last two years on S3.
    2. Train a Regression Model on SageMaker using the data on S3.
    3. Make predictions on this year's marks and save them back to S3.

#### 2.2 (10 points)

What approach would you use to assess the data models and help with the data analysis of the results?

    1. Split the data (i.e. marks from the last 2 years) into training set and test set, use cross validation on the training set and calculate the RMSE on the test set.
    2. After doing the predictions mark the final exams and calculate the RMSE between them and the actual marks. The RMSE will be used to assess the data model.

### Question 3 (10 points)

A software developer wants to create a Drobox-like application for Photographers where they could seamlessly upload pictures from a local machine to the cloud and synchronise the data across multiple devices (Computer, Mobile Phones, etc.) for authenticated users. For every image uploaded by the users, she wants to save the metadata related to the file. Given the files uploaded by users are very important, she wants to allow restoring such files even if users delete the images on purpose. In addition, the software developer wants to automatically create labels for the uploaded images so they can perform searches of images based on the generated labels.

Describe your approach using AWS technologies to create that application.

    1. Use Rekognition to automatically create labels for the uploaded images.
    2. Use Cognito to create authentication, authorisation, and user management.
    3. Use S3 for users to upload images from a local machine to the cloud and enable versioning in the case of user deleting files and wanting to restore them.
    4. Use DynamoDB to store user information and metadata for their files.
    5. Use Amplify (Mobile Hub) to develop and deploy the mobile and web app needed for the users to use it across multiple devices.

### Question 4 (20 points)

A MedTech company in Perth has created a novel algorithm for detecting heart diseases from X-rays and CT scans (medical images) using machine learning and computer vision. The company now wants to commercialise it as a Software-as-a-service (SaaS) product. Initially, this product should allow authorised radiologist working at the Royal Perth Hospital to upload such images. Then, once the algorithm can process the image (it could take a couple of minutes) it should retrieve the prediction. The solution should be scalable so it can be used in other hospitals in the future.

Give 10 recommendations to the company on how they could use AWS to create this platform. **Provide your answer as a list of bullet points**.

    1. Use S3 to store the scans and prediction results.
    2. Use SageMaker to run the machine learning algorithm.
    3. Use Cognito to allow authorised radiologist working at the Royal Perth Hospital to access the platform.
    4. Use EC2 to run the novel algorithm.
    5. Use Load Balancer to load balance the EC2 instances for scaling up the number of instances to handle large workload.
    6. Use CodeDeploy to automate the application deployments to EC2 instances.
    7. Package the application in a container and use ECS to manage the containers so it can be deployed easily for other hospitals to use.
    8. Use KMS to encrypt the scans as they are sensitive user data.
    9. Use Amplify (Mobile Hub) to develop the platform.
    10. Use Rekognition to help with computer vision tasks.

### Question 5 (20 points)

You are a consultant who has been asked to write a report for a rapidly growing pet food company (PFC), based in Perth who would like to upgrade their systems to cope with the increasing global demand for their products. The company has rented space in a data centre for their systems that are a mix of Windows and Linux Servers, networking and firewall equipment and a range of storage devices (SANs, NAS, disk drives in servers). The company uses a range of software that they have purchased over the years that run on these machines. The functionality covered is everything from finance, sales and manufacturing to online product sales through their website. PFC have received venture capital funding and want to expand into new markets, especially Asia and China in particular. To do this, they will need to be able to use modern systems that scale and operate at global scale.

Provide 5 pros and 5 cons of moving infrastructure from being on-premises to cloud based. Consider this in the context of global expansion and resilience. **Provide your answer as a list of bullet points**.

    Pros:

    1. More cost efficient.
    2. No need to manage the physical infrastructure on-premises and maintain data centres.
    3. Easy to scale up or down.
    4. Increase speed and agility, the time it takes to experiment and develop is significantly lower.
    5. Available globally as it is very easy to deploy the product in multiple regions around the world, so it can operate at global scale.

    Cons:

    1. Even though cloud providers have regions all around the world but not every major city gets one. PFC wants to expend into new markets especially China but AWS does not even have an availability zone anywhere in China.
    2. Data sovereignty.
    3. Security might not be guaranteed on the cloud as compare to having full control over their own data centres on-premises.
    4. There is a bottleneck on transfering large amount of data to the Cloud when moving infrastructure from being on-premises to cloud based.
    5. There might be performance unpredictability for example when VMs share the same disk there might be I/O interference or HPC tasks that require coordinated scheduling.

## 2018 - 2019

### Question 1. Cloud Computing (20 points)

A company is trying to decide if it should use Cloud Computing for all of its computing service needs rather than using its own machines in a data centre. As background, this company runs its own web applications, databases and carries out data analysis, machine learning and other ad hoc computing functions.

You have been asked to provide a brief summary of the advantages and disadvantages of using Cloud Computing versus owning and running its own infrastructure and services. These should be stated from a technical, economic, security and efficiency perspectives.

    Advantages:

    1. Increase speed and agility, the time it takes to experiment and develop is significantly lower as the cloud provides a broad range of technologies.
    2. Easy to scale up or down.
    3. More economic and save costs.
    4. No need to manage the physical infrastructure on-premises and maintain data centres.
    5. Available globally as it is very easy to deploy the product in multiple regions around the world, so it can operate at global scale.

    Disadvantages:

    1. Not able to choose the location of the data centre suited for the customers, even though cloud providers have regions all over the world but not every major city gets one.
    2. Data sovereignty.
    3. Security might not be guaranteed on the cloud as compare to having full control over their own data centres on-premises.
    4. There is a bottleneck on transfering large amount of data to the Cloud when moving infrastructure from being on-premises to cloud based.
    5. There might be performance unpredictability for example when VMs share the same disk there might be I/O interference or HPC tasks that require coordinated scheduling.

### Question 3. Storage (10 points)

#### a. [5 points]

Describe what S3 is and discuss its similarities and differences with the data store DynamoDB.

#### b. [5 points]

Describe what S3 is and describe its “eventual consistency” mechanism. What are the potential considerations if you are writing a multi-user application that uses S3? What other technology could you use if you want to avoid the problems of eventual consistency?

### Question 4. Identity and Access Management (20 points)

A medium sized company has users that belong in different departments and perform different functions. The company has implemented a policy of document access that is specific to the job that a person does and their level in the organisation.

Describe how you could use AWS IAM to provide authorization and authentication in this organisation to access to documents, as well as access and perform actions using applications.

    1. Create an IAM group for each department.
    2. Create a policy for each group and assign it to the group.
    3. Create IAM users for each person in each department and add them to their respective group, each user can have their own credentials for authenticating to AWS.
    4. Create IAM roles for users who need document access for specific jobs that is different from the rest of the users in the same department, as they are temporary the roles can be removed when the user no longer needs those access.

### Question 6. DevOps (10 points)

You have been asked to set up the ability to automatically build and test code updated in a repository. Discuss which AWS service you would use to do this, and the steps involved in getting it to work. What information would be needed in the configuration file for this service?

    CodeBuild can be used to build source code, run unit tests and produce artifacts that are ready to deploy.

    Steps:

    1. Create the source code.
    2. Create the buildspec file.
    3. Create S3 buckets to store the build input and output.
    4. Upload the source code and the buildspec file to S3.
    5. Create the build project.
    6. Run the build.
    7. View the build information in CloudWatch Logs.
    8. Get the build output from S3.

    Information needed in the configuration files:

    1. version of the config
    2. phases
    3. commands to run in each phrase
    4. name of the files to be produced by CodeBuild (artifacts)

### Question 7. Machine Learning (10 points)

A dog recognition program recognises 10 dogs in a picture of 14 dogs and some cats. Of the 10 dogs, 7 are true positives and 3 are false positives.

i. How many actual dogs did the recognition program recognise?

    7
ii. What is the precision of the program?

    7 / 10 = 0.7
iii. What is the recall of the program?

    7 / 14 = 0.5

## Sample Exam

### Question 1

Your best friend pitched to you an idea of an app where the user can take a picture with their mobile phone and the app will reply with a voice describing what is inside the picture. He calls it "¡See". He also mentions that the main target for this app are people that are visually impaired (someone with the partial or full loss of sight in one or both eyes). He is sure that this app will help millions of people around the world. Your friend ask you for advice on how to create this app. You as a software developer and expert in Cloud Computing want to provide some advice to your friend. Explain what technologies you would use to create this app using AWS.

    1. Amplify (Mobile Hub)
    2. S3
    3. Rekognition
    4. Polly
    5. Lambda

### Question 2

After one year of launching iSee, your friend came back to you for advice. He mentioned that the app has been downloaded more than 100,000 times in the Play Store (Android users) and more than 90,000 times in the App store (iOS users). Given the success of the app, he mentioned that now he wants to add the feature of describing videos as well. Also, he wants all the actions of the app to be controlled by voice. Provide 3 examples of AWS services that your friend could use to implement the new feature and explain how it would solve the problem.

    1. SageMaker
    2. Lex
    3. EC2

### Question 3

The App of your friend "iSee" has been one of the most popular apps in the last year. Your friend even gave a Ted Talk related to technology, innovation an social good. After the immense success of the app, and raising 5M dollars from investors your friend now has a start-up company with more than 30 people. He ask you to please consider a position in the company as a CTO. In the first month in your new role, you noticed that there are many different things that could be improved in the app. For example, you realized that for the image description feature, iSee uses an EC2 instance for the processing. For the video feature, iSee uses another big EC2 instance. You think there is a better way of processing images that would cost less money. The same goes for the video processing feature. You also believe that one single instance is not enough to handle the future users once the version 2.0 is released. At the end of the month, you have to give a report providing suggestions to improve the app. What are the solutions that you gave in that report?

    1. Use Rekognition instead of a EC2 for video processing to save money.
    2. Add auto scaling groups for the EC2 instances so that when a single instance is not enough to handle the future users it will automatically scale it.
    3. Finally add a Load Balancer for the EC2 instances.

### Question 4

After successfully implementing your suggestions to the app "¡See. You got a report that there is a small group of users, that have uploaded images or videos that are considered "inappropriate content", which is prohibited according to your policies. You are very surprised to learn that those users have been infringing the policies of "iSee" many times in the past but just now someone from the Quality Assurance group noticed this problem. You decide that is time to implement a feature that automatically checks the images or videos that will be uploaded to the app to check for what could be considered "inappropriate content". Provide 5 advices (as bullet points) on how to achieve this using AWS.

    1. Use the `DetectModerationLabels` operation in Rekognition to determine if an image contains inappropriate content.
    2. Train a NLP model in SageMaker that given the moderation labels returned by Rekognition, it filters the inappropriate content even further based on our policies as `DetectModerationLabels` might be too strict or infringe with our policies.
    3. Create a Lambda function that will be triggered by S3 everytime an image is uploaded by a user. This function will first call the Rekognition API to get the labels then pass them to the trained model to determine whether it is inappropriate.
    4. Use Cognito to mangage user pools where users are required to upload a proof of age upon registration to use the app so that their age information is recorded. After the the Lambda function makes the prediction using the model, if the uploaded image does contain inappropriate content it can find out whether the user is underage and only then it will give a warning.
    5. If a user gets too many warnings within a certain time period we should backlist them and keep a list of blacklisted users in a file on S3.

### Question 5

Taking into account all previous information that you got from the last 4 questions. Design an architecture for "iSee". What technologies you would use? What kind of architecture?

    1. DynamoDB to store user information, S3 to store files.
    2. Due to the popularity of the app use EC2 with auto scaling groups and Load Balancers for video processing because Lambda would be too expensive with high workload.
    3. Lambda can be used to invoke the inappropriate content detection and blacklist users if needed.
    4. The UI is developed through Amplify.
    5. Cognito is used for authentication, authorisation, and user management.
    6. Machine Learning services to be invoked including Lex, Polly, Rekognition and SageMaker.
