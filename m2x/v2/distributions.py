from m2x.v2.resource import Resource
from m2x.v2.metadata import Metadata
from m2x.v2.devices import Device

class DistributionDevice(Device):
    COLLECTION_PATH = 'distributions/{distribution_id}/devices'

class Distribution(Resource, Metadata):
    """ Wrapper for AT&T M2X `Distribution API <https://m2x.att.com/developer/documentation/v2/distribution>`_
    """
    COLLECTION_PATH = 'distributions'
    ITEM_PATH = 'distributions/{id}'
    ITEMS_KEY = 'distributions'

    def devices(self, **params):
        """ Method for `List Devices from an existing Distribution <https://m2x.att.com/developer/documentation/v2/distribution#List-Devices-from-an-existing-Distribution>`_ endpoint.

        :param params: Query parameters passed as keyword arguments. View M2X API Docs for listing of available parameters.

        :return: List of Devices associated with this Distribution as :class:`.DistributionDevice` objects
        :rtype: `list <https://docs.python.org/2/library/functions.html#list>`_

        :raises: :class:`~requests.exceptions.HTTPError` if an error occurs when sending the HTTP request
        """
        return DistributionDevice.list(self.api, distribution_id=self.id, **params)

    def add_device(self, serial):
        """ Method for `Add Device to an Existing Distribution <https://m2x.att.com/developer/documentation/v2/distribution#Add-Device-to-an-existing-Distribution>`_ endpoint.

        :param serial: The unique (account-wide) serial for the DistributionDevice being added to the Distribution

        :return: The newly created DistributionDevice
        :rtype: DistributionDevice

        :raises: :class:`~requests.exceptions.HTTPError` if an error occurs when sending the HTTP request
        """
        return DistributionDevice.create(self.api, distribution_id=self.id,
                                         serial=serial)
