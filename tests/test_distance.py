# tests/test_lib.py
from mlproject.distance import haversine

def test_distnce():
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 38.73297824127983, -9.14260214286911
    distance = haversine(lon1, lat1, lon2, lat2)

    assert distance > 0
    assert type(distance) == float

    if __name__ == "__main__":
        assert lat1 == 48.865070
        assert lat2 == 38.73297824127983
        assert distance == haversine(lon1, lat1, lon2, lat2)
