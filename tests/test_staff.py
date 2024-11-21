from client import client

# This is the test for the staff router. It serves as an example for the other routers.


def test_staff():
    response = client.post(
        "/staff",
        json={
            "data": {
                "username": "teststaff",
                "password": "testpassword",
                "email": "teststaff@gmail.com",
            }
        },
    )

    assert response.status_code == 201
    assert response.json()["data"]["username"] == "teststaff"
    assert response.json()["data"]["email"] == "teststaff@gmail.com"

    print("Staff created successfully!")

    # get staff
    response = client.get("/staff")
    first = response.json()["data"][0]

    assert response.status_code == 200

    print("Staff retrieved successfully!")

    # delete staff
    response = client.delete(f"/staff/{first['id']}")
    assert response.status_code == 200

    print("Staff deleted successfully!")


if __name__ == "__main__":
    test_staff()
