#!/usr/bin/env python


class jpeg(object):

    def __init__(self, ra=None, dec=None, scale=0.396, 
                 height=512, width=512, options=''):

        self.ra = ra
        self.dec = dec
        self.width = width
        self.height = height
        self.scale = scale

        option_list = [op for op in options if op in 'GLPSTOBFMQI']
        self.options = ''.join(option_list)

        self.url = self.createURL()


    def createURL(self):
        prefix = "http://skyservice.pha.jhu.edu/DR12/ImgCutout/"

        url = prefix+"getjpeg.aspx?ra={0}&dec={1}&width={2}&height={3}"\
              "&scale={4}&opt={5}.jpg".format(self.ra, self.dec, self.width,
                                              self.height, self.scale, self.options)
        return url


class fileCreator(object):

    @staticmethod
    def bashScript(SDSSDataList, filename):

        F = open(filename,'w')
        for entry in SDSSDataList:

            s = jpegURL(ra=entry['ra'], dec=entry['dec'], 
                        width=entry['width'], height=entry['height'],
                        scale=entry['scale'], options=entry['options'])
            F.write('wget {0}\n'.format(s.url))
        F.close()
        return filename

    @staticmethod
    def asciiList(SDSSDataList, filename):

        F = open(filename,'w')
        for entry in SDSSDataList:
            s = jpegURL(ra=entry['ra'], dec=entry['dec'], options=entry['options'])
            F.write('{0}\n'.format(s.url))
        F.close()
        return filename

"""
def create_wget_file(ra, dec, options=None):

    supply a table of ra/dec 
    creates a bash script which fetches SDSS urls for each image in the sample


    F = open('get_SDSSjpegs.sh','w')

    for ra, dec in zip(ra, dec):
        F.write('wget "%s%f%s%f%s"\n'%(one, ra, two, dec, three))
    F.close()

    print "Successfully created bash file of jpeg urls for wget."
 
 
 
def get_SDSS_jpegs(*args, **kwargs)

    for filetype in ['ascii', 'fits']:
        try:
            sample = Table.read(args.filename, format=filetype)
            break
        except ProgrammingError:
            continue
    else:
        raise ProgrammingError("Filetype must be ascii or fits.")
        sys.exit()

    colnames = sample.colnames

    if 'ra' in colnames and 'dec' in colnames:
        print "Found RA/DEC columns. Creating SDSS urls."
        create_wget_file(sample['ra'], sample['dec'], args)

    elif 'RA' in colnames and 'DEC' in colnames:
        print "Found RA/DEC columns. Creating SDSS urls."
        create_wget_file(sample['RA'], sample['DEC'], args)

    else:
        print "Did not find RA/DEC columns! Exiting."
        sys.exit()


    answer = raw_input("Would you like to execute bash command "\
                       "to wget jpegs? [y/n] ")

    if 'y' in answer.lower():
        check = subprocess.check_call("bash get_SDSSjpegs.sh", shell=True)
    else:
        print "To excecute bash script yourself:"
        print ">>> bash get_SDSSjpeg.sh"

"""
"""
if __name__ == '__main__':
    # --------------------------------------------------------------------- #  
    parser = ArgumentParser()
    parser.add_argument('filename', help="Name of file containing "\
                        "RA/DEC of SDSS images for which you wish to get jpegs.")

    args = parser.parse_args()

    main(args)
"""
