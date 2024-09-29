from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class ResearchPaper(BaseModel):
    paper_title: Optional[str] = None
    paper_link: Optional[str] = None
    demo_video_link: Optional[str] = None
    project_website: Optional[str] = None


class ResearchProfile(BaseModel):
    google_scholar_link: Optional[str] = None
    personal_website_link: Optional[str] = None
    organization: Optional[str] = None
    title: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    paper: Optional[list[ResearchPaper]] = None


class Config:
    json_schema_extra = {
        "example": {
            "google_scholar_link": "https://scholar.google.com/citations?user=l2g4PFYAAAAJ&hl=en",
            "personal_website_link": "https://www.chingyitsai.com/",
            "organization": "Princeton University",
            "title": "Ph.D. Student",
            "age": 27,
            "sex": "Male",
            "paper": [
                {
                    "paper_title": "Airracket: Perceptual design of ungrounded, directional force feedback to improve virtual racket sports experiences",
                    "paper_link": "https://dl.acm.org/doi/abs/10.1145/3491102.3502034", 
                    "demo_video_link": "https://www.youtube.com/watch?v=UAoQlSbQRYY",
                    "project_website": "https://www.chingyitsai.com/_posts/projects/AirRacket.html", 
                }
            ]
        }
    }
