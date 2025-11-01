# OctoFit Tracker AI Agent Instructions

This document provides essential guidance for AI agents working on the OctoFit Tracker project, a fitness tracking application for Mergington High School.

## Project Architecture

### Stack Overview
- Frontend: React.js application (`octofit-tracker/frontend/`)
- Backend: Django REST API (`octofit-tracker/backend/`)
- Database: MongoDB
- Development Environment: GitHub Codespaces

### Project Structure
```
octofit-tracker/
├── backend/
│   ├── venv/              # Python virtual environment
│   └── octofit_tracker/   # Django project root
└── frontend/              # React application root
```

## Critical Workflows

### Environment Setup
1. Python virtual environment must be created and activated:
   ```bash
   python3 -m venv octofit-tracker/backend/venv
   source octofit-tracker/backend/venv/bin/activate
   ```

2. Install backend dependencies from requirements.txt:
   ```bash
   pip install -r octofit-tracker/backend/requirements.txt
   ```

### Port Configuration
- Backend (Django): Port 8000 (public)
- Frontend (React): Port 3000 (public)
- MongoDB: Port 27017 (private)

## Project-Specific Conventions

### Directory Management
- Never change directories when in agent mode
- Always use absolute paths when running commands
- Point to specific directories in commands instead of changing into them

### MongoDB Integration
- Always use Django's ORM for database operations
- Never write direct MongoDB scripts
- Use `ps aux | grep mongod` to check MongoDB server status

### Django Project Dependencies
Specific version requirements must be maintained:
- Django 4.1.7
- djangorestframework 3.14.0
- djongo 1.3.6 (for MongoDB integration)
- pymongo 3.12

## Cross-Component Communication

### Frontend-Backend Integration
- Backend exposes REST API endpoints via Django REST framework
- Frontend React components consume these endpoints
- CORS headers are configured for frontend-backend communication

### Authentication Flow
- Uses django-allauth (0.51.0) for user authentication
- JWT-based authentication via dj-rest-auth (2.2.6)

## Reference Files
- Backend setup: `.github/instructions/octofit_tracker_django_backend.instructions.md`
- Frontend configuration: `.github/instructions/octofit_tracker_react_frontend.instructions.md`
- Project setup: `.github/instructions/octofit_tracker_setup_project.instructions.md`