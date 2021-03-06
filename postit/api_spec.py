API_SPEC = {
    'api': {
        '.endpoint': {
            'permissions': [('*',) * 6],
        },
        'teams': {
            '.collection': {},
            '.drf_collection': {
                'model': 'postit.models.Team',
            },
            '*': {
                'id': {
                    '.drf_field': {},
                    '.integer': {},
                    '.required': {}
                },
                'name': {
                    '.required': {},
                    '.drf_field': {},
                    '.string': {'max_length': 100},
                },
            },
            '.actions=': {
                '.create': {},
                '.list': {},
                '.retrieve': {},
            }
        },
        'students': {
            '.collection': {},
            '.drf_collection': {
                'model': 'postit.models.Student',
            },
            '*': {
                'id': {
                    '.readonly': {},
                    '.drf_field': {},
                    '.serial': {}
                },
                'first_name': {
                    '.required': {},
                    '.drf_field': {},
                    '.string': {'max_length': 50},
                },
                'last_name': {
                    '.required': {},
                    '.drf_field': {},
                    '.string': {'max_length': 50},
                },
                'am': {
                    '.required': {},
                    '.drf_field': {},
                    '.integer': {'max_length': 10},
                },
                'email': {
                    '.required': {},
                    '.drf_field': {},
                    '.email': {}
                },
                'github_username': {
                    '.blankable': {},
                    '.drf_field': {},
                    '.string': {'max_length': 10},
                },
                'linkedin_url': {
                    '.blankable': {},
                    '.drf_field': {},
                    '.string': {'max_length': 50},
                },
                'about': {
                    '.required': {},
                    '.drf_field': {},
                    '.text': {'max_length': 150},
                },
                'knowledge': {
                    '.required': {},
                    '.drf_field': {},
                    '.text': {'max_length': 150},
                },
                'skills': {
                    '.required': {},
                    '.drf_field': {},
                    '.text': {'max_length': 150},
                },
                'preferred_teams': {
                    '.blankable': {},
                    '.drf_field': {},
                    '.text': {'max_length': 150},
                },
                'team': {
                    '.drf_field': {},
                    '.ref': {'to': 'api/teams'},
                    '.readonly': {}
                },
                'available': {
                    '.drf_field': {},
                    '.boolean': {},
                    '.readonly': {}
                },
                'image_url': {
                    '.drf_field': {},
                    '.file': {}
                },
            },
            '.actions=': {
                '.create': {},
                '.list': {},
                '.retrieve': {},
                '.update': {}
            }
        },
    }
}
