from rest_framework.routers import DefaultRouter
from .views import BooksViewset

router = DefaultRouter()
router.register('books', BooksViewset)
