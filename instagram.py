import requests

# Set up the necessary variables
access_token = 'EAANXgQZCF5eQBANfK3iZCly4K1RTh70Xi27BuIboBcZAoTGZAFTwfFH6ZBmVs5ipURPwpdLPlqP5CqxrXZAXR0UUjmgYac8s6zEO5NrXqD4SW10TvMvFWz0iwnSiVZBSnoivZCl3o5ZCZCWUoAL1ZALzBWZB3kTVdZCQsYZC6HBs8iQuCrVGOyy5jtu6V9C6jvYvElgKYLFPXYAZCsGpCyOdBWputMoZC6OKmSyOXqs3HGqAvvtZBLnEuB2ZBnDX9js'
instagram_user_id = 'the_rest_frame'
image_url = 'https://images.pexels.com/photos/2913125/pexels-photo-2913125.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
caption = 'This is the caption for the post.'

# Create the media container
media_data = {
    'media_type': 'IMAGE',
    'image_url': image_url
}

media_response = requests.post(
    f'https://graph.facebook.com/{instagram_user_id}/media',
    params={'access_token': access_token},
    json=media_data
)

media_id = media_response.json()['id']

# Publish the post
post_data = {
    'caption': caption
}

post_response = requests.post(
    f'https://graph.facebook.com/{media_id}/children',
    params={'access_token': access_token},
    json=post_data
)

if post_response.status_code == 200:
    print('Post shared successfully!')
else:
    print('Error sharing the post:', post_response.json()['error']['message'])
