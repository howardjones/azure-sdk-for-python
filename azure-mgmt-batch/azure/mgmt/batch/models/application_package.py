# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationPackage(Model):
    """
    Contains information about an application package.

    :param version: The version of the application package.
    :type version: str
    :param state: The current state of the application package. Possible
     values include: 'pending', 'active', 'unmapped'
    :type state: str
    :param format: The format of the application package, if known.
    :type format: str
    :param last_activation_time: The time at which the package was last
     activated, if the package is active.
    :type last_activation_time: datetime
    """ 

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'state': {'key': 'state', 'type': 'PackageState'},
        'format': {'key': 'format', 'type': 'str'},
        'last_activation_time': {'key': 'lastActivationTime', 'type': 'iso-8601'},
    }

    def __init__(self, version=None, state=None, format=None, last_activation_time=None, **kwargs):
        self.version = version
        self.state = state
        self.format = format
        self.last_activation_time = last_activation_time
