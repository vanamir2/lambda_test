# lambda_test

Test of https://aws.amazon.com/lambda/.

How to
1. Create a new lambda and use `generate_qr_lambda.py`
2. It won't work as there is no dependency `qrcode` in the lambda environment
   3. Fix it by creating a layer with `qrcode` and `Pillow`
   4. Run and upload it as a new layer (main Lambda menu)
    ```shell
     mkdir -p qr_code_layer/python
     pip install qrcode[pil] Pillow -t qr_code_layer/python
     cd qr_code_layer
     zip -r qr_code_layer.zip python
    ```
   
3. Add the layer to the lambda
4. Enable access to the lambda from the internet

and it fails is it packages dependencies for different OS, not AWS Linux


## Steps again

Prepare folders
```shell
mkdir qr_code_layer
cd qr_code_layer
mkdir python
```

Create a `requirements.txt` file with the following content:

```shell
qrcode[pil]
Pillow
```

Prepare libraries using AWS image
```shell
docker run --rm -v "$(pwd):/var/task" amazonlinux:2 bash -c "
yum install -y python3-pip && \
pip3 install --upgrade pip && \
pip3 install --target /var/task/python -r /var/task/requirements.txt && \
ls -l /var/task/python"
```

Zip it

```shell
zip -r qr_code_layer.zip python

```



## Another attemp

https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions


Howt to test it locally - SAM: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-local-invoke.html



```shell
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 654654291772.dkr.ecr.eu-central-1.amazonaws.com

aws ecr create-repository --repository-name qr-code --region eu-central-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
# repository URL: 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code

docker tag qr-code:0.0.1 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code:latest
docker push 654654291772.dkr.ecr.eu-central-1.amazonaws.com/qr-code:latest

```

Finally create a new Lambda and use the image. Possible from UI