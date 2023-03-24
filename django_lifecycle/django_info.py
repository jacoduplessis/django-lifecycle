import django

DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES = []


from django.db.models.fields.related_descriptors import (
    ForwardManyToOneDescriptor,
    ReverseOneToOneDescriptor,
    ReverseManyToOneDescriptor,
    ManyToManyDescriptor,
    ForwardOneToOneDescriptor,
)

DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES.extend(
    [
        ForwardManyToOneDescriptor,
        ReverseOneToOneDescriptor,
        ReverseManyToOneDescriptor,
        ManyToManyDescriptor,
    ]
)


DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES.extend([ForwardOneToOneDescriptor])

DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES = tuple(DJANGO_RELATED_FIELD_DESCRIPTOR_CLASSES)
