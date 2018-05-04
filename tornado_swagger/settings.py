#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path

__author__ = 'serena'

SWAGGER_VERSION = '1.2'

URL_SWAGGER_API_DOCS = 'swagger-api-docs'
URL_SWAGGER_API_LIST = 'swagger-api-list'
URL_SWAGGER_API_SPEC = 'swagger-api-spec'

URL_SWAGGER2_API_DOCS = 'swagger-api-docs'
URL_SWAGGER2_API_LIST = 'swagger-api-list'
URL_SWAGGER2_API_SPEC = 'swagger-api-spec'

ROOT_PATH = os.path.dirname(os.path.normpath(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'static')
STATIC_V2_PATH = os.path.join(ROOT_PATH, 'static_v2')

default_settings = {
    'base_url': '/',
    'static_path': STATIC_PATH,
	'static_v2_path': STATIC_V2_PATH,
    'swagger_prefix': '/swagger',
    'api_version': 'v1.0',
    'api_key': '',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'exclude_namespaces': [],
}

models = []
