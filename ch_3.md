# Chapter 3: Software Requirements Engineering (6 hours, 8 marks)

---

## 3.1 Requirement Engineering Process

> **What is requirement engineering? Explain its steps. [4 marks] (2074 Chaitra - IOE - Old Syllabus Relevant)**
>
> **What do you mean by a software requirements document? [2 marks] (2078 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Explain the requirement engineering process in detail. [6 marks] (2078 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Why is it so difficult to gain a clear understanding of what the customer wants? [3 marks] (2081 Bhadra - IOE - Old Syllabus Relevant)**
>
> **What are the different techniques used for requirements gathering and analysis? Explain any three methods in detail. [7 marks] (2070 Ashad - IOE - Old Syllabus Relevant)**

**Requirements engineering (RE)** is the broad spectrum of tasks and techniques that lead to an understanding of requirements. It begins during the communication activity and continues into modeling. RE establishes the solid base for design and construction — without it, the resulting software has a high probability of not meeting customer needs.

### Seven Tasks of Requirements Engineering

**1. Inception** — establish a basic understanding of the problem, the people who want a solution, and the nature of the desired solution. At inception, stakeholders are identified, project scope is outlined, and initial communication is established.

**2. Elicitation** — actively gather requirements from stakeholders. Ask what the system must accomplish, how it fits into business needs, and how it will be used daily. Elicitation also involves understanding business goals (functional and non-functional) and prioritizing them.

**3. Elaboration** — develop a refined requirements model that identifies various aspects of software function, behavior, and information. User scenarios from elicitation are parsed to extract analysis classes, attributes, and services. The key is to describe the problem sufficiently for design and then move on — do not obsess over unnecessary detail.

**4. Negotiation** — reconcile conflicting requirements among stakeholders. Customers and users rank requirements and discuss priority conflicts. The goal is a "win-win" result: both sides achieve some measure of satisfaction. Requirements are eliminated, combined, or modified based on cost, risk, and priority assessment.

**5. Specification** — document the agreed-upon requirements. A specification can be a written document, graphical models, a formal mathematical model, a collection of usage scenarios, a prototype, or any combination. For large systems, a formal SRS document is used; for smaller products, user stories or use cases may suffice.

**6. Validation** — assess the quality of requirements work products. Ensure requirements are stated unambiguously, are consistent, and that omissions and errors are corrected. The primary mechanism is a **technical review** involving software engineers, customers, users, and other stakeholders.

**7. Management** — identify, control, and track requirements and changes to requirements throughout the project lifecycle. Requirements change constantly, and management activities ensure that changes are handled systematically (closely related to software configuration management).

### Why It Is Difficult to Understand Customer Requirements

- Customers may have only a vague idea of what is required.
- Different stakeholders have conflicting opinions and priorities.
- Stakeholders may have unspoken assumptions and interpret meanings differently.
- Requirements are often stated in ambiguous or untestable terms (e.g., "the system should be user-friendly").
- Customers may not know exactly what they want until they see working software.
- Project goals may be unclear, and technical knowledge of customers may be limited.
- Requirements continue to change throughout the project.

### Requirements Gathering Techniques

**Interviews** — one-on-one or group sessions where the requirements engineer asks structured or unstructured questions to stakeholders. Effective for understanding individual perspectives, uncovering implicit needs, and clarifying details. Best combined with other methods.

**Facilitated Meetings (Workshops / JAD Sessions)** — structured meetings attended by both software engineers and stakeholders. A facilitator controls the meeting. Participants develop lists of objects, services, constraints, and performance criteria. Combined lists are refined through discussion to reach consensus. Rules for preparation and participation are established beforehand.

**Prototyping** — build a preliminary version of the system (or part of it) to help stakeholders visualize and refine requirements. Particularly useful when requirements are fuzzy or when the UI is a major concern.

**Observation (Ethnography)** — observe end users performing their actual work to understand how the existing system is used and identify implicit requirements that users may not articulate. Useful for understanding workflows and business processes.

**Questionnaires/Surveys** — collect requirements from a large number of stakeholders simultaneously. Useful for gathering quantitative data on preferences and priorities.

**Document Analysis** — study existing documentation (manuals, forms, reports, regulations, legacy system specifications) to understand the problem domain and extract requirements.

### A Software Requirements Document

A **software requirements document (SRD)** — commonly called the Software Requirements Specification (SRS) — is a formal, written understanding of the problem that all parties agree upon. It describes the required informational, functional, and behavioral domains for the system, serves as a contractual basis between customer and developer, and provides the foundation for design, testing, and maintenance.

---

## 3.2 SRS (Structure, Characteristics, Users)

> **What is the importance of the SRS document in software development? [3 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Identify and document functional as well as non-functional requirements for "issuing a book from a library." [5 marks] (2079 Bhadra - IOE - Old Syllabus Relevant)**

### Importance of the SRS

- Provides a clear, shared understanding of what the software must do — eliminating ambiguity between customers, developers, and testers.
- Serves as a contractual agreement between the customer and the development team.
- Acts as the basis for project planning, cost estimation, and scheduling.
- Provides the foundation for system design, implementation, and testing (traceability).
- Serves as a reference for maintenance and future enhancements.
- Reduces the risk of building the wrong product.

### SRS Structure (Based on IEEE 830 / ISO/IEC/IEEE 29148)

**Section 1: Introduction** — Purpose of the SRS, scope of the software, definitions/acronyms, references, and document overview.

**Section 2: Overall Description** — Product perspective (context within a larger system), product functions (high-level summary), user characteristics (profiles of target users, their expertise), constraints (hardware, software, regulatory), and assumptions/dependencies.

**Section 3: Specific Requirements** — Functional requirements (detailed descriptions of each function), external interface requirements (user, hardware, software, communication interfaces), performance requirements (response time, throughput), design constraints, and non-functional attributes (reliability, security, maintainability, portability).

### Characteristics of a Good SRS

- **Correct** — accurately represents stakeholder needs.
- **Unambiguous** — each requirement has only one interpretation.
- **Complete** — contains all significant requirements; no TBD placeholders.
- **Consistent** — no requirement conflicts with another.
- **Verifiable (Testable)** — every requirement can be tested through an objective process.
- **Modifiable** — structure allows easy changes while maintaining consistency.
- **Traceable** — each requirement can be traced to its source and to corresponding design/test elements.
- **Feasible** — achievable within budget, schedule, and technology constraints.

### Users of the SRS

- **Customers/Clients** — verify that the document captures their needs.
- **Project Managers** — use it for planning, estimation, and tracking.
- **Developers/Designers** — use it as the basis for design and implementation.
- **Testers/QA** — derive test cases from requirements to validate the system.
- **Maintenance Engineers** — reference it for understanding the system during future modifications.

### Example: Requirements for "Issuing a Book from a Library"

**Functional Requirements:**

- The system shall allow the librarian to search for a book by title, author, or ISBN.
- The system shall verify the borrower's library membership status before issuing.
- The system shall check if the book is available (not already issued or reserved).
- The system shall record the issue date and calculate the due date (e.g., 14 days from issue).
- The system shall update the book's status to "issued" and associate it with the borrower's account.
- The system shall generate an issue receipt for the borrower.

**Non-Functional Requirements:**

- **Performance** — the system shall process a book issue transaction within 3 seconds.
- **Usability** — the interface shall be simple enough for a librarian with minimal computer training.
- **Security** — only authorized librarians shall be able to issue books.
- **Reliability** — the system shall be available during all library operating hours (99.5% uptime).
- **Maintainability** — the system shall be designed to allow easy addition of new book categories.

### Complete SRS Example (IEEE 830 Format) — Online Library Management System

**SOFTWARE REQUIREMENTS SPECIFICATION**
**Online Library Management System (OLMS)**
**Version 1.0**

**1. Introduction**

**1.1 Purpose**
This SRS describes the functional and non-functional requirements for the Online Library Management System (OLMS). It is intended for use by the development team, testers, project managers, and the library administration (client).

**1.2 Scope**
OLMS is a web-based application that automates the core operations of a college library — cataloging books, managing member registrations, issuing and returning books, tracking overdue items, and generating reports. The system will replace the existing manual register-based process. It will not handle inter-library loans or e-book licensing in this version.

**1.3 Definitions, Acronyms, and Abbreviations**

- **OLMS** — Online Library Management System.
- **Member** — a registered student or faculty who can borrow books.
- **Librarian** — an authorized staff member who manages the system.
- **ISBN** — International Standard Book Number.

**1.4 References**

- IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications.
- College Library Policy Document, Version 3.2.

**1.5 Overview**
Section 2 provides an overall description of the product. Section 3 specifies detailed functional and non-functional requirements.

---

**2. Overall Description**

**2.1 Product Perspective**
OLMS is a standalone web application. It interfaces with an existing college student database for member verification. It runs on a web server (Apache/Nginx) with a MySQL database backend and is accessed through standard web browsers.

**2.2 Product Functions (High-Level)**

- Book catalog management (add, update, delete, search).
- Member registration and profile management.
- Book issuing and returning.
- Fine calculation for overdue books.
- Reservation of books currently issued to others.
- Report generation (most borrowed books, overdue list, member activity).

**2.3 User Characteristics**

- **Librarian** — moderate computer literacy; primary user who performs all administrative operations.
- **Member (Student/Faculty)** — basic computer literacy; uses the system to search the catalog, view their borrowing history, and reserve books.
- **Administrator** — technical staff responsible for system configuration and user management.

**2.4 Constraints**

- The system must run on the college's existing Linux server infrastructure.
- The system must comply with the college's data privacy policy.
- Maximum budget: NPR 5,00,000.

**2.5 Assumptions and Dependencies**

- Members already have valid college IDs for authentication.
- The college provides a stable internet connection for the server.
- The student database API is available and documented.

---

**3. Specific Requirements**

**3.1 Functional Requirements**

**FR-01: Search Book** — The system shall allow members and librarians to search the catalog by title, author, ISBN, or category. Search results shall display book title, author, availability status, and shelf location.

**FR-02: Add New Book** — The system shall allow the librarian to add a new book by entering title, author(s), ISBN, publisher, edition, category, quantity, and shelf location.

**FR-03: Register Member** — The system shall allow the librarian to register a new member by entering name, college ID, department, contact number, and email. The system shall verify the college ID against the student database.

**FR-04: Issue Book** — The system shall allow the librarian to issue a book to a member. The system shall verify: (a) the member's account is active, (b) the member has not exceeded the borrowing limit (max 3 books), and (c) the book is available. Upon issuing, the system shall record the issue date, set the due date (14 days), and update the book's availability status.

**FR-05: Return Book** — The system shall allow the librarian to process a book return. If the book is overdue, the system shall automatically calculate the fine (NPR 5 per day). The system shall update the book's status to "available."

**FR-06: Reserve Book** — The system shall allow a member to reserve a book that is currently issued. When the book is returned, the system shall notify the reserving member via email.

**FR-07: Generate Reports** — The system shall generate the following reports: (a) list of overdue books with member details, (b) most borrowed books in a given period, (c) member borrowing history.

**FR-08: User Login** — The system shall authenticate users (librarian, member, admin) using college ID and password. Passwords shall be hashed before storage.

**3.2 External Interface Requirements**

**User Interface** — The system shall provide a responsive web interface accessible on desktop browsers (Chrome, Firefox, Edge). The librarian dashboard shall display pending returns and overdue alerts on the home screen.

**Hardware Interface** — The system shall interface with a barcode scanner for reading book ISBNs and member IDs during issue/return operations.

**Software Interface** — The system shall connect to the college student database via a REST API to verify member registration.

**Communication Interface** — The system shall send email notifications (overdue reminders, reservation availability) via SMTP.

**3.3 Performance Requirements**

- The system shall support at least 100 concurrent users.
- Search results shall be displayed within 2 seconds.
- Book issue/return transactions shall complete within 3 seconds.

**3.4 Design Constraints**

- The system shall be developed using HTML/CSS, JavaScript (frontend) and Python/Django (backend) with MySQL database.
- The system shall follow a three-tier architecture (presentation, application, data).

**3.5 Non-Functional Requirements**

- **Reliability** — the system shall have 99% uptime during library operating hours (8 AM – 8 PM).
- **Security** — only authenticated librarians shall issue/return books. All passwords shall be stored using bcrypt hashing. The system shall enforce session timeout after 15 minutes of inactivity.
- **Usability** — a new librarian shall be able to issue a book within 2 minutes of first use without external assistance.
- **Maintainability** — the codebase shall follow MVC architecture with documented APIs to allow future enhancements (e.g., e-book support).
- **Portability** — the system shall be deployable on any Linux server with Python 3.8+ and MySQL 8.0+.

---

## 3.3 Functional and Non-Functional Requirements

> **Explain functional and non-functional requirements with examples. [6 marks] (2069 Ashad - IOE - Old Syllabus Relevant)**
>
> **Differentiate functional and non-functional requirements. [7 marks] (2069 Chaitra - IOE - Old Syllabus Relevant)**
>
> **Distinguish between user and system requirements. [2 marks] (2079 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Why should an engineer ensure that functional and non-functional needs are in a requirements specification document? [4 marks] (2079 Bhadra - IOE - Old Syllabus Relevant)**
>
> **List and explain functional (any two) and non-functional requirements of an airlines reservation system. [6 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Explain functional (Order Food, Make Payment) and non-functional (all) requirements of an online food ordering system. [6 marks] (2081 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Prepare functional requirements for an online ticket booking system for a movie theatre. [4 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**
>
> **List functional and non-functional requirements for a Restaurant Information System. [5 marks] (2068 Chaitra - IOE - Old Syllabus Relevant)**

### Functional Requirements

Functional requirements describe **what** the system must do — the specific functions, features, services, and behaviors the software must provide. They define the system's response to specific inputs under specific conditions.

**Example:** "The system shall allow users to search flights by origin, destination, and date."

### Non-Functional Requirements (NFRs)

Non-functional requirements describe **how well** the system must perform — quality attributes, performance characteristics, security constraints, and general system constraints. They constrain the overall functioning of the system rather than defining specific features.

**Categories of NFRs:**

- **Performance** — response time, throughput, capacity (e.g., "The page shall load within 2 seconds under 1000 concurrent users").
- **Reliability** — mean time between failures, availability (e.g., "99.9% uptime").
- **Usability** — ease of use, learnability (e.g., "A new user shall be able to complete registration within 3 minutes without help").
- **Security** — authentication, authorization, data encryption (e.g., "All passwords shall be stored using bcrypt hashing").
- **Maintainability** — ease of modification, modular design.
- **Portability** — ability to operate across different platforms.
- **Scalability** — ability to handle growth in users, data, or transactions.

### Functional vs. Non-Functional Requirements

| Functional Requirements                                                   | Non-Functional Requirements                                 |
| ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Describe what the system does                                             | Describe how well the system performs                       |
| Specify specific features and behaviors                                   | Specify quality attributes and constraints                  |
| Example: "User can place an order"                                        | Example: "Order confirmation within 2 seconds"              |
| Tested by executing the function directly                                 | Tested by measuring performance, stress, security, etc.     |
| If absent, the system is incomplete because required features are missing | If absent, the system becomes unreliable, slow, or insecure |
| Documented as use cases, user stories, or feature lists                   | Documented as quality metrics, constraints, or SLA targets  |

### Why Both Must Be in the SRS

Functional requirements alone do not guarantee a usable system. A system may perform all required functions but fail if it is too slow, insecure, or difficult to use. Conversely, meeting NFRs without delivering required features is meaningless. Both types are essential for:

- Complete system specification — developers know what to build and to what standard.
- Testing — testers need both functional test cases and performance/security benchmarks.
- Contract enforcement — stakeholders need measurable criteria for acceptance.
- Risk reduction — missing NFRs often lead to costly rework or system rejection.

### User Requirements vs. System Requirements

- **User requirements** — high-level statements written in natural language (possibly with diagrams) describing what the system should provide to users and the constraints under which it operates. Written for customers and managers. Example: "The system should allow customers to book flights."
- **System requirements** — detailed, precise descriptions of system functions, services, and constraints. Written for developers and testers. Example: "The system shall accept origin (IATA code), destination (IATA code), departure date (YYYY-MM-DD), and number of passengers (1–9) as search parameters and return matching flights sorted by price within 3 seconds."

### Example: Airlines Reservation System

**Functional Requirements:**

- **Search Flights** — the system shall allow passengers to search for flights by origin, destination, date, and class. Results shall display flight number, departure/arrival times, duration, and price.
- **Book a Ticket** — the system shall allow passengers to select a flight, enter passenger details, choose a seat, and confirm the booking. A booking confirmation with a PNR number shall be generated.

**Non-Functional Requirements:**

- **Performance** — search results shall be returned within 3 seconds.
- **Availability** — the system shall be available 24/7 with 99.9% uptime.
- **Security** — payment information shall be encrypted using TLS 1.2 or higher; PCI-DSS compliance is mandatory.
- **Scalability** — the system shall support at least 10,000 concurrent users.
- **Usability** — the booking process shall be completable within 5 steps.

### Example: Online Food Ordering System

**Functional Requirements:**

- **Order Food** — the customer shall browse the menu, select food items, specify quantity, add customizations (e.g., extra cheese, no onions), and add items to the cart. The cart shall display a summary with item-wise and total prices.
- **Make Payment** — the system shall support multiple payment methods (credit/debit card, digital wallet, cash on delivery). Upon successful payment, an order confirmation with an estimated delivery time shall be displayed.

**Non-Functional Requirements:**

- **Performance** — the payment transaction shall complete within 5 seconds.
- **Security** — all payment data shall be transmitted over encrypted connections; user passwords shall be hashed.
- **Usability** — the system shall support a mobile-responsive design.
- **Reliability** — the system shall handle order processing without data loss during peak hours.
- **Availability** — 99.5% uptime during restaurant operating hours.

### Example: Online Ticket Booking System for a Movie Theatre

**Functional Requirements:**

- The system shall display currently running movies with showtimes, language, and format (2D/3D).
- The system shall allow users to select a movie, showtime, and preferred seats from a seat map.
- The system shall hold selected seats for a limited time (e.g., 10 minutes) during payment processing.
- The system shall process online payment and generate an e-ticket with a unique booking ID and QR code.
- The system shall allow users to cancel a booking up to 2 hours before showtime and process a refund.
- The system shall send booking confirmation and e-ticket via email and SMS.

### Example: Restaurant Information System

**Functional Requirements:**

- The system shall allow customers to view the restaurant menu with prices, descriptions, and images.
- The system shall allow customers to place dine-in or takeaway orders.
- The system shall allow waitstaff to update order status (received, preparing, served).
- The system shall generate a bill with itemized charges and applicable taxes.
- The system shall support table reservation with date, time, and party size.

**Non-Functional Requirements:**

- **Performance** — order placement shall be processed within 2 seconds.
- **Usability** — the interface shall be operable on tablets used by waitstaff.
- **Reliability** — the system shall not lose orders during power failures (persistent storage).
- **Security** — customer payment data shall be handled per PCI-DSS standards.
- **Scalability** — the system shall handle peak-hour load without degradation.

---

## 3.4 Gathering Requirements Using Use Case Modeling and Scenarios

> **Prepare a use case diagram for an event management system. [4 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram for an online food ordering system. [5 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram for an online appointment booking app. [5 marks] (2081 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Prepare use case diagrams for an automated ticket issuing system. [5 marks] (2081 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram illustrating interactions between a doctor, patients, and prescriptions. [5 marks] (2078 Bhadra - IOE - Old Syllabus Relevant)**

### Use Cases

A **use case** describes how an end user (playing a specific role) interacts with the system under a specific set of circumstances. It tells a stylized story from the end user's point of view. Use cases can be expressed as narrative text (user stories), outlines, template-based descriptions, or UML diagrams.

### Key Elements of a Use Case

- **Actor** — any external entity (person, device, or external system) that communicates with the system. Actors represent roles, not specific individuals. A single user may play multiple roles (and thus be multiple actors).
- **Primary actor** — directly interacts with and derives benefit from the system.
- **Secondary actor** — supports the system so primary actors can do their work.
- **Use case** — a specific function or service provided by the system, described from the actor's perspective.
- **System boundary** — a rectangle that defines the scope of the system; actors are outside, use cases are inside.

### Relationships in Use Case Diagrams

- **Association** — a solid line connecting an actor to a use case, indicating interaction.
- **Include (<<include>>)** — a dashed arrow from the base use case to the included use case. The included use case is **always** executed as part of the base use case. Used for common, reusable functionality. Example: "Place Order" includes "Verify Login."
- **Extend (<<extend>>)** — a dashed arrow from the extending use case to the base use case. The extending use case is executed **only under certain conditions**. The base use case is complete on its own. Example: "Checkout" may be extended by "Apply Coupon."
- **Generalization** — a solid line with a hollow triangle arrowhead, representing inheritance between actors or between use cases.

### Writing a Use Case (Template-Based Description)

A formal use case includes: use case name, primary actor, goal, preconditions, trigger, main scenario (numbered steps), exceptions/alternate flows, priority, frequency of use, and open issues.

### Use Case Diagram Examples

**Note:** In exams, draw these with: a rectangle for the system boundary (labeled with the system name), stick figures for actors (outside the boundary), ovals for use cases (inside the boundary), solid lines for associations, and dashed arrows with stereotypes for <<include>> and <<extend>> relationships.

**Event Management System:**

- **Actors:** Organizer, Attendee, Admin.
- **Use Cases:** Create Event, Edit Event, Delete Event, Register for Event, View Event Details, Search Events, Cancel Registration, Generate Reports, Manage Venues, Send Notifications.
- **Relationships:** "Create Event" includes "Verify Organizer Login." "Register for Event" includes "Make Payment." "Register for Event" may extend "Apply Discount Code."

**Online Food Ordering System:**

- **Actors:** Customer, Restaurant Admin, Delivery Personnel.
- **Use Cases:** Browse Menu, Search Items, Add to Cart, Place Order, Make Payment, Track Order, Rate/Review, Manage Menu, Update Order Status, Assign Delivery.
- **Relationships:** "Place Order" includes "Make Payment." "Place Order" may extend "Apply Coupon."

**Online Appointment Booking App:**

- **Actors:** Patient, Doctor, Admin.
- **Use Cases:** Register/Login, Search Doctor, View Available Slots, Book Appointment, Cancel Appointment, View Appointment History, Manage Schedule, Send Reminder Notification.
- **Relationships:** "Book Appointment" includes "Verify Patient Login." "Book Appointment" may extend "Send Reminder Notification."

**Automated Ticket Issuing System:**

- **Actors:** Passenger, Admin, Payment Gateway.
- **Use Cases:** Select Route, Select Seat, Make Payment, Issue Ticket, Cancel Ticket, View Schedule, Generate Reports.
- **Relationships:** "Issue Ticket" includes "Make Payment." "Cancel Ticket" may extend "Process Refund."

**Doctor-Patient-Prescription System:**

- **Actors:** Doctor, Patient, Pharmacist.
- **Use Cases:** Register Patient, View Patient History, Diagnose, Write Prescription, View Prescription, Dispense Medicine, Schedule Follow-Up.
- **Relationships:** "Diagnose" includes "View Patient History." "Write Prescription" is associated with Doctor. "View Prescription" and "Dispense Medicine" are associated with Pharmacist.

---

## 3.5 Agile Requirements Engineering

### 3.5.1 User Stories and Acceptance Criteria

A **user story** is a short, informal description of a feature told from the perspective of the user who wants the capability. It serves as a placeholder for conversation rather than a rigid specification.

**Standard Format:**

> As a [type of user], I want [some goal] so that [some reason/benefit].

**Example:** "As a customer, I want to filter products by price range so that I can find items within my budget."

**INVEST Criteria for Good User Stories:**

- **I — Independent** — the story is self-contained and not dependent on other stories.
- **N — Negotiable** — details are open for discussion; the story is not a rigid contract.
- **V — Valuable** — it delivers clear value to the user or business.
- **E — Estimable** — the team can estimate the effort required.
- **S — Small** — small enough to be completed within a single sprint.
- **T — Testable** — it has clear criteria that allow verification.

**Acceptance Criteria** define the specific conditions that must be satisfied for a user story to be considered complete. They bridge the gap between the user story and the implementation.

**Given-When-Then Format (BDD Style):**

- **Given** [a precondition/context],
- **When** [an action is performed],
- **Then** [an expected result occurs].

**Example:**

- Story: "As a customer, I want to reset my password so that I can regain access if I forget it."
- Acceptance criteria:
  - Given the user is on the login page, when they click "Forgot Password" and enter a registered email, then a password reset link shall be sent to that email within 1 minute.
  - Given the user clicks the reset link, when they enter a new password meeting complexity rules, then the password shall be updated and a confirmation displayed.
  - Given the user enters an unregistered email, when they submit the form, then an error message "Email not found" shall be displayed.

### 3.5.2 Product Backlog Creation and Prioritization

The **product backlog** is an ordered, evolving list of everything needed in the product — features, enhancements, bug fixes, and technical tasks. It is the single source of requirements for the development team. The **Product Owner** is responsible for maintaining and prioritizing the backlog.

**Creating the Product Backlog:**

- Gather initial user stories from stakeholders through interviews, workshops, and brainstorming.
- Write each requirement as a user story with acceptance criteria.
- Estimate effort for each story (using story points or ideal days).
- Order the backlog by priority — highest-priority items at the top are refined in detail; lower items remain coarser.

**Prioritization Techniques:**

- **MoSCoW Method** — categorize items as Must Have (essential, non-negotiable), Should Have (important but not critical for current release), Could Have (desirable if time permits), and Won't Have (explicitly out of scope for now).
- **Business Value vs. Effort** — prioritize items that deliver the highest business value relative to their development effort.
- **Risk-Based** — address high-risk items early to reduce uncertainty.
- **Kano Model** — classify features as Basic (expected), Performance (more is better), or Delighters (unexpected positive features).

### 3.5.3 Story Mapping Basics

**User story mapping**, popularized by Jeff Patton, is a visual technique for organizing user stories to provide the "big picture" of the product while maintaining the detail of individual stories. It addresses the limitation of flat backlogs, which often lose context of the overall user experience.

**Structure of a Story Map:**

- **Backbone (horizontal axis)** — the high-level user activities arranged left-to-right following the narrative flow of the user journey (the sequence of steps a user takes to achieve a goal).
- **Ribs (vertical axis)** — beneath each backbone activity, specific user tasks and stories are stacked vertically in order of priority (most important at top).
- **Release slices (horizontal lines)** — drawn across the map to group stories into releases. The topmost slice forms the **Minimum Viable Product (MVP)** or "walking skeleton."

**Steps to Create a Story Map:**

- Frame the problem — identify users and their goals.
- Map the user journey — outline the main activities (backbone).
- Break down activities into user tasks and specific stories (ribs).
- Prioritize stories vertically under each activity.
- Slice horizontally for release planning.

**Benefits:**

- Visualizes the entire product scope and prevents losing sight of the big picture.
- Identifies gaps, dependencies, and missing functionality.
- Facilitates release planning by enabling teams to slice out cohesive, valuable releases.
- Improves communication and shared understanding among team members and stakeholders.

### 3.5.4 Continuous Requirements Refinement (Backlog Grooming)

**Backlog refinement** (also called backlog grooming) is the ongoing process of reviewing, updating, and elaborating product backlog items to ensure they are ready for upcoming sprints. It is not a one-time event but a continuous activity throughout the project.

**Activities during backlog refinement:**

- **Adding detail** — break down large stories (epics) into smaller, implementable user stories.
- **Re-estimating** — update effort estimates as the team gains more understanding.
- **Re-prioritizing** — adjust the order of backlog items based on changing business needs, customer feedback, or new information learned from recent sprints.
- **Removing obsolete items** — delete stories that are no longer relevant.
- **Adding acceptance criteria** — ensure each story near the top of the backlog has clear, testable acceptance criteria.
- **Identifying dependencies** — flag stories that depend on others so the team can plan accordingly.

**When it happens:**

- Typically, teams dedicate about 10% of sprint capacity to backlog refinement.
- It can occur during a dedicated refinement meeting (mid-sprint) or informally throughout the sprint.
- The Product Owner, development team, and Scrum Master participate.

**Goal:** Ensure that items at the top of the backlog are "ready" — small enough, well-understood, estimated, and have clear acceptance criteria — so that sprint planning is efficient and the team can begin work immediately.

**Refinement vs. Sprint Planning:** Refinement prepares items for future sprints; sprint planning selects and commits to items for the upcoming sprint. Without effective refinement, sprint planning becomes chaotic and time-consuming.

---
