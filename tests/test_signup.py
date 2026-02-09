import pytest


def test_signup_for_activity_success(client, reset_activities):
    """Test successful signup for an activity"""
    response = client.post(
        "/activities/Chess Club/signup?email=newstudent@mergington.edu"
    )
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "newstudent@mergington.edu" in data["message"]
    assert "Chess Club" in data["message"]


def test_signup_adds_participant(client, reset_activities):
    """Test that signup actually adds the participant to the activity"""
    email = "newstudent@mergington.edu"
    
    # Signup
    client.post(f"/activities/Chess Club/signup?email={email}")
    
    # Check if participant was added
    response = client.get("/activities")
    data = response.json()
    assert email in data["Chess Club"]["participants"]


def test_signup_nonexistent_activity(client, reset_activities):
    """Test signup for non-existent activity returns 404"""
    response = client.post(
        "/activities/Nonexistent Club/signup?email=student@mergington.edu"
    )
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_duplicate_student(client, reset_activities):
    """Test that duplicate signup returns 400 error"""
    email = "michael@mergington.edu"  # Already signed up for Chess Club
    
    response = client.post(
        f"/activities/Chess Club/signup?email={email}"
    )
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_same_student_different_activity(client, reset_activities):
    """Test that same student can signup for different activities"""
    email = "michael@mergington.edu"  # Already signed up for Chess Club
    
    response = client.post(
        f"/activities/Programming Class/signup?email={email}"
    )
    assert response.status_code == 200
    
    # Verify they were added
    response = client.get("/activities")
    data = response.json()
    assert email in data["Programming Class"]["participants"]
