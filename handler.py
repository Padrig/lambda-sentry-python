import json
import os
import logging
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

#init Sentry *outside* handler
sentry_sdk.init(
    os.environ['SENTRY_DSN'],
    integrations=[AwsLambdaIntegration()],
    debug=True,
)

def hello(event, context):

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    logger = logging.getLogger('main')
    logger.error('Oops!')

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
