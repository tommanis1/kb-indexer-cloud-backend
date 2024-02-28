# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job_configuration import JobConfiguration  # noqa: F401,E501
from swagger_server import util


class Job(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, job_id: str=None, job_configuration: JobConfiguration=None):  # noqa: E501
        """Job - a model defined in Swagger

        :param job_id: The job_id of this Job.  # noqa: E501
        :type job_id: str
        :param job_configuration: The job_configuration of this Job.  # noqa: E501
        :type job_configuration: JobConfiguration
        """
        self.swagger_types = {
            'job_id': str,
            'job_configuration': JobConfiguration
        }

        self.attribute_map = {
            'job_id': 'jobId',
            'job_configuration': 'jobConfiguration'
        }
        self._job_id = job_id
        self._job_configuration = job_configuration

    @classmethod
    def from_dict(cls, dikt) -> 'Job':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Job of this Job.  # noqa: E501
        :rtype: Job
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self) -> str:
        """Gets the job_id of this Job.

        Unique identifier for the job  # noqa: E501

        :return: The job_id of this Job.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: str):
        """Sets the job_id of this Job.

        Unique identifier for the job  # noqa: E501

        :param job_id: The job_id of this Job.
        :type job_id: str
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def job_configuration(self) -> JobConfiguration:
        """Gets the job_configuration of this Job.


        :return: The job_configuration of this Job.
        :rtype: JobConfiguration
        """
        return self._job_configuration

    @job_configuration.setter
    def job_configuration(self, job_configuration: JobConfiguration):
        """Sets the job_configuration of this Job.


        :param job_configuration: The job_configuration of this Job.
        :type job_configuration: JobConfiguration
        """
        if job_configuration is None:
            raise ValueError("Invalid value for `job_configuration`, must not be `None`")  # noqa: E501

        self._job_configuration = job_configuration
