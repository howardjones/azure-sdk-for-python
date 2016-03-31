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


class NodeRebootParameter(Model):
    """
    Parameters for a ComputeNodeOperations.Reboot request.

    :param node_reboot_option: Sets when to reboot the compute node and what
     to do with currently running tasks. The default value is requeue.
     Possible values include: 'requeue', 'terminate', 'taskcompletion',
     'retaineddata'
    :type node_reboot_option: str
    """ 

    _attribute_map = {
        'node_reboot_option': {'key': 'nodeRebootOption', 'type': 'ComputeNodeRebootOption'},
    }

    def __init__(self, node_reboot_option=None, **kwargs):
        self.node_reboot_option = node_reboot_option
