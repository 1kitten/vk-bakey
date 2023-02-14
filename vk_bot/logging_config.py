LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'base'
        }
    },
    'formatters': {
        'base': {
            'format': '%(asctime)s - %(message)s - %(levelname)s - %(module)s'
        }
    },
    'loggers': {
        'bot_logger': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'sections_log': {
            'handlers': ['console'],
            'level': 'INFO'
        },
        'products_log': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}
