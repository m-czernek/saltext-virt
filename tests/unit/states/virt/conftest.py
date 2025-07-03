from unittest.mock import MagicMock

import pytest


class LibvirtMock(MagicMock):  # pylint: disable=too-many-ancestors
    """
    Libvirt library mock
    """

    #  pylint: disable-next=invalid-name
    class libvirtError(Exception):
        """
        libvirtError mock
        """

        def __init__(self, msg):
            super().__init__(msg)
            self.msg = msg

        def get_error_message(self):
            return self.msg


@pytest.fixture
def libvirt_mock():
    return LibvirtMock()


@pytest.fixture(params=[True, False], ids=["test", "notest"])
def test(request):
    """
    Run the test with both True and False test values
    """
    return request.param
