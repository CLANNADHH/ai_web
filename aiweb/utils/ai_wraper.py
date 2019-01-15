from functools import wraps

def check_cors(f):
    """Wraps a request handler with CORS headers checking."""

    @wraps(f)
    def decorated(*args, **kwargs):
        self = args[0]
        request = args[1]
        origin = request.getHeader('Origin')

        if origin:
            if '*' in self.cors_origins:
                request.setHeader('Access-Control-Allow-Origin', '*')
            elif origin in self.cors_origins:
                request.setHeader('Access-Control-Allow-Origin', origin)
            else:
                request.setResponseCode(403)
                return 'forbidden'

        if request.method.decode('utf-8', 'strict') == 'OPTIONS':
            return ''  # if this is an options call we skip running `f`
        else:
            return f(*args, **kwargs)

    return decorated