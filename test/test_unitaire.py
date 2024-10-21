import sys
import os

from server import app
from .config import client

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'),
    ),
)

def test_index(client):
    response= client.get('/')
    assert response.status_code == 200
    assert b'your secretary' in response.data

def test_show_summary_valid_email(client):
    response = client.post('/showSummary',data={'email':'admin@irontemple.com'})
    assert response.status_code == 200
    assert b'Iron Temple' in response.data

def test_show_summary_wrong_email(client):
    response = client.post('/showSummary',data={'email':'admin@irontemple.comm'})
    assert response.status_code == 200
    assert b'Email introuvable' in response.data    