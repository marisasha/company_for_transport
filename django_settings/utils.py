from django.core.paginator import Paginator



def native_paginate(request, object_list, per_page):
    selected_page = request.GET.get(key="page", default=1)
    page_objs = Paginator(object_list=object_list, per_page=per_page)
    page_obj = page_objs.page(number=selected_page)
    return page_obj