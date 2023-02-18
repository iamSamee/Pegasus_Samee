from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    # aws_sqs as sqs,
)
from constructs import Construct

class TestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        hw_lambda = self.create_lambda("MyFirstLambda", 'hw_lambda.lambda_handler', './resources')
        # example resource
        # queue = sqs.Queue(
        #     self, "TestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        
    def create_lambda(self, id_, handler, path):
        lambda_.Function(self, id_,
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler=handler,
            code=lambda_.Code.from_asset(path))
        