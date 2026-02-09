import pytest


def test_unregister_success(client, reset_activities):
    """Test successful unregistration from an activity"""
    email = "michael@mergington.edu"  # Already signed up for Chess Club
    
    response = client.delete(
        f"/activities/Chess Club/unregister?email={email}"
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert email in data["message"]
    assert "Chess Club" in data["message"]


def test_unregister_removes_participant(client, reset_activities):
    """Test that unregister actually removes the participant"""
    email = "michael@mergington.edu"
    
    # Unregister
    client.delete(f"/activities/Chess Club/unregister?email={email}")
    
    # Check if participant was removed
    response = client.get("/activities")
    data = response.json()
    assert email not in data["Chess Club"]["participants"]


def test_unregister_nonexistent_activity(client, reset_activities):
    """Test unregister from non-existent activity returns 404"""
    response = client.delete(
        "/activities/Nonexistent Club/unregister?email=student@mergington.edu"
    )
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_student_not_signed_up(client, reset_activities):
    """Test unregister for student not signed up returns 400"""
    email = "notstudent@mergington.edu"  # Not signed up for anything
    
    response = client.delete(
        f"/activities/Chess Club/unregister?email={email}"
    )
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_then_signup_again(client, reset_activities):
    """Test that a student can signup again after unregistering"""
    email = "michael@mergington.edu"
    
    # Unregister
    client.delete(f"/activities/Chess Club/unregister?email={email}")
    
    # Signup again
    response = client.post(
        f"/activities/Chess Club/signup?email={email}"
    )
    assert response.status_code == 200
    
    # Verify they were re-added
    response = client.get("/activities")
    data = response.json()
    assert email in data["Chess Club"]["participants"]
