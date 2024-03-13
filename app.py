from flask import Flask, jsonify
import asyncio
import aiohttp

app = Flask(__name__)

@app.route("/")
def bringKanyeQuote():
    url = "https://api.kanye.rest/json"

    async def fetch_kanye():
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as respuesta:
                if respuesta.ok:
                    return await respuesta.json()
                else:
                    return None

    loop = asyncio.new_event_loop() 
    asyncio.set_event_loop(loop)
    kanyeQuote = loop.run_until_complete(fetch_kanye())

    if kanyeQuote:
        # returns the Kanye quote on json format on the browser
        return jsonify(kanyeQuote)
    else:
        return "Something went wrong :("

if __name__ == "__main__":
    app.run(debug=True)


