# Software Engineering — Practical Guide

---

## Practical 1: Preparation and Organization of SRS Using Standard Templates

**Duration:** 2 hours

### Objective

Prepare a complete Software Requirements Specification (SRS) document for a chosen project using the IEEE 830-based standard template.

### Tool Setup

**Option A — Google Docs / MS Word:** No installation needed. Use heading styles to structure sections. Best for collaborative editing.

**Option B — Markdown + VS Code:** Install VS Code from https://code.visualstudio.com. Install the "Markdown All in One" extension. Create a file named `SRS.md`. Markdown is version-control-friendly and can be converted to PDF via extensions.

Pick a project domain first. Common choices: Library Management System, Online Food Ordering System, Hospital Management System, E-Commerce Platform, Student Attendance System.

### MS Word Formatting Guidelines

Follow these formatting rules when preparing the SRS in Microsoft Word:

**Page Layout:**

- **Margins:** 1 inch (2.54 cm) on all sides — Top, Bottom, Left, Right. Set via Layout > Margins > Normal.
- **Paper size:** A4 (210 × 297 mm).
- **Orientation:** Portrait.
- **Line spacing:** 1.15 or 1.5 for body text. Set via Home > Line Spacing.

**Font Settings:**

- **Body text:** Times New Roman, 12 pt. Left-aligned (not justified).
- **Heading 1** (main sections like "1. Introduction"): Times New Roman, 16 pt, Bold.
- **Heading 2** (subsections like "1.1 Purpose"): Times New Roman, 14 pt, Bold.
- **Heading 3** (sub-subsections like "3.1.1 User Interfaces"): Times New Roman, 12 pt, Bold.
- **Figure/Table captions:** Times New Roman, 10 pt, Centered below figures, above tables.
- Apply these using the **Styles gallery** on the Home tab — do not manually bold/resize each heading individually. Using Styles allows auto-generation of Table of Contents.

**Page Numbering (Roman + Arabic):**

The SRS uses two numbering schemes, separated by a **section break**:

- **Front matter** (Title Page, Table of Contents, List of Figures) — lowercase Roman numerals: i, ii, iii, iv...
- **Main body** (from "1. Introduction" onward) — Arabic numerals starting from 1: 1, 2, 3, 4...
- **Title page** has no page number.

**How to set up in Word:**

1. Type out the Title Page and Table of Contents pages.
2. After the last front-matter page, go to Layout > Breaks > **Next Page** (Section Break).
3. Double-click the footer area of the front-matter section. Insert > Page Number > Bottom of Page. Right-click the page number > Format Page Numbers > Number format: **i, ii, iii**. Start at: **i**.
4. Move to the footer of the main body section. Click **Link to Previous** to unlink it from the front matter footer.
5. Right-click the page number > Format Page Numbers > Number format: **1, 2, 3**. Start at: **1**.
6. On the Title Page footer, simply delete the page number.

**Title Page Must Include:**

- Document title: "Software Requirements Specification"
- Project/System name: e.g., "Library Management System"
- Team members / Author names with roll numbers
- Date of submission
- Course name and instructor name
- College/University name

**Table of Contents:**

After formatting all headings with Styles, go to References > Table of Contents > Automatic Table 1. Word auto-generates a clickable TOC. Right-click it > Update Field to refresh after edits.

**Other Formatting Rules:**

- Number all figures and tables sequentially: Figure 1, Figure 2, Table 1, Table 2.
- Use consistent bullet styles (disc for level 1, circle for level 2).
- Start each major section (1, 2, 3, 4) on a new page — insert a page break before each.
- Include a **Revision History** table on the page after the title page.

| Version | Date       | Author | Description                       |
| ------- | ---------- | ------ | --------------------------------- |
| 1.0     | 2026-05-13 | Team A | Initial draft                     |
| 1.1     | 2026-05-20 | Team A | Added non-functional requirements |

---

### SRS Template (IEEE 830-Based)

Use the following structure. Every section must be filled — leave nothing blank. If a section is genuinely not applicable, write "N/A" with a brief justification.

---

**1. Introduction**

**1.1 Purpose** — State the purpose of this SRS document and the intended software product. Example: "This document specifies the functional and non-functional requirements for a Library Management System (LMS) to be developed for XYZ College."

**1.2 Document Conventions** — Describe any notation, formatting, or priority conventions used. Example: "Requirements are numbered as REQ-F-xx for functional and REQ-NF-xx for non-functional. Priority levels: High, Medium, Low."

**1.3 Intended Audience** — List who will read this document: developers, testers, project managers, instructors. Briefly describe what each audience should focus on.

**1.4 Product Scope** — A concise description (3-5 sentences) of what the software does, its goals, and its boundaries (what it will NOT do).

**1.5 References** — List all referenced documents, standards, URLs. At minimum, cite the IEEE 830 standard and any domain-specific material.

---

**2. Overall Description**

**2.1 Product Perspective** — Is this a standalone system or part of a larger system? Include a simple context diagram or block diagram showing the system and its external interfaces.

**2.2 Product Functions** — A bulleted summary of the major functions. Do not go into detail — just list the high-level features (5-10 bullets). Example for LMS: Issue book, Return book, Search catalog, Manage members, Generate reports, Send overdue notifications.

**2.3 User Classes and Characteristics** — Define all user types and their technical expertise. Example: Admin (full access, technically proficient), Librarian (moderate access, trained), Student (limited access, minimal training expected).

**2.4 Operating Environment** — Specify: OS (Windows/Linux/macOS), browser requirements (if web-based), database (MySQL/PostgreSQL/SQLite), server (Apache/Nginx), programming language/framework.

**2.5 Design and Implementation Constraints** — List any constraints: specific language required, database choice, regulatory requirements (e.g., data privacy), hardware limitations.

**2.6 User Documentation** — What documentation will be provided? User manual, inline help, FAQ, video tutorial.

**2.7 Assumptions and Dependencies** — List assumptions (e.g., "Users have reliable internet access") and dependencies (e.g., "System depends on a third-party payment gateway").

---

**3. Specific Requirements**

**3.1 External Interface Requirements**

- **User Interfaces** — Describe the UI approach: web-based forms, mobile app screens, CLI. Mention any UI standards or frameworks (e.g., responsive design, Bootstrap).
- **Hardware Interfaces** — Barcode scanner, printer, biometric device, etc. Write "N/A" if none.
- **Software Interfaces** — APIs, external databases, third-party services (e.g., email service, payment gateway). Specify name, version, and purpose.
- **Communication Interfaces** — Network protocols (HTTP/HTTPS, SMTP for email), data formats (JSON, XML).

**3.2 Functional Requirements** — This is the core section. Write each requirement as a separate entry with:

- **ID** (e.g., REQ-F-01)
- **Title** (e.g., "User Registration")
- **Description** (1-3 sentences: input, processing, output)
- **Priority** (High / Medium / Low)

Example:

```
REQ-F-01: User Registration
The system shall allow a new user to register by providing name, email,
phone number, and password. The system shall validate email uniqueness
and send a confirmation email upon successful registration.
Priority: High
```

Write at least 10-15 functional requirements for a meaningful SRS.

**3.3 Non-Functional Requirements** — Cover the following categories with specific, measurable statements:

- **Performance:** "The system shall load any page within 2 seconds under normal load (up to 100 concurrent users)."
- **Security:** "All passwords shall be stored using bcrypt hashing. All data transmission shall use HTTPS."
- **Reliability:** "The system shall have 99.5% uptime during operating hours."
- **Usability:** "A new user shall be able to complete the registration process without external help within 3 minutes."
- **Scalability:** "The system shall support up to 10,000 registered users without degradation."
- **Maintainability:** "The codebase shall follow MVC architecture to allow independent modification of layers."

**3.4 Design Constraints** — Reiterate any technical restrictions that affect design choices.

---

**4. Appendices**

- **Glossary** — Define all domain-specific terms and acronyms used in the document.
- **Analysis Models** — Attach or reference any diagrams: Use Case Diagram, Context-Level DFD, ER Diagram. (These will be developed in Practical 2.)

---

### Complete SRS Example: Library Management System

The following is a complete, filled-out SRS that can be used as a direct reference. Copy this structure and adapt it to your own project.

---

**Software Requirements Specification**
**Library Management System (LMS)**
Version 1.0 | Date: 2026-05-13 | Author: Team A

---

**1. Introduction**

**1.1 Purpose**

This document specifies the complete software requirements for the Library Management System (LMS) to be developed for ABC Engineering College. It serves as the primary reference for developers, testers, and the project supervisor. The LMS will automate book issuing, returning, cataloging, and member management.

**1.2 Document Conventions**

- Functional requirements are labeled REQ-F-01, REQ-F-02, etc.
- Non-functional requirements are labeled REQ-NF-01, REQ-NF-02, etc.
- Priority levels: **High** (must have), **Medium** (should have), **Low** (nice to have).
- "The system shall..." is used for mandatory requirements. "The system should..." is used for desirable features.

**1.3 Intended Audience**

- **Developers:** Focus on Sections 3.1 and 3.2 for interface and functional details.
- **Testers:** Focus on Sections 3.2 and 3.3 to derive test cases.
- **Project Supervisor:** Focus on Sections 1 and 2 for scope and feasibility.
- **End Users (Librarians):** Focus on Section 2.2 for a summary of features.

**1.4 Product Scope**

The LMS is a web-based application that allows librarians to manage the college library's book catalog, issue and return books, manage member records, track overdue books, and generate reports. Students can search the catalog, view their borrowing history, and check book availability. The system does NOT handle inter-library loans, e-book management, or online payment processing.

**1.5 References**

- IEEE 830-1998, Recommended Practice for Software Requirements Specifications.
- Pressman, R. S. (2019). Software Engineering: A Practitioner's Approach, 9th Edition.
- ABC Engineering College Library Policy Manual, 2025.

---

**2. Overall Description**

**2.1 Product Perspective**

The LMS is a standalone web application. It replaces the current manual register-based system. It interfaces with a web browser (client), a backend server, and a relational database. It does not interface with any external third-party systems in the initial release.

**2.2 Product Functions**

- User registration and authentication (Librarian and Student roles)
- Add, update, delete, and search books in the catalog
- Issue books to registered students
- Process book returns and calculate overdue fines
- View borrowing history for each student
- Generate reports (most borrowed books, overdue list, member activity)
- Send email notifications for overdue books

**2.3 User Classes and Characteristics**

- **Admin:** Full system access. Manages librarian accounts and system settings. Technically proficient.
- **Librarian:** Manages books, issues/returns, and generates reports. Moderate technical skill; requires minimal training.
- **Student:** Searches catalog, views own borrowing history, and checks availability. Minimal technical skill expected.

**2.4 Operating Environment**

- **Server OS:** Ubuntu 22.04 LTS or Windows Server 2022.
- **Client:** Any modern web browser (Chrome, Firefox, Edge) on desktop or mobile.
- **Backend:** Python 3.11, FastAPI framework.
- **Database:** SQLite for development; PostgreSQL 15 for production.
- **Web Server:** Uvicorn (development), Nginx + Uvicorn (production).

**2.5 Design and Implementation Constraints**

- The system must be developed using Python and FastAPI as mandated by the course.
- The database must be a relational database (SQLite or PostgreSQL).
- The application must be deployable in a Docker container.
- All source code must be maintained in a Git repository.

**2.6 User Documentation**

- A user manual (PDF) describing all features with screenshots.
- Inline help tooltips on the web interface for key actions.
- API documentation auto-generated by FastAPI Swagger UI at `/docs`.

**2.7 Assumptions and Dependencies**

- Users have access to a modern web browser and reliable internet connectivity.
- The college provides a server for deployment (or a cloud VM is available).
- Students have been assigned a valid college email address for registration.
- The SMTP server for sending email notifications is available and configured.

---

**3. Specific Requirements**

**3.1 External Interface Requirements**

**3.1.1 User Interfaces**

The system provides a responsive web interface built with HTML, CSS, and JavaScript. The interface includes a login page, a dashboard (different views for Admin, Librarian, Student), a book catalog search page, an issue/return form, and a reports page. All pages follow a consistent navigation layout with a sidebar menu and a top header bar.

**3.1.2 Hardware Interfaces**

- Barcode scanner (optional): For scanning book ISBN during issue/return. Connected via USB; input is treated as keyboard input.
- Standard printer: For printing reports. No special driver integration required — uses browser print functionality.

**3.1.3 Software Interfaces**

- **SQLite / PostgreSQL:** Database for persistent storage of all book, member, and transaction records.
- **SMTP Email Service:** For sending overdue notifications. Interface via Python `smtplib` or a third-party library (e.g., `fastapi-mail`).
- **FastAPI Swagger UI:** Auto-generated API documentation accessible at `/docs`.

**3.1.4 Communication Interfaces**

- Client-server communication via HTTPS (port 443 in production, port 8000 in development).
- API data format: JSON for all request and response bodies.
- Email communication via SMTP (port 587, TLS).

---

**3.2 Functional Requirements**

**REQ-F-01: User Registration**
The system shall allow new users to register by providing full name, email, phone number, role (Student/Librarian), and password. The system shall validate that the email is unique and the password is at least 8 characters. Upon successful registration, the user account shall be created with an inactive status pending Admin approval.
Priority: High

**REQ-F-02: User Login**
The system shall allow registered users to log in using their email and password. Upon successful authentication, the system shall redirect the user to the role-appropriate dashboard. After 3 consecutive failed login attempts, the account shall be temporarily locked for 15 minutes.
Priority: High

**REQ-F-03: Add Book**
The system shall allow Librarians to add a new book to the catalog by entering: title, author, ISBN (13 digits), publisher, edition, quantity, and category. The system shall validate ISBN uniqueness. If the ISBN already exists, the system shall prompt the Librarian to update the existing record's quantity instead.
Priority: High

**REQ-F-04: Search Book**
The system shall allow all users to search for books by title, author, ISBN, or category. Search results shall display: title, author, ISBN, availability status (available/issued), and total copies. Results shall be paginated (20 results per page).
Priority: High

**REQ-F-05: Issue Book**
The system shall allow Librarians to issue a book to a registered Student by entering the Student ID and Book ID (or scanning the ISBN barcode). The system shall verify: (a) the student has not exceeded the maximum borrowing limit (5 books), (b) the book has available copies, and (c) the student has no overdue books with unpaid fines. Upon successful issue, the system shall decrement the available quantity by 1 and record the issue date and due date (14 days from issue).
Priority: High

**REQ-F-06: Return Book**
The system shall allow Librarians to process a book return by entering the Transaction ID or scanning the book ISBN. The system shall calculate if the book is overdue. If overdue, the system shall calculate the fine at Rs. 2 per day and display it. Upon successful return, the available quantity shall be incremented by 1.
Priority: High

**REQ-F-07: View Borrowing History**
The system shall allow Students to view their own borrowing history, showing: book title, issue date, due date, return date (if returned), and fine amount (if any). Librarians shall be able to view the borrowing history of any student.
Priority: Medium

**REQ-F-08: Generate Reports**
The system shall allow Librarians to generate the following reports: (a) List of all currently issued books, (b) List of overdue books with student details, (c) Most borrowed books (top 10) in a given date range, (d) New books added in a given date range. Reports shall be viewable on screen and downloadable as PDF.
Priority: Medium

**REQ-F-09: Manage Members**
The system shall allow Admins to view, activate, deactivate, or delete user accounts. Admins shall be able to filter the member list by role (Student/Librarian) and status (Active/Inactive).
Priority: Medium

**REQ-F-10: Send Overdue Notifications**
The system shall automatically send an email notification to students who have overdue books. Notifications shall be sent daily at 8:00 AM for all books that are past their due date. The email shall include: book title, due date, number of days overdue, and current fine amount.
Priority: Low

**REQ-F-11: Update Book Details**
The system shall allow Librarians to update the details (title, author, publisher, edition, quantity, category) of an existing book record.
Priority: Medium

**REQ-F-12: Delete Book**
The system shall allow Librarians to delete a book record from the catalog only if no copies of that book are currently issued to any student.
Priority: Low

---

**3.3 Non-Functional Requirements**

**REQ-NF-01: Performance**
The system shall respond to any user request (page load, search, form submission) within 2 seconds under normal load (up to 50 concurrent users).

**REQ-NF-02: Security**
All user passwords shall be stored using bcrypt hashing with a cost factor of 12. All client-server communication in production shall use HTTPS. Session tokens shall expire after 30 minutes of inactivity.

**REQ-NF-03: Reliability**
The system shall have 99% uptime during college operating hours (8 AM to 6 PM, Sunday to Friday). The database shall be backed up daily.

**REQ-NF-04: Usability**
A trained librarian shall be able to complete a book issue transaction in under 1 minute. A student shall be able to search for and find a book in under 30 seconds. The interface shall be usable on both desktop and mobile browsers.

**REQ-NF-05: Scalability**
The system shall support up to 5,000 registered students and a catalog of up to 50,000 book records without performance degradation.

**REQ-NF-06: Maintainability**
The system shall follow a layered architecture (presentation, business logic, data access) to allow modification of any layer without affecting others. Code shall follow PEP 8 style guidelines.

**REQ-NF-07: Portability**
The system shall run on any platform that supports Python 3.10+ and Docker. No platform-specific dependencies shall be used.

---

**3.4 Design Constraints**

- Backend must use Python 3.11 and FastAPI framework.
- Database must be a relational database (SQLite for development, PostgreSQL for production).
- Application must be containerizable using Docker.
- All source code must be maintained in a Git repository with a clear branching strategy.

---

**4. Appendices**

**4.1 Glossary**

| Term | Definition                                                                                           |
| ---- | ---------------------------------------------------------------------------------------------------- |
| LMS  | Library Management System                                                                            |
| ISBN | International Standard Book Number (13-digit unique book identifier)                                 |
| CRUD | Create, Read, Update, Delete — basic database operations                                             |
| SRS  | Software Requirements Specification                                                                  |
| ORM  | Object-Relational Mapping — technique for converting between database tables and programming objects |

**4.2 Analysis Models**

- Use Case Diagram: See Practical 2 deliverables.
- Context-Level DFD: See Practical 2 deliverables.

---

### Practical Checklist (Before Submission)

- [ ] All sections of the template are filled (no empty sections without justification).
- [ ] Every functional requirement has a unique ID, description, and priority.
- [ ] Non-functional requirements are specific and measurable (not vague like "the system should be fast").
- [ ] The document is internally consistent (terms used in Section 1 match those in Section 3).
- [ ] At least one diagram is included (context diagram or use case diagram).
- [ ] Document has a title page with project name, team members, date, and college name.
- [ ] Table of Contents is auto-generated from heading styles.
- [ ] Front matter uses Roman numeral page numbers (i, ii, iii); main body uses Arabic (1, 2, 3).
- [ ] Margins are 1 inch on all sides; body font is Times New Roman 12 pt.
- [ ] Headings use the Styles gallery (Heading 1/2/3) — not manually formatted.
- [ ] Revision History table is included.
- [ ] Each major section starts on a new page.

---

## Practical 2: Construction of UML Diagrams Using Modeling Tools

**Duration:** 2 hours

### Objective

Construct four UML diagrams — Use Case, Activity, Class, and Sequence — for the project chosen in Practical 1, using a UML modeling tool.

### Tool Setup

**Recommended: draw.io (diagrams.net)** — Free, no installation required for web version.

1. Open https://app.diagrams.net in a browser.
2. Choose storage location (Device, Google Drive, or GitHub).
3. Click **+ More Shapes** at the bottom of the left sidebar.
4. Under the **Software** category, enable **UML** and **UML 2.5**. Click **Apply**.
5. The left sidebar now shows UML shapes: actors, use case ovals, class boxes, lifelines, etc.

**Alternative: StarUML** — Download from https://staruml.io. More rigorous UML enforcement. File > New Project > right-click model > Add Diagram > select diagram type. The toolbox updates automatically for each diagram type.

**Alternative: Lucidchart** — Free tier at https://lucid.app. Web-based, collaborative, has UML templates.

---

### Diagram 1: Use Case Diagram

**Purpose:** Show what the system does (functions) and who interacts with it (actors).

**Steps:**

1. **Identify actors.** List all user roles and external systems. Example for LMS: Student, Librarian, Admin, Email Service.
2. **Identify use cases.** List the major functions from SRS Section 2.2. Each function becomes a use case oval.
3. **Draw the system boundary.** Drag a rectangle onto the canvas. Label it with the system name (e.g., "Library Management System").
4. **Place use case ovals inside the boundary.** Label each with a verb phrase: "Search Book," "Issue Book," "Return Book," "Manage Members," "Generate Report."
5. **Place actors outside the boundary.** Use stick figures for human actors, labeled rectangles for systems.
6. **Draw associations.** Connect each actor to the use cases they participate in using solid lines.
7. **Add relationships (if applicable):**
   - **<<include>>** — dashed arrow from base use case to included use case. Example: "Issue Book" <<include>> "Authenticate User."
   - **<<extend>>** — dashed arrow from extending use case to base use case. Example: "Apply Fine" <<extend>> "Return Book."
   - **Generalization** — solid line with hollow triangle from child actor/use case to parent.

**Deliverable:** A single use case diagram with 4-8 use cases, 2-4 actors, and at least one <<include>> or <<extend>> relationship.

#### Example: Use Case Diagram — Library Management System

```
┌─────────────────────────────────────────────────────────────┐
│                 Library Management System                    │
│                                                             │
│    ┌──────────────────┐      ┌──────────────────┐          │
│    │   Search Book     │      │  Register User    │          │
│    └──────────────────┘      └──────────────────┘          │
│                                                             │
│    ┌──────────────────┐      ┌──────────────────┐          │
│    │   Issue Book      │─ ─ ─▶│ Authenticate User │          │
│    └──────────────────┘  «include»  └──────────────────┘   │
│            │                         ▲                      │
│            │                         │ «include»            │
│    ┌──────────────────┐              │                      │
│    │   Return Book     │─ ─ ─ ─ ─ ─ ─┘                      │
│    └──────────────────┘                                     │
│            ▲                                                │
│            │ «extend»                                       │
│    ┌──────────────────┐                                     │
│    │   Calculate Fine  │                                     │
│    └──────────────────┘      ┌──────────────────┐          │
│                               │  Generate Report  │          │
│    ┌──────────────────┐      └──────────────────┘          │
│    │  Manage Members   │                                     │
│    └──────────────────┘      ┌──────────────────┐          │
│                               │ Send Notification │          │
│                               └──────────────────┘          │
└─────────────────────────────────────────────────────────────┘
      │        │          │           │              │
  Student  Student    Librarian   Librarian    Email Service
                                    Admin
```

**Actors and their use cases:**

| Actor | Use Cases |
| --- | --- |
| Student | Search Book, Register User |
| Librarian | Search Book, Issue Book, Return Book, Generate Report, Authenticate User |
| Admin | Manage Members, Register User |
| Email Service | Send Notification |

**Relationships:**

- Issue Book **<<include>>** Authenticate User (authentication always happens before issuing)
- Return Book **<<include>>** Authenticate User (authentication always happens before returning)
- Calculate Fine **<<extend>>** Return Book (fine calculation happens only if the book is overdue)

---

### Diagram 2: Activity Diagram

**Purpose:** Model the flow of control for one specific use case — showing steps, decisions, and parallel activities.

**Steps:**

1. **Choose a use case** from Diagram 1 that has non-trivial flow (e.g., "Issue Book" or "Place Order").
2. **Draw the initial node** (filled black circle) at the top.
3. **Add activity nodes** (rounded rectangles) for each step. Label with verb phrases: "Enter Book ID," "Check Availability," "Record Transaction."
4. **Connect with arrows** showing the sequence of steps.
5. **Add decision nodes** (diamonds) where the flow branches. Label outgoing arrows with guard conditions in square brackets: [book available], [book not available].
6. **Add merge nodes** (diamonds) to bring alternative paths back together.
7. **Add fork/join bars** (thick horizontal lines) if any activities happen in parallel. Example: After "Approve Issue," two parallel activities: "Update Database" and "Print Receipt" — use a fork to split and a join to synchronize.
8. **Draw the final node** (bullseye — filled circle inside a hollow circle) at the bottom.
9. **(Optional) Add swimlanes.** Divide the diagram into vertical columns labeled with the responsible actor/component (e.g., "Student," "Librarian," "System"). Place each activity in the appropriate lane.

**Deliverable:** An activity diagram for one use case with at least one decision node and the complete flow from initial to final node.

#### Example: Activity Diagram — "Issue Book" Use Case

```
                         ● (Initial Node)
                         │
                         ▼
               ┌───────────────────┐
               │  Librarian enters  │
               │  Student ID and    │
               │  Book ID           │
               └────────┬──────────┘
                         │
                         ▼
               ┌───────────────────┐
               │  Verify student    │
               │  membership        │
               └────────┬──────────┘
                         │
                         ▼
                     ◆ Decision
                    ╱         ╲
     [invalid member]          [valid member]
                  │                    │
                  ▼                    ▼
      ┌─────────────────┐   ┌───────────────────┐
      │ Display "Invalid │   │  Check book        │
      │ Student" error   │   │  availability      │
      └────────┬────────┘   └────────┬──────────┘
               │                     │
               │                     ▼
               │                 ◆ Decision
               │                ╱         ╲
               │  [not available]          [available]
               │         │                     │
               │         ▼                     ▼
               │  ┌──────────────┐   ┌───────────────────┐
               │  │ Display "Book│   │  Check borrowing   │
               │  │ not available│   │  limit (max 5)     │
               │  │ " message    │   └────────┬──────────┘
               │  └──────┬───────┘            │
               │         │                    ▼
               │         │                ◆ Decision
               │         │               ╱         ╲
               │         │   [limit exceeded]    [within limit]
               │         │        │                    │
               │         │        ▼                    ▼
               │         │ ┌────────────┐    ══════════════════
               │         │ │Display     │    ║  Fork (parallel) ║
               │         │ │"Limit      │    ══════════════════
               │         │ │exceeded"   │        │          │
               │         │ └─────┬──────┘        ▼          ▼
               │         │       │    ┌──────────────┐ ┌──────────┐
               │         │       │    │ Update book   │ │ Record   │
               │         │       │    │ quantity (-1)  │ │ issue    │
               │         │       │    └──────┬───────┘ │ transaction│
               │         │       │           │         └─────┬────┘
               │         │       │           │               │
               │         │       │       ══════════════════
               │         │       │       ║  Join (sync)    ║
               │         │       │       ══════════════════
               │         │       │               │
               │         │       │               ▼
               │         │       │    ┌───────────────────┐
               │         │       │    │ Display "Book      │
               │         │       │    │ issued successfully"│
               │         │       │    └────────┬──────────┘
               │         │       │             │
               ▼         ▼       ▼             ▼
                     ◆ Merge (all paths)
                         │
                         ▼
                       ◉ (Final Node)
```

**Key elements in this diagram:**

- **3 decision nodes:** Verify membership, Check availability, Check borrowing limit
- **1 fork/join pair:** "Update book quantity" and "Record issue transaction" happen in parallel
- **Guard conditions:** [valid member], [invalid member], [available], [not available], [within limit], [limit exceeded]

---

### Diagram 3: Class Diagram

**Purpose:** Show the static structure — classes, their attributes, operations, and relationships.

**Steps:**

1. **Identify classes.** Use the grammatical parse: extract nouns from your use cases and SRS. Typical classes for LMS: `Book`, `Member`, `Librarian`, `Transaction`, `Fine`, `Category`.
2. **Define attributes.** For each class, list data properties. Example: `Book` — bookID, title, author, ISBN, quantity, status.
3. **Define operations.** For each class, list behaviors. Example: `Book` — addBook(), removeBook(), searchBook(), updateDetails().
4. **Draw class boxes.** Each class is a rectangle with three compartments: name (top), attributes (middle), operations (bottom).
5. **Draw relationships:**
   - **Association** (solid line): `Member` — `Transaction` (a member makes transactions).
   - **Multiplicity** at both ends: `Member` 1 ——— 0..\* `Transaction`.
   - **Aggregation** (hollow diamond): `Library` ◇——— `Book` (library has books, but books can exist independently).
   - **Composition** (filled diamond): `Order` ◆——— `OrderItem` (items cannot exist without the order).
   - **Generalization** (hollow triangle arrow): `Student` and `Faculty` inherit from `Member`.
6. **Add multiplicity labels** at both ends of every association.

**Deliverable:** A class diagram with 4-6 classes, each having at least 3 attributes and 2 operations, with associations and multiplicity labels.

#### Example: Class Diagram — Library Management System

```
┌──────────────────────────┐          ┌──────────────────────────┐
│         Member           │          │          Book            │
├──────────────────────────┤          ├──────────────────────────┤
│ - memberID: int          │          │ - bookID: int            │
│ - name: String           │          │ - title: String          │
│ - email: String          │          │ - author: String         │
│ - phone: String          │          │ - isbn: String           │
│ - password: String       │          │ - quantity: int          │
│ - role: String           │          │ - status: String         │
│ - status: String         │          ├──────────────────────────┤
├──────────────────────────┤          │ + addBook()              │
│ + register()             │          │ + updateBook()           │
│ + login()                │          │ + deleteBook()           │
│ + updateProfile()        │          │ + searchBook()           │
│ + viewHistory()          │          │ + checkAvailability()    │
└──────────┬───────────────┘          └──────────┬───────────────┘
           │                                     │
      ◁────┤ Generalization                      │
      │    │                                     │
┌─────┴──────────┐  ┌──────────────────┐         │
│    Student     │  │   Librarian      │         │
├────────────────┤  ├──────────────────┤         │
│ - rollNo: String│  │ - empID: String  │         │
│ - department:  │  │ - shift: String  │         │
│   String       │  ├──────────────────┤         │
├────────────────┤  │ + issueBook()    │         │
│ + searchBook() │  │ + returnBook()   │         │
│ + viewFines()  │  │ + generateReport()│        │
└────────────────┘  └──────────────────┘         │
                                                  │
                    1                    0..*     │
     Member ─────────────────────── Transaction   │
                                                  │
┌──────────────────────────┐          ┌───────────┴──────────────┐
│       Transaction        │          │         Fine             │
├──────────────────────────┤          ├──────────────────────────┤
│ - transactionID: int     │          │ - fineID: int            │
│ - issueDate: Date        │          │ - amount: float          │
│ - dueDate: Date          │          │ - daysOverdue: int       │
│ - returnDate: Date       │          │ - paidStatus: boolean    │
│ - status: String         │          ├──────────────────────────┤
├──────────────────────────┤          │ + calculateFine()        │
│ + createTransaction()    │          │ + payFine()              │
│ + getDetails()           │          │ + waiveFine()            │
│ + markReturned()         │          └──────────────────────────┘
└──────────────────────────┘
```

**Relationships:**

| Relationship | Type | Multiplicity | Meaning |
| --- | --- | --- | --- |
| Member — Transaction | Association | 1 Member to 0..* Transactions | A member can have zero or many transactions |
| Transaction — Book | Association | 0..* Transactions to 1 Book | Each transaction involves exactly one book; a book can appear in many transactions |
| Transaction — Fine | Association | 1 Transaction to 0..1 Fine | A transaction may or may not have a fine |
| Member ◁— Student | Generalization | — | Student inherits all attributes/operations of Member |
| Member ◁— Librarian | Generalization | — | Librarian inherits all attributes/operations of Member |

**Visibility notation:** `-` means private, `+` means public. Use these prefixes before attribute/operation names.

---

### Diagram 4: Sequence Diagram

**Purpose:** Show how objects interact over time for a specific scenario — the order of messages exchanged.

**Steps:**

1. **Choose a scenario.** Pick the same use case as your activity diagram (e.g., "Issue Book").
2. **Identify participating objects.** These come from your class diagram. Example: `:Student`, `:Librarian`, `:System`, `:BookDB`, `:TransactionDB`.
3. **Draw lifelines.** Place objects as labeled rectangles across the top. Drop a dashed vertical line (lifeline) below each one, extending downward.
4. **Draw messages as horizontal arrows** between lifelines, numbered in sequence:
   - `1: requestIssue(bookID)` — Student to Librarian
   - `2: verifyMembership(memberID)` — Librarian to System
   - `3: checkAvailability(bookID)` — System to BookDB
   - `4: return(status)` — BookDB to System
   - `5: issueBook(bookID, memberID)` — System to TransactionDB
   - `6: confirmation()` — System to Librarian
   - `7: issueConfirmation()` — Librarian to Student
5. **Add activation bars** (narrow rectangles on lifelines) to show when an object is actively processing.
6. **Add alt/opt fragments** (rectangles labeled `alt` or `opt`) if the flow involves conditional logic. Example: `alt [book available]` / `[book not available]`.

**Deliverable:** A sequence diagram with 4-6 objects, at least 6 messages in sequence, and activation bars.

#### Example: Sequence Diagram — "Issue Book" Scenario

```
  :Student        :Librarian         :System         :BookDB      :TransactionDB
     │                │                  │               │               │
     │ 1: requestIssue│(bookID, studentID)               │               │
     │───────────────▶│                  │               │               │
     │                │                  │               │               │
     │                │ 2: verifyMember  │(studentID)    │               │
     │                │─────────────────▶│               │               │
     │                │                  │               │               │
     │                │                  │ 3: checkAvailability(bookID)  │
     │                │                  │──────────────▶│               │
     │                │                  │               │               │
     │                │                  │ 4: return     │(available=true)
     │                │                  │◀──────────────│               │
     │                │                  │               │               │
     │         ┌──────┼──────────────────┼───────────────┼───────────────┤
     │         │ alt  [book available]   │               │               │
     │         │      │                  │               │               │
     │         │      │                  │ 5: checkBorrowLimit(studentID)│
     │         │      │                  │──────────────▶│               │
     │         │      │                  │               │               │
     │         │      │                  │ 6: return(withinLimit=true)   │
     │         │      │                  │◀──────────────│               │
     │         │      │                  │               │               │
     │         │      │                  │ 7: createTransaction(bookID, studentID)
     │         │      │                  │──────────────────────────────▶│
     │         │      │                  │               │               │
     │         │      │                  │ 8: return     │(transactionID)│
     │         │      │                  │◀──────────────────────────────│
     │         │      │                  │               │               │
     │         │      │                  │ 9: updateQuantity(bookID, -1) │
     │         │      │                  │──────────────▶│               │
     │         │      │                  │               │               │
     │         │      │ 10: issueSuccess │(transactionID)│               │
     │         │      │◀─────────────────│               │               │
     │         │      │                  │               │               │
     │         │      │ 11: issueConfirmation(bookTitle, dueDate)        │
     │         │◀─────│                  │               │               │
     │         │──────┼──────────────────┼───────────────┼───────────────┤
     │         │ [book not available]    │               │               │
     │         │      │                  │               │               │
     │         │      │ 12: notAvailable │(bookTitle)    │               │
     │         │      │◀─────────────────│               │               │
     │         │      │                  │               │               │
     │         │      │ 13: displayError │("Book not available")         │
     │         │◀─────│                  │               │               │
     │         └──────┼──────────────────┼───────────────┼───────────────┤
     │                │                  │               │               │
     ▼                ▼                  ▼               ▼               ▼
```

**Reading the diagram:**

| Message # | From | To | Description |
| --- | --- | --- | --- |
| 1 | Student | Librarian | Student requests to borrow a book |
| 2 | Librarian | System | System verifies student membership |
| 3 | System | BookDB | System checks if book has available copies |
| 4 | BookDB | System | Returns availability status |
| 5 | System | BookDB | Checks if student is within borrowing limit |
| 6 | BookDB | System | Returns limit status |
| 7 | System | TransactionDB | Creates a new issue transaction record |
| 8 | TransactionDB | System | Returns the new transaction ID |
| 9 | System | BookDB | Decrements available quantity by 1 |
| 10 | System | Librarian | Confirms successful issue |
| 11 | Librarian | Student | Displays book title and due date |
| 12 | System | Librarian | (alt) Notifies book is not available |
| 13 | Librarian | Student | (alt) Displays error message |

**Key elements:** The `alt` fragment shows two alternative paths — one for when the book is available (messages 5-11) and one for when it is not (messages 12-13). Return messages (dashed arrows going back) are numbered sequentially. Activation bars should be drawn on each lifeline during the time the object is processing.

---

### Practical Checklist (Before Submission)

- [ ] All four diagrams are complete: Use Case, Activity, Class, Sequence.
- [ ] Diagrams use correct UML notation (not freehand approximation).
- [ ] Each diagram has a clear title.
- [ ] Use case diagram has system boundary, actors outside, use cases inside.
- [ ] Activity diagram has initial node, final node, and at least one decision.
- [ ] Class diagram has multiplicity labels on all associations.
- [ ] Sequence diagram has numbered messages and lifelines.
- [ ] Export all diagrams as PNG or PDF for submission.

---

## Practical 3: Design of System Architecture and Component Structure Using CASE Tools

**Duration:** 2 hours

### Objective

Design the system architecture (selecting and diagramming an architectural style) and define the component structure for the project, using a CASE tool.

### Tool Setup

**Recommended: draw.io (diagrams.net)** — Same tool as Practical 2.

1. Ensure **UML** and **UML 2.5** shape libraries are enabled (done in Practical 2).
2. Also enable **General** and **Advanced** shape libraries for boxes, containers, and connectors useful in architecture diagrams.
3. For cloud-based projects, enable **AWS / Azure / GCP** icon libraries under the **Networking** category.

**Alternative: Visual Paradigm Community Edition** — Free. Download from https://www.visual-paradigm.com/download/community.php. Supports UML component diagrams, package diagrams, and deployment diagrams with proper notation.

---

### Part A: Architectural Design

**Step 1: Choose an architectural style.** Based on the nature of your project, select one (or a combination):

- **Layered architecture** — best for most web/desktop applications. Organize into: Presentation Layer, Business Logic Layer, Data Access Layer, Database Layer.
- **Client-Server** — best for systems with a clear separation between user-facing clients and back-end servers.
- **MVC (Model-View-Controller)** — best for web applications where UI changes frequently.
- **Repository/Data-centered** — best for systems where multiple components access a shared data store (e.g., IDE, CASE tools).
- **Pipe-and-Filter** — best for data transformation pipelines (e.g., compiler, ETL systems).

**Step 2: Draw the architectural diagram.**

For a **layered architecture** (most common for student projects):

1. Create 3-4 stacked horizontal rectangles (containers), each representing a layer. Label them top to bottom:
   - **Presentation Layer** — UI components (web pages, forms, API endpoints)
   - **Business Logic Layer** — core processing (validation, calculations, rules)
   - **Data Access Layer** — database queries, ORM, API clients
   - **Database Layer** — the actual database (MySQL, PostgreSQL, MongoDB)
2. Inside each layer rectangle, place smaller boxes representing the key components in that layer.
3. Draw downward arrows between layers to show the direction of dependency (upper layers depend on lower layers, not vice versa).
4. Add labels on arrows to describe the nature of interaction (e.g., "HTTP requests," "SQL queries," "method calls").

For a **client-server architecture:**

1. Draw a "Client" box on the left and a "Server" box on the right, separated by a vertical dashed line labeled "Network."
2. Inside the Client box, place components: UI, Local Cache, Request Handler.
3. Inside the Server box, place components: API Gateway, Business Logic, Database.
4. Draw bidirectional arrows across the network boundary: Client sends "HTTP Request" → Server returns "HTTP Response."

For **MVC:**

1. Draw three boxes: Model, View, Controller.
2. Arrow from User to Controller: "user input."
3. Arrow from Controller to Model: "update/query."
4. Arrow from Model to View: "data."
5. Arrow from View to User: "display."

**Step 3: Annotate the diagram.** Add a brief note explaining why this style was chosen. Example: "Layered architecture was chosen because the LMS is a web application where the UI, business logic, and data access have distinct responsibilities and may evolve independently."

#### Example: Layered Architecture Diagram — Library Management System

```
┌─────────────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                             │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────┐ │
│  │  Login Page   │  │ Book Search  │  │ Issue/Return │  │ Reports│ │
│  │  (HTML/CSS)   │  │   Page       │  │    Form      │  │  Page  │ │
│  └──────────────┘  └──────────────┘  └──────────────┘  └────────┘ │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐                                │
│  │ Member Mgmt  │  │  Dashboard   │                                │
│  │   Page       │  │              │                                │
│  └──────────────┘  └──────────────┘                                │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ HTTP Requests / API Calls
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     BUSINESS LOGIC LAYER                            │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────┐ │
│  │ Auth Service  │  │ Book Service │  │ Transaction  │  │ Report │ │
│  │ (login,      │  │ (add, search,│  │  Service     │  │Service │ │
│  │  register,   │  │  update,     │  │ (issue,      │  │(generate│ │
│  │  validate)   │  │  delete)     │  │  return,     │  │ PDF,   │ │
│  └──────────────┘  └──────────────┘  │  fine calc)  │  │ stats) │ │
│                                       └──────────────┘  └────────┘ │
│  ┌──────────────┐  ┌──────────────┐                                │
│  │ Member       │  │ Notification │                                │
│  │ Service      │  │ Service      │                                │
│  │ (CRUD,       │  │ (email       │                                │
│  │  activate)   │  │  alerts)     │                                │
│  └──────────────┘  └──────────────┘                                │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ Method Calls / ORM Queries
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA ACCESS LAYER                              │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────┐ │
│  │ Book         │  │ Member       │  │ Transaction  │  │ Fine   │ │
│  │ Repository   │  │ Repository   │  │ Repository   │  │ Repo   │ │
│  │ (CRUD ops)   │  │ (CRUD ops)   │  │ (CRUD ops)   │  │        │ │
│  └──────────────┘  └──────────────┘  └──────────────┘  └────────┘ │
│                                                                     │
│  ┌──────────────────────────────────────┐                          │
│  │  ORM Layer (SQLAlchemy models)       │                          │
│  └──────────────────────────────────────┘                          │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ SQL Queries
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       DATABASE LAYER                                │
│                                                                     │
│              ┌───────────────────────────────┐                     │
│              │   PostgreSQL / SQLite          │                     │
│              │                               │                     │
│              │  Tables: books, members,      │                     │
│              │  transactions, fines           │                     │
│              └───────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Justification:** "Layered architecture is chosen because the LMS is a web application where the user interface, business rules, data access logic, and database storage have distinct responsibilities. Each layer can be modified independently — for example, the database can be changed from SQLite to PostgreSQL without modifying the business logic or UI. Upper layers depend on lower layers, but lower layers have no knowledge of upper layers, ensuring loose coupling."

**Layer-to-layer interaction summary:**

| From Layer | To Layer | Interaction Type | Example |
| --- | --- | --- | --- |
| Presentation | Business Logic | HTTP requests / API calls | Login form sends POST /auth/login |
| Business Logic | Data Access | Method calls / ORM queries | BookService calls BookRepository.search() |
| Data Access | Database | SQL queries via ORM | BookRepository executes SELECT * FROM books |

---

### Part B: Component Design

**Step 1: Identify the major components.** Break the system into 5-8 components based on the functional requirements from the SRS. Example for LMS:

- User Authentication Module
- Book Management Module
- Member Management Module
- Transaction (Issue/Return) Module
- Fine Calculation Module
- Report Generation Module
- Notification Module (email alerts)

**Step 2: Draw a UML Component Diagram.**

1. For each component, drag a **component** shape from the UML library (rectangle with the component icon — two small rectangles on the left edge).
2. Label each component clearly.
3. Draw **interfaces** using the lollipop notation (small circle on a line extending from the component). Label the interface with the service it provides. Example: The Book Management component provides an `IBookSearch` interface.
4. Draw **dependency arrows** (dashed arrows) from one component to another to show which components depend on which. Example: Transaction Module depends on Book Management (to check availability) and Member Management (to verify membership).
5. Group related components inside **package** boxes if they belong to the same subsystem or layer. Example: All database-related components inside a "Data Access" package.

**Step 3: Create an Interface Specification Table.**

For each component, document:

| Component          | Provided Interface      | Required Interface                    | Description                                       |
| ------------------ | ----------------------- | ------------------------------------- | ------------------------------------------------- |
| Book Management    | IBookSearch, IBookCRUD  | IDatabase                             | Manages book catalog: add, remove, search, update |
| Transaction Module | IIssueBook, IReturnBook | IBookSearch, IMemberVerify, IDatabase | Handles book issue and return transactions        |
| Fine Calculation   | IFineCalc               | IReturnBook, IDatabase                | Calculates fines based on return date             |
| Notification       | ISendAlert              | IMemberInfo                           | Sends email/SMS notifications for overdue books   |

#### Example: UML Component Diagram — Library Management System

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        «package» Core Services                          │
│                                                                         │
│  ┌─────────────────────┐          ┌─────────────────────┐              │
│  │ ┌─┐                 │          │ ┌─┐                 │              │
│  │ │ │ User             │          │ │ │ Book             │              │
│  │ └─┘ Authentication   │          │ └─┘ Management      │              │
│  │                     │          │                     │              │
│  │  ○─ ILogin          │          │  ○─ IBookSearch     │              │
│  │  ○─ IRegister       │          │  ○─ IBookCRUD       │              │
│  │  ○─ ITokenValidate  │          │  ○─ IAvailability   │              │
│  └─────────────────────┘          └──────────┬──────────┘              │
│                                              │                         │
│  ┌─────────────────────┐          ┌──────────┼──────────┐              │
│  │ ┌─┐                 │          │ ┌─┐      │          │              │
│  │ │ │ Member           │          │ │ │ Transaction     │              │
│  │ └─┘ Management      │          │ └─┘ Module          │              │
│  │                     │          │          │          │              │
│  │  ○─ IMemberVerify   │◄─ ─ ─ ─ │          │          │              │
│  │  ○─ IMemberCRUD     │          │  ○─ IIssueBook     │              │
│  │  ○─ IMemberInfo     │          │  ○─ IReturnBook    │              │
│  └─────────────────────┘          └──────────┬──────────┘              │
│                                              │                         │
│                                   ┌──────────┼──────────┐              │
│                                   │ ┌─┐      │          │              │
│                                   │ │ │ Fine             │              │
│                                   │ └─┘ Calculation     │              │
│                                   │          │          │              │
│                                   │  ○─ IFineCalc      │              │
│                                   └─────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                       «package» Support Services                        │
│                                                                         │
│  ┌─────────────────────┐          ┌─────────────────────┐              │
│  │ ┌─┐                 │          │ ┌─┐                 │              │
│  │ │ │ Report           │          │ │ │ Notification     │              │
│  │ └─┘ Generation      │          │ └─┘ Module          │              │
│  │                     │          │                     │              │
│  │  ○─ IGenerateReport │          │  ○─ ISendAlert      │              │
│  │  ○─ IExportPDF      │          │  ○─ IEmailService   │              │
│  └─────────────────────┘          └─────────────────────┘              │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                       «package» Data Access                             │
│                                                                         │
│              ┌─────────────────────────────────────────┐               │
│              │ ┌─┐                                     │               │
│              │ │ │ Database Access Layer                │               │
│              │ └─┘ (SQLAlchemy ORM)                    │               │
│              │                                         │               │
│              │  ○─ IDatabase                           │               │
│              └─────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────────────────┘

DEPENDENCY ARROWS (draw as dashed arrows - - - -▶ in the tool):

  Transaction Module  - - - -▶  Book Management        (uses IBookSearch, IAvailability)
  Transaction Module  - - - -▶  Member Management      (uses IMemberVerify)
  Transaction Module  - - - -▶  Fine Calculation       (uses IFineCalc)
  Fine Calculation    - - - -▶  Transaction Module     (uses IReturnBook)
  Report Generation   - - - -▶  Transaction Module     (uses IIssueBook, IReturnBook)
  Report Generation   - - - -▶  Book Management        (uses IBookSearch)
  Notification Module - - - -▶  Member Management      (uses IMemberInfo)
  All Core Modules    - - - -▶  Database Access Layer   (uses IDatabase)
```

**Reading the diagram:**

- The `┌─┐ │ │ └─┘` symbol represents the UML component icon (two small rectangles on the left edge of the component box). In draw.io, use the "Component" shape from the UML library.
- The `○─` symbol represents a **provided interface** (lollipop notation). In draw.io, use a small circle connected to the component edge with a short line.
- Dashed arrows (`- - -▶`) represent **dependency** — the arrow points toward the component being depended upon.
- Components are grouped into **packages** (Core Services, Support Services, Data Access) to show subsystem boundaries.

**Complete Interface Specification Table:**

| Component | Provided Interfaces | Required Interfaces | Description |
| --- | --- | --- | --- |
| User Authentication | ILogin, IRegister, ITokenValidate | IDatabase, IMemberCRUD | Handles user registration, login, and JWT token validation |
| Book Management | IBookSearch, IBookCRUD, IAvailability | IDatabase | Manages the book catalog: add, update, delete, search, check availability |
| Member Management | IMemberVerify, IMemberCRUD, IMemberInfo | IDatabase | Manages member records: create, update, activate/deactivate, verify status |
| Transaction Module | IIssueBook, IReturnBook | IBookSearch, IAvailability, IMemberVerify, IFineCalc, IDatabase | Handles book issue and return transactions, enforces borrowing limits |
| Fine Calculation | IFineCalc | IReturnBook, IDatabase | Calculates overdue fines based on return date vs. due date |
| Report Generation | IGenerateReport, IExportPDF | IBookSearch, IIssueBook, IReturnBook, IDatabase | Generates overdue lists, popular books, and member activity reports |
| Notification Module | ISendAlert, IEmailService | IMemberInfo, IDatabase | Sends email notifications for overdue books and account updates |
| Database Access Layer | IDatabase | — (external: PostgreSQL/SQLite) | Provides ORM-based CRUD operations to all other modules |

---

### Part C: Modular Design Principles (Apply and Document)

For each component identified above, briefly document how you applied modular design principles:

**Cohesion:** State the type of cohesion each module exhibits. Example: "Book Management Module exhibits functional cohesion — all its operations (add, search, update, delete) are focused on managing book data."

**Coupling:** State how coupling is minimized. Example: "The Transaction Module accesses Book data only through the IBookSearch interface, not by directly accessing the Book database. This is data coupling (only needed parameters are passed)."

**Information Hiding:** State what is hidden. Example: "The internal database schema and SQL queries are hidden inside the Data Access Layer. Other components interact only through defined interfaces."

#### Example: Modular Design Principles — Library Management System

| Module | Cohesion Type | Cohesion Justification | Coupling Type | Coupling Justification | Information Hidden |
| --- | --- | --- | --- | --- | --- |
| User Authentication | Functional | All operations (login, register, validate token) serve the single purpose of user identity management | Data coupling | Receives only username/password; returns only a token. No shared data structures with other modules | Password hashing algorithm, token generation logic, session storage mechanism |
| Book Management | Functional | All operations (add, search, update, delete, check availability) are focused on managing the book catalog | Data coupling | Exposes only IBookSearch and IBookCRUD interfaces; other modules pass only bookID or search parameters | Internal SQL queries, database table schema, indexing strategy |
| Member Management | Functional | All operations (create, update, verify, activate/deactivate) relate to managing member records | Data coupling | Provides IMemberVerify that accepts memberID and returns a boolean; no internal state is shared | Member password storage, internal validation rules, activation workflow |
| Transaction Module | Functional | All operations (issue, return, check limit) relate to managing borrowing transactions | Stamp coupling | Receives BookCreate and MemberInfo objects from other modules — passes structured data, not primitive values | Internal transaction state machine, due date calculation logic, limit enforcement rules |
| Fine Calculation | Functional | Single purpose — calculate fine amount based on overdue days | Data coupling | Receives only returnDate and dueDate; returns only fineAmount (a float). Minimal interface | Fine rate (Rs. 2/day), maximum fine cap, waiver rules |
| Report Generation | Communicational | Multiple operations (overdue report, popular books, member activity) work on the same data set (transactions, books) | Data coupling | Queries other modules via read-only interfaces; passes only date ranges and filter parameters | Report formatting logic, PDF generation library, chart rendering |
| Notification Module | Functional | Single purpose — send notifications to members | Data coupling | Receives only email address and message content; no access to internal member records | SMTP configuration, email template engine, retry logic |
| Database Access Layer | Functional | Single purpose — provide ORM-based database operations to all modules | Data coupling | Accepts model objects and query parameters; returns result sets. No knowledge of business rules | Connection string, connection pooling, SQL dialect, migration scripts |

**Key observations from the table:**

- **All modules achieve functional cohesion** — each module's operations serve a single, well-defined purpose. The only exception is Report Generation, which exhibits communicational cohesion (multiple functions operating on the same data set).
- **Data coupling is dominant** — modules communicate by passing only the minimum required parameters (IDs, simple values). No module shares global variables or internal data structures with another.
- **Information hiding is enforced** — every module hides its implementation details behind interfaces. The Database Access Layer hides SQL; Authentication hides password hashing; Fine Calculation hides the rate formula.

---

### Practical Checklist (Before Submission)

- [ ] Architectural style is explicitly named and justified.
- [ ] Architecture diagram shows layers/tiers with components placed inside them.
- [ ] Arrows show direction of dependency and are labeled.
- [ ] Component diagram has 5-8 components with proper UML notation.
- [ ] At least 3 interfaces are shown using lollipop notation.
- [ ] Dependency arrows between components are drawn.
- [ ] Interface specification table is filled for all major components.
- [ ] Cohesion, coupling, and information hiding are documented for at least 3 modules.
- [ ] All diagrams are exported as PNG or PDF.

---

## Practical 4: Implementation of Key System Modules Following Coding Standards

**Duration:** 2 hours

### Objective

Implement core API modules for the project using FastAPI, following clean code practices, proper project structure, and coding standards.

### Tool Setup

**Step 1: Install Python.** Download Python 3.10+ from https://www.python.org/downloads. During installation, check "Add Python to PATH."

Verify installation:

```bash
python --version
pip --version
```

**Step 2: Create the project directory and virtual environment.**

```bash
mkdir library_api
cd library_api
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**Step 3: Install dependencies.**

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

**Step 4: Freeze dependencies.**

```bash
pip freeze > requirements.txt
```

---

### Project Structure

Organize code using a layered architecture. Every file has a single responsibility.

```
library_api/
├── app/
│   ├── __init__.py
│   ├── main.py            # App entry point
│   ├── database.py        # DB engine & session
│   ├── models.py          # SQLAlchemy ORM models
│   ├── schemas.py         # Pydantic request/response schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   └── books.py       # Book-related API endpoints
│   └── crud.py            # Database operations (CRUD)
├── tests/                 # (Practical 5)
├── requirements.txt
└── README.md
```

---

### Step-by-Step Implementation

#### File 1: `app/database.py` — Database Connection

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """Dependency: yields a DB session, closes it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### File 2: `app/models.py` — ORM Models

```python
from sqlalchemy import Column, Integer, String
from app.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    author = Column(String(100), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    quantity = Column(Integer, default=1)
```

#### File 3: `app/schemas.py` — Pydantic Schemas

Schemas define what data the API accepts and returns. Never expose ORM models directly.

```python
from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    """Schema for creating a new book (request body)."""
    title: str
    author: str
    isbn: str
    quantity: int = 1


class BookResponse(BaseModel):
    """Schema for returning book data (response body)."""
    id: int
    title: str
    author: str
    isbn: str
    quantity: int

    model_config = ConfigDict(from_attributes=True)
```

#### File 4: `app/crud.py` — CRUD Operations

All database operations are isolated here. Routers never write raw queries.

```python
from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookCreate


def create_book(db: Session, book_data: BookCreate) -> Book:
    """Insert a new book into the database."""
    book = Book(**book_data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_all_books(db: Session) -> list[Book]:
    """Retrieve all books."""
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int) -> Book | None:
    """Retrieve a single book by its ID."""
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int) -> bool:
    """Delete a book by ID. Returns True if deleted, False if not found."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True
```

#### File 5: `app/routers/books.py` — API Router

Routers are thin — they parse input, call CRUD functions, and return responses.

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import BookCreate, BookResponse
from app import crud

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookResponse, status_code=201)
def add_book(book_data: BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the library."""
    return crud.create_book(db, book_data)


@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    """Get all books in the library."""
    return crud.get_all_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a single book by ID."""
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/{book_id}", status_code=204)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
```

#### File 6: `app/main.py` — Application Entry Point

```python
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books

# Create all database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API", version="1.0.0")

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "Library Management API is running"}
```

---

### Run the Application

```bash
uvicorn app.main:app --reload
```

Open the browser at http://127.0.0.1:8000/docs — FastAPI automatically generates interactive Swagger UI documentation. Test all endpoints directly from the browser.

---

### Coding Standards Applied

**Naming conventions:** Functions and variables use `snake_case`. Classes use `PascalCase`. Constants use `UPPER_SNAKE_CASE`. File names use `snake_case`.

**Single Responsibility Principle:** Each file has one job — `models.py` defines tables, `schemas.py` defines data shapes, `crud.py` handles queries, routers handle HTTP.

**Separation of Concerns:** Routers never contain SQL queries. Database logic never handles HTTP status codes.

**Dependency Injection:** `get_db()` is injected via `Depends()` — this makes the database session swappable for testing.

**Type Hints:** All function parameters and return types are annotated. Pydantic enforces input validation automatically.

**Docstrings:** Every function has a one-line docstring explaining its purpose.

---

### Practical Checklist (Before Submission)

- [ ] Project structure matches the layered layout shown above.
- [ ] Application runs without errors via `uvicorn app.main:app --reload`.
- [ ] All four CRUD endpoints work in Swagger UI (`/docs`).
- [ ] ORM models and Pydantic schemas are separate.
- [ ] All functions have type hints and docstrings.
- [ ] `requirements.txt` is present and complete.
- [ ] No business logic inside routers — all logic is in `crud.py`.

---

## Practical 5: Execution of Testing Procedures (Unit and Integration) and Documentation of Results

**Duration:** 2 hours

### Objective

Write and execute unit tests and integration tests for the FastAPI application built in Practical 4. Document test results.

### Tool Setup

Install testing dependencies (with virtual environment activated):

```bash
pip install pytest httpx
pip freeze > requirements.txt
```

- **pytest** — the testing framework. Discovers and runs test files automatically.
- **httpx** — required by FastAPI's `TestClient` for sending HTTP requests in tests.

---

### Project Structure Update

```
library_api/
├── app/
│   └── ... (from Practical 4)
├── tests/
│   ├── __init__.py
│   ├── conftest.py        # Shared test fixtures
│   ├── test_books.py      # Integration tests for book endpoints
│   └── test_crud.py       # Unit tests for CRUD functions
└── requirements.txt
```

---

### Step 1: Test Configuration — `tests/conftest.py`

This file creates an isolated test database (in-memory SQLite) so tests never touch the real database.

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test.db"
test_engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    """Provide a test database session."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Override the real DB dependency with the test DB
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test, drop them after."""
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture
def client():
    """Provide a TestClient for making HTTP requests."""
    return TestClient(app)


@pytest.fixture
def db_session():
    """Provide a raw DB session for unit tests."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

### Step 2: Unit Tests — `tests/test_crud.py`

Unit tests test individual functions in isolation (the `crud.py` functions). They call the function directly with a test DB session — no HTTP involved.

```python
from app.crud import create_book, get_all_books, get_book_by_id, delete_book
from app.schemas import BookCreate


def test_create_book(db_session):
    """Test that a book can be created in the database."""
    book_data = BookCreate(title="Clean Code", author="Robert Martin", isbn="9780132350884")
    book = create_book(db_session, book_data)

    assert book.id is not None
    assert book.title == "Clean Code"
    assert book.author == "Robert Martin"
    assert book.isbn == "9780132350884"
    assert book.quantity == 1


def test_get_all_books_empty(db_session):
    """Test that an empty database returns an empty list."""
    books = get_all_books(db_session)
    assert books == []


def test_get_all_books_with_data(db_session):
    """Test that all books are returned after insertion."""
    create_book(db_session, BookCreate(title="Book A", author="Author A", isbn="1111111111111"))
    create_book(db_session, BookCreate(title="Book B", author="Author B", isbn="2222222222222"))
    books = get_all_books(db_session)
    assert len(books) == 2


def test_get_book_by_id_found(db_session):
    """Test retrieving a book that exists."""
    book = create_book(db_session, BookCreate(title="Test", author="Tester", isbn="3333333333333"))
    found = get_book_by_id(db_session, book.id)
    assert found is not None
    assert found.title == "Test"


def test_get_book_by_id_not_found(db_session):
    """Test retrieving a book that does not exist."""
    found = get_book_by_id(db_session, 9999)
    assert found is None


def test_delete_book_success(db_session):
    """Test deleting an existing book."""
    book = create_book(db_session, BookCreate(title="Delete Me", author="Author", isbn="4444444444444"))
    result = delete_book(db_session, book.id)
    assert result is True
    assert get_book_by_id(db_session, book.id) is None


def test_delete_book_not_found(db_session):
    """Test deleting a book that does not exist."""
    result = delete_book(db_session, 9999)
    assert result is False
```

---

### Step 3: Integration Tests — `tests/test_books.py`

Integration tests test the full HTTP request-response cycle through the API — routing, validation, database, and response serialization all working together.

```python
def test_root_endpoint(client):
    """Test the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Library Management API is running"


def test_add_book(client):
    """Test creating a book via POST /books/."""
    response = client.post("/books/", json={
        "title": "Clean Code",
        "author": "Robert Martin",
        "isbn": "9780132350884",
        "quantity": 3
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Clean Code"
    assert data["isbn"] == "9780132350884"
    assert "id" in data


def test_list_books_empty(client):
    """Test GET /books/ returns empty list initially."""
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_books_after_add(client):
    """Test GET /books/ returns books after adding one."""
    client.post("/books/", json={
        "title": "Book A", "author": "Author A", "isbn": "1111111111111"
    })
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_book_by_id(client):
    """Test GET /books/{id} returns the correct book."""
    post_response = client.post("/books/", json={
        "title": "Specific Book", "author": "Author", "isbn": "5555555555555"
    })
    book_id = post_response.json()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Specific Book"


def test_get_book_not_found(client):
    """Test GET /books/{id} returns 404 for non-existent book."""
    response = client.get("/books/9999")
    assert response.status_code == 404


def test_delete_book(client):
    """Test DELETE /books/{id} removes the book."""
    post_response = client.post("/books/", json={
        "title": "To Delete", "author": "Author", "isbn": "6666666666666"
    })
    book_id = post_response.json()["id"]
    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 204

    # Verify it's gone
    get_response = client.get(f"/books/{book_id}")
    assert get_response.status_code == 404


def test_delete_book_not_found(client):
    """Test DELETE /books/{id} returns 404 for non-existent book."""
    response = client.delete("/books/9999")
    assert response.status_code == 404


def test_add_book_validation_error(client):
    """Test POST /books/ with missing required field returns 422."""
    response = client.post("/books/", json={"title": "Incomplete"})
    assert response.status_code == 422
```

---

### Step 4: Run Tests

```bash
# Run all tests with verbose output
pytest -v

# Run only unit tests
pytest tests/test_crud.py -v

# Run only integration tests
pytest tests/test_books.py -v

# Run with coverage report (install pytest-cov first: pip install pytest-cov)
pip install pytest-cov
pytest --cov=app --cov-report=term-missing
```

---

### Step 5: Document Test Results

Create a test results table in your submission document:

| Test ID | Test Name                      | Type        | Input / Action                   | Expected Result                   | Actual Result       | Status |
| ------- | ------------------------------ | ----------- | -------------------------------- | --------------------------------- | ------------------- | ------ |
| T-01    | test_create_book               | Unit        | BookCreate with valid data       | Book saved with auto-generated ID | Book saved, ID=1    | PASS   |
| T-02    | test_get_all_books_empty       | Unit        | No books in DB                   | Empty list returned               | [] returned         | PASS   |
| T-03    | test_add_book                  | Integration | POST /books/ with JSON body      | 201 status, book data in response | 201, correct JSON   | PASS   |
| T-04    | test_get_book_not_found        | Integration | GET /books/9999                  | 404 status                        | 404 returned        | PASS   |
| T-05    | test_add_book_validation_error | Integration | POST /books/ with missing fields | 422 status                        | 422 returned        | PASS   |
| T-06    | test_delete_book               | Integration | DELETE /books/{id}               | 204 status, book removed          | 204, confirmed gone | PASS   |

Fill this table with actual results from your `pytest -v` output. Include all tests.

---

### Key Testing Concepts Applied

**Unit test vs. Integration test:** Unit tests call `crud.py` functions directly with a raw DB session — they test business logic in isolation. Integration tests use `TestClient` to send real HTTP requests — they test the full stack (routing + validation + CRUD + DB + serialization).

**Test isolation:** The `setup_database` fixture creates fresh tables before each test and drops them after. No test data leaks between tests.

**Dependency override:** `app.dependency_overrides[get_db]` swaps the production database for a test database without changing any application code.

**Black-box testing (integration):** Tests only interact with the API through its public HTTP interface. They don't know about internal implementation — they only verify inputs and outputs.

**White-box testing (unit):** Tests directly call internal functions and verify internal state (database records).

---

### Practical Checklist (Before Submission)

- [ ] At least 6 unit tests in `test_crud.py` (cover create, read, delete, edge cases).
- [ ] At least 6 integration tests in `test_books.py` (cover all endpoints + error cases).
- [ ] All tests pass when running `pytest -v`.
- [ ] Test database is isolated (not the production `library.db`).
- [ ] Test results table is documented with all test IDs, names, types, and pass/fail status.
- [ ] `requirements.txt` updated with `pytest` and `httpx`.

---

## Practical 6: Version Control (Git), CI/CD Workflow Setup, and Containerization Using Docker

**Duration:** 2 hours

### Objective

Apply version control using Git (commit, branch, merge, conflict resolution), set up a basic CI/CD pipeline using GitHub Actions, and containerize the FastAPI application using Docker.

---

### Part A: Version Control with Git

#### Tool Setup

**Step 1: Install Git.** Download from https://git-scm.com/downloads. During installation on Windows, select "Git from the command line and also from 3rd-party software."

Verify:

```bash
git --version
```

**Step 2: Configure Git (one-time setup).**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Initialize the Repository

Navigate to the project directory (from Practical 4) and initialize Git:

```bash
cd library_api
git init
```

#### Create `.gitignore`

Create a `.gitignore` file in the project root to exclude unnecessary files:

```
venv/
__pycache__/
*.pyc
*.db
.env
.pytest_cache/
test.db
```

#### Basic Git Workflow: Add, Commit, Push

```bash
# Stage all files
git add .

# Commit with a descriptive message
git commit -m "feat: initial FastAPI project with book CRUD endpoints"

# Create a GitHub repository (do this on github.com first), then link it
git remote add origin https://github.com/yourusername/library-api.git
git branch -M main
git push -u origin main
```

#### Branching and Merging

```bash
# Create and switch to a new feature branch
git checkout -b feature/add-members

# Make changes (e.g., add a members module)
# ... edit files ...

# Stage and commit changes on the feature branch
git add .
git commit -m "feat: add member model and CRUD endpoints"

# Switch back to main
git checkout main

# Merge the feature branch into main
git merge feature/add-members

# Push the updated main branch
git push origin main

# Delete the feature branch (optional, cleanup)
git branch -d feature/add-members
```

#### Simulating and Resolving a Merge Conflict

```bash
# On main, edit line 1 of README.md to say "# Library API v1"
git add README.md
git commit -m "docs: update title to v1"

# Create a branch and edit the same line differently
git checkout -b feature/rename
# Edit line 1 of README.md to say "# Library Management System"
git add README.md
git commit -m "docs: rename to Library Management System"

# Switch back to main and try to merge
git checkout main
git merge feature/rename
# OUTPUT: CONFLICT (content): Merge conflict in README.md
```

**Resolve the conflict:** Open `README.md`. Git marks the conflict:

```
<<<<<<< HEAD
# Library API v1
=======
# Library Management System
>>>>>>> feature/rename
```

Choose the correct version (or combine them). Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`). Save the file. Then:

```bash
git add README.md
git commit -m "fix: resolve merge conflict in README"
```

#### Useful Git Commands Reference

| Command                   | Purpose                                            |
| ------------------------- | -------------------------------------------------- |
| `git status`              | See which files are modified, staged, or untracked |
| `git log --oneline -5`    | View last 5 commits in compact format              |
| `git diff`                | See unstaged changes                               |
| `git stash`               | Temporarily save uncommitted changes               |
| `git stash pop`           | Restore stashed changes                            |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged              |

---

### Part B: Containerization Using Docker

#### Tool Setup

**Step 1: Install Docker Desktop.** Download from https://www.docker.com/products/docker-desktop. On Windows, ensure WSL 2 is enabled (the installer will prompt you). After installation, verify:

```bash
docker --version
```

#### Create `Dockerfile`

Create a file named `Dockerfile` (no extension) in the project root:

```dockerfile
# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Create `.dockerignore`

Create `.dockerignore` in the project root to keep the image small:

```
venv/
__pycache__/
*.pyc
*.db
.git/
.pytest_cache/
tests/
.env
```

#### Build and Run the Docker Container

```bash
# Build the Docker image (the dot refers to the current directory)
docker build -t library-api .

# Run the container
docker run -d -p 8000:8000 --name library-container library-api

# Verify it's running
docker ps
```

Open http://localhost:8000/docs in a browser — the Swagger UI should appear, served from inside the container.

#### Useful Docker Commands

| Command                         | Purpose                                 |
| ------------------------------- | --------------------------------------- |
| `docker ps`                     | List running containers                 |
| `docker ps -a`                  | List all containers (including stopped) |
| `docker logs library-container` | View container logs                     |
| `docker stop library-container` | Stop the container                      |
| `docker rm library-container`   | Remove the container                    |
| `docker images`                 | List all local images                   |
| `docker rmi library-api`        | Remove the image                        |

---

### Part C: CI/CD Workflow with GitHub Actions

#### What Is CI/CD?

**Continuous Integration (CI):** Every time code is pushed to GitHub, automated checks run — linting, tests, builds. If any check fails, the team is notified before the broken code reaches production.

**Continuous Deployment (CD):** After CI passes, the application is automatically built into a Docker image and pushed to a container registry (e.g., Docker Hub), ready for deployment.

#### Create the Workflow File

Create the directory structure and file:

```
.github/
└── workflows/
    └── ci.yml
```

#### Write the CI Workflow — `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

# Trigger: run on every push or pull request to main
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository code
      - name: Checkout code
        uses: actions/checkout@v4

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest httpx pytest-cov

      # Step 4: Run tests
      - name: Run tests
        run: pytest -v --cov=app --cov-report=term-missing

  docker:
    runs-on: ubuntu-latest
    needs: test # Only build Docker image if tests pass

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t library-api .

      - name: Verify Docker image runs
        run: |
          docker run -d -p 8000:8000 --name test-container library-api
          sleep 5
          curl -f http://localhost:8000/ || exit 1
          docker stop test-container
```

#### How It Works

1. Every time you `git push` to the `main` branch, GitHub Actions automatically runs the `test` job — installs dependencies, runs all pytest tests.
2. If all tests pass, the `docker` job runs — builds the Docker image and verifies the container starts successfully.
3. If any step fails, the pipeline stops and GitHub shows a red ❌ on the commit. If all pass, a green ✅ appears.

#### Commit and Push the Workflow

```bash
git add .github/workflows/ci.yml Dockerfile .dockerignore
git commit -m "ci: add GitHub Actions workflow and Dockerfile"
git push origin main
```

Go to your GitHub repository → **Actions** tab → watch the pipeline execute.

---

### Practical Checklist (Before Submission)

- [ ] Git repository is initialized with a clean `.gitignore`.
- [ ] At least 3 meaningful commits with descriptive messages (use conventional format: `feat:`, `fix:`, `docs:`, `ci:`).
- [ ] At least one feature branch was created, committed to, and merged into main.
- [ ] A merge conflict was simulated and resolved (document the conflict with a screenshot or paste).
- [ ] `Dockerfile` is present and the application runs successfully inside a container.
- [ ] Docker container is accessible at `http://localhost:8000/docs`.
- [ ] `.github/workflows/ci.yml` is present and pushes trigger the pipeline.
- [ ] GitHub Actions shows a passing (green ✅) pipeline run (screenshot the Actions tab).
- [ ] Repository is pushed to GitHub with all files.

---
