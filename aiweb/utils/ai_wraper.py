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
    

def check_route(f):
    """Wraps a request handler with router."""
    @wraps(f)
    def decorated(*args, **kwargs):
        self = args[0]
        request = args[1]
        url = request.uri.decode()
        html_404 = '''<title>404 Not Found</title>
                    <h1>Hey!Easy~</h1>
                    <p>If you see this page,it means you have to add the <span style="color:red;font-size:20px">PREDICT_CLASS </span>and <span style="color:red;font-size:20px">PREDICT_FUNC</span> in you <span style="color:blue;font-size:20px">config.ini</span>.</p>'''
        if url not in self.router:
            request.setResponseCode(404)
            return html_404
        else:
            return f(*args, **kwargs)
    return decorated      
        
        
def check_ai(f):
    """Wraps a request handler with router."""
    @wraps(f)
    def decorated(*args, **kwargs):
        print(args)
        print(kwargs)
        return f(*args, **kwargs)
    return decorated   
    