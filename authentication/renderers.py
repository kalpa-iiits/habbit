'''
This module is to convert callable objects to json

'''

from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    """
    Class cointaining method to render callable objects to json
        
    Methods
    -------------------------------
    Json renderer
    
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return response
