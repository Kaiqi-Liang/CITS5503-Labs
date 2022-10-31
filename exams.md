# Exam

## 2021

### Question 1 (20 points)

The creative designers of a marketing and video editing company in Melbourne use a commercial web-based application for converting videos to different formats. In addition, one of the main advantages of this software is the ability to publish those videos in popular social media networks such as YouTube, Instagram, Twitter, etc. This allows the user to convert and edit a video and then publish the same video at the same time to all different social media that the user selects in the software. This is particularly useful for marketing campaigns were usually a video is published in different social media networks. In the past, before using that software they used to spend around 5-10 hours to convert a single video to different formats, resolutions, etc. and upload them to all different social media. Now using this software this process is reduced to only 45mins to 1 hour. Since they started using this software, they have to pay a monthly subscription fee of 25.000 AUD per month or around 300.000 AUD per year regardless of the number of videos they process per year. Despite all the benefits from this software, the CTO of the company believes they should pay a software developer to replicate this web-based software instead of keep paying those high fees. While he knows building software is expensive, he also believes there must be a way of designing this new software to reduce the cost and make it profitable in the long term. You as a Software Developer and Cloud Computing expert are hired for this task.

#### 1.1 (10 points)

You initially think on using EC2 instances for processing. Briefly explain what other AWS technologies you would use to replicate the web-based software functionalities and what architecture you would use to satisfy the needs of the client using such technologies.

1. Use Load Balancer to balance the load of the EC2 instances.
2. Use S3 to store the different formats of the videos.
3. Use Amplify (Mobile Hub) to develop and deploy the web app.

Use a client server architecture where the Load Balancer and the EC2 instances behind it acting as the server, and the application is the client.

#### 1.2 (10 points)

The company currently creates on average 50 videos per month and it’s not likely to increase the demand of clients for the next couple of years. Take also into account that there are less than 20 people that will be using the system. Discuss how you could change the previous solution using now a full serverless architecture and what benefits and disadvantages would have this new architecture over the previous architecture using EC2 instances.

Move the processing code from EC2 to Lambda and add an API Gateway to implement this Serverless architecture.

Benefits:

1. Lambda provides simplicity and less complexity over EC2.
2. No need to manage server infrastructure so that developers can focus on the business problem they are trying to solve.
3. It's more economic as paymen is as per the throughput, Lambda charges on the number of function calls as opposed to EC2 charges on the hours even when the machines are idle.
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
4. Use DynamoDb to store user information and metadata for their files.
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

#### a. [10 points]

A medium sized company has users that belong in different departments and perform different functions. The company has implemented a policy of document access that is specific to the job that a person does and their level in the organisation.

Describe how you could use AWS IAM to provide authorization and authentication in this organisation to access to documents, as well as access and perform actions using applications.

#### b. [10 points]

An organisation has 5 departments and has separated out each of the IAM users into separate groups using paths following the pattern `companybucket/department1/*`, `companybucket/department2/*`, `companybucket/department3/*` etc.

Their IAM account names follow the pattern `user@department1.company.com`, `user@department2.company.com` etc.

You are tasked with securing a bucket that contains a folder for each of 5 departments in an organisation. Only people within a department can write to their own folder. Everyone can read from all folders.

Discuss the principles that you would use to create a policy that would achieve this objective. Write the policy as a JSON file that you would use.
Note: you can have individual statements for each department.

### Question 6. DevOps (10 points)

You have been asked to set up the ability to automatically build and test code updated in a repository. Discuss which AWS service you would use to do this, and the steps involved in getting it to work. What information would be needed in the configuration file for this service?

### Question 7. Machine Learning (10 points)

A dog recognition program recognises 10 dogs in a picture of 14 dogs and some cats. Of the 10 dogs, 7 are true positives and 3 are false positives.

i. How many actual dogs did the recognition program recognise?
>7
ii. What is the precision of the program?
>0.7
iii. What is the recall of the program?
>0.63
