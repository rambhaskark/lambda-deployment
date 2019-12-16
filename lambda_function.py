import json

print('Loading function...')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    # print("value1 => " + event['body'])
    a = eval(event['body'])
    # print ("value1 => " + a['key1'])
    # print("value2 => " + a['key2'])
    # print("value3 => " + a['key3'])
    return {
        'statusCode': 200,
        'body': json.dumps('Greeting Message:' + a['key1'] + ' ' + a['key2'] + ' ' + a['key3'])
    }
    # return ( a['key1'] + ' ' + a['key2'] + ' ' + a['key3'] ) # Echo back the key values
    #raise Exception('Something went wrong')
