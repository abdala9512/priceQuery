#!"c:\users\miguel arquez abdala\google drive\projects\price-query-repo\pricequery\pricequeryheroku\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'dash==1.14.0','console_scripts','dash-generate-components'
__requires__ = 'dash==1.14.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('dash==1.14.0', 'console_scripts', 'dash-generate-components')()
    )
