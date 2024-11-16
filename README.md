# lambda_test

Test of https://aws.amazon.com/lambda/.

## Guide

- Do not try to add a custom layer with dependencies, use complete Docker image instead
  - it may help you to avoid weird errors

### Guide
[python-image-istructions](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)


[Howt to test it locally - SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-invoke.html)


Once ou have image ready, you can proceed with the following steps to upload image to AWS ECR and use it in Lambda. (also part of `python-image-istructions` above):

```shell
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 654654291772.dkr.ecr.eu-central-1.amazonaws.com

aws ecr create-repository --repository-name qr-code --region eu-central-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
# repository URL: 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code

docker tag qr-code:0.0.1 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code:latest
docker push 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code:latest

```

Finally create a new Lambda and use the image. Possible from UI

You can go to Lambda > Configuration >  Function URL and enable public access.

`https://dnsqgyxszisbs2vp3nuhrudrp40rrhxy.lambda-url.eu-central-1.on.aws?test=YOUR_TEXT_HERE`