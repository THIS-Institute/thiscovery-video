# add/edit your dev configuration parameters here
import os

SECRETS_NAMESPACE = '/hello/'
UNIT_TEST_NAMESPACE = '/world/'

# Settings for tests
# TEST_ON_AWS = False
TEST_ON_AWS = True

os.environ['TEST_ON_AWS'] = str(TEST_ON_AWS)
os.environ['SECRETS_NAMESPACE'] = SECRETS_NAMESPACE
os.environ['UNIT_TEST_NAMESPACE'] = UNIT_TEST_NAMESPACE