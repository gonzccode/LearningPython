import requests as http


def test_get_transactions():
    r = http.get("http://127.0.0.1:8000/transactions")
    data = r.json()
    assert data == {"message": "get all my movements"}


def test_one_transactions():
    r = http.get("http://127.0.0.1:8000/transaction/5")
    data = r.json()
    assert data == {"message": "get all my movements 5"}