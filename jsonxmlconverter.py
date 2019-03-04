#!/usr/bin/env python3

"""
.. module:: xmljsonconverteri

   This module provides a conversion tool for converting from JSON to XML.
"""

import  json
import argparse
class XMLJSONConverter():
    """
    .. class:: XMLJSONConverter()

    This class provides a conversion tool for converting from JSON
    files to XML.
    """

    def convertJSONtoXML(self, json_file, xml_file):
        """
        .. method:: convertJSONtoXML(json_file, xml_file)

        This method converts the JSON in the given file to the XML and
        outputs to the given file.

        The implementer of this method is responsible for opening both
        files, reading from the JSON file and writing to the XML
        file. He must ensure that all the proper error handling is
        performed.

        :param str json_file: A string representing a file path to a
                              JSON file.
        :param str xml_file: A string representing a file path to
                            output XML after converting it from the
                            given JSON file
        :returns: None
        :rtype: NoneType
        """
        ## Todo: Implement this method
        try:

            xml_list = list()
            global level
            self.json_file = json_file
            self.xml_file = xml_file
            level = 0
            indent = " " * level
            with open(self.json_file,'r') as f:
                data = f.read()
                json_data = json.loads(data)

                xml_list.append("<object>")

                def jsonToxml(data):
                    """recursively call the jsonToxml function
                    if value of the element is array(list) or
                    object(dictionary)
                    """

                    global level
                    global indent

                    if isinstance(data, type({})):

                        level += 4
                        indent = " " * level

                        for ind,key in enumerate(data):

                            val = data[key]

                            if isinstance(val, type({})) or isinstance(val, type([])):

                                if isinstance(val,type({})):

                                    xml_list.append("{}<object name=\"{}\">".format(indent,key))

                                elif isinstance(val,type([])):
                                    xml_list.append("{}<array name=\"{}\">".format(indent,key))

                                jsonToxml(val)


                            elif isinstance(val,str):
                                xml_list.append("{}<string name=\"{}\">{}</string>".format(indent,key,val))

                            elif isinstance(val,int) and not isinstance(val,bool):
                                xml_list.append("{}<number name=\"{}\">{}</number>".format(indent,key,val))

                            elif isinstance(val,float):
                                xml_list.append("{}<number name=\"{}\">{:.1f}</number>".format(indent,key,val))

                            elif val is None:
                                xml_list.append("{}<null name=\"{}\"/>".format(indent,key))

                            elif isinstance(val,bool):
                                xml_list.append("{}<boolean name=\"{}\">{}</boolean>".format(indent,key,val))


                            if ind == len(data) - 1:
                                level -= 4
                                indent = " " * level
                                xml_list.append("{}</object>".format(indent))

                    elif isinstance(data, type([])):
                        level += 4
                        indent = " " * level

                        for ind in range(len(data)):
                            elem = data[ind]

                            if isinstance(elem, type({})) or isinstance(elem, type([])):

                                if isinstance(elem,type([])):
                                    xml_list.append("{}<array>".format(indent))
                                elif isinstance(elem,type({})):
                                    xml_list.append("{}<object>".format(indent))
                                jsonToxml(elem)

                            else:
                                if isinstance(elem,str):
                                    xml_list.append("{}<string>{}</string>".format(indent,elem))
                                elif isinstance(elem,float):
                                    xml_list.append("{}<number>{:.1f}</number>".format(indent,elem))
                                elif isinstance(elem,int):
                                    xml_list.append("{}<number>{}</number>".format(indent,elem))
                                elif elem is None:
                                    xml_list.append("{}<null/>".format(indent))
                                elif isinstance(elem,bool):
                                    xml_list.append("{}<boolean>{}</boolean>".format(indent,elem))

                            if ind == len(data) - 1:
                                level -= 4
                                indent = " " * level
                                xml_list.append("{}</array>".format(indent))


                jsonToxml(json_data)

                result = "\n".join(xml_list)

                with open(self.xml_file,'w') as f:
                    f.write(result)

                return

        except ValueError as VE:
            print("Error: The input file is not a valid json: {}".format(VE))

        except IOError as IOR:
            print("I/O error: {}".format(IOR))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(dest="json_file")
    parser.add_argument(dest="xml_file")
    args = parser.parse_args()

    xml_obj = XMLJSONConverter()
    xml_obj.convertJSONtoXML(args.json_file,args.xml_file)


if __name__ == "__main__":
    main()
