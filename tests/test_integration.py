import requests


def test_services() -> None:
    # given
    ping_service_url = 'http://localhost:8080/api/v1/ping'
    receiver_service_url = 'http://ReceiverService:8080/api/v1/info'
    ping_service_payload = {
        'url': receiver_service_url,
    }

    # when
    response = requests.post(ping_service_url, json=ping_service_payload, timeout=1.0)

    # then
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() == {
        'Receiver': 'Cisco is the best!'
    }
