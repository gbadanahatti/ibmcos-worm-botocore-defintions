# Introduction

This repository contains scripts that will enhance botocore S3 service definitions to include IBM COS WORM Opertions

# Installation

1. Download and install the botocore version of your choice. Ensure botocore is available universally.
2. Clone this repo.
3. Run the script based on your platform. 
	3a. On your mac
	  sudo python add-worm-constructs-to-botocore.py
	3b. On your windows
	  Install AWS CLI from msi installer
	  Run the cmd prompt as an Administrator
	  python add-worm-costructs-to-botocore.py
	3c. On your linux system
	  sudo python add-worm-constructs-to-botocore.py


After installation, the following functionality will be available:

1. Add a Legal hold
2. Delete a Legal hold.
3. Extend retention.
4. Configure a bucket for retention.
5. Get a bucket's retention configuration
5. List all the legal holds on an object.
7. Put an object with retention.
8. Copy an object with retention.
9. Get metadata of an object that includes retention.

# AWS CLI

AWS CLI delegates all s3api requests to botcore library. When botocore is enhanced, the above operations also become available on the AWS CLI

## AWS CLI Examples

### Put Retention Sub resource on a bucket
aws s3api put-bucket-protection --endpoint <endpoint> --bucket <bucketname> --protection-configuration DefaultRetention={Days=2},MaximumRetention={Days=10},MinimumRetention={Days=1},Status=Retention

### Get Retention Sub resource on a bucket
aws s3api get-bucket-protection --endpoint <endpoint> --bucket <bucketname>

Sample Output
{
    "Status": "COMPLIANCE", 
    "MinimumRetention": {
        "Days": 1
    }, 
    "DefaultRetention": {
        "Days": 2
    }, 
    "MaximumRetention": {
        "Days": 10
    }
}

### Upload an object with retention
aws s3api put-object --endpoint <endpoint> --bucket <bucket name> --key <object key> --retention-period <retention period> --body <filename>

Sample Output
{
    "ETag": "\"ee291792809d07760f68d0ccd4e4cd97\""
}

### Get metadata of an object
aws s3api head-object --endpoint http://10.155.228.111 --profile botocore --bucket botocore3 --key ttt

Sample Output
{
    "AcceptRanges": "bytes", 
    "ContentType": "binary/octet-stream", 
    "LastModified": "Tue, 24 Jul 2018 19:27:12 GMT", 
    "ContentLength": 687, 
    "RetentionPeriod": 86405, 
    "ETag": "\"ee291792809d07760f68d0ccd4e4cd97\"", 
    "RetentionExpirationDate": "Wed, 25 Jul 2018 19:27:17 GMT", 
    "Metadata": {}
}

### Add a legal hold on an object
aws s3api add-legal-hold  --endpoint <endpoint> --bucket <bucketname> --key <objectkey> --retention-legal-hold-id <legalholdid>

### List legal holds on an object
aws s3api list-legal-holds  --endpoint <endpoints> --bucket <bucketname> --key <objectkey> 

Sample Output
{
    "RetentionPeriod": 86405, 
    "LegalHolds": [
        {
            "Date": "Tue, 24 Jul 2018 19:34:08 GMT", 
            "ID": "abcdef"
        }
    ], 
    "CreateTime": "Tue, 24 Jul 2018 19:27:12 GMT", 
    "RetentionPeriodExpirationDate": "Wed, 25 Jul 2018 19:27:17 GMT"
}

### Delete legal hold on an object
aws s3api delete-legal-hold  --endpoint <endpoint>  --bucket <bucketname> --key <objectkey> --retention-legal-hold-id <legalholdid>

### Extending object retention
aws s3api extend-object-retention  --endpoint <endpoint>  --bucket <bucketname> --key <objectkey> --new-retention-period <newretentionperiod>

