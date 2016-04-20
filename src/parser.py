import os
from lxml import html
import re


class Parser:
    def __init__(self):
        self.dir = os.path.dirname(__file__)

    def get_fixture(self, filename):
        """
        Helper method, load fixture files
        :param filename: fixture file name
        :return:
        """
        fixture_path = os.path.join(self.dir, "..", "fixtures", filename)
        fh = open(fixture_path)
        return fh.read()

    def fixture1(self):
        """
        Load first fixture
        :return: content of the html file fixture1
        """
        return self.get_fixture("fixture1.html")

    def fixture2(self):
        """
        Load second fixture
        :return: content of the html file fixture2
        """
        return self.get_fixture("fixture2.html")

    def parse(self, html_string):
        """
        Parse html content, extracting address, suite and postcode
        As a bonus try to extract description as well!

        :param html_string: x=parser.get_fixture('path_to_file/file.html')
        :return: tuple containing address, suite, postcode and description
        """
        rawstring = html.fromstring(html_string)
        content = rawstring.xpath('//div[@class="display_address"]/text()') #search HTML with xpath to locate the right div

        #SUITE
        suitePattern = re.search(r'[Ss]uite[ ]?\d{1,2}', content[0]) #type(content)=list -> take the 1st element
        if suitePattern == None:
            suite = None
        else:
            suite = suitePattern.group(0)

        #POSTCODE
        postcodePattern = re.search(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', content[0])
        if postcodePattern == None:
            postcode = None
        else:
            postcode = postcodePattern.group(0)

        #ADDRESS
        addressPattern = re.sub(r'[Ss]uite[ ]?\d{1,2}', '', content[0]) #removes the "suite xx" part
        addressPattern = re.sub(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', '', addressPattern) #removes the postcode
        addressPattern = addressPattern.strip() #removes spaces at the beginning and at the end
        addressPattern = re.sub(r'\W$', '', addressPattern) #removes "," at the end
        if addressPattern == None:
            address = None
        else:
            address = addressPattern

        # BONUS
        description = None

        return (address, suite, postcode, description)