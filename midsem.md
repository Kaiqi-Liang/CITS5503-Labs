# 2021 Midsemester Test

## Question 1 (5 points)

A car sales company in Australia prepares reports with sales figures daily in PDF format. You are tasked to provide a storage solution using AWS that also allows for these reports to be protected against users accidentally deleting those documents. What storage solution would you use and what would be your approach for preventing unintended user actions? Justify your answer.

    I would use S3 to store the most recent reports which allows the users to access them quickly and have a backup move on Glacier as well as moving older reports there as they're less frequently accessed and it's a much cheaper storage option than S3. In the case of users deleting those documents by accident they can retrive a backup from Glacier which takes longer to access.

## Question 2 (5 points)

The Data Science Club (DSC) at UWA launched a website with basic information about the club, information about upcoming events organised by the club, and a system to buy tickets for those events. The events organised by the club are very popular among the students and tickets for the events are usually sold out after few hours of being released. To create the website, the organisers of DSC used a single EC2 instance nano in AWS. For the first month, the performance of the website seems to be optimal. However, DSC members noticed that every time they announce a new event, the website response gets slower during the next few hours until it finally crashes.

### a) (2 points)

Explain briefly what is the most likely reason for the website to crash.

    When they announce a new event the tickets are usually sold out in the first hour which means a lot of people are on the ticketing system at the same time making requests to the server. Just a single EC2 instance nano will not be able to handle that spikes without auto-scaling.

### b) (3 points)

Describe the concepts of vertical and horizontal scale. Give 2 examples in which you could help the Data Science Club to scale their website.

    Vertical scale is increasing the hardware configuration by adding more physical resources. Horizontal scale is adding more machines with similar hardware specification. One example is to scale the EC2 instance type from nano to something more powerful. The other is add more EC2 instances.

## Question 3 (5 points)

Describe what virtualisation is and describe the characteristic attributes of the different types of virtualisation (Language, Operating System and Hardware).

## Question 4 (5 points)

Describe what containers are with reference to Docker and discuss their similarities and differences from operating system virtualisation perspective as provided by VirtualBox.

## Question 5 (5 Points)

What is DynamoDB? (1 points) What are DynamoDB main features and its core components? (4 points)

A NoSQL database which is non relational and stores data as key value pairs in tables. It has built-in replication, automatic indexing and stronger consistency guarantees than S3. It is highly scalable.

## Question 6 (5 points)

You are presented with the IAM policy below. Explain what Version, Statement, Effect, Action, Resource, and Conditions are. Provide a brief explanation of what this policy does.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ec2:StartInstances",
                "ec2:RunInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": "ap-southeast-2"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": [
                "ec2:StartInstances",
                "ec2:RunInstances"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:instance/*"
            ],
            "Condition": {
                "StringNotLike": {
                    "ec2:InstanceType": [
                        "t2.small",
                        "t2.micro",
                        "t2.nano"
                    ]
                }
            }
        }
    ]
}
```

    Version: Specify the version of the policy language.
    Statement: The container for the main policy elements.
    Effect: Use Allow or Deny to indicate whether the policy allows or denies access.
    Action: A list of actions that the policy allows or denies.
    Resource: A list of resources to which the actions apply.
    Conditions: Specify the circumstances under which the policy grants permission.
    This policy prevents starting and running any EC2 instance that is not of type "t2.small", "t2.micro" or "t2.nano" in any region that is not "ap-southeast-2"
