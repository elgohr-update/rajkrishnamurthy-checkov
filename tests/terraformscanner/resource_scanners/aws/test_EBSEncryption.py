import unittest

from checkov.terraformscanner.models.enums import ScanResult
from checkov.terraformscanner.resource_scanners.aws.EBSEncryption import scanner


class TestEBSEncryption(unittest.TestCase):

    def test_failure(self):
        resource_conf =  {'volume_id': ['${aws_ebs_volume.example.id}']}
        scan_result = scanner.scan_resource_conf(conf=resource_conf)
        self.assertEqual(ScanResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf =  {'volume_id': ['${aws_ebs_volume.example.id}'], 'encrypted': [True]}
        scan_result = scanner.scan_resource_conf(conf=resource_conf)
        self.assertEqual(ScanResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()