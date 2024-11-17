from .models import Category

def categories(request):
    """
        We make this context processors to show our categories in header.html.
    """
    
    category_query = Category.objects.available_categories
    
    context = {
        'categories' : category_query,
    }
    
    return context
