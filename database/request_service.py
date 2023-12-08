from database.models import Request
from database import get_db
import openai


def add_request(request):
    db = next(get_db())
    req = Request(request=request)
    OPENAI_API_KEY = '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'
    openai.api_key = OPENAI_API_KEY
    if req:
        db.add(req)
        db.commit()
    else:
        return False

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request,
        max_tokens=2500
    )

    if response.choices:
        bot_reply = response.choices[0].text.strip()
        return {'status': 1,
                'message': bot_reply}

    else:
        return {'status': 0,
                'message': 'ОЙ, попробуйте в следующий раз...'}

