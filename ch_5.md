# Chapter 5: System Modeling (9 hours)

---

## 5.1 System Modeling

> **Why is system modeling important? [2 marks] (2068 Chaitra - IOE - Old Syllabus Relevant)**

### What Is System Modeling?

**System modeling** is the process of developing abstract representations (models) of a system. Each model presents a different view or perspective of that system, including its data, its functions, its behavior, or its structure. Models are typically expressed using a standardized graphical notation, most commonly the **Unified Modeling Language (UML)**.

System models are used during requirements analysis to help understand the existing system and the requirements for the new system. They are also used during design to describe the system to engineers implementing it. Because models are abstractions, they deliberately omit detail. They are simpler than the reality they represent, allowing stakeholders to focus on specific aspects of the system without being overwhelmed by complexity.

### 5.1.1 Need for System Modeling

- **Clarifies understanding.** Models force stakeholders and developers to think carefully about system requirements, exposing ambiguities, inconsistencies, and gaps that text descriptions alone may hide.
- **Facilitates communication.** Graphical models serve as a common language between developers, customers, managers, and testers. A well-drawn diagram often conveys structure and flow more effectively than pages of text.
- **Bridges requirements to design.** The requirements model establishes a foundation upon which architectural, interface, and component-level designs are built. It provides traceability from customer needs through design to implementation.
- **Supports analysis and validation.** Models can be reviewed, checked against requirements, and validated before any code is written, catching errors when they are least expensive to fix.
- **Documents the system.** Models serve as long-term documentation that supports maintenance and evolution of the software.

The requirements model must achieve three primary objectives: (1) describe what the customer requires, (2) establish a basis for creating the software design, and (3) define a set of requirements that can be validated once the software is built.

### 5.1.2 Role of Abstractions in Managing Complexity

**Abstraction** is the fundamental mechanism used to manage complexity in system modeling. Complex real-world systems involve thousands of interacting elements such as users, devices, data, rules, and functions. Attempting to model everything simultaneously is impossible. Abstraction works by:

- **Hiding unnecessary detail.** At each level of modeling, only the information relevant to that level's purpose is shown. For example, a context diagram hides internal processes; a class diagram hides algorithmic detail.
- **Separating concerns.** Different models address different concerns: use cases capture functional interactions, class diagrams capture data structures, activity diagrams capture flow of control, and state diagrams capture behavior. No single model attempts to capture everything.
- **Enabling hierarchical decomposition.** Complex systems are modeled top-down. A single high-level abstraction (e.g., "the entire system" in a context diagram) is progressively decomposed into finer-grained components. This allows engineers to manage each piece independently.
- **Supporting multiple viewpoints.** Different stakeholders need different views of the same system. A customer needs a use-case view; an architect needs a structural view; a tester needs a behavioral view. Abstraction enables the creation of multiple complementary models, each targeted at a specific audience.

The five key principles of requirements modeling (Pressman):

**Principle 1:** The information domain (data flowing in, out, and stored within the system) must be represented and understood.

**Principle 2:** The functions the software performs must be defined, including both user-visible functions and internal processing.

**Principle 3:** The software's behavior (as a consequence of external events) must be represented.

**Principle 4:** Models of information, function, and behavior must be partitioned hierarchically to uncover detail in a layered fashion.

**Principle 5:** The analysis should move from essential (problem-domain) information toward implementation detail.

---

## 5.2 Process Modeling Using DFD

> **Design Level-0 and Level-1 DFD for an Examination Management System. [5 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Draw Level-0 and Level-1 DFD of a Student Attendance Management System. [6 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Design Level-0 and Level-1 DFD for an Airline Ticketing System. [7 marks] (2081 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Develop a Context diagram and Level-1 DFD for an online food ordering system. [3+5 marks] (2081 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Draw Level-0 and Level-1 DFD for an online shopping system. [3+5 marks] (2079 Bhadra - IOE - Old Syllabus Relevant)**

### What Is a Data Flow Diagram (DFD)?

A **Data Flow Diagram (DFD)** is a graphical representation that models how data moves through a system. It shows the inputs, outputs, processes (transformations), and data stores involved in a system without prescribing implementation details. DFDs are a core technique of **structured analysis** and focus on **what** the system does with data, not **how** it does it.

### DFD Notation (Symbols)

There are two common notations. The **Yourdon-DeMarco** notation is most commonly used in academic settings:

A **Process** is represented as a circle (Yourdon-DeMarco) or a rounded rectangle (Gane-Sarson). A process transforms incoming data flows into outgoing data flows. Processes are named with verbs (e.g., "Validate Order," "Calculate Total").

A **Data Flow** is represented as a named arrow. It shows the direction and path of data movement between processes, data stores, and external entities. Data flows are named with nouns (e.g., "order details," "payment confirmation").

A **Data Store** is represented as two parallel horizontal lines (Yourdon-DeMarco) or an open-ended rectangle (Gane-Sarson). It represents data at rest, such as a file, a database table, or any repository where data is stored for later use. Data stores are named with nouns (e.g., "Customer Database," "Order File").

An **External Entity** is represented as a rectangle. It represents a source or destination of data that is outside the system boundary. External entities are people, organizations, devices, or other systems that interact with the system. They are named with nouns (e.g., "Customer," "Bank," "Sensor").

### Levels of DFD

DFDs are organized hierarchically into levels, each providing progressively more detail:

**Context Diagram (Level-0 DFD):** The highest-level view of the system. The entire system is represented as a single process (a single circle or rounded rectangle). External entities are shown around it, and data flows between the system and external entities are drawn as labeled arrows. No internal processes or data stores are shown. The context diagram establishes the system boundary, defining what is inside the system and what is outside.

**Level-1 DFD:** Decomposes the single process from the context diagram into its major sub-processes. Shows the main functional areas of the system, the data flows between them, the data stores used to hold information, and the interactions with external entities. Each sub-process in a Level-1 DFD can be further decomposed into a Level-2 DFD, and so on, until each process represents a single, simple, atomic function.

**Level-2+ DFDs:** Further decompose individual processes from Level-1 into more granular detail. They are not always necessary. Decomposition stops when each process is simple enough to be described in a short process specification (minispec).

### Rules for Drawing DFDs

- Every process must have at least one input data flow and at least one output data flow (no "black holes" or "miracles").
- Data cannot flow directly between two external entities. It must pass through at least one process.
- Data cannot flow directly between two data stores. It must pass through at least one process.
- Data cannot flow directly from an external entity to a data store (or vice versa). It must pass through a process.
- Each process, data flow, data store, and external entity must be named.
- **Balancing rule:** All data flows entering/leaving a parent process must also appear in its child (decomposed) diagram. The parent and child diagrams must be consistent.

### Example: Online Food Ordering System (Context Diagram + Level-1 DFD)

**Context Diagram (Level-0):**

The system is represented as a single process: "Online Food Ordering System." External entities include: Customer, Restaurant, Delivery Personnel, Payment Gateway. Data flows: Customer sends "order request" and "payment info" to the system; system sends "order confirmation" and "delivery status" to Customer; system sends "order details" to Restaurant; Restaurant sends "order acceptance" to system; system sends "delivery assignment" to Delivery Personnel; Delivery Personnel sends "delivery update" to system; system sends "payment request" to Payment Gateway; Payment Gateway sends "payment confirmation" to system.

**Level-1 DFD (major processes):**

- **P1: Manage User Account** handles registration, login, and profile updates. It reads from and writes to D1: User Database.
- **P2: Browse Menu** retrieves menu items from D2: Menu Database and displays them to the Customer.
- **P3: Place Order** receives the order request from the Customer, validates items, and creates an order record in D3: Order Database.
- **P4: Process Payment** sends a payment request to the Payment Gateway, receives confirmation, and updates D3: Order Database.
- **P5: Assign Delivery** assigns the order to Delivery Personnel, updates D3: Order Database, and sends the delivery assignment.
- **P6: Track Delivery** receives delivery updates from Delivery Personnel and sends delivery status to the Customer.

---

## 5.3 Scenario-Based Analysis

> **Prepare a use case diagram for an event management system. [4 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram for an online food ordering system. [5 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram for an online appointment booking app. [5 marks] (2081 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Prepare use case diagrams for an automated ticket issuing system. [5 marks] (2081 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Draw a use case diagram illustrating interactions between a doctor, patients, and prescriptions. [5 marks] (2078 Bhadra - IOE - Old Syllabus Relevant)**

### 5.3.1 Concept of Scenarios

A **scenario** is a specific sequence of actions and interactions between an actor and a system that accomplishes a particular goal. Scenarios describe the system from the user's point of view and answer the question: "How will the system be used?"

Scenarios are the foundation of **scenario-based modeling**. The primary tool for capturing scenarios is the **use case**. A use case describes a specific usage scenario, serving as a "contract for behavior," in straightforward language from the perspective of a defined actor. Use cases are often the first part of the requirements model to be developed because they directly capture user expectations.

Scenarios serve multiple purposes: they help stakeholders validate that the system will meet their needs, they provide developers with clear functional expectations, they drive the identification of classes and objects, and they form the basis for test case development.

### 5.3.2 Use-Case Descriptions and Diagrams

#### Actors

An **actor** represents an entity that interacts with the system. Actors may be:

- **Human users** playing a specific role (e.g., Customer, Administrator, Manager). A single physical person can play multiple roles and thus be represented by multiple actors.
- **External systems** or devices that communicate with the system (e.g., Payment Gateway, Sensor, Email Server).

Actors are classified as **primary actors**, who directly use the system to achieve a goal (e.g., a Customer placing an order), or **secondary actors**, who support the system so that primary actors can do their work (e.g., a System Administrator configuring the system).

#### Writing Use Cases

Use cases can be written at different levels of detail:

**Informal narrative:** A free-flowing paragraph describing the interaction from the actor's perspective. Useful for initial brainstorming and stakeholder communication.

**Structured (ordered) narrative:** The interaction is described as a numbered sequence of steps. Each step is a declarative sentence describing either an actor action or a system response. This is the most common format for exam answers.

**Formal use case (template-based):** A structured document with fields for: Use case name, Primary actor, Goal in context, Preconditions, Trigger, Scenario (main success steps), Exceptions (alternative and error paths), Priority, Frequency of use, Open issues, etc.

#### Primary and Secondary Scenarios

A **primary scenario** describes the main success path, also known as the "happy path," where everything goes as expected. For example, the steps for a successful login and order placement.

A **secondary scenario** (exception) describes an alternative path triggered by an error condition, an alternative choice by the actor, or an external event. For each step in the primary scenario, the analyst should ask: (1) Can the actor take some other action at this point? (2) Is it possible the actor will encounter an error condition? (3) Could external behavior interrupt at this point?

#### Use Case Diagrams (UML)

A **use case diagram** provides a graphical overview of a system's functional requirements by showing the relationships between actors and use cases.

**Elements of a use case diagram:**

- The **system boundary** is a rectangle representing the scope of the system. The system name is written at the top.
- **Use cases** are ovals inside the system boundary, each labeled with a verb phrase describing the function (e.g., "Place Order," "Generate Report").
- **Actors** are stick figures (for humans) or labeled rectangles (for systems/devices) placed outside the system boundary.
- **Associations** are solid lines connecting actors to the use cases they participate in.

**Relationships between use cases:**

- **Include (<<include>>):** A use case that always includes the behavior of another use case. Used to extract common behavior shared by multiple use cases. Drawn as a dashed arrow from the base use case to the included use case, labeled <<include>>. Example: Both "Place Order" and "Cancel Order" include "Authenticate User."
- **Extend (<<extend>>):** A use case that optionally extends the behavior of another use case under specific conditions. Drawn as a dashed arrow from the extending use case to the base use case, labeled <<extend>>. Example: "Apply Discount Code" extends "Place Order" (only if the user has a code).
- **Generalization:** An inheritance relationship between actors or between use cases. A child actor/use case inherits the behavior of the parent. Drawn as a solid line with a hollow triangular arrowhead from child to parent.

#### Example: Use Case Diagram for an Online Food Ordering System

**Actors:** Customer, Restaurant Owner, Delivery Personnel, Payment Gateway (external system).

**Use Cases (inside system boundary):**

- Register / Login
- Browse Menu
- Place Order (<<include>> Authenticate User)
- Make Payment (<<include>> Authenticate User)
- Track Order
- Apply Discount Code (<<extend>> Place Order)
- Manage Menu (Restaurant Owner)
- Accept/Reject Order (Restaurant Owner)
- Update Delivery Status (Delivery Personnel)
- Process Payment (Payment Gateway)

---

## 5.4 Behavioral and Structural Modeling

### 5.4.1 Activity Diagrams

A **UML activity diagram** models the flow of control or data from one activity to another within a system or a specific use case. It is similar to a flowchart but with support for parallel (concurrent) behavior. Activity diagrams are particularly useful for modeling complex processing logic, workflows, and business processes.

#### Elements of an Activity Diagram

The **initial node** is a filled black circle. It represents the starting point of the activity flow. Every activity diagram has exactly one initial node.

An **activity (action) node** is a rounded rectangle containing the name of the activity or action. It represents a single step in the process and is named with a verb phrase (e.g., "Validate Password," "Send Notification").

A **flow (edge)** is an arrow connecting activity nodes. It shows the sequence in which activities are performed. Control flows from one activity to the next along the arrow.

A **decision node** is a diamond with one incoming flow and two or more outgoing flows. Each outgoing flow has a **guard condition** (written in square brackets, e.g., [password valid], [password invalid]) that determines which path the control follows. Exactly one guard condition must be true at any decision point.

A **merge node** is a diamond with two or more incoming flows and one outgoing flow. It brings together alternative paths that were separated by a previous decision node. It does not synchronize and simply passes through whatever flow arrives.

A **fork node** is a thick horizontal (or vertical) bar with one incoming flow and multiple outgoing flows. It splits the control flow into two or more **concurrent (parallel)** activities that execute simultaneously.

A **join node** is a thick horizontal (or vertical) bar with multiple incoming flows and one outgoing flow. It synchronizes concurrent activities. The outgoing flow is not triggered until **all** incoming parallel flows have completed.

The **final node** is a filled black circle inside a hollow circle (bullseye). It represents the end of the activity flow.

#### Swimlane Diagrams (Activity Partitions)

A **swimlane diagram** is a variation of the activity diagram that partitions activities by the entity (actor, department, class, or system component) responsible for performing them. The diagram is divided into vertical (or horizontal) bands called **swimlanes**, each labeled with the responsible entity. Activities are placed in the swimlane of the entity that performs them. Arrows crossing swimlane boundaries indicate handoffs between entities.

Swimlane diagrams answer the question "who does what?" and are especially useful for modeling business processes involving multiple actors or departments.

#### Example: Activity Diagram for User Login

1. **Initial node** → "Enter Username and Password"
2. → Decision node: [credentials valid?]
3. [Yes] → "Display Dashboard" → **Final node**
4. [No] → Decision node: [attempts remaining?]
5. [Yes] → "Display Error Message" → "Enter Username and Password" (loop back)
6. [No] → "Lock Account" → "Display Lockout Message" → **Final node**

### 5.4.2 Class-Based Modeling

Class-based modeling represents the objects (things) that the system will manipulate, the attributes (data) that describe those objects, the operations (behaviors) that can be applied to those objects, and the relationships between objects.

#### Identifying Analysis Classes

The primary technique for identifying classes is the **grammatical parse**, which involves examining use cases or processing narratives and extracting nouns and noun phrases as candidate classes. The process:

1. Underline every noun and noun phrase in the use case or processing narrative.
2. List all nouns as potential classes.
3. Eliminate duplicates, synonyms, and nouns that are clearly attributes rather than classes.
4. Apply selection criteria to determine which potential classes should be included in the model.

**Selection criteria for classes** (Coad and Yourdon):

- **Retained information:** The system must remember information about the class for it to function.
- **Needed services:** The class must have identifiable operations that change the values of its attributes.
- **Multiple attributes:** A class with only a single attribute is probably better represented as an attribute of another class.
- **Common attributes:** A set of attributes can be defined that apply to all instances of the class.
- **Common operations:** A set of operations can be defined that apply to all instances of the class.
- **Essential requirements:** External entities that produce or consume information essential to the system should almost always be defined as classes.

**Categories of analysis classes:** External entities (other systems, devices, people), Things (reports, displays, signals), Occurrences/events, Roles (played by people), Organizational units, Places, Structures (sensors, vehicles).

#### Attributes and Operations

**Attributes** describe the properties of a class. They are the data items that define the class in the context of the problem. Attributes are identified by asking: "What data items fully define this class?" For example, a `Sensor` class might have attributes: `sensorID`, `sensorType`, `location`, `status`.

**Operations** define the behavior of a class. They are the actions that can be performed on or by instances of the class. Operations are identified by extracting verbs from use cases and processing narratives. Operations generally fall into four categories: (1) data manipulation (add, delete, format, select), (2) computation, (3) state inquiry, and (4) event monitoring.

#### UML Class Diagrams

A **UML class diagram** shows classes, their attributes and operations, and the relationships between classes. Each class is represented as a rectangle divided into three compartments:

- The **top compartment** contains the class name (capitalized, e.g., `Customer`).
- The **middle compartment** contains the attributes (e.g., `customerID: int`, `name: String`, `email: String`).
- The **bottom compartment** contains the operations (e.g., `placeOrder()`, `getProfile()`, `updateAddress()`).

#### Relationships Between Classes

**Association** is the most general relationship. It is a structural connection between two classes indicating they collaborate or hold references to each other. It is drawn as a solid line between classes and can be labeled with a role name and **multiplicity** (e.g., `1`, `0..1`, `1..*`, `0..*`).

**Aggregation** is a "whole-part" relationship where the part can exist independently of the whole. It is drawn as a solid line with a **hollow diamond** at the "whole" end. Example: A `Department` has `Employees`, but employees can exist without the department.

**Composition** is a stronger form of aggregation where the part cannot exist without the whole. If the whole is destroyed, its parts are also destroyed. It is drawn as a solid line with a **filled (solid) diamond** at the "whole" end. Example: A `House` is composed of `Rooms`. If the house is demolished, the rooms cease to exist.

**Generalization (Inheritance)** is an "is-a" relationship where a subclass inherits attributes and operations from a superclass. The subclass is a specialized version of the superclass. It is drawn as a solid line with an **unfilled (hollow) triangular arrowhead** pointing from subclass to superclass. Example: `SavingsAccount` and `CheckingAccount` are subclasses of `BankAccount`.

**Dependency** is a weaker relationship where one class depends on another (e.g., uses it as a parameter in an operation). It is drawn as a dashed arrow from the dependent class to the class it depends on.

#### Multiplicity

Multiplicity specifies how many instances of one class can be associated with a single instance of another class:

- `1` means exactly one.
- `0..1` means zero or one (optional).
- `1..*` means one or more (at least one).
- `0..*` or `*` means zero or more (any number).

Example: A `Customer` places `0..*` Orders (a customer may have no orders or many orders). Each `Order` belongs to exactly `1` Customer.

#### Class-Responsibility-Collaborator (CRC) Modeling

**CRC modeling** is a simple technique for identifying and organizing classes. Each class is represented on an index card with three sections:

- **Class name** (top)
- **Responsibilities** (left side) list the attributes the class maintains and the operations it performs.
- **Collaborators** (right side) list other classes that provide information or actions needed to fulfill a responsibility.

CRC cards are useful for brainstorming classes and for **role-playing reviews**. In a role-playing review, a group of reviewers each holds cards for different classes and walks through use cases to verify that all responsibilities are assigned and all collaborations work correctly.

---
