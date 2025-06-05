from core.models import *

def get_common_context():
    """
    Frontend Sayfaları için ortak context verilerini döndürmesi için kullanıyorum. 
    """
    
    menus = MenuModel.active_objects.all()
    
    
    common_data = {
        'menus':menus,
    }
    
    return common_data