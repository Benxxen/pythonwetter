__author__ = 'Patrick'

def windrichtung(winddir):
    if winddir <= 23:
        winddir = 'N'
    elif winddir <= 67:
        winddir = 'NE'
    elif winddir <= 113:
        winddir = 'E'
    elif winddir <= 158:
        winddir = 'SE'
    elif winddir <= 203:
        winddir = 'S'
    elif winddir <= 248:
        winddir = 'SW'
    elif winddir <= 293:
        winddir = 'W'
    elif winddir <= 338:
        winddir = 'NW'
    else:
        winddir = 'nn'
    return winddir

