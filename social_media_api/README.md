SetUP
## Create a Django Project and App
*django-admin startproject myproject 
python manage.py startapp accounts

## Configure settings.py
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
]
*set up CustomUser model in settings.py*
AUTH_USER_MODEL = 'accounts.CustomUser'

*Enabled Token Authentication and Permission*
REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',],
        }

*Applied Migrations*
python manage.py makemigrations accounts
python manage.py migrate


# OVERVIEW OF CUSTOMUSER MODEL
The CustomUser model extends AbstractUser and adds:
bio: A text field for user bio.
profile_picture: An image field for user profile pictures.
followers: A Many-to-Many self-referencing relationship (users can follow each other).


# AUTHENTICATION ENDPOINTS

 POST /register/
POST /login/
POST /logout/
POST /follow/{user_id}/            *FOLLOW A USER*
POST /unfollow/{user_id}/          *UNFOLLOW A USER *
GET /followers/                    * GET LIST OF FOLLOWERS*
GET /following/                    *GET LIST OF FOLLOWING USERS*
POST /posts/                       *CREATE A POST*       
POST /posts/{post_id}/comments/    *COMMENT ON A POST
GET /feed/                         *VIEW A POST FIELD*

- *ENDPOINT SUPPORT FOR PAGINATION*
 /posts/?page=2  # Fetches page 2 of posts
- *ENDPOINT SUPPORT FOR FILTERING*
/posts/?search=AI  # Fetches posts containing "AI"

## Likes and Notifications System API Documentation

*Features*

- Users can like and unlike posts.
- Users receive notifications when their posts are liked.
- Users can view and mark notifications as read.

*Endpoints*

POST /posts/{post_id}/like/
DELETE /posts/{post_id}/unlike/
GET /notifications/
PUT /notifications/read/

*User Interaction & Engagement Benefits

- Increased Engagement: Users can actively interact with posts, boosting community participation.
- Real-time Feedback: Users are notified when their posts receive interactions, keeping them informed.
- Better User Experience: A well-structured notification system helps users stay updated without manually checking interactions.
