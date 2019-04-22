# Trying our Sentry SDK on AWS Lambda Python

Demonstrate how to get Sentry to work with AWS Lambda

## Learnings
- Lambdas sometimes get killed before Sentry request is made
- AwsLambdaIntegration adds blocking calls
- sentry_sdk should be initialized *outside* the handler

```bash
npm install -g serverless
```
```bash
python -m venv venv
source venv/bin/activate #mac, linux
venv/Scripts/activate #windows
npm install

sls deploy

sls deploy -f hello
sls invoke -f hello --log
```