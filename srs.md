# Complete SRS Example (IEEE 830 Format) for Online Library Management System

# SOFTWARE REQUIREMENTS SPECIFICATION

## Online Library Management System (OLMS)

### Version 1.0

## 1. Introduction

### 1.1 Purpose

This SRS describes the functional and non-functional requirements for the Online Library Management System (OLMS). It is intended for use by the development team, testers, project managers, and the library administration (client).

### 1.2 Scope

OLMS is a web-based application that automates the core operations of a college library, including cataloging books, managing member registrations, issuing and returning books, tracking overdue items, and generating reports. The system will replace the existing manual register-based process. It will not handle inter-library loans or e-book licensing in this version.

### 1.3 Definitions, Acronyms, and Abbreviations

- **OLMS:** It refers to the Online Library Management System.
- **Member:** It refers to a registered student or faculty member who can borrow books.
- **Librarian:** It refers to an authorized staff member who manages the system.
- **ISBN:** It refers to International Standard Book Number.

### 1.4 References

- IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications.
- College Library Policy Document, Version 3.2.

### 1.5 Overview

Section 2 provides an overall description of the product. Section 3 specifies detailed functional and non-functional requirements.

## 2. Overall Description

### 2.1 Product Perspective

OLMS is a standalone web application. It interfaces with an existing college student database for member verification. It runs on a web server (Apache/Nginx) with a MySQL database backend and is accessed through standard web browsers.

### 2.2 Product Functions (High-Level)

- Book catalog management (add, update, delete, search).
- Member registration and profile management.
- Book issuing and returning.
- Fine calculation for overdue books.
- Reservation of books currently issued to others.
- Report generation (most borrowed books, overdue list, member activity).

### 2.3 User Characteristics

- **Librarian:** This user has moderate computer literacy and is the primary user who performs all administrative operations.
- **Member (Student/Faculty):** This user has basic computer literacy and uses the system to search the catalog, view their borrowing history, and reserve books.
- **Administrator:** This user is the technical staff responsible for system configuration and user management.

### 2.4 Constraints

- The system must run on the college's existing Linux server infrastructure.
- The system must comply with the college's data privacy policy.
- Maximum budget: NPR 5,00,000.

### 2.5 Assumptions and Dependencies

- Members already have valid college IDs for authentication.
- The college provides a stable internet connection for the server.
- The student database API is available and documented.

## 3. Specific Requirements

### 3.1 Functional Requirements

**FR-01: Search Book.** The system shall allow members and librarians to search the catalog by title, author, ISBN, or category. Search results shall display book title, author, availability status, and shelf location.

**FR-02: Add New Book.** The system shall allow the librarian to add a new book by entering title, author(s), ISBN, publisher, edition, category, quantity, and shelf location.

**FR-03: Register Member.** The system shall allow the librarian to register a new member by entering name, college ID, department, contact number, and email. The system shall verify the college ID against the student database.

**FR-04: Issue Book.** The system shall allow the librarian to issue a book to a member. The system shall verify: (a) the member's account is active, (b) the member has not exceeded the borrowing limit (max 3 books), and (c) the book is available. Upon issuing, the system shall record the issue date, set the due date (14 days), and update the book's availability status.

**FR-05: Return Book.** The system shall allow the librarian to process a book return. If the book is overdue, the system shall automatically calculate the fine (NPR 5 per day). The system shall update the book's status to "available."

**FR-06: Reserve Book.** The system shall allow a member to reserve a book that is currently issued. When the book is returned, the system shall notify the reserving member via email.

**FR-07: Generate Reports.** The system shall generate the following reports: (a) list of overdue books with member details, (b) most borrowed books in a given period, (c) member borrowing history.

**FR-08: User Login.** The system shall authenticate users (librarian, member, admin) using college ID and password. Passwords shall be hashed before storage.

### 3.2 External Interface Requirements

**User Interface.** The system shall provide a responsive web interface accessible on desktop browsers (Chrome, Firefox, Edge). The librarian dashboard shall display pending returns and overdue alerts on the home screen.

**Hardware Interface.** The system shall interface with a barcode scanner for reading book ISBNs and member IDs during issue/return operations.

**Software Interface.** The system shall connect to the college student database via a REST API to verify member registration.

**Communication Interface.** The system shall send email notifications (overdue reminders, reservation availability) via SMTP.

### 3.3 Performance Requirements

- The system shall support at least 100 concurrent users.
- Search results shall be displayed within 2 seconds.
- Book issue/return transactions shall complete within 3 seconds.

### 3.4 Design Constraints

- The system shall be developed using HTML/CSS, JavaScript (frontend) and Python/Django (backend) with MySQL database.
- The system shall follow a three-tier architecture (presentation, application, data).

### 3.5 Non-Functional Requirements

- **Reliability:** The system shall have 99% uptime during library operating hours from 8 AM to 8 PM.
- **Security:** Only authenticated librarians shall issue or return books. All passwords shall be stored using bcrypt hashing. The system shall enforce session timeout after 15 minutes of inactivity.
- **Usability:** A new librarian shall be able to issue a book within 2 minutes of first use without external assistance.
- **Maintainability:** The codebase shall follow MVC architecture with documented APIs to allow future enhancements such as e-book support.
- **Portability:** The system shall be deployable on any Linux server with Python 3.8+ and MySQL 8.0+.
