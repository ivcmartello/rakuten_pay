from resources import handler_request
from resources.routes import category_routes


def find_all():
    return handler_request.get(category_routes.CATEGORY_LINK)
