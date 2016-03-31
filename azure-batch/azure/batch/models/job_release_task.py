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


class JobReleaseTask(Model):
    """
    A Job Release task to run on job completion on any compute node where the
    job has run.

    :param id: Gets or sets a string that uniquely identifies the Job Release
     task within the job. The id can contain any combination of alphanumeric
     characters including hyphens and underscores and cannot contain more
     than 64 characters.
    :type id: str
    :param command_line: Gets or sets the command line of the Job Release
     task.
    :type command_line: str
    :param resource_files: Gets or sets a list of files that Batch will
     download to the compute node before running the command line.
    :type resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    :param environment_settings: Gets or sets a list of environment variable
     settings for the Job Release task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param max_wall_clock_time: Gets or sets the maximum elapsed time that
     the Job Release task may run on a given compute node, measured from the
     time the task starts. If the task does not complete within the time
     limit, the Batch service terminates it. The default value is 15 minutes.
    :type max_wall_clock_time: timedelta
    :param retention_time: Gets or sets the minimum time to retain the
     working directory for the Job Release task on the compute node.  After
     this time, the Batch service may delete the working directory and all
     its contents. The default is infinite.
    :type retention_time: timedelta
    :param run_elevated: Gets or sets whether to run the Job Release task in
     elevated mode. The default value is false.
    :type run_elevated: bool
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'max_wall_clock_time': {'key': 'maxWallClockTime', 'type': 'duration'},
        'retention_time': {'key': 'retentionTime', 'type': 'duration'},
        'run_elevated': {'key': 'runElevated', 'type': 'bool'},
    }

    def __init__(self, id=None, command_line=None, resource_files=None, environment_settings=None, max_wall_clock_time=None, retention_time=None, run_elevated=None, **kwargs):
        self.id = id
        self.command_line = command_line
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.max_wall_clock_time = max_wall_clock_time
        self.retention_time = retention_time
        self.run_elevated = run_elevated
