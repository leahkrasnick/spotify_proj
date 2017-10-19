Final Project Readme Template

1. 

My project is a program where the user can get a list of playlists to listen to based on the weather of where they are located or any place they want to see. The user inputs their zip code or a zip code that they want to test and the output will be a list of playlists from Spotify that reflect the mood of the weather outside, in order from most tracks to least tracks. I wanted to create this project because i wanted to make a way for users to get music based not the mood of the weather, like when its cold out or grey outside, people want to listen to sad or gloomy playlists and when its nice out they may want cheerful playlists and this program with grab these playlists for you based on what the weather is.

2.
DIRECTIONS:

-First run python 106finalproj.py in the terminal

-Then it will ask you for a zip code, so type in the zip code you want to get the weather from. For example 48109 for Ann Arbor

-This will create the file Playlists.txt in your directory which will have the 5 playlists, each playlists name and who it was created by, in order of most tracks to least tracks in the playlist taken from Spotify that reflect your weather. 

-Then to complete the test cases, in the terminal after entering the zip code for the first time,to make sure all the data you are getting is correct, you must input/type your same zip code 3 times when the terminal asks for your zip code “Please enter a valid zip code”(this will make sure the data/playlists you get back are correct)


3.

All files i will be turning in:
1) 106finalproj.py
2) README.txt
3) cacheWeatherData.txt
4) cacheSpotifyData.txt
5) I will also be turning in the Playlists.txt that i get when i use my home zip code of 48070


4. 
The user must install the requests module.

5.
SOURCES:
I imported os.path at the beginning of my python code and received help from stack over flow - http://stackoverflow.com/questions/2724348/should-i-use-import-os-path-or-import-os

I also used the hacked to help with some of the spotify authentication and getting tokens

I also used the textbook to refresh myself on REST APIs, sorting, and creating functions

For caching I did it a little differently than in class and i used stack over flow pages as ideas on how to create my own cacheing code —> http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python 

To understand the unicode errors i used stack overflow to help figure out how to use “.encode('utf-8’)” http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20/9942822



6. Approximate line numbers in Python file to find the following mechanics requirements:
- Sorting with a key function:130-138
- Class definition:7-83, 85-164
- Creating instance of a class:169-171
- Calling methods on a class instance (list all line numbers where you invoke any method on a class instance):169, 171, 
- Beginnings of each class method definition:8, 14, 20,35,50,59,80, 87, 93, 102, 109, 117, 130, 141, 148
- (If applicable) Beginnings of each function definition outside classes:
- Beginning of code that handles data caching/using cached data:44, 80, 102, 127
- Test cases: 1738-213

8. Rationale for project: I did this project because i love music and sometimes when I’m hanging out alone or with my friends i want to play music but don’t know what songs to play, and this project allows the code to grab a playlist for the user and grabs it based on the weather. The weather always affects my mood so i thought it was a good parameter to base the lists of playlists off of. I found it interesting because the weather API was very cool in the sense that it provided a lot more than just the temperature and gave me lots of cool data to use. While the sorted function i used may not seem that important because it is just sorting the playlists from highest to lowest amount of tracks and grabbing the top five playlists from that sorted list, i think that the sorted function is essential because it makes sure that the user does not get any playlists that only have 1 track in them or a playlist with very few tracks because spotify is full of tons of unfinished playlists that the user would not want to listen to. The project mostly worked out how I wanted but with a couple spots where i got stuck and didn’t get the exact output i was hoping for. I wanted to be able to grab playlists that just had the theme of the “mood” but the Spotify api doesn’t really generalize playlists to certain themes or moods so i just had to get playlists that had that “mood” word in them, but usually if it had the “mood” word in it, it is most like likely to have songs relating to that theme/mood. I also did not like the way my unit tests make the user input their zip code 4 times but it was the only way it worked because all of the data depended on the zip code. 