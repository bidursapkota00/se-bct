## SOFTWARE REQUIREMENTS SPECIFICATION

## Online Library Management System (OLMS)

### Version 2.0

## 1. Introduction

### 1.1 Purpose

This SRS describes the functional and non-functional requirements for the Online Library Management System (OLMS). It is intended for use by the development team, testers, project managers, and the library administration (client).

### 1.2 Scope

OLMS is a web-based application that automates the core operations of a college library, including cataloging books, managing member registrations, issuing and returning books, tracking overdue items, and generating reports. The system will replace the existing manual register-based process.

### 1.3 Definitions, Acronyms, and Abbreviations

- **OLMS:** Online Library Management System.
- **Member:** A registered student or faculty member who can borrow books.
- **Librarian:** An authorized staff member who manages the system.
- **ISBN:** International Standard Book Number.
- **RBAC:** Role-Based Access Control.

### 1.4 References

- IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications.
- College Library Policy Document, Version 3.2.

### 1.5 Overview

Section 2 provides an overall description of the product.

Section 3 specifies detailed functional and non-functional requirements compliant with the IEEE Std 830-1998 structural layout, utilizing Use Case specifications for functional behaviors.

<div style="page-break-after: always;"></div>

## 2. Overall Description

### 2.1 Product Perspective

OLMS is a standalone web application. It interfaces with an existing college student database for member verification. It runs on a web server (Apache/Nginx) with a MySQL database backend and is accessed through standard web browsers.

### 2.2 Product Functions

- Book catalog management (add, update, delete, search).
- Member registration and profile management.
- Book issuing and returning.
- Fine calculation for overdue books.
- Reservation of books currently issued to others.
- Report generation (most borrowed books, overdue list, member activity).

### 2.3 User Characteristics

- **Librarian:** The primary administrative user. Expected to have the ability to operate standard web browsers, use peripheral devices (barcode scanners), and perform data entry.
- **Member (Student/Faculty):** Expected to have basic familiarity with web navigation to utilize search functions and web forms.
- **Administrator:** The technical staff responsible for system configuration, server maintenance, and top-level user management.

### 2.4 Constraints

- The system must run on the college's existing Linux server infrastructure.
- The system must comply with the college's data privacy policy.
- Maximum budget: NPR 5,00,000.

### 2.5 Assumptions and Dependencies

- Members already have valid college IDs for authentication.
- The college provides a stable, continuous internet connection for the server.
- The student database REST API is highly available and fully documented.

### 2.6 Apportioning of Requirements

Features such as inter-library loans and e-book licensing are not included in the current version of the system and are deferred to future releases.

<div style="page-break-after: always;"></div>

## 3. Specific Requirements

### 3.1 External Interface Requirements

#### 3.1.1 User Interfaces

The system shall provide a responsive HTML5/CSS3 web interface accessible on standard desktop browsers (Chrome, Firefox, Edge). The librarian dashboard shall display a summary widget for pending returns and overdue alerts upon successful login.

#### 3.1.2 Hardware Interfaces

The system shall interface via USB/Bluetooth with standard barcode scanners to read book ISBNs and member IDs directly into text input fields during issue/return operations.

#### 3.1.3 Software Interfaces

The system shall connect to the college student database via a REST API. The API will accept a `StudentID` parameter and return a JSON payload confirming student enrollment status.

#### 3.1.4 Communications Interfaces

The system shall utilize SMTP over TLS (Port 587) to send email notifications (overdue reminders, reservation availability) to users.

---

### 3.2 Functional Requirements (Use Case Specifications)

#### UC-01: Search Catalog

| Element           | Details                                                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actors**        | Member, Librarian                                                                                                                                                                                                                                                   |
| **Precondition**  | User has accessed the OLMS search portal.                                                                                                                                                                                                                           |
| **Main Flow**     | 1. User enters search criteria (Title, Author, ISBN, or Category).<br>2. User submits the search query.<br>3. System queries the catalog database.<br>4. System displays a list of matching books including Title, Author, Availability Status, and Shelf Location. |
| **Exceptions**    | 1. No Match Found: System displays a "No books found matching your criteria" message and suggests checking spelling or broadening the search.                                                                                                                   |
| **Postcondition** | Relevant book information is displayed to the user.                                                                                                                                                                                                                 |
| **Priority**      | Essential                                                                                                                                                                                                                                                           |

#### UC-02: Add New Book

| Element           | Details                                                                                                                                                                                                                                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Actors**        | Librarian                                                                                                                                                                                                                                                                                                                      |
| **Precondition**  | Librarian is logged in and navigated to the Catalog Management module.                                                                                                                                                                                                                                                         |
| **Main Flow**     | 1. Librarian enters book details (Title, Author, ISBN, Publisher, Edition, Category, Quantity, Shelf Location).<br>2. Librarian submits the form.<br>3. System validates the ISBN against existing records.<br>4. System saves the new book record to the database.<br>5. System displays a "Successfully Added" confirmation. |
| **Exceptions**    | 1. Duplicate ISBN: System halts the save operation, displays "Error: Book with this ISBN already exists," and highlights the conflicting field.                                                                                                                                                                            |
| **Postcondition** | The new book is available in the catalog and can be searched or issued.                                                                                                                                                                                                                                                        |
| **Priority**      | Essential                                                                                                                                                                                                                                                                                                                      |

#### UC-03: Register Member

| Element           | Details                                                                                                                                                                                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Actors**        | Librarian                                                                                                                                                                                                                                                                                                                                  |
| **Precondition**  | Librarian is logged in and navigated to the Member Management module.                                                                                                                                                                                                                                                                      |
| **Main Flow**     | 1. Librarian enters member details (Name, College ID, Department, Contact Number, Email).<br>2. Librarian submits the registration form.<br>3. System pings the Student Database REST API with the College ID.<br>4. API confirms active enrollment.<br>5. System creates a local Member Profile.<br>6. System displays a success message. |
| **Exceptions**    | 1. Invalid/Inactive ID: The REST API returns 'Inactive' or 'Not Found'. System aborts registration and displays: "Error: Invalid or Inactive College ID."                                                                                                                                                                              |
| **Postcondition** | Member is successfully registered and granted borrowing privileges.                                                                                                                                                                                                                                                                        |
| **Priority**      | Essential                                                                                                                                                                                                                                                                                                                                  |

#### UC-04: Issue Book

| Element           | Details                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actors**        | Librarian                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Precondition**  | Librarian is logged in; the book is physically present at the desk.                                                                                                                                                                                                                                                                                                                                                                 |
| **Main Flow**     | 1. Librarian inputs/scans the Member ID.<br>2. Librarian inputs/scans the Book ISBN.<br>3. System verifies the Member account is Active.<br>4. System verifies the Member has borrowed fewer than 3 books.<br>5. System verifies the Book is 'Available'.<br>6. System updates book status to 'Issued'.<br>7. System records the Issue Date and sets Due Date (Current Date + 14 days).<br>8. System displays success confirmation. |
| **Exceptions**    | 1. Member Inactive: System displays "Error: Member account is inactive/suspended."<br>2. Limit Exceeded: System displays "Error: Member has reached the maximum borrowing limit of 3 books."<br>3. Book Unavailable: System displays "Error: Book is currently unavailable."                                                                                                                                            |
| **Postcondition** | The transaction is recorded, and the physical book is handed to the member.                                                                                                                                                                                                                                                                                                                                                         |
| **Priority**      | Essential                                                                                                                                                                                                                                                                                                                                                                                                                           |

#### UC-05: Return Book

| Element           | Details                                                                                                                                                                                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Actors**        | Librarian                                                                                                                                                                                                                                                                                                                |
| **Precondition**  | Librarian is logged in; the physical book is returned to the desk.                                                                                                                                                                                                                                                       |
| **Main Flow**     | 1. Librarian inputs/scans the Book ISBN.<br>2. System retrieves the active transaction record.<br>3. System compares Current Date against Due Date (verifies it is not overdue).<br>4. System closes the transaction record.<br>5. System updates book status to 'Available'.<br>6. System displays return confirmation. |
| **Exceptions**    | 1. Book Overdue: System detects Current Date > Due Date. System calculates fine (Days Overdue × NPR 5), posts the fine amount to the Member Account ledger, alerts the Librarian of the fine, and then proceeds to steps 4-6.                                                                                        |
| **Postcondition** | Book status is 'Available' (triggering any pending reservation emails), and transaction is closed.                                                                                                                                                                                                                       |
| **Priority**      | Essential                                                                                                                                                                                                                                                                                                                |

#### UC-06: Reserve Book

| Element           | Details                                                                                                                                                                                                                                                        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Actors**        | Member                                                                                                                                                                                                                                                         |
| **Precondition**  | Member is logged in; the desired book is currently marked as 'Issued'.                                                                                                                                                                                         |
| **Main Flow**     | 1. Member clicks "Reserve Book" on the catalog details page.<br>2. System confirms the book is eligible for reservation.<br>3. System flags the book with a reservation tag linked to the Member ID.<br>4. System displays a "Reservation Successful" message. |
| **Exceptions**    | 1. Queue Full: If the system is configured with a maximum reservation queue and it is full, display "Reservation queue is currently full for this item."                                                                                                   |
| **Postcondition** | Member is added to the reservation queue. When UC-05 (Return Book) is executed on this item, an automated email is triggered.                                                                                                                                  |
| **Priority**      | Conditional: Only applicable when the requested book is currently issued to another member.                                                                                                                                                                     |

---

### 3.3 Performance Requirements

- **PR-01:** The system backend and database shall comfortably support a minimum of 100 concurrent active sessions.
- **PR-02:** Search queries (UC-01) shall execute and render UI results within 2.0 seconds under the peak load of 100 concurrent users.
- **PR-03:** Transactional database commits for Book Issue (UC-04) and Return (UC-05) shall complete within 3.0 seconds under the peak load of 100 concurrent users.

### 3.4 Design Constraints

- **DC-01:** The frontend shall utilize HTML5, CSS3, and vanilla JavaScript.
- **DC-02:** The backend logic shall be built using Python 3.8+ and the Django Web Framework.
- **DC-03:** The primary data store shall be MySQL 8.0+.
- **DC-04:** The system architecture must adhere strictly to the Model-View-Controller (MVC) design pattern.

### 3.5 Software System Attributes

#### 3.5.1 Reliability

The system shall maintain an uptime of 99% during core library operating hours (08:00 to 20:00 NPT).

#### 3.5.2 Security & Authorization

- **Authentication:** All users must authenticate via College ID and password.
- **Data Protection:** All passwords shall be hashed prior to database storage using the `bcrypt` cryptographic algorithm.
- **Session Management:** The system shall automatically terminate user sessions and require re-authentication after 15 minutes of inactivity.
- **Role-Based Access Control (RBAC):**
- _Members_ have read-only access to catalogs and write-access only to their personal reservation queue.
- _Librarians_ have read/write access to catalog management, member profiles, and transaction processing.

#### 3.5.3 Usability

The UI workflow for UC-04 (Issue Book) shall be streamlined so that a newly trained librarian can complete a transaction in under 3 clicks and 2 minutes of active interface time.

#### 3.5.4 Maintainability

The application shall document all internal application programming interfaces (APIs) to facilitate future modular integrations, such as third-party payment gateways for fines or e-book DRM modules.

#### 3.5.5 Portability

The system codebase shall be containerized (e.g., Docker) to ensure it is OS-agnostic and deployable on any standard Linux distribution supporting Python 3.8 and MySQL 8.0.

### 3.6 Other Requirements

#### 3.6.1 Logical Database Requirements

- **DB-01: Core Entities:** The database shall be normalized to at least 3NF, containing distinct relational tables for `Members`, `Books`, `Transactions`, and `Fines`.
- **DB-02: Data Retention:** System logs, transaction histories, and fine ledgers must be retained persistently for a minimum of 3 calendar years to comply with college auditing standards.
- **DB-03: Integrity Constraints:** The system shall restrict the deletion of a `Book` row via foreign key constraints if it is currently tied to an open `Transaction` record.
