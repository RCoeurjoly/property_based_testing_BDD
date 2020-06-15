from behave import given, when, then, step
from hypothesis import given as given_PBT
from hamcrest import assert_that, equal_to
from hypothesis.strategies import integers

@given('I have any integer')
def step_impl(context):
    pass

@when('we multiply it by zero')
def step_impl(context):
    pass

@then('we should get a zero')
def step_impl(context):
    @given_PBT(integers())
    def test_multiply(my_integer):
        print("Multiplying " + str(my_integer) + " with zero")
        assert_that(my_integer*0, equal_to(0))
    test_multiply()
