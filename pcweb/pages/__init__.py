from pcweb.route import Route
from .docs import doc_routes
from .blog import blog_routes
from .index import index

routes = [r for r in locals().values() if isinstance(r, Route)]
