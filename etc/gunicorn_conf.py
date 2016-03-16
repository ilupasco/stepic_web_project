CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=16',
        '--timeout=60',
        '--log-file=/home/box/web/error_log.log',
        'hello:wsgi_app',
    ),
}

