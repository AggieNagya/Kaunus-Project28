from django.utils.text import slugify

def unique_slug_generator(model_instance, title, slug_field):
    """

    :param model_instance:
    :param title:
    :param slug_field:
    :return:
    """

    slug = slugify(title)
    model_class = model_instance.__class__  # __class__ method returns the name of the class which we called model_class

    """
     The while loop below checks to see if the slug already exists
     The function _default_manager is objects, then we filter the slug in question to see if exists .exists()
     function
     For example of are are working with Trench model it would look like:
     Trench.objects,filter(slug=slug).exists()
    """
    while model_class._default_manager.filter(slug=slug).exists():
        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug
