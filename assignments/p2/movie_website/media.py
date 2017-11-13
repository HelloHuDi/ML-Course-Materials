#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube,protagonist="无"):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_ulr = trailer_youtube
        self.protagonist = "主演："+protagonist

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_ulr)
