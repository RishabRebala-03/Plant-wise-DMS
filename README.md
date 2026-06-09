# Plant-wise Document Intelligence Portal

![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)

![Status](https://img.shields.io/badge/Status-Production_Ready-success)
![Architecture](https://img.shields.io/badge/Architecture-Full_Stack-blue)
![Type](https://img.shields.io/badge/Project-Document_Intelligence-purple)

---

## Overview

PlantWise centralizes document management, project tracking, governance controls, security monitoring, analytics, and executive oversight across multiple plant locations.

Built for mining and industrial environments, the platform enables plant teams to manage operational records while providing leadership with real-time visibility, compliance monitoring, audit readiness, and security controls.

Unlike traditional document repositories, PlantWise combines document workflows, governance policies, analytics, collaboration, and access management into a unified platform.

---

## Core Capabilities

### Document Intelligence

* Plant-wise document management
* Project-linked document workflows
* Version control and history tracking
* Document categorization and search
* Browser preview and download support
* GridFS-based file storage

### Governance & Compliance

* Upload governance policies
* Business-hour upload restrictions
* Audit logging
* Activity monitoring
* Security event tracking
* Compliance-ready reporting

### Plant Operations

* Plant-level dashboards
* Project tracking
* Document readiness monitoring
* Upload activity tracking
* Operational visibility across facilities

### Executive Oversight

* Cross-plant analytics
* Executive review workflows
* CEO comments and notes
* Risk identification
* Stalled-plant detection
* Leadership dashboards

### Collaboration

* Document conversations
* Internal messaging
* Mention-based discussions
* Notifications and alerts
* Executive feedback workflows

### Security & Access Control

* Role-based permissions
* Capability-based access controls
* Session monitoring
* IP restrictions
* Password hashing
* Security alerting
* Client fingerprint validation

---

## User Roles

### Mining Manager

Manage:

* Plant projects
* Document uploads
* Operational records
* Project documentation
* Plant-specific dashboards

### CEO

Access:

* Enterprise-wide visibility
* Plant performance analytics
* Executive oversight dashboards
* Governance reporting
* Cross-plant monitoring

### Administrator

Manage:

* Users
* Access controls
* Governance policies
* Plant master data
* Security settings
* Session monitoring

---

## Technology Stack

### Frontend

* React 19
* TypeScript
* Vite 6
* React Router 7
* Tailwind CSS 4
* Radix UI
* Lucide React
* Recharts
* React Hook Form

### Backend

* Python
* Flask 3
* Flask-CORS
* Gunicorn

### Database & Storage

* MongoDB
* PyMongo
* GridFS

### Security

* bcrypt
* Role-Based Access Control (RBAC)
* Capability-Based Authorization
* IP Governance Rules
* Session Tracking

### Infrastructure

* Docker Compose
* MongoDB 7
* Environment Configuration via python-dotenv

---

## Architecture

```text
React + TypeScript Frontend
            │
            ▼
        Flask APIs
            │
            ▼
MongoDB + GridFS Storage
```

### High-Level Design

* Modern React-based user interface
* Flask REST API backend
* MongoDB document storage
* GridFS file management
* Real-time governance controls
* Role-aware application architecture

---

## Platform Modules

### Document Management

* Upload
* Review
* Versioning
* Search
* Export
* Audit Tracking

### Project Management

* Plant Projects
* Status Tracking
* Document Coverage
* Operational Visibility

### Analytics

* Upload Trends
* Plant Performance
* Category Distribution
* Executive Dashboards

### Security

* Session Monitoring
* IP Access Control
* Audit Logs
* Security Alerts

### Governance

* Upload Policies
* Access Rules
* Business-Hour Controls
* Compliance Monitoring

---

## Business Value

PlantWise improves operational transparency, document traceability, governance enforcement, and executive visibility across distributed facilities.

The platform enables organizations to reduce fragmented document handling, improve compliance readiness, strengthen security controls, and create a structured document lifecycle process.

---

## Future Roadmap

* AI-Powered Document Classification
* Semantic Search & Retrieval
* Automated Compliance Monitoring
* Predictive Operational Insights
* Advanced Executive Reporting
* AI Governance Assistant

---

## Stack Summary

**React 19 + TypeScript + Flask + MongoDB + GridFS + Docker**

An enterprise document intelligence platform built for governance, security, oversight, and operational visibility.
