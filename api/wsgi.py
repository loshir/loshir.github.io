import sys
import os

# Add parent directory to path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# WSGI entry point for Vercel serverless functions
def handler(request):
    """
    Vercel serverless function handler.
    Routes all requests through the Flask WSGI app.
    """
    # Create a WSGI environ dict from the Vercel request
    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.path,
        'QUERY_STRING': request.url.split('?')[1] if '?' in request.url else '',
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': request.headers.get('content-length', ''),
        'SERVER_NAME': request.headers.get('host', 'localhost').split(':')[0],
        'SERVER_PORT': request.headers.get('host', 'localhost').split(':')[1] if ':' in request.headers.get('host', '') else '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': None,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': True,
        'wsgi.run_once': False,
    }
    
    # Add headers to environ
    for header, value in request.headers.items():
        header = header.upper().replace('-', '_')
        if header not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{header}'] = value
    
    # Collect response
    response_started = False
    status = None
    response_headers = []
    
    def start_response(status_str, headers, exc_info=None):
        nonlocal response_started, status, response_headers
        if exc_info:
            try:
                if response_started:
                    raise exc_info[1].with_traceback(exc_info[2])
            finally:
                exc_info = None
        elif response_headers:
            raise RuntimeError('Response already started')
        
        response_started = True
        status = int(status_str.split(' ', 1)[0])
        response_headers = headers
        return lambda s: None  # write() function (deprecated but required)
    
    # Call the Flask app
    app_iter = app(environ, start_response)
    
    try:
        body = b''.join(app_iter)
    finally:
        if hasattr(app_iter, 'close'):
            app_iter.close()
    
    # Return Vercel response format
    return {
        'statusCode': status or 200,
        'headers': dict(response_headers),
        'body': body.decode('utf-8') if isinstance(body, bytes) else body,
    }
