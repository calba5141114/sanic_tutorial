from sanic import Sanic
from sanic.response import json

app = Sanic()

cat_list = []


class Cat(object):

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "weight": self.weight
        }


@app.route("create_cat", methods=["POST"])
async def create_cat(request):
    try:
        data = request.json
        cat = Cat(data["name"], data["age"], data["weight"])
        cat_list.append(cat)
        return json(cat, status=201)
    except Exception as error:
        print(error)
        return json({"message": "cat creation failed"}, status=500)


@app.route("get_cats", methods=["GET"])
async def get_cats(request):
    try:
        return json(cat_list, status=200)
    except Exception as error:
        print(error)
        return json({"message": "getting cats failed"}, status=500)


if __name__ == "__main__":
    # python3 server.py
    app.run(host="0.0.0.0", port=3000)
