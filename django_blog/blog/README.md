*. This is a README.md file documenting 
    - the authentication system
    - set up instructions
    - user guides
    - tests 


# The authentication system/guides

User Registration (New users can create accounts)
    -Users provide a username, email, and password.
    -The system validates inputs and saves the user.
    -The user is redirected to the login page upon successful registration.

User Login (Registered users can sign in)
    -Users enter their username and password.
    -If credentials are valid, Django authenticates the user and redirects them to their profile.

User Logout (Users can log out securely)
    -Users click the Logout button.
    -The system logs them out and redirects them to the home page.

Profile Management (Users can update their details)
    -Users can update their profile picture and bio.
    -The system validates and saves the updated profile information.


# Authentication Process/set-up instructions
-   Created UserProfile model which has a OneToOne relationship with the default Django User model
-   Created a Django ModelForm using the UserProfile model
-   Created signals in signals.pyfor the UserProfile model to ensure that a User profile is created automatically upon successful registration 
-   Ensured the signals are connected in apps.py
-   Created register view which upon success redirects to the home page
-   Created profile view which uses the @login_required decorator to ensure that user can only edit profile upon successful login. It is defined in such a way that user remains in the session while update takes place
-   defined view to list all posts created in a users account

- registered the views in blog/urls.py
/register/
/profile/
/home/
/post/

- used Django's built-in authentication views
/login/
/logout/

# tests

**Testing Instructions**

## Registration Test
    Visit http://127.0.0.1:8000/register/
    Enter a username, email, and password.
    Click Sign Up.
    Verify the user is created in the database.
    Ensure redirection to the login page.
## Login Test
    Visit http://127.0.0.1:8000/login/
    Enter a registered username and password.
    Click Login.
    Verify redirection to the profile page.
## Logout Test
    Click the Logout button.
    Verify that access to http://127.0.0.1:8000/profile/ requires login.
## Profile Update Test
    Log in and go to http://127.0.0.1:8000/profile/
    Update profile details (e.g., bio, profile picture).
    Click Update Profile.
    Ensure changes are saved.



# Django Blog - Comment System Documentation

## How to Add a Comment
    Navigate to the detail page of a blog post.
    Scroll down to the comments section.
    If logged in, you will see a text box to enter your comment.
    Type your comment and click the **Submit** button.
    Your comment will be added and displayed under the post.

## Who Can Edit/Delete a Comment
    Only the **author** of a comment can edit or delete it.
    Other users cannot modify or remove comments they did not create.
    Admin users (staff) can manage all comments if needed.

## Permissions Required for Actions
    **Adding a Comment**: Requires the user to be **authenticated (logged in).**
    **Editing a Comment**: Only the **original author** of the comment can edit it.
    **Deleting a Comment**: Only the **original author** can delete their comment.
    **Viewing Comments**: Comments are publicly visible to all users, regardless of authentication status.


# Blog Post Tagging & Search

## Adding Tags to Posts
1. When creating a new post, enter comma-separated tags in the "Tags" field.
2. Click "Submit" to save the post with tags.

## Searching for Posts
1. Enter keywords in the search bar.
2. Results will include posts matching the title, content, or tags.

## Filtering Posts by Tags
1. Click on a tag in any post to view all posts associated with it.

## Permissions
- Any user can search and view posts.
- Only authenticated users can create/edit/delete posts with tags.

