import unittest
from xmljsonconverter import XMLJSONConverter
from collections import OrderedDict
import xmltodict

class Json2XmlTest(unittest.TestCase):
    def test_xmljsonconv(self):
        """ Testing the generated xml data
        using xmltodict module which returns
        dictionary of OrderedDict type on
        xml input
        """
        xmldata = XMLJSONConverter()
        xmldata.convertJSONtoXML('input.json','output.xml')
        with open('output.xml','r') as f:
            data = f.read().replace("\n","").replace("\t","")
            udict = xmltodict.parse(data)
            self.assertTrue(type(udict) == OrderedDict)


if __name__ == '__main__':
    unittest.main()
