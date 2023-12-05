from functools import partial, wraps
from minidetector import detect_mobile


def ua_detector(standard, mobile=None):
    """User Agent detector. Redirects django_annoying's render_to_response decorator to point the
    template path one way or another, depending on mobile vs desktop.
    
    Right now "user agent" means "mobile vs desktop"
    
    Use it like:
    @render_to()
    @ua_detector(standard="templates/filename")
    def view_function(response):
        return dict()
    
    Or
    @render_to()
    @ua_detector(standard="template/filename", mobile="templates/mobile/filename")
    def view_function(response):
        return dict()
    
    This assumes you have minidetector <http://code.google.com/p/minidetector> installed.
    A fork with a setup.py file is at <http://github.com/brosner/minidetector>.
    
    I like installing minidetector with PIP:
    $ pip install -e git://github.com/brosner/minidetector.git#egg=minidetector
    
    """
        
    def decorator_function(decorator_or_function):
        @wraps(decorator_or_function)
        def kick_it_off(params_for_function_or_decorator):
            # this function works on the fact that render_to CAN look for a key in
            # the returned dictionary, key name TEMPLATE
            #
            # params_for_function_or_decorator is our request object
            
            out_dict = decorator_or_function(params_for_function_or_decorator)
            if (params_for_function_or_decorator.mobile and mobile):
                out_dict["TEMPLATE"] = mobile
            else:
                out_dict["TEMPLATE"] = standard
            return out_dict
        
        return kick_it_off
    
    return decorator_function


