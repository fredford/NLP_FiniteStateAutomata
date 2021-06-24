import re

class Extractor:

    def __init__ (self, dataFile, filename):
        self.dataFile = dataFile    # Data file to be processed
        self.filename = filename    # Name of the file currently being processed
        self.list_results = []      # List of results to be filled by the extractor

    def get_data(self):
        """
        Function used to get the results from the Extractor.

        Arguments:
            None

        Return:
            self.list_results -- List of results produced by running the REs on the data file
        """
        return self.list_results

    def process_data(self):
        """
        Function used to process the data file and and extract data from the text

        Arguments:
            None

        Return:
            None
        """

        text = ''

        for line in self.dataFile:
            text += (line[:-1] + " ")
        text = text[:-1]

        RE_list = []

        ###############################
        #        Simple Dates         #
        ###############################


        # Expression set 1
        # Day Month Year format
        RE_list.append(['(\d{1,2}\sJanuary\s\d{4}|\d{1,2}\sFebruary\s\d{4}|\d{1,2}\sMarch\s\d{4}|\d{1,2}\sApril\s\d{4}|\d{1,2}\sMay\s\d{4}|\d{1,2}\sJune\s\d{4}|\d{1,2}\sJuly\s\d{4}|\d{1,2}\sAugust\s\d{4}|\d{1,2}\sSeptember\s\d{4}|\d{1,2}\sOctober\s\d{4}|\d{1,2}\sNovember\s\d{4}|\d{1,2}\sDecember\s\d{4})', "simple"])

        # Day Month, Year format
        RE_list.append(['(\d{1,2}\sJanuary,\s\d{4}|\d{1,2}\sFebruary,\s\d{4}|\d{1,2}\sMarch,\s\d{4}|\d{1,2}\sApril,\s\d{4}|\d{1,2}\sMay,\s\d{4}|\d{1,2}\sJune,\s\d{4}|\d{1,2}\sJuly,\s\d{4}|\d{1,2}\sAugust,\s\d{4}|\d{1,2}\sSeptember,\s\d{4}|\d{1,2}\sOctober,\s\d{4}|\d{1,2}\sNovember,\s\d{4}|\d{1,2}\sDecember,\s\d{4})', "simple"])

        # Month Day Year format
        RE_list.append(['(January\s[\d]{1,2}\s[\d]{4}|February\s[\d]{1,2}\s[\d]{4}|March\s[\d]{1,2}\s[\d]{4}|April\s[\d]{1,2}\s[\d]{4}|May\s[\d]{1,2}\s[\d]{4}|June\s[\d]{1,2}\s[\d]{4}|July\s[\d]{1,2}\s[\d]{4}|August\s[\d]{1,2}\s[\d]{4}|September\s[\d]{1,2}\s[\d]{4}|October\s[\d]{1,2}\s[\d]{4}|November\s[\d]{1,2}\s[\d]{4}|December\s[\d]{1,2}\s[\d]4})', "simple"])

        # Month Day, Year format
        RE_list.append(['(January\s[\d]{1,2},\s[\d]{4}|February\s[\d]{1,2},\s[\d]{4}|March\s[\d]{1,2},\s[\d]{4}|April\s[\d]{1,2},\s[\d]{4}|May\s[\d]{1,2},\s[\d]{4}|June\s[\d]{1,2},\s[\d]{4}|July\s[\d]{1,2},\s[\d]{4}|August\s[\d]{1,2},\s[\d]{4}|September\s[\d]{1,2},\s[\d]{4}|October\s[\d]{1,2},\s[\d]{4}|November\s[\d]{1,2},\s[\d]{4}|December\s[\d]{1,2},\s[\d]4})', "simple"])

        # Expression set 2
        # Find a range of years

        RE_list.append(['(\d{4}-\d{4})', 'simple'])

        ###############################
        #        Deictic Dates        #
        ###############################

        # Expression set 1
        RE_list.append(['([Yy]esterday|[Tt]oday|[Tt]omorrow|Day|[Ww]eek|[Yy]ear|[Nn]ext\sday|[Nn]ext\sweek|[Nn]ext\smonth|[Nn]ext\syear|[Nn]ext\s[Qq]uarter|[Ll]ast\sday|[Ll]ast\sweek|[Ll]ast\smonth|[Ll]ast\syear|[Ll]ast\s[Qq]uarter|[Pp]revious\sday|[Pp]revious\sweek|[Pp]revious\smonth|[Pp]revious\syear|[Pp]revious\s[Qq]uarter)', "deictic"])


        # Expression set 2
        # Going through each version of month
        RE_list.append(['([Tt]his\sJanuary|[Nn]ext\sJanuary|[Ll]ast\sJanuary|[Pp]revious\sJanuary|[Bb]efore\sJanuary|[Aa]fter\sJanuary|[Pp]rior\sJanuary|[Pp]rior\sto\sJanuary)', "deictic"])
        RE_list.append(['([Tt]his\sFebruary|[Nn]ext\sFebruary|[Ll]ast\sFebruary|[Pp]revious\sFebruary|[Bb]efore\sFebruary|[Aa]fter\sFebruary|[Pp]rior\sFebruary|[Pp]rior\sto\sFebruary)', "deictic"])
        RE_list.append(['([Tt]his\sMarch|[Nn]ext\sMarch|[Ll]ast\sMarch|[Pp]revious\sMarch|[Bb]efore\sMarch|[Aa]fter\sMarch|[Pp]rior\sMarch|[Pp]rior\sto\sMarch)', "deictic"])
        RE_list.append(['([Tt]his\sApril|[Nn]ext\sApril|[Ll]ast\sApril|[Pp]revious\sApril|[Bb]efore\sApril|[Aa]fter\sApril|[Pp]rior\sApril|[Pp]rior\sto\sApril)', "deictic"])
        RE_list.append(['([Tt]his\sMay|[Nn]ext\sMay|[Ll]ast\sMay|[Pp]revious\sMay|[Bb]efore\sMay|[Aa]fter\sMay|[Pp]rior\sMay|[Pp]rior\sto\sMay)', "deictic"])
        RE_list.append(['([Tt]his\sJune|[Nn]ext\sJune|[Ll]ast\sJune|[Pp]revious\sJune|[Bb]efore\sJune|[Aa]fter\sJune|[Pp]rior\sJune|[Pp]rior\sto\sJune)', "deictic"])
        RE_list.append(['([Tt]his\sJuly|[Nn]ext\sJuly|[Ll]ast\sJuly|[Pp]revious\sJuly|[Bb]efore\sJuly|[Aa]fter\sJuly|[Pp]rior\sJuly|[Pp]rior\sto\sJuly)', "deictic"])
        RE_list.append(['([Tt]his\sAugust|[Nn]ext\sAugust|[Ll]ast\sAugust|[Pp]revious\sAugust|[Bb]efore\sAugust|[Aa]fter\sAugust|[Pp]rior\sAugust|[Pp]rior\sto\sAugust)', "deictic"])
        RE_list.append(['([Tt]his\sSeptember|[Nn]ext\sSeptember|[Ll]ast\sSeptember|[Pp]revious\sSeptember|[Bb]efore\sSeptember|[Aa]fter\sSeptember|[Pp]rior\sSeptember|[Pp]rior\sto\sSeptember)', "deictic"])
        RE_list.append(['([Tt]his\sOctober|[Nn]ext\sOctober|[Ll]ast\sOctober|[Pp]revious\sOctober|[Bb]efore\sOctober|[Aa]fter\sOctober|[Pp]rior\sOctober|[Pp]rior\sto\sOctober)', "deictic"])
        RE_list.append(['([Tt]his\sNovember|[Nn]ext\sNovember|[Ll]ast\sNovember|[Pp]revious\sNovember|[Bb]efore\sNovember|[Aa]fter\sNovember|[Pp]rior\sNovember|[Pp]rior\sto\sNovember)', "deictic"])
        RE_list.append(['([Tt]his\sDecember|[Nn]ext\sDecember|[Ll]ast\sDecember|[Pp]revious\sDecember|[Bb]efore\sDecember|[Aa]fter\sDecember|[Pp]rior\sDecember|[Pp]rior\sto\sDecember)', "deictic"])

        # Expression set 3
        # Checking the seasons
        RE_list.append(["\s([Aa]utumn|[Ff]all|[Ww]inter|[Ss]ummer|[Ss]pring)", "deictic"])

        # Expression set 4
        # Checking the days of the week
        RE_list.append(['(Monday|[Tt]his\sMonday|[Nn]ext\sMonday|[Ll]ast\sMonday|[Pp]revious\sMonday|[Bb]efore\sMonday|[Aa]fter\sMonday|[Pp]rior\sMonday|[Pp]rior\sto\sMonday)', "deictic"])
        RE_list.append(['(Tuesday|[Tt]his\sTuesday|[Nn]ext\sTuesday|[Ll]ast\sTuesday|[Pp]revious\sTuesday|[Bb]efore\sTuesday|[Aa]fter\sTuesday|[Pp]rior\sTuesday|[Pp]rior\sto\sTuesday)', "deictic"])
        RE_list.append(['(Wednesday|[Tt]his\sWednesday|[Nn]ext\sWednesday|[Ll]ast\sWednesday|[Pp]revious\sWednesday|[Bb]efore\sWednesday|[Aa]fter\sWednesday|[Pp]rior\sWednesday|[Pp]rior\sto\sWednesday)', "deictic"])
        RE_list.append(['(Thursday|[Tt]his\sThursday|[Nn]ext\sThursday|[Ll]ast\sThursday|[Pp]revious\sThursday|[Bb]efore\sThursday|[Aa]fter\sThursday|[Pp]rior\sThursday|[Pp]rior\sto\sThursday)', "deictic"])
        RE_list.append(['(Friday|[Tt]his\sFriday|[Nn]ext\sFriday|[Ll]ast\sFriday|[Pp]revious\sFriday|[Bb]efore\sFriday|[Aa]fter\sFriday|[Pp]rior\sFriday|[Pp]rior\sto\sFriday)', "deictic"])
        RE_list.append(['(Saturday|[Tt]his\sSaturday|[Nn]ext\sSaturday|[Ll]ast\sSaturday|[Pp]revious\sSaturday|[Bb]efore\sSaturday|[Aa]fter\sSaturday|[Pp]rior\sSaturday|[Pp]rior\sto\sSaturday)', "deictic"])
        RE_list.append(['(Sunday|[Tt]his\sSunday|[Nn]ext\sSunday|[Ll]ast\sSunday|[Pp]revious\sSunday|[Bb]efore\sSunday|[Aa]fter\sSunday|[Pp]rior\sSunday|[Pp]rior\sto\sSunday)', "deictic"])

        # Iterate through Regular Expressions setup
        for regEx in RE_list:

            # Run the RegEx over the current text block
            results = self.find_regex(text,regEx[0])

            # Establish a counter of the place in the text from the start
            counter = 0

            # Iterate through the results of the current RegEx
            for row in results:

                # If the output result is empty add to the counter
                if ( row == '' ):
                    counter += 1

                # If the output result contains a valid search result then add it to the results list
                else:
                    # Append the file name, expression type, results and offset counter
                    self.list_results.append([ self.filename, regEx[1], row, counter])

    def find_regex(self, text, regex):

        reg = ''
        reg = reg + regex
        reg = reg +'|'

        return re.findall(reg, text)