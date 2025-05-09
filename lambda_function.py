import json
import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            # First level: parse SQS record body
            outer_message = json.loads(record['body'])
            print("Outer SNS message:", outer_message)

            # Second level: parse 'Message' field from SNS payload
            message = json.loads(outer_message['Message'])
            print("Parsed order message:", message)

            # Save to DynamoDB
            table.put_item(Item={
                'orderId': message['orderId'],
                'userId': message['userId'],
                'itemName': message['itemName'],
                'quantity': int(message['quantity']),
                'status': message['status'],
                'timestamp': message['timestamp']
            })

            print(f"Order {message['orderId']} saved to DynamoDB.")

        except Exception as e:
            print("Error processing record:", record)
            print("Exception:", e)
            raise e

    return {
        'statusCode': 200,
        'body': 'Processed messages.'
    }
