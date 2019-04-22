# Trying our Sentry SDK on AWS Lambda Python

Demonstrate how to get Sentry to work with AWS Lambda

## Learnings
- Lambdas sometimes get killed before Sentry request is made
- AwsLambdaIntegration adds blocking calls
- sentry_sdk should be initialized *outside* the handler

```bash
virtualenv venv
source venv/bin/activate
npm install -g serverless

sls deploy

sls deploy -f hello
sls invoke -f hello --log
```