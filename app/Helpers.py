import datetime



def convertDateObjToDateString(dateObj):
    '''
    Converts datetime.date object to string 
    output: '1978-05-14'
    '''
    return dateObj.strftime('%Y-%m-%d')