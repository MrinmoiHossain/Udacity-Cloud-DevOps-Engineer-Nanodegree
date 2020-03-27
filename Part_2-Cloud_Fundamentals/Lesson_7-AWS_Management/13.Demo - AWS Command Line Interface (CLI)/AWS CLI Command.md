# check version
$ aws --version

# look at the EC2 instances running
$ aws ec2 describe-instances

# start ec2 instance using instance id
$ aws ec2 start-instances --instance-ids idNumber

# listen the contents of an S3 bucket
$ aws s3 ls s3://bucketname