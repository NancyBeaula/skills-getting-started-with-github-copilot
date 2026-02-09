import pytest
import sys
from pathlib import Path

# Add src directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to original state after each test"""
    from app import activities
    
    original = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and critical thinking skills",
            "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore painting, drawing, and creative expression",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Train and compete in basketball",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["james@mergington.edu"]
        }
    }
    
    yield
    
    # Reset activities
    activities.clear()
    activities.update(original)
