from jpegCreator import jpegURL

prefix="http://skyservice.pha.jhu.edu/DR10/ImgCutout/"


def test_jpegCreator_ra():
	s = jpegURL(ra=35., dec=45., options='G')
	assert s.ra==35., "ra is wrong"

def test_jpegCreator_dec():
	s = jpegURL(ra=35., dec=45.)
	assert s.dec==45.,  "dec is wrong"


def test_jpegCreator_options():
	s = jpegURL(ra=35., dec=45., options='GLBMQI')
	assert 'G' in s.options,  "G isn't an option yet"

def test_jpegCreator_options2():
	s = jpegURL(ra=35., dec=45., options='GLBMQI')
	assert 'O' not in s.options,  "O shouldn't be an option yet"


def test_jpegCreator_url():
	s = jpegURL(ra=35., dec=45., options='GLBMQI') 
	assert s.url==prefix+"getjpeg.aspx?ra=35.0&dec=45.0&width=512&height=512"\
                     "&scale=0.396&opt=GLBMQI.jpg", "url is still fucked."


def test_jpegCreator_url2():
	s = jpegURL(ra=35., dec=45., options='GLRo9BMp~QI') 
	assert s.url==prefix+"getjpeg.aspx?ra=35.0&dec=45.0&width=512&height=512"\
                     "&scale=0.396&opt=GLBMQI.jpg", "url is still fucked."

def test_jpegCreator_url3():
	s = jpegURL(ra=35., dec=45.) 
	assert s.url==prefix+"getjpeg.aspx?ra=35.0&dec=45.0&width=512&height=512"\
                     "&scale=0.396&opt=.jpg", "url is still fucked."