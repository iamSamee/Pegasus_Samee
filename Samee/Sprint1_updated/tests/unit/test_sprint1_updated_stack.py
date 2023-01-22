import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint1_updated.sprint1_updated_stack import Sprint1UpdatedStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint1_updated/sprint1_updated_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint1UpdatedStack(app, "sprint1-updated")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
