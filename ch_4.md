# Chapter 4: Architectural Design (3 hours, 4 marks)

---

## 4.1 Introduction and Importance

> **What is architectural design? [2 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Why is architectural design important in software engineering? [2 marks] (2076 Ashwin - IOE - Old Syllabus Relevant)**
>
> **Explain why it may be necessary to design the system architecture before specifications are written. [3 marks] (2075 Ashwin - IOE - Old Syllabus Relevant)**

### What Is Architectural Design?

**Architectural design** is the process of defining the overall structure of a software system — its major components, the relationships and interactions among those components, and the properties that govern their composition. It represents the "big picture" of the software before detailed component-level design begins. The output is an **architectural model** that depicts the system's structural elements (modules, objects, subsystems), their interfaces, the connectors that enable communication and coordination among them, and the constraints that define how they can be integrated.

Software architecture is analogous to a building's floor plan — it shows the layout of rooms (components), how they connect (interfaces and connectors), and the overall structural form, without specifying plumbing or wiring details (component internals).

### Why Is Architecture Important?

- **Facilitates communication among stakeholders.** The architecture serves as a common vocabulary for developers, managers, customers, and testers to discuss and reason about the system at a high level.
- **Highlights early design decisions.** Architectural choices (e.g., selecting a layered vs. client-server style) have a profound impact on all subsequent development — data structures, interfaces, control flow, testing strategy, and maintainability. Correcting architectural mistakes late in the project is extremely expensive.
- **Provides a transferable model.** Architectural styles and patterns are reusable across projects. Once an architecture is proven for one system, it can serve as a template for similar systems.
- **Enables quality assessment before implementation.** The architecture can be analyzed for performance, reliability, security, and modifiability before any code is written.
- **Reduces risk.** By evaluating architectural alternatives early, the team can identify and mitigate structural risks before they propagate into the codebase.

### Why Design Architecture Before Detailed Specifications?

- The architecture defines the structural "skeleton" on which all detailed specifications and components will be built. Without it, specifications may describe features that are structurally incompatible or impossible to integrate.
- Early architectural design enables the team to identify subsystems and allocate work to parallel development teams.
- It allows assessment of non-functional requirements (performance, scalability, security) at a stage when changes are still inexpensive.
- In iterative/agile projects, a preliminary architecture (a "walking skeleton") guides sprint planning even as detailed requirements continue to evolve.

---

## 4.2 Architectural Design Principles

Architectural design is guided by a set of fundamental principles that apply regardless of the specific method, style, or programming language used:

**Principle 1: Design should be traceable to the requirements model.** Every element in the architectural design — subsystems, components, interfaces — should map back to one or more requirements. If a component cannot be traced to a requirement, it may be unnecessary; if a requirement has no corresponding component, the design is incomplete.

**Principle 2: Always consider the architecture first.** Architecture affects interfaces, data structures, control flow, testability, and maintainability. Component-level details should only be addressed after the architecture is established.

**Principle 3: Data design is as important as processing design.** The way data objects are structured and stored fundamentally shapes the program's architecture and flow. A well-designed data architecture simplifies component implementation and improves processing efficiency.

**Principle 4: Interfaces must be designed with care.** Both internal interfaces (between components) and external interfaces (to users, devices, other systems) critically affect integration ease, error propagation, and design simplicity. A well-designed interface makes integration easier and helps testers validate component functions.

**Principle 5: User interface design should prioritize ease of use.** No matter how sophisticated the internal architecture, a poorly designed UI leads to the perception that the software is "bad."

**Principle 6: Components should be functionally independent.** Each component should be cohesive — focused on a single, well-defined function. This simplifies development, testing, and maintenance.

**Principle 7: Components should be loosely coupled.** Minimize dependencies between components. High coupling increases error propagation and reduces maintainability.

**Principle 8: Design representations should be easily understandable.** The architectural model must serve as an effective communication medium for coders, testers, and maintainers.

**Principle 9: Design should be developed iteratively.** Each iteration refines the architecture, corrects errors, and strives for greater simplicity.

**Principle 10: Agile projects still need architectural design.** Even in agile development, a design model (kept lean and in sync with code) provides essential context that source code alone cannot convey — especially regarding high-level purpose and inter-module interactions.

---

## 4.3 Taxonomy of Architectural Styles

> **Explain client-server architecture with a suitable example. [5 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Describe layered architecture for software with an example. [4 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Differentiate repository model and layered model with their advantages and disadvantages. [3+3 marks] (2080 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Explain multi-tier (2-tier and 3-tier) architecture with examples. [4 marks] (2078 Bhadra - IOE - Old Syllabus Relevant)**

An **architectural style** defines a family of systems in terms of a pattern of structural organization. Each style describes: (1) a set of **components** that perform system functions, (2) a set of **connectors** that enable communication, coordination, and cooperation among components, (3) **constraints** that define how components can be integrated, and (4) **semantic models** that help understand the overall system properties.

### Data-Centered (Repository) Architecture

A central **data store** (database, file, or shared repository) resides at the center of the architecture. All other components access, add, update, or delete data from this store. Components operate independently and do not communicate directly with each other — they interact only through the shared data store.

- In a **passive repository**, client components access data independently of other clients. The repository simply stores and retrieves data on request.
- In a **blackboard** variant, the repository is active — it sends notifications to client components when data of interest changes, triggering further processing. This is useful for problems with no deterministic solution path (e.g., speech recognition, AI systems).

**Advantages:** Components can be changed or added independently without affecting other components (high integrability). Centralized data management simplifies backup, security, and consistency. Efficient for systems where many components share large volumes of data.

**Disadvantages:** The repository is a single point of failure. Components become tightly coupled to the data model — changes to the data schema may require updates across many components. Can be difficult to distribute across multiple machines.

**Example:** A CASE (Computer-Aided Software Engineering) tool suite where all tools (editor, compiler, debugger, version control) access a shared project repository.

### Data-Flow (Pipe-and-Filter) Architecture

Input data is transformed through a series of processing components (called **filters**) connected by **pipes** that transmit data from one filter to the next. Each filter works independently — it receives input in a defined format, processes it, and produces output in a defined format. Filters do not need to know the internal workings of neighboring filters.

**Advantages:** Supports reuse (filters can be recombined). Easy to understand, add new filters, or replace existing ones. Naturally supports concurrent processing.

**Disadvantages:** Not suitable for interactive applications. Can have performance overhead due to data transformation between filters. Not well-suited for complex, branching control flows.

**Example:** A Unix command pipeline: `cat file.txt | grep "error" | sort | uniq -c` — each command is a filter connected by pipes.

### Call-and-Return Architecture

A program structure where a "main" program invokes subprograms, which may in turn invoke further subprograms, forming a control hierarchy. Two common substyles:

- **Main program/subprogram:** Classic hierarchical decomposition where the main program delegates tasks to subprograms.
- **Remote procedure call (RPC):** The same hierarchy, but components are distributed across multiple computers on a network.

**Advantages:** Relatively easy to modify and scale. Well-understood, traditional approach. Clear control flow.

**Disadvantages:** Can be rigid. Changes to the hierarchy may require restructuring. Tightly coupled control flow can reduce flexibility.

### Object-Oriented Architecture

Components encapsulate both data and the operations that manipulate it. Communication between components is achieved through **message passing**. Each object manages its own state and exposes behavior through well-defined interfaces.

**Advantages:** Promotes reuse, modularity, and information hiding. Changes to one object's internal representation do not affect others. Natural mapping to real-world problem domains.

**Disadvantages:** Can be harder to visualize the overall system structure. Performance overhead from message passing. Potential for complex interdependencies if not designed carefully.

### Layered Architecture

The system is organized into horizontal **layers**, each providing a set of services to the layer above it and using services from the layer below. Each layer accomplishes operations that progressively become closer to the hardware level.

- **Outermost layer** — user interface operations.
- **Intermediate layers** — application logic and utility services.
- **Innermost layer** — operating system interfacing and low-level services.

**Advantages:** Separation of concerns — each layer has a clearly defined responsibility. Layers can be developed, tested, and modified independently. Changes in one layer generally do not affect others (as long as the interface is preserved). Supports reuse of layers across applications.

**Disadvantages:** Performance overhead — requests may have to traverse multiple layers. Not all systems decompose cleanly into layers. Excessive layering can introduce complexity and rigidity.

**Example:** A web application with four layers — (1) Presentation layer (HTML/CSS/JS in the browser), (2) Application layer (controllers handling HTTP requests), (3) Business logic layer (domain rules and processing), (4) Data access layer (database queries and ORM).

### Client-Server Architecture

A distributed architecture that partitions work between **servers** (providers of resources/services) and **clients** (requesters of services). The server hosts shared resources (data, processing logic, files) and listens for client requests. Clients present the user interface and send requests to the server over a network.

**Advantages:** Centralized management of data and security. Scalable — servers can be upgraded or additional servers added. Resource-efficient — thin clients can access powerful server-side processing. Data integrity maintained at the server.

**Disadvantages:** Server is a single point of failure. Entirely dependent on network connectivity. Server can become a bottleneck under heavy load. Higher infrastructure cost.

**Example:** An online banking system — the mobile app (client) sends transaction requests to the bank's application server, which processes business logic and communicates with the database server to fetch/update account information. The server returns results to the client for display.

### Multi-Tier Architecture

An extension of client-server that separates functionality into distinct tiers, each running on separate infrastructure:

**2-Tier Architecture:** The client communicates directly with the server. The client handles the UI and some application logic; the server handles data storage and remaining logic. Example: A desktop database application where the client application connects directly to a database server.

**3-Tier Architecture:** Adds a middle tier between client and server — (1) **Presentation tier** (client — UI), (2) **Application/Logic tier** (middle — business rules and processing), (3) **Data tier** (server — database). Each tier can be developed, deployed, and scaled independently.

**Example:** An e-commerce website — the browser (presentation tier) sends requests to a web/application server (logic tier) that processes orders, applies business rules, and queries the database server (data tier).

**Advantages of 3-tier over 2-tier:** Better separation of concerns. The middle tier can be scaled independently. Improved security — the database is not directly exposed to clients. Easier maintenance — business logic changes do not affect the client or database.

### Model-View-Controller (MVC) Architecture

A widely used architectural pattern, particularly in web and mobile applications, that separates an application into three interconnected components:

- **Model** — encapsulates application data, business logic, and rules. Manages data access and state.
- **View** — presents data from the model to the user. Handles all UI rendering and display logic.
- **Controller** — receives user input, interprets it, and invokes appropriate model operations. Selects the view to display the response.

**Flow:** The user interacts with the View → the Controller receives the request → the Controller invokes the Model → the Model processes data and returns results → the Controller selects the appropriate View → the View renders the response to the user.

**Advantages:** Clear separation of concerns — designers can work on the UI (View) independently of developers working on business logic (Model). Supports multiple views for the same data. Facilitates testing (Model can be tested independently).

**Disadvantages:** Can increase complexity for simple applications. Tight coupling between Controller and Model can emerge if not designed carefully.

### Repository Model vs. Layered Model (Comparison)

| Aspect                  | Repository Model                                                      | Layered Model                                                              |
| ----------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Structure               | Central data store accessed by independent components                 | Horizontal layers, each serving the layer above                            |
| Communication           | All components interact through the shared data store                 | Each layer communicates only with adjacent layers                          |
| Data sharing            | Efficient for systems with large shared data sets                     | Data passes through layers, may introduce overhead                         |
| Coupling                | Components coupled to the data model, not to each other               | Layers coupled only through well-defined interfaces                        |
| Modifiability           | Adding/removing components is easy; changing the data schema is hard  | Changing a layer is easy if the interface is preserved                     |
| Single point of failure | The data store is a single point of failure                           | No single point of failure (unless a critical layer fails)                 |
| Best suited for         | Systems with shared, complex data (CASE tools, IDEs, data warehouses) | Systems with clear functional separation (web apps, OS, network protocols) |

---

## 4.4 Modular Design, Cohesion, and Coupling

> **What are the different modular decomposition styles used during system design? Explain with examples. [5 marks] (2075 Chaitra - IOE - Old Syllabus Relevant)**
>
> **How is the modular decomposition concept practiced in the system design process? [4 marks] (2071 Shrawan - IOE - Old Syllabus Relevant)**

### Modular Design

**Modularity** is the most common manifestation of the "separation of concerns" principle. The software is divided into separately named and addressable components called **modules**, each of which is integrated to satisfy overall system requirements. A monolithic program (one large module) is nearly impossible to understand, test, or maintain. Modularization makes software intellectually manageable.

**Why modularize?** Development can be more easily planned. Software increments can be defined and delivered. Changes can be more easily accommodated. Testing, debugging, and long-term maintenance can be conducted more efficiently and without serious side effects.

**The modularization trade-off:** As the number of modules increases, the cost per individual module decreases (smaller, simpler modules). However, the cost of integrating modules increases (more interfaces, more communication). There is an optimal number of modules (M) that minimizes total development cost. Too few modules means each is too complex; too many modules means excessive integration overhead.

### Modular Decomposition Styles

**Functional decomposition (top-down):** The system is decomposed by function. A high-level function is broken into sub-functions, which are further broken into smaller sub-functions until each module performs a single, well-defined task. Example: An order processing system decomposed into modules for "Validate Order," "Calculate Total," "Process Payment," and "Generate Invoice."

**Object-oriented decomposition:** The system is decomposed into objects (classes) that encapsulate data and the operations on that data. Modules correspond to real-world entities. Example: An e-commerce system decomposed into objects like `Customer`, `Product`, `ShoppingCart`, `Order`, and `Payment`.

### Information Hiding

The principle of **information hiding** (proposed by David Parnas) states that modules should be designed so that internal details (algorithms, data structures, design decisions) are hidden from other modules. Only the module's interface (what it does, not how it does it) is visible to the outside.

- Effective modularity is achieved by defining independent modules that communicate only information necessary to achieve software function.
- Information hiding reduces error propagation — inadvertent errors introduced during modification are less likely to spread to other parts of the software.
- It provides the greatest benefits during testing and maintenance, when modifications are frequent.

### Functional Independence

A module is **functionally independent** if it performs a single, well-defined function and interacts with other modules only through simple, well-defined interfaces. Functional independence is a direct outgrowth of separation of concerns, modularity, abstraction, and information hiding.

**Why functional independence matters:**

- Independent modules are easier to develop (function is compartmentalized, interfaces are simplified).
- Independent modules are easier to test and maintain (secondary effects of modifications are limited, error propagation is reduced).
- Independent modules are more reusable.

Functional independence is assessed using two qualitative criteria: **cohesion** and **coupling**. The goal is **high cohesion** and **low coupling**.

### Cohesion

**Cohesion** measures how closely related and focused the responsibilities within a single module are. A cohesive module performs a single task, requiring little interaction with other modules. Types of cohesion (from worst to best):

**Coincidental cohesion** — module parts are completely unrelated; grouped arbitrarily. This is the weakest form. Example: A "utility" module containing unrelated functions like `printReport()`, `calculateTax()`, and `validateEmail()` simply because they were written by the same developer.

**Logical cohesion** — module parts perform logically similar functions but are otherwise unrelated. Example: A module that handles all input operations (keyboard, file, network) through a single function with a control flag.

**Temporal cohesion** — module parts are grouped because they are executed at the same time (e.g., initialization, cleanup). Example: A `startup()` function that initializes the database connection, loads configuration, and sets the system clock.

**Procedural cohesion** — module parts are grouped because they always execute in a specific sequence. Example: A module that reads a record, validates it, and writes it to a file — the steps are related only by sequence, not by function.

**Communicational cohesion** — module parts operate on the same data or contribute to the same output. Example: A module that generates a report by reading customer data, calculating totals, and formatting the output — all operations share the same data.

**Sequential cohesion** — the output of one part serves as the input for the next part. Example: A module where `parseInput()` produces data consumed by `validateData()`, whose output is consumed by `transformData()`.

**Functional cohesion** — every element of the module is essential for the execution of a single, well-defined function. This is the strongest and most desirable form. Example: A `computeSquareRoot()` module that performs only the square root computation and returns the result.

**Guideline:** Always strive for functional cohesion. Communicational and sequential cohesion are also acceptable. Avoid coincidental, logical, and temporal cohesion.

### Coupling

**Coupling** measures the degree of interdependence between modules. Low coupling means modules are relatively independent; high coupling means modules are heavily dependent on each other. Types of coupling (from worst to best):

**Content coupling** — one module directly accesses or modifies the internal data or code of another module. This violates information hiding and is the most harmful form. Example: Module A directly modifies a local variable inside Module B.

**Common coupling** — multiple modules share the same global data. A change to the global data structure can affect all modules that use it. Example: Several modules read and write a global configuration array.

**Control coupling** — one module passes a control flag to another module that directs its internal logic. Example: Module A calls `processRecord(flag)` where the flag tells Module B whether to insert, update, or delete. Changes to Module B's logic may require changes to the flag's meaning in Module A.

**Stamp coupling** — modules share a composite data structure (e.g., a struct or object) but each uses only part of it. The modules become dependent on the structure's format. Example: Passing an entire `Customer` object to a module that only needs the customer's email address.

**Data coupling** — modules communicate only through simple parameters (primitive data types). Each parameter is an independent data item needed by the module. This is the most desirable form. Example: `calculateArea(length, width)` — only the required primitive values are passed.

**Guideline:** Always strive for data coupling. Avoid content coupling and common coupling. Minimize control coupling by redesigning interfaces.

### Relationship Between Cohesion and Coupling

Cohesion and coupling are inversely related — increasing cohesion within modules tends to decrease coupling between modules. A system with high cohesion and low coupling is easier to understand, test, maintain, and reuse. This is the hallmark of a well-designed modular system.

---
