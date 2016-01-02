import httplib2
import json

def getGeoCodeLocation(inputString):
    google_API_key = "AIzaSyDe9JPbdMWt8VL7oPm4hLxgDtUz0DkrPdk"
    locationString =  inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString,google_API_key))
    print(url)
    h = httplib2.Http()
    response,content = h.request(url,'GET')
    strResponse = content.decode('utf-8')
    result = json.loads(strResponse)
    print ("response header = %s \n\n" %response)

    Location = {'Lng' : result ['results'][0]['geometry']['location']['lng'] , 'Lat' : result ['results'][0]['geometry']['location']['lat']}
    
    return Location
