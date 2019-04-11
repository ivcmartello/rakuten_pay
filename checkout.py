from resources import handler_request
from resources.routes import checkout_routes


def get(document, value):
    return handler_request.get(checkout_routes.CHECKOUT_DATA_LINK.format(document, value))
