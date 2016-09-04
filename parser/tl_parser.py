import re
from tl import TLObject


class TLParser:
    """Class used to parse .tl files"""

    @staticmethod
    def parse_file(file_path):
        """This method yields TLObjects from a given .tl file"""

        with open(file_path, encoding='utf-8') as file:
            # Start by assuming that the next found line won't be a function (and will hence be a type)
            is_function = False

            # Read all the lines from the .tl file
            for line in file:
                line = line.strip()

                # Ensure that the line is not a comment
                if line and not line.startswith('//'):

                    # Check whether the line is a type change (types ⋄ functions) or not
                    match = re.match('---(\w+)---', line)
                    if match:
                        following_types = match.group(1)
                        is_function = following_types == 'functions'

                    else:
                        yield TLObject.from_tl(line, is_function)
