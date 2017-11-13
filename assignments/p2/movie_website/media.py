#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import webbrowser


class Movie():

    """
    This class stores movie data.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, protagonist="无"):
        """
        Input: title => the title of a movie
               storyline=>the movie story line
               poster_image_url=>an url of the movie poster image
               trailer_youtube_url => an url of youtube video
               protagonist => the movie protagonist
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_ulr = trailer_youtube
        self.protagonist = "主演：" + protagonist

    """
    show trailer
    """

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_ulr)
