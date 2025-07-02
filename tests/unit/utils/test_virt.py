import pytest
import salt.exceptions

import saltext.virt.utils.virt


def test_virt_key(tmp_path):
    opts = {"pki_dir": f"{tmp_path / 'pki'}"}
    saltext.virt.utils.virt.VirtKey("asdf", "minion", opts)


def test_virt_key_bad_hyper(tmp_path):
    opts = {"pki_dir": f"{tmp_path / 'pki'}"}
    with pytest.raises(salt.exceptions.SaltValidationError):
        saltext.virt.utils.virt.VirtKey("asdf/../../../sdf", "minion", opts)


def test_virt_key_bad_id_(tmp_path):
    opts = {"pki_dir": f"{tmp_path / 'pki'}"}
    with pytest.raises(salt.exceptions.SaltValidationError):
        saltext.virt.utils.virt.VirtKey("hyper", "minion/../../", opts)
