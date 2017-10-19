import json
import requests
import unittest
import os.path
from pprint import pprint

class Weather():
    def __init__(self):
        self.zipcode=self.askUserZipcode()
        self.baseurl='http://api.openweathermap.org/data/2.5/weather'
        self.APIKEY = '7998acf455da4c814a740c4eb032d883'
        self.api_response= 'cacheWeatherData.txt'

    def mainWeather(self):
        self.weatherDict()
        self.weatherData()
        self.cacheWeatherData()
        return self.weatherMood()

    def askUserZipcode(self):
        #this function returns a valid zipcode make sure it is an int
        # zipcode = ""
        # i = 0
        # while(True):
        #     if zipcode.isdigit():
        #         return zipcode
        #     else:
        #         if i != 0:
        #             print "Please enter a valid zipcode!"
                #zipcode = raw_input("Please enter a valid zipcode: ")
            #i+=1
        zipcode = raw_input("Please enter a valid zipcode: ")
        return int(zipcode)

    def weatherDict(self):
        #weatherDict() returns a dictionary of the weather data for a specific zipcode
        try:
            params= {}
            params['zip']=self.zipcode
            params['APPID']=self.APIKEY
            params['units']='imperial'
            response = requests.get(self.baseurl, params=params)
            self.api_response = json.loads(response.text) 
        except:
            with open('cacheWeatherData.txt') as data:
                self.api_response = json.load(data)
        #print self.api_response
        return self.api_response

    def weatherData(self):
#       #WeatherData is supposed to return the temperature, mthe "main" which is like the large description (i.e. "Snow") and description should be a little more detailed description of the weather
        self.all_data_weather = {}
        self.all_data_weather['Temperature'] = self.api_response['main']['temp']
        self.all_data_weather['Main'] = self.api_response['weather'][0]['main']
        self.all_data_weather['Description'] = self.api_response['weather'][0]['description']
        print self.all_data_weather
        return self.all_data_weather

    def weatherMood(self):
        #WeatherMood should take the details from WeatherData and categorize the diffferent types of weather into different playlist categories/moods
        if self.all_data_weather['Main'] =='Clouds' or self.all_data_weather['Main'] =='Mist':
            return 'Relaxing'
        elif self.all_data_weather['Main'] == 'Clear':
            return 'Cheerful'
        elif self.all_data_weather['Main'] == 'Rain':
            return 'Sad'
        elif self.all_data_weather['Main']=='Sunny' and float(self.all_data_weather['Temperature']) > 65:
            return 'Feel Good'
        elif self.all_data_weather['Main']=='Sunny' and float(self.all_data_weather['Temperature']) < 65:
            return 'Nice Day'
        elif self.all_data_weather['Main'] == 'Snow':
            return 'Winter'
        elif self.all_data_weather['Main'] == 'Haze':
            return "Chill"
        elif self.all_data_weather['Main'] == 'Extreme':
            return "Rock n Roll"
        else:
            return 'Random'

    def cacheWeatherData(self):
        #This function will cache the data from the API, if it fails in the weatherDict() method it will use the cached txt file data
        with open('cacheWeatherData.txt', 'w') as outfile:
            return json.dump(self.api_response, outfile)

class Spotify():
    
    def __init__(self, mood):
        self.CLIENT_ID = '38dd759872bd4c0cb48bb802f9509322'
        self.CLIENT_SECRET = '776c4f51dce94123b41ba5e5230d635c'
        self.API_TOKEN = self.getToken()
        self.mood = mood

    def spotifyMain(self):
        
        self.getSpotifyPlaylist()
        self.sortByNumberTracks()
        self.calculateAverageTracks()
        self.cacheSpotifyData()
        return self.writeTextFile()
        

    def cacheSpotifyData(self):
        #This function will cache the data from the API, if it fails in the weatherDict() method it will use the cached txt file data
        with open('cacheSpotifyData.txt', 'w') as outfile:
            return json.dump(self.api_response_spotify, outfile)



    def getToken(self):
       
        #Will make a request to spotify to get an API token... 
        payload = {'grant_type': 'client_credentials'}
        auth = (self.CLIENT_ID, self.CLIENT_SECRET)
        url = 'https://accounts.spotify.com/api/token'
        return json.loads(requests.post(url, data=payload, auth = auth).text)['access_token']

    def getSpotifyPlaylist(self):
        #This will call the spotify API
        try:
            url = 'https://api.spotify.com/v1/search'
            params = {}
            params['q'] = "*"+self.mood+"*" #have to add in two wildcard characters
            params['type'] = "playlist"
            results = requests.get(url, headers={"Authorization":"Bearer " + self.API_TOKEN}, params = params).text
            self.api_response_spotify = json.loads(results)
        except:
            self.api_response_spotify = self.cacheSpotifyData()
        return self.api_response_spotify

    def sortByNumberTracks(self):
        #This will sort from highest to lowest on number of tracks in the playlist
        self.sortedPlaylistByTracks = sorted(self.api_response_spotify['playlists']['items'], key = lambda x: x ['tracks']['total'], reverse = True)
        for playlist in self.sortedPlaylistByTracks[0:5]:
            # t=(playlist['name'], playlist['owner']['id'],playlist['tracks']['total'])
            # List_of_playlists= "Playlist: {} by user {} has {} tracks".format(*t)
            List_of_playlists="Playlist: %s by user %s has %d tracks" % tuple([playlist['name'].encode('utf-8'), playlist['owner']['id'].encode('utf-8'), playlist['tracks']['total']])
            print List_of_playlists
        return self.sortedPlaylistByTracks
        #return List_of_playlists

    def calculateAverageTracks(self):
        count = 0 
        for playlist in self.sortByNumberTracks():
            count += int(playlist['tracks']['total'])
               
        return int(count) 

    def writeTextFile(self):
        # fname= open("SpotifyPlaylist.csv", "wb")
        # fname.write("Playlist Name:, Average # of tracks\n")
        # for obj in self.sortedPlaylistByTracks:
        #     Playlist = self.sortedPlaylistByTracks['playlist']['name']
        #     AvgTrack= self.sortedPlaylistByTracks['playlist']['tracks']['total']
        #     data=(Playlist,AvgTrack)
        #     fname.write("{}, {}\n".format(*data))
        file = open("Playlists.txt", "w")
        
        # for playlists in self.sortedPlaylistByTracks[0:5]:
            # t=(playlists['name'], playlists['owner']['id'])
            # List_of_playlists= "Playlist: {} by user {}\n".format(*t)
        self.sortedPlaylistByTracks = sorted(self.api_response_spotify['playlists']['items'], key = lambda x: x ['tracks']['total'], reverse = True)
        for playlist in self.sortedPlaylistByTracks[0:5]:
            List_of_playlists="Playlist: %s by user %s has %d tracks\n" % tuple([playlist['name'].encode('utf-8'), playlist['owner']['id'].encode('utf-8'), playlist['tracks']['total']])
            file.write((List_of_playlists))
       

        file.close()

overallMood = (Weather().mainWeather())
print "The overall mood is {}".format(overallMood)
Spotify(overallMood).spotifyMain()



    ############TEST CASES##########


class UnitTest(unittest.TestCase):

        #change this one
        #Tests to make sure a valid zipcode is an attribute of the weather class (int)
        #self.assertEqual(type(Weather().zipcode), type(int))
    def test_zipcode(self):
        self.assertEqual(type(Weather().zipcode), type(3), "testing if the zipcode is a valid number/integer")


        #good
    def test_weatherDictionaryKeys(self):
        #Tests weather the all_data object contains the correct keys : Main, Temperature, Description
        
        weather = Weather()
        weather.mainWeather()
        self.assertEqual(weather.all_data_weather.keys(), ['Main', 'Temperature', 'Description'], "Testing if these are keys in the weather dictionary")

    def test_spotifyAPIToken(self):
        #Tests to make sure a valid api token is returned and it is not empty
        self.assertTrue(Spotify("Happy").getToken().strip() != "", "Testing if the api token that is returned is not empty")

    def test_cacheFileWeatherAPI(self):
        #Got the `os.path.isfile(fname)` code from stack overflow checking if file exists
        self.assertTrue(os.path.isfile('cacheWeatherData.txt'), "Testing if the cached file exitsts for the weather data")

    def test_cacheFileSpotifyAPI(self):
        #Got the `os.path.isfile(fname)` code from stack overflow checking if file exists
        self.assertTrue(os.path.isfile('cacheSpotifyData.txt'), "Testing if the cached file exitsts for the spotify data")

        #change this one
    # def test_ListOfPlaylists(self):
    #     self.assertEqual(Spotify("Happy").calculateAverageTracks(), type(int))

        #change this one
    def test_y(self):
        self.assertEqual(type(Weather().mainWeather()),type(""), "Testing if the overall mood of the weather is a word")

    # def test_y_2(self):
    #     with open('cacheWeatherData.txt') as data:
    #         self.api_response =(json.load(data))
    #         self.assertTrue(self.api_response == type({}))
   
unittest.main(verbosity=2)


