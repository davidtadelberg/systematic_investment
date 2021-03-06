__author__ = "David Adelberg"
__copyright__ = "Copyright 2016, David Adelberg"
__credits__ = ["David Adelberg"]

__license__ = """May be used by members of the Yale College Student Investment
                 Group for education, research, and management of the  
                 organization's portfolio. All other uses require the express
                 permission of the copyright holder. Other interested persons
                 should contact the copyright holder."""
__version__ = "0.1.0"
__maintainer__ = "David Adelberg"
__email__ = "david.adelberg@yale.edu"
__status__ = "Prototype"

def qd_bulk_downloader_func(info):
    from systematic_investment.data.quandl.QuandlBulkDBLoader import QuandlBulkDBLoader
    return(lambda: QuandlBulkDBLoader(info.downloaded_data.path))
    
def qd_downloader_func(info):
    """Returns a QuandlDBLoader constructor function.
    
    info: a Info object with an authtoken field.
    
    """
    from systematic_investment.data import QuandlDBLoader
    return(lambda: QuandlDBLoader(info.top().authtoken))