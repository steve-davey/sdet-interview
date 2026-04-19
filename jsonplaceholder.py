import requests
import json

# Base URL for JSONPlaceholder API
base_url = "https://jsonplaceholder.typicode.com"

# Function to fetch a list of posts using GET request
def fetch_posts():
    # Construct the URL for fetching posts
    url = f"{base_url}/posts"
    # Make a GET request to fetch the posts
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully fetched the posts.")
        # Parse and print the posts data
        posts = response.json()
        print("Posts Data:", json.dumps(posts, indent=4))
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

# Function to create a new post using POST request
def create_post(new_post):
    # Construct the URL for creating a post
    url = f"{base_url}/posts"
    # Make a POST request to create the post
    response = requests.post(url, json=new_post) 

    # Check if the request was successful
    if response.status_code == 201:
        print("Successfully created a new post.")
        # Parse and print the new post data
        created_post = response.json()
        print("Created Post Data:", json.dumps(created_post, indent=4))
    else:
        print(f"Failed to create post. Status code: {response.status_code}")

# Function to update a post using PUT request
def update_post(post_id, updated_data):
    # Construct the URL for updating the post
    url = f"{base_url}/posts/{post_id}"
    # Make a PUT request to update the post
    response = requests.put(url, json=updated_data) 

    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully updated the post.")
        # Parse and print the updated post data
        updated_post = response.json()
        print("Updated Post Data:", json.dumps(updated_post, indent=4))
    else:
        print(f"Failed to update post. Status code: {response.status_code}")

# Function to delete a post using DELETE request
def delete_post(post_id):
    # Construct the URL for deleting the post
    url = f"{base_url}/posts/{post_id}"
    # Make a DELETE request to delete the post
    response = requests.delete(url)

    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully deleted the post.")
    else:
        print(f"Failed to delete post. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Fetch posts
    fetch_posts() 

# Create a new post
    new_post = {
        "title": "New Post Title",
        "body": "This is the body of the new post.",
        "userId": 1
    } 

create_post(new_post)
# Update a post
post_id_to_update = 1
updated_post_data = {
    "id": post_id_to_update,
    "title": "Updated Post Title",
    "body": "This is the updated body of the post.",
    "userId": 1
}

update_post(post_id_to_update, updated_post_data)
# Delete a post
post_id_to_delete = 1
delete_post(post_id_to_delete)