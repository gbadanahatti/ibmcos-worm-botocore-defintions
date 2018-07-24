# Introduction

This repository contains scripts that will enhance botocore S3 service definitions to include IBM COS WORM Opertions

# Installation

1. Download and install the botocore version of your choice. Ensure botocore is available universally.
2. Clone this repo.
3. Run the script based on your platform.

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

#AWS CLI

AWS CLI delegates all s3api requests to botcore library. When botocore is enhanced, the above operations also become available on the AWS CLI
 
