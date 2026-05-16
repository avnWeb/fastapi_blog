import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "May 16, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better",
        "date_posted": "May 17, 2026",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
async def home():
    return f"<h1>{posts[0]["title"]}</h1>"


@app.get("/api/posts")
async def get_posts():
    return posts


# if __name__ == "__main__":
#     asyncio.run(home())
