import boto3, json, typing

def invokeLambdaFunction(*, functionName:str=None, payload:typing.Mapping[str, str]=None):
    if  functionName == None:
        raise Exception('ERROR: functionName parameter cannot be NULL')
    payloadStr = json.dumps(payload)
    payloadBytesArr = bytes(payloadStr, encoding='utf8')
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=functionName,
        InvocationType="RequestResponse",
        Payload=payloadBytesArr
    )
    return response


list_of_function_names = ["collecting_cases",
                            "collecting_patient_info", 
                            "collecting_region_info",
                            "collecting_searchtrend_info", 
                            "collecting_time", 
                            "collecting_time_age",
                            "collecting_time_gender", 
                            "collecting_time_provience", 
                            "collecting_weather_info", 
                            "collecting_schemeless_info"
                    
                        ]

for func in list_of_function_names:
    payloadObj = {"something" : "1111111-222222-333333-bba8-1111111"}
    res = invokeLambdaFunction(functionName = func , payload = payloadObj )
    print(func , " is stored in DynamoDB")