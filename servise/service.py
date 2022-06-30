def upload_image_product(instance, file):
    return f'shop/{instance.category}/{file}'
