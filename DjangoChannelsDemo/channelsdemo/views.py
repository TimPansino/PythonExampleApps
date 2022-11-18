from django.http import HttpResponse

from textwrap import dedent

def index(request):
    absolute_url = request.build_absolute_uri().rstrip("/")

    text = dedent(f"""
    <body>
        <p>
            This is a Django Channels demo adapted from https://channels.readthedocs.io/en/latest/tutorial/index.html
        </p>
        <p>
            To connect using websockets, proceed to
        </p>
        <p>
            <a href="{absolute_url}/chatasync/">Async Chatrooms</a>
        </p>
        <p>
            or
        </p>
        <p>
            <a href="{absolute_url}/chatsync/">Sync Chatrooms</a>
        </p>
        <p>
            Both sync and async chatrooms can freely communicate with each other, provided you use the same chat room name.
        </p>
    </body>
    """).strip()

    return HttpResponse(text, content_type="text/html")
