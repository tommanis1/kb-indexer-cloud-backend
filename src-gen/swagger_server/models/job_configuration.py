# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.environment_variable import EnvironmentVariable  # noqa: F401,E501
from swagger_server.models.indexer_configuration import IndexerConfiguration  # noqa: F401,E501
from swagger_server import util


class JobConfiguration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, command: str=None, indexer_configuration: IndexerConfiguration=None, environment_variables: List[EnvironmentVariable]=None, repeat: str=None):  # noqa: E501
        """JobConfiguration - a model defined in Swagger

        :param command: The command of this JobConfiguration.  # noqa: E501
        :type command: str
        :param indexer_configuration: The indexer_configuration of this JobConfiguration.  # noqa: E501
        :type indexer_configuration: IndexerConfiguration
        :param environment_variables: The environment_variables of this JobConfiguration.  # noqa: E501
        :type environment_variables: List[EnvironmentVariable]
        :param repeat: The repeat of this JobConfiguration.  # noqa: E501
        :type repeat: str
        """
        self.swagger_types = {
            'command': str,
            'indexer_configuration': IndexerConfiguration,
            'environment_variables': List[EnvironmentVariable],
            'repeat': str
        }

        self.attribute_map = {
            'command': 'command',
            'indexer_configuration': 'indexerConfiguration',
            'environment_variables': 'environmentVariables',
            'repeat': 'repeat'
        }
        self._command = command
        self._indexer_configuration = indexer_configuration
        self._environment_variables = environment_variables
        self._repeat = repeat

    @classmethod
    def from_dict(cls, dikt) -> 'JobConfiguration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobConfiguration of this JobConfiguration.  # noqa: E501
        :rtype: JobConfiguration
        """
        return util.deserialize_model(dikt, cls)
    
    @classmethod
    def to_dict(self):
            """Converts this instance to a dictionary."""
            result = {}
            for attr, _ in self.swagger_types.items():
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[self.attribute_map[attr]] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[self.attribute_map[attr]] = value.to_dict()
                elif isinstance(value, dict):
                    result[self.attribute_map[attr]] = dict(map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[self.attribute_map[attr]] = value
            return result


    @property
    def command(self) -> str:
        """Gets the command of this JobConfiguration.

        Shell command used to run the job  # noqa: E501

        :return: The command of this JobConfiguration.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command: str):
        """Sets the command of this JobConfiguration.

        Shell command used to run the job  # noqa: E501

        :param command: The command of this JobConfiguration.
        :type command: str
        """

        self._command = command

    @property
    def indexer_configuration(self) -> IndexerConfiguration:
        """Gets the indexer_configuration of this JobConfiguration.


        :return: The indexer_configuration of this JobConfiguration.
        :rtype: IndexerConfiguration
        """
        return self._indexer_configuration

    @indexer_configuration.setter
    def indexer_configuration(self, indexer_configuration: IndexerConfiguration):
        """Sets the indexer_configuration of this JobConfiguration.


        :param indexer_configuration: The indexer_configuration of this JobConfiguration.
        :type indexer_configuration: IndexerConfiguration
        """

        self._indexer_configuration = indexer_configuration

    @property
    def environment_variables(self) -> List[EnvironmentVariable]:
        """Gets the environment_variables of this JobConfiguration.

        Add environment variables for the job  # noqa: E501

        :return: The environment_variables of this JobConfiguration.
        :rtype: List[EnvironmentVariable]
        """
        return self._environment_variables

    @environment_variables.setter
    def environment_variables(self, environment_variables: List[EnvironmentVariable]):
        """Sets the environment_variables of this JobConfiguration.

        Add environment variables for the job  # noqa: E501

        :param environment_variables: The environment_variables of this JobConfiguration.
        :type environment_variables: List[EnvironmentVariable]
        """

        self._environment_variables = environment_variables

    @property
    def repeat(self) -> str:
        """Gets the repeat of this JobConfiguration.

        Optional field for how often the task should repeat (e.g., hourly, daily, weekly)  # noqa: E501

        :return: The repeat of this JobConfiguration.
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat: str):
        """Sets the repeat of this JobConfiguration.

        Optional field for how often the task should repeat (e.g., hourly, daily, weekly)  # noqa: E501

        :param repeat: The repeat of this JobConfiguration.
        :type repeat: str
        """

        self._repeat = repeat
