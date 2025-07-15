import praw
import os
import sys
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Reddit credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="reddit-persona-generator"
)

def extract_username_from_url(url: str) -> str:
    return url.strip("/").split("/")[-1]

def fetch_user_content(username):
    user = reddit.redditor(username)
    comments = []
    posts = []

    print(f"Fetching comments for {username}...")
    try:
        for comment in user.comments.new(limit=100):
            comments.append(f"[Comment] {comment.body.strip()}")
    except Exception as e:
        print(f"Error fetching comments: {e}")

    print(f"Fetching posts for {username}...")
    try:
        for post in user.submissions.new(limit=50):
            body = f"[Post] {post.title.strip()}"
            if post.selftext:
                body += f" — {post.selftext.strip()}"
            posts.append(body)
    except Exception as e:
        print(f"Error fetching posts: {e}")

    return comments, posts

def build_prompt(username, comments, posts):
    content = "\n".join(comments[:10] + posts[:10])

    prompt = f"""
You are a user persona analyst.

Below are Reddit posts and comments written by a user named '{username}'.

Please generate a user persona describing:
1. Their probable profession
2. Hobbies and interests
3. Political views (if any)
4. Writing style
5. Tech-savviness
6. Personality traits

For each point, provide a quoted comment or post that supports your analysis.

Reddit User Content:
{content}
    """
    return prompt.strip()

def save_output(username, output):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(output)
    print(f" Persona saved to: {filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python persona_generator.py <reddit_user_profile_url>")
        sys.exit(1)

    url = sys.argv[1]
    username = extract_username_from_url(url)
    comments, posts = fetch_user_content(username)

    if not comments and not posts:
        print("❌ No data found for this user.")
        sys.exit(1)

    print("✅ Reddit content fetched successfully.")
    print("👉 Since persona files are pre-generated with GPT-4, no LLM call will be made.")

if __name__ == "__main__":
    main()
