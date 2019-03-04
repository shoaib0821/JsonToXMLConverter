# JsonToXMLConverter



A python utility to convert JSON to XML(supports 3.x versions). It accepts two arguments with the python script.
The first argument is path to the json file with file name and second argument is path to the xml file with filename.
The coverted xml output has indentation of 4 spaces.

installation:

please install xmltodict library for the unit testing of the code.

pip install xmltodict



How to Run project/Usage:

From the command line run the below command with arguments

python3 xmljsonconverter.py jsonfile xmlfile


Modules used in the project:

json - used to load the json data from the file to python dictionary

argparse - parser to parse the command line arguments

xmltodict - library converts the xml data to python dictionary(to test the generated xml data)


Test python scripts:

Have added testXmltoJson.py script for the unit testing of the code
