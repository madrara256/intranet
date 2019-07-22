from . models import (Department, Organisation, Branch, Application, PublicDocument, DocumentCategory, ImageTag, ImageGallery)
from . utils import memoize

def all_globals(request):
    return {
    "organisations":memoize(
    lambda: Organisation.objects.get(id=1)
    ),
    "branches":memoize(
    lambda:Branch.objects.all()
    ),
    "departments": memoize(
        lambda: Department.objects.order_by('-id')
    ),
    "applications": memoize(
        lambda: Application.objects.all()
    ),
    "public_documents": memoize(
        lambda: PublicDocument.objects.all()
    ),
    "categories": memoize(
        lambda: DocumentCategory.objects.all()
    ),
    "image_tags":(
        lambda:ImageTag.objects.all()
        ),
    "images": memoize(
        lambda: ImageGallery.objects.all()
        ),

    }
