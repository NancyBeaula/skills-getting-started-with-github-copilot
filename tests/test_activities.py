import pytest


def test_get_activities(client, reset_activities):
    """Test getting all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    
    data = response.json()
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data
    assert "Debate Team" in data
    assert "Art Club" in data
    assert "Basketball Team" in data


def test_get_activities_has_correct_structure(client, reset_activities):
    """Test that activity data has correct structure"""
    response = client.get("/activities")
    data = response.json()
    
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)
