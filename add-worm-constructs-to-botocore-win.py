import os
import json
import shutil


for root,dirs,files in os.walk("C:\\Program Files\\Amazon\\AWSCLI\\botocore\\data\\s3\\2006-03-01"):
            servicePath  = root + "\service-2.json"
            print ("Processing " + servicePath)
            serviceContents = open(servicePath)
            serviceContentsJson = json.load(serviceContents)

            ###
            #Add NEW WORM Operations
            ###

            serviceContentsJson['operations']['AddLegalHold'] = { \
              "name": "AddLegalHold",
              "http": {
                "method":"POST",
                "requestUri":"/{Bucket}/{Key+}?legalHold&add={RetentionLegalHoldId}"
              },
              "input":{"shape":"LegalHoldRequest"},
              "documentation": "Add a legal hold on an object. The legal hold identifiers are stored in the object metadata along with the timestamp of when they are POSTed to the object. The presence of any legal hold identifiers prevents the modification or deletion of the object data, even if the retention period has expired. The presence of a retention period header is required, otherwise a 400 error is returned."
            }
            serviceContentsJson['operations']['DeleteLegalHold'] = { \
              "name": "DeleteLegalHold",
              "http": {
                "method":"POST",
                "requestUri":"/{Bucket}/{Key+}?legalHold&remove={RetentionLegalHoldId}"
              },
              "input":{"shape":"LegalHoldRequest"},
              "documentation": "Remove Legal hold on an object. The legal hold identifiers are stored in the object metadata along with the timestamp of when they are POSTed to the object. The presence of any legal hold identifiers prevents the modification or deletion of the object data, even if the retention period has expired. The presence of a retention period header is required, otherwise a 400 error is returned."
            }
            serviceContentsJson['operations']['ExtendObjectRetention'] = {
               "name": "ExtendObjectRetention",
                "http":{
                  "method": "POST",
                   "requestUri": "/{Bucket}/{Key+}?extendRetention"
                 },
                "input": {"shape": "ExtendObjectRetentionRequest"},
                "documentation": "This implementation of the POST operation uses the extendRetention sub-resource to extend the retention period of a protected object in a protected vault."
            }
            serviceContentsJson['operations']['GetBucketProtection']  = {
                "name":"GetBucketProtection",
                "http":{
                    "method":"GET",
                    "requestUri":"/{Bucket}?protection"
                },
                "input":{"shape":"GetBucketProtectionRequest"},
                "output":{"shape":"ProtectionConfigurationOutput"},
                "documentation":"Returns the lifecycle configuration information set on the bucket."
            }
            serviceContentsJson['operations']['ListLegalHolds'] = {
                "name":"ListLegalHolds",
                "http": {
                    "method": "GET",
                    "requestUri": "/{Bucket}/{Key+}?legalHold"
                },
                "input":{"shape": "ListLegalHoldsRequest"},
                "output":{"shape": "ListLegalHoldsOutput"},
                "documentation": "Returns a list of legal holds on an object"
            }
            serviceContentsJson['operations']['PutBucketProtection']  = {
                "name":"PutBucketProtection",
                "http":{
                    "method":"PUT",
                    "requestUri":"/{Bucket}?protection"
                },
                "input":{"shape":"PutBucketProtectionRequest"},
                "documentation":"Sets protection configuration on the bucket. If a protection configuration exists, it replaces it."
            }

            ###
            #Add New Shapes
            ###


            serviceContentsJson['shapes']['ExtendObjectRetentionRequest'] = {
                  "type":"structure",
                  "required":[
                    "Bucket",
                    "Key"
                  ],
                  "members":{
                    "Bucket":{
                      "shape":"BucketName",
                      "location":"uri",
                      "locationName":"Bucket"
                    },
                    "Key":{
                      "shape":"ObjectKey",
                      "location":"uri",
                      "locationName":"Key"
                    },
                    "AdditionalRetentionPeriod": {
                      "shape": "Additional-Retention-Period",
                      "location": "header",
                      "locationName": "Additional-Retention-Period"
                    },
                    "NewRetentionPeriod": {
                      "shape": "New-Retention-Period",
                      "location": "header",
                      "locationName": "New-Retention-Period"
                    },
                    "NewRetentionDate": {
                      "shape": "New-Retention-Date",
                      "location": "header",
                      "locationName": "New-Retention-Date"
                    }
                  },
                  "documentation":"Container for making extensions to object retention"
            }
            serviceContentsJson['shapes']['Additional-Retention-Period'] = {"type": "integer"}
            serviceContentsJson['shapes']['DefaultRetention']  = {
                  "type": "structure",
                  "members": {
                  "Days": {
                    "shape": "RetentionDays"
                    }
                  },
                  "documentation":"Default retention period for an object in days."
            }
            serviceContentsJson['shapes']['GetBucketProtectionRequest']  = {
              "type":"structure",
              "required":["Bucket"],
              "members":{
                "Bucket":{
                  "shape":"BucketName",
                  "location":"uri",
                  "locationName":"Bucket"
                }
              }
            }
            serviceContentsJson['shapes']['LegalHolds']  = {
                  "type": "list",
                  "member": {
                      "shape":"LegalHold"
                  }
                }
            serviceContentsJson['shapes']['LegalHold'] = {
                  "type": "structure",
                  "members": {
                    "ID":{
                      "shape": "LegalHoldID"
                    },
                    "Date": {
                      "shape": "Date"
                    }
                  }
                }
            serviceContentsJson['shapes']['LegalHoldID'] =  {"type": "string"}
            serviceContentsJson['shapes']['LegalHoldRequest'] = {
                 "type": "structure",
                  "required":["Bucket", "Key"],
                  "members":{
                    "Bucket": {
                      "shape": "BucketName",
                      "location": "uri",
                      "locationName":"Bucket"
                    },
                    "Key":{
                      "shape":"ObjectKey",
                      "location":"uri",
                      "locationName":"Key"
                    },
                    "RetentionLegalHoldId":{
                      "shape": "Retention-Legal-Hold-ID",
                      "location": "uri"
                    }
                  }
                }
            serviceContentsJson['shapes']['Legal-Hold-Operation'] = {"type": "string"}
            serviceContentsJson['shapes']['ListLegalHoldsOutput'] = {
                  "type": "structure",
                  "members": {
                    "CreateTime":{
                      "shape": "Date"
                    },
                    "RetentionPeriod":{
                      "shape": "Retention-Period"
                    },
                    "RetentionPeriodExpirationDate":{
                      "shape": "Retention-Expiration-Date"
                    },
                    "LegalHolds":{
                      "shape": "LegalHolds"
                    }
                  }
                }
            serviceContentsJson['shapes']['ListLegalHoldsRequest'] = {
                  "type": "structure",
                  "required":["Bucket", "Key"],
                  "members":{
                    "Bucket": {
                      "shape": "BucketName",
                      "location": "uri",
                      "locationName":"Bucket"
                    },
                    "Key":{
                      "shape":"ObjectKey",
                      "location":"uri",
                      "locationName":"Key"
                    }
                  }
                }
            serviceContentsJson['shapes']['MaximumRetention'] = {
                 "type": "structure",
                 "members": {
                 "Days": {
                        "shape": "RetentionDays"
                    }
                 },
                 "documentation":"Maximum retention period for an object in days"
                }
            serviceContentsJson['shapes']['MinimumRetention'] = {
                "type": "structure",
                "members": {
                "Days": {
                "shape": "RetentionDays"
                    }
                },
                "documentation":"Minimum Retention period in days"
                }
            serviceContentsJson['shapes']['New-Retention-Period'] = {
                "type": "integer",
                "documentation": "Retention period, in seconds, to use for the object in place of the existing retention period stored for the object. If this value is less than the existing value stored for the object, a 400 error will be returned. If this field and Additional-Retention-Period and/or New-Retention-Date are specified, a 400 error will be returned. If none of the Request Headers are specified, a 400 error will be returned."
                }
            serviceContentsJson['shapes']['New-Retention-Date'] = {"type":"timestamp","timestampFormat":"iso8601"}
            serviceContentsJson['shapes']['ProtectionConfiguration'] = {
                 "type": "structure",
                 "members" : {
                    "Status": {
                      "shape":"ProtectionStatus",
                      "location": "ProtectionStatus"
                    },
                    "MinimumRetention": {
                      "shape": "MinimumRetention",
                      "location": "MinimumRetention"
                    },
                    "DefaultRetention": {
                      "shape": "DefaultRetention",
                      "location": "DefaultRetention"
                    },
                    "MaximumRetention": {
                      "shape": "MaximumRetention",
                      "location": "MaximumRetention"
                    }
                  },
                  "documentation": "Container for describing the retention state of the bucket"
                }
            serviceContentsJson['shapes']['ProtectionConfigurationOutput'] = {
                  "type": "structure",
                  "members" : {
                    "Status": {
                      "shape":"ProtectionStatus"
                    },
                    "MinimumRetention": {
                      "shape": "MinimumRetention"
                    },
                    "DefaultRetention": {
                      "shape": "DefaultRetention"
                    },
                    "MaximumRetention": {
                      "shape": "MaximumRetention"
                    }
                  },
                  "documentation":"Container for describing retention state of the bucket"
                }
            serviceContentsJson['shapes']['ProtectionStatus'] = {
                  "type": "string",
                  "documentation":"Status of protection for the bucket"
                }
            serviceContentsJson['shapes']['PutBucketProtectionRequest'] = {
                  "type":"structure",
                  "required":["Bucket"],
                  "members":{
                    "Bucket":{
                      "shape":"BucketName",
                      "location":"uri",
                      "locationName":"Bucket"
                      },
                  "ProtectionConfiguration" : {
                  "shape":"ProtectionConfiguration",
                  "locationName":"ProtectionConfiguration",
                  "xmlNamespace":{"uri":"http://s3.amazonaws.com/doc/2006-03-01/"}
                    }
                  },
                  "payload":"ProtectionConfiguration"
            }
            serviceContentsJson['shapes']['RetentionDays'] = {"type": "integer"}
            serviceContentsJson['shapes']['Retention-Period'] = {
                  "type": "integer",
                  "documentation":"Retention period to store on the object in seconds. The object can be neither overwritten nor deleted until the amount of time specified in the retention period has elapsed. If this field and Retention-Expiration-Date are specified a 400 error is returned. If neither is specified the bucket's DefaultRetention period will be used. 0 is a legal value assuming the bucket's minimum retention period is also 0."
            }
            serviceContentsJson['shapes']['Retention-Expiration-Date'] = {"type":"timestamp","timestampFormat":"iso8601"}
            serviceContentsJson['shapes']['Retention-Legal-Hold-ID'] = {"type": "string"}
            serviceContentsJson['shapes']['Retention-Legal-Hold-Count'] = {"type": "integer"}
            serviceContentsJson['shapes']['Retention-Directive'] = {"type": "string", "enum":["COPY","REPLACE"]}

            ###
            #Modifiy Shapes
            ###
            serviceContentsJson['shapes']['PutObjectRequest']['members']['RetentionPeriod'] = {
                      "shape": "Retention-Period",
                      "documentation": "Retention period to store on the object in seconds. If this field and Retention-Expiration-Date are specified a 400 error is returned. If neither is specified the bucket's DefaultRetention period will be used. 0 is a legal value assuming the bucket's minimum retention period is also 0.",
                      "location": "header",
                      "locationName": "Retention-Period"
                    }
            serviceContentsJson['shapes']['PutObjectRequest']['members']['RetentionExpirationDate'] = {
                      "shape": "Retention-Expiration-Date",
                      "documentation": "Date on which it will be legal to delete or modify the object. You can only specify this or the Retention-Period header. If both are specified a 400 error will be returned. If neither is specified the bucket's DefaultRetention period will be used. This header should be used to calculate a retention period in seconds and then stored in that manner.", \
                      "location": "header",
                      "locationName": "Retention-Expiration-Date"
                    }
            serviceContentsJson['shapes']['PutObjectRequest']['members']['RetentionLegalHoldId'] = {
                      "shape": "Retention-Legal-Hold-ID",
                      "documentation": "A single legal hold to apply to the object. A legal hold is a Y character long string. The object cannot be overwritten or deleted until all legal holds associated with the object are removed.",
                      "location": "header",
                      "locationName": "Retention-Legal-Hold-ID"
                  }
            serviceContentsJson['shapes']['CopyObjectRequest']['members']['Retention-Directive'] = {
                    "shape": "Retention-Directive",
                    "documentation": "This header controls how the Protection state of the source object is copied to the destination object.If copied, the retention period and all legal holds are copied onto the new object. The legal hold date's is set to the date of the copy.",
                    "location": "header",
                    "locationName":"Retention-Directive"
                    }
            serviceContentsJson['shapes']['CopyObjectRequest']['members']['RetentionPeriod']  = {
                    "shape": "Retention-Period",
                    "documentation": "Retention period to store on the object in seconds. If this field and Retention-Expiration-Date are specified a 400 error is returned. If neither is specified the bucket's DefaultRetention period will be used. 0 is a legal value assuming the bucket's minimum retention period is also 0.",
                    "location": "header",
                    "locationName": "Retention-Period"
                 }
            serviceContentsJson['shapes']['CopyObjectRequest']['members']['RetentionExpirationDate'] = {
                    "shape": "Retention-Expiration-Date",
                    "documentation": "Date on which it will be legal to delete or modify the object. You can only specify this or the Retention-Period header. If both are specified a 400 error will be returned. If neither is specified the bucket's DefaultRetention period will be used. This header should be used to calculate a retention period in seconds and then stored in that manner.",
                    "location": "header",
                    "locationName": "Retention-Expiration-Date"
                 }
            serviceContentsJson['shapes']['CopyObjectRequest']['members']['RetentionLegalHoldId'] = {
                    "shape": "Retention-Legal-Hold-ID",
                    "documentation": "A single legal hold to apply to the object. A legal hold is a Y character long string. The object cannot be overwritten or deleted until all legal holds associated with the object are removed.",
                    "location": "header",
                    "locationName": "Retention-Legal-Hold-ID"
                }
            serviceContentsJson['shapes']['HeadObjectOutput']['members']['RetentionPeriod'] = {
                    "shape": "Retention-Period",
                    "documentation": "Retention period to store on the object in seconds. If this field and Retention-Expiration-Date are specified a 400 error is returned. If neither is specified the bucket's DefaultRetention period will be used. 0 is a legal value assuming the bucket's minimum retention period is also 0.",
                    "location": "header", \
                    "locationName": "Retention-Period"
                }
            serviceContentsJson['shapes']['HeadObjectOutput']['members']['RetentionExpirationDate'] = {
                          "shape": "Retention-Expiration-Date",
                          "documentation": "Date on which it will be legal to delete or modify the object. You can only specify this or the Retention-Period header. If both are specified a 400 error will be returned. If neither is specified the bucket's DefaultRetention period will be used. This header should be used to calculate a retention period in seconds and then stored in that manner.",
                          "location": "header",
                          "locationName": "Retention-Expiration-Date"
                        }
            serviceContentsJson['shapes']['HeadObjectOutput']['members']['RetentionLegalHoldCount']  = {
                          "shape": "Retention-Legal-Hold-Count",
                          "documentation": "Returns the count of legal holds on the object. If there are no legal holds, the header is not returned",
                          "location": "header",
                          "locationName": "Retention-Legal-Hold-Count"
                        }

            outputContents = json.dumps(serviceContentsJson, indent=4, sort_keys=True,
                      separators=(',', ': '))

            ###
            #Make a copy of the original service definition and write new service file
            ###

            dstFile = root + "\service-2.json.bak"
            print ("Backing up the old service definition before overwriting..")
            shutil.copy(servicePath, dstFile)
            f = open(servicePath, 'w')
            f.write(outputContents)
            print ("New WORM service defitions are now available.")
