from user.utils import download_image


def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    if user.image:
        return None
    url = 'https://w7.pngwing.com/pngs/893/926/png-transparent-silhouette-user-icon-profile-silhouette-silhouette-avatar-profile-silhouette-thumbnail.png'
    if backend.name == 'facebook':
        url = f"https://graph.facebook.com/{response['id']}/picture?width=600&height=600"
    if backend.name == 'google-oauth2':
        url = response['picture']
    if url:
        user.image = download_image(url)
        user.save()