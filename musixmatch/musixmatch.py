import requests
import json

from .utils import _set_page_size


class Musixmatch(object):

    def __init__(self, apikey):
        self.__apikey = apikey
        self.__url = 'http://api.musixmatch.com/ws/1.1/'

    def _get_url(self, url):
        return self.__url + '{}&apikey={}'.format(url, self._apikey)

    @property
    def _apikey(self):
        return self.__apikey

    def _request(self, url):
        data = requests.get(url).json()
        return data

    def chart_artists(self, page, page_size, country='us', _format='json'):
        """This api provides you the list
        of the top artists of a given country.
        """
        data = self._request(self._get_url('chart.artists.get?'
                                           'page={}&page_size={}'
                                           '&country={}&format={}'
                                           .format(page,
                                                   _set_page_size(page_size),
                                                   country, _format)))
        return data
