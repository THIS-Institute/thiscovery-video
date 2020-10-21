#
#   Thiscovery API - THIS Institute’s citizen science platform
#   Copyright (C) 2019 THIS Institute
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   A copy of the GNU Affero General Public License is available in the
#   docs folder of this project.  It is also available www.gnu.org/licenses/
#
import local.dev_config  # sets env variable 'TEST_ON_AWS'
import os
import unittest

import thiscovery_dev_tools.testing_tools as test_tools
from src.common.constants import STACK_NAME
from thiscovery_lib.lambda_utilities import Lambda


class MiscTestCase(test_tools.BaseTestCase):

    @unittest.skipUnless(os.environ['TEST_ON_AWS'] == 'True', 'Invokes lambda on AWS')
    def test_01_raise_error(self):
        lambda_client = Lambda(stack_name=STACK_NAME)
        response = lambda_client.invoke(
            function_name='RaiseError'
        )
        self.assertNotIn('FunctionError', response.keys())
        self.assertEqual(list(), response['Payload'])
