# Weekly Questions CITS5503 2022

## Week 1

[1.0] [5 points] The evolution of Cloud Computing has been compared to the evolution of electricity supply as a utility. Describe specific problems that Cloud Computing solves as compared to businesses running their own data centres.

1. Businesses running their own data centres means they have to maintain it themselves. It not only takes a long time to build but also costs a lot of money. The biggest problem is scaling, scaling up has all the aforementioned problems because the only way to do so is building more data centres, while scaling down is impossible so when the machines are no longer needed they will be idle and still consume energy, generate heat and it's just a waste.

2. Cloud Computing solves all of those problems as it takes seconds to spin up as many machines as you need as opposed to months to build them. You pay as you go and when the machines are idle you can shut them down and stop getting charged. Auto scaling allows you to scale up and down easily.

[2.0] [5 points] Describe the different categories of services (XaaS) cloud computing can provide with specific examples of each service.

1. Software as a Service (SaaS) provides an entire application for example Microsoft Teams.
2. Platform as a Service (PaaS) provides middleware/infrastructure for example S3.
3. Infrastructure as a Service (IaaS) provides raw computing resources for example an EC2 instance that provides raw metal like CPUs and GPUs.

[3.0] [10 points] An established financial company is about to launch their new banking application. Give 5 reasons why the company should use their own data centre rather than cloud computing.

1. Security might not be guaranteed on the cloud. An established financial company might want to keep their sensitive data on premisis so they have full control over it.
2. Data sovereignty.
3. Able to choose the location of the data centre suited for the customers, even though cloud providers have regions all around the world but not every major city gets one.
4. It is cheaper because an established financial company will need a lot of backups and longterm persistent storage which might not fit cloud's pay as you go model.
5. There might be performance unpredictability for example when VMs share the same disk there might be I/O interference or HPC tasks that require coordinated scheduling.

[4.0] [20 points] Describe the concepts of vertical and horizontal scale. Describe 2 different ways in which you could scale a web application horizontally. Describe a potential architecture to scale the database to handle the scaling out of the web servers.

Concepts of vertical and horizontal scale:

1. Vertical scale is increasing the hardware configuration by addming more physical resources.
2. Horizontal scale is adding more machines with similar hardware specification.

Ways to scale a web application horizontally:

1. Replication: create multiple copies of the same data and store them into multiple machines.
2. Partitioning: split the data into smaller and independent units and assign one or more partitions to a single machine across multiple machines.

Architecture to scale database

1. Use DynamoDB to store most of the web application's data as they are structured.
2. Backup the data regularly on S3 in case the data is corrupted and have to roll back.
3. Store older backups or archives to Glacier.

[5.0] [20 points] How could a mobile device benefit from cloud computing? Explain the reasons or provide your arguments supporting the contrary. Discuss several cloud applications for mobile devices; explain which one of the three cloud computing delivery models, SaaS, PaaS, or IaaS, would be used by each one of the applications and why.

Benefits:

1. Extended battery life, run most of the heavy computing tasks on the cloud.
2. Abundant Storage Space, store information on the cloud instead of on the device itself.
3. Having a backup, if the mobile device breaks down or gets lost the data is saved on the cloud.

Cloud applications for mobile devices:

1. Mobile robots run heavy computer vision and NLP computation on the cloud (PaaS).
2. Mobile phones have a lot of applications using the cloud for example Dropbox (SaaS).

## Week 2

[5.0] [20 points] Describe the steps which you would take on AWS and the decisions that would need to be made to create, configure and run a Virtual Machine Instance.

1. Pick an OS image, what operating system do you want to run.
2. Pick an instance type, how many resources do you need for this virtual machine instance.
3. Create a key pair, no decision needed.
4. Create security group with inbound rules, who do you want to allow to access the virtual machine.
5. Configure the size of the EBS volume, how much storage do you need.

[6.0] [10 points] Describe EBS and what features it offers.

1. EBS stands for Elastic Block Storage which is a high performance block storage device from 1GB to 1TB in size.

2. It can be attached to an instance so that it can be replicated across multiple servers to avoid losing data when a server fails.

3. A snapshot of the EBS volumes can be created at any time as a backup and its size can be increase automatically.

[7.0] [10 points] What is CLI and Boto? What are advantages of using CLI? How does Boto function helps in AWS operation?

1. CLI is commandline interface which allows you to interact with AWS through the terminal.

2. Boto is a Python library that allows you to do what you can do through the console in Python so that you can write a script to automate the process and run for many times without having to click through the GUI manually which could help reduce the chance of human error when selecting and configuring resources.

## Week 3

[8.0] [10 points] Describe what virtualisation is and describe the characteristic attributes of the different types of virtualisation (Language, Operating System and Hardware).

1. Virtualisation is a way to support multiple self-contained environments that act like separate computers on a single machine that share the same physical resources.

2. Language level virtualisation like Java Virtual Machine allows the execution of the same code (Java) on different architectures for example JVM.

3. OS level virtualisation runs a hypervisor on top of the host OS for example differnet types of VMs like VirtualBox, VMware Fusion.

4. Hareware level virtualisation runs a hypervisor on top of bare metals and divide the physical resources for different guest OS and it does not have a host OS for example EC2.

[9.0] [10 points] Describe what containers are with reference to Docker and discuss their similarities and differences from operating system virtualisation perspective as provided by VirtualBox.

1. Containers are cut down VMs used to execute code in an isolated environment.

2. The differences are VMs run multiple OS on a single physical machine while containers use the host OS so it is lighter than VMs. VMs' entire state can be saved to files while containers are not really designed to save state as they are temporary. VMs provide fault and security isolation at the hardware level while containers do it at the software level. VMs give each instance its own physical resources while containers share the physical resources between instances.

3. The similarities are they both divide system resources, preserve performance with resource controls and they are both hardware independent.

[10.0] [10 points] There was an evolution of operating system during the half century from 1960 to 2010. Identify the virtualisation milestones in this above evolution and explain them briefly.

1. 1972 first VM architected by IBM to provide full VM of mainframe machine.
2. 1997 Virtual PC for Mac by Connectix.
3. 1999 VMware's VMware Virtual Platform.
4. 2003 Open Source hypervisor Xen.
5. 2005 VMware Player.
6. 2007 VirtualBox.

## Week 4

[11.0] [5 points] You are asked to store data about music albums in a DynamoDB table. For each album, you need to record the title of the album and the artist name. Describe the commands you would use to create a table to store such information and write an entry to that table in DynamoDB.

[12.0] [5 points] Describe how S3 handles consistency of objects and how this approach affects the state of objects when they are read using a GET.

1. Eventually consistent. When we GET an unversioned request likely receives the last version but this is not guaranteed depending on propagation delays.

[13.0] [5 points] What are the core components of DynamoDB

1. tables
2. items
3. attributes

[14.0] [5 points] When a Bucket is created, AWS allows the specification of a number of features that can be managed. What are the key properties and features?

Properties:

1. Users with special permissions of Read and Write.
2. Grant public read access to the bucket.

Features:

1. Lifecycle: Transition objects that are infrequently accessed to cold storage.
2. Replication: Automatically copy objects to another bucket in a different region.
3. Analytics: Suggest how to manage objects based on access patterns.
4. Metrics: Stats on operations on objects in the bucket.
5. Inventory: Provide a regular snapshot of contents of bucket.

[15.0] [5 points] We can leave S3 buckets open to public. Is this suitable for a specific application? Why and why not? Justify your answer.

## Week 5

[15] [10 points] An organisation has 5 departments and has separated out each of the IAM users into separate groups using paths following the pattern companybucket/department1/*, companybucket /department2/*, companybucket /department3/* etc.

Their IAM account names follow the pattern user@department1.company.com, user@department2.company.com etc.

You are tasked with securing a bucket that contains a folder for each of 5 departments in an organisation. Only people within a department can write to their own folder. Everyone can read from all folders.  

Discuss the principles that you would use to create a policy that would achieve this objective.

Write the policy as a JSON file that you would use.

Note: you can have individual statements for each department.

[16] [5 points]  What aspects of security does the OSI Security Architecture X.800 standard cover? Which particular components of this standard does AWS Identity and Access Management deal with?

1. Authentication: Assurance that communicating entity is the one claimed.
2. Access Control: Prevention of the unauthorized use of a resource.
3. Data Confidentiality: Protection of data from unauthorized disclosure.
4. Data Integrity: Assurance that data received is as sent by an authorized entity
5. Non-Repudiation: Protection against denial by one of the parties in a communication.
6. Availability: Resource accessible/usable.

AWS IAM deals with 1, 2 and 5.

[17] [5 points] Name 3 of the keys that you would find in a Policy. Explain their role. An example of a key is `Version` that specifies the version of the policy syntax and is normally `"Version": 2012-10-17`.

1. Effect: Use `Allow` or `Deny` to indicate whether the policy allows or denies access.
2. Action: Include a list of actions that the policy allows or denies.
3. Condition: Specify the circumstances under which the policy grants permission.
