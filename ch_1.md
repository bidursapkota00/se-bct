# Chapter 1: Introduction (4 hours, 5 marks)

---

## 1.1 Software and Software Engineering

**Software** is: (1) instructions (computer programs) that when executed provide desired features, function, and performance; (2) data structures that enable the programs to adequately manipulate information; and (3) descriptive information in both hard copy and virtual forms that describes the operation and use of the programs.

**Software Engineering** (IEEE definition): The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software.

Software engineering is a **layered technology** built on four layers (bottom to top):

- **Quality focus** — the bedrock; organizational commitment to continuous quality improvement (e.g., TQM, Six Sigma).
- **Process** — the foundation; defines a framework for management control, milestones, and change management.
- **Methods** — the technical how-to's; communication, requirements analysis, design modeling, construction, testing, and support.
- **Tools** — automated or semi-automated support for process and methods (CASE tools).

Modern software engineering emerged to address recurring problems: late delivery, cost overruns, unreliable software, and difficulty maintaining existing systems.

---

## 1.2 Nature and Characteristics of Software

Software is a **logical** element, not a physical one. Its key characteristics that distinguish it from hardware:

- **Software is developed or engineered; it is not manufactured** in the classical sense. Although similarities exist between software development and hardware manufacturing, the two activities are fundamentally different. Software quality is achieved through good design, not through production control.
- **Software doesn't "wear out."** Hardware follows a "bathtub curve" — high early failure rate (infant mortality), then a steady-state, then increasing failures due to wear. Software has no physical wear. Its failure curve is idealized as a high initial failure rate (undiscovered defects) that drops and flattens as defects are corrected. However, software **deteriorates** — each change introduces new errors, causing failure rate spikes. Over time, the baseline failure rate rises.
- **Software has no spare parts.** Every failure indicates a design error. Unlike hardware where a worn-out component is replaced with a spare, software maintenance involves fixing design flaws, which is inherently more complex.
- **Most software is custom-built** rather than assembled from standard components, although the industry is moving toward component-based construction and reuse.

**Characteristics of good software** (quality attributes):

- **Functionality** — delivers the required features.
- **Reliability** — performs without failure under stated conditions.
- **Usability** — easy for the intended users.
- **Efficiency** — optimal use of system resources.
- **Maintainability** — easy to modify, correct, and improve.
- **Portability** — can operate across different environments.

---

## 1.3 Software Application Domains

Seven broad categories of computer software:

- **System software** — programs that service other programs (e.g., compilers, editors, OS components, drivers, networking software). Processes complex information structures, often with indeterminate input/output.
- **Application software** — standalone programs that solve specific business needs (e.g., payroll, inventory). Processes business or technical data for decision making.
- **Engineering/scientific software** — "number-crunching" programs for scientific computation (e.g., CAD, weather forecasting, stress analysis, data science applications).
- **Embedded software** — resides within a product or system to control features and functions (e.g., fuel control in automobiles, microwave oven key pad, braking systems).
- **Product-line software** — composed of reusable components, designed for use by many customers (e.g., word processors, spreadsheets, inventory control products).
- **Web/mobile applications** — network-centric software spanning browser-based apps, cloud computing, service-based computing, and mobile device software.
- **Artificial intelligence software** — uses heuristics to solve complex problems not amenable to regular computation (e.g., robotics, machine learning, pattern recognition, game playing, decision-making systems).

---

## 1.4 Legacy Software

**Legacy software** refers to older programs, often developed decades ago, that have been continually modified to meet changing business requirements and computing platforms.

**Why legacy software matters:**
- Often supports core business functions and is indispensable.
- Costly to maintain and risky to evolve.
- May have poor quality by modern standards: inextensible designs, convoluted code, poor/absent documentation, no archived test cases, and poorly managed change history.

**When legacy systems must evolve:**
- Must be **adapted** to new computing environments or technology.
- Must be **enhanced** to meet new business requirements.
- Must be **extended** to work with modern systems or databases.
- Must be **re-architected** to remain viable in an evolving environment.

If a legacy system meets users' needs and runs reliably, it does not need to be fixed. But when evolution is needed, it must be **reengineered** for future viability.

---

## 1.5 Software Crisis

The **software crisis** is a term coined in the late 1960s (at the 1968 NATO conference) to describe the chronic problems in software development — the inability to produce useful, reliable software on time and within budget as systems grew in complexity.

**Causes of the software crisis:**
- Rapidly increasing complexity of software requirements while tools and techniques remained primitive.
- Rising demand for new software outpacing the industry's ability to produce it.
- Inadequate, informal development techniques that could not scale to large systems.
- Poor project management and lack of standardized engineering methodologies.
- Maintenance challenges: cost of maintenance often exceeded initial development cost.
- Shortage of trained software practitioners.

**Manifestations:**
- Projects running significantly over budget and past deadlines.
- Delivered software failing to meet customer requirements.
- Software that was error-prone, unreliable, and poorly documented.
- Large projects becoming unmanageable or being cancelled entirely.

**Historical examples:**
- **IBM OS/360 (1963–65)** — massive delays and cost overruns in creating a unified OS.
- **Therac-25 (1985–87)** — software-based safety failures in a radiation therapy machine caused patient fatalities.
- **Denver Airport Baggage System (1995)** — automated baggage system's software glitches delayed airport opening for 16 months.
- **Ariane 5 Rocket (1996)** — an integer overflow in control software caused the rocket to crash 37 seconds after launch.

**Solutions proposed:**
- Adoption of systematic software engineering practices (process models, methods, tools).
- Better requirements gathering and management.
- Use of formal reviews, inspections, and testing strategies.
- Standards and quality assurance frameworks.
- Training and education in software engineering principles.

---

## 1.6 Software Myths

Software myths are widely held but false beliefs that lead to mismanagement, unrealistic expectations, and project failures. They are classified into three categories:

### Management Myths

**Myth:** "We already have a book full of standards and procedures for building software. Won't that provide my people with everything they need to know?"
**Reality:** Standards may exist but are often incomplete, outdated, or not actually used. Having a book does not mean the practice is adequate or that practitioners follow it.

**Myth:** "If we get behind schedule, we can add more programmers and catch up."
**Reality:** Adding people to a late project makes it later (Brooks' Law). New staff need time to learn the system, and communication overhead increases quadratically with team size.

**Myth:** "If I decide to outsource the software project, I can just relax and let the vendor build it."
**Reality:** If an organization cannot manage and control software internally, it will invariably struggle when outsourcing. Oversight and involvement remain essential.

### Customer Myths

**Myth:** "A general statement of objectives is sufficient to begin writing programs — we can fill in the details later."
**Reality:** Ambiguous requirements are the primary cause of failed projects. A formal and detailed requirements specification is essential to minimize rework and miscommunication.

**Myth:** "Software requirements continually change, but changes can be easily accommodated because software is flexible."
**Reality:** While software is inherently malleable, the cost of change increases dramatically as development progresses. A change made during design can be 1.5–6× more costly than during requirements; during testing, 60–100× more costly.

### Practitioner (Developer) Myths

**Myth:** "Once we write the program and get it to work, our job is done."
**Reality:** 60–80% of total effort is expended after the first delivery, during maintenance (bug fixing, enhancements, adaptation).

**Myth:** "Until I get the program running, I have no way of assessing its quality."
**Reality:** Quality can be assessed from inception through formal technical reviews, design analysis, and inspections — long before a single line of code is compiled.

**Myth:** "The only deliverable for a successful project is the working program."
**Reality:** Documentation, models, test plans, and design specifications are equally critical deliverables for long-term maintainability and success.

**Myth:** "Software engineering will make us create voluminous and unnecessary documentation and will slow us down."
**Reality:** Software engineering is about creating quality; it often leads to reduced rework, which results in faster delivery.

---

## 1.7 Software Engineering Practice: Essence of Practice, General Principles

### The Essence of Practice

Based on George Polya's problem-solving approach (*How to Solve It*, 1945), software engineering practice follows four essential steps:

**1. Understand the problem** (communication and analysis)
- Who are the stakeholders?
- What are the unknowns? What data, functions, and features are required?
- Can the problem be decomposed into smaller, more manageable problems?
- Can the problem be represented graphically? Can an analysis model be created?

**2. Plan a solution** (modeling and software design)
- Have you seen similar problems before? Are there reusable patterns or existing software?
- Can subproblems be defined with readily apparent solutions?
- Can a design model be created that leads to effective implementation?

**3. Carry out the plan** (code generation)
- Does the solution conform to the design plan? Is the code traceable to the design model?
- Is each component provably correct? Has the code been reviewed?

**4. Examine the result for accuracy** (testing and quality assurance)
- Has a reasonable testing strategy been implemented?
- Does the solution produce results that conform to requirements?
- Has the software been validated against all stakeholder requirements?

### General Principles (Hooker's Seven Principles)

**1. The Reason It All Exists** — A software system exists to provide value to its users. All decisions should be made with this in mind. If something does not add real value, don't do it.

**2. KISS (Keep It Simple, Stupid!)** — All design should be as simple as possible, but no simpler. Simpler designs are easier to understand, maintain, and less error-prone. Simplicity takes thoughtful effort over multiple iterations.

**3. Maintain the Vision** — A clear architectural vision is essential for success. Without conceptual integrity, a system becomes a patchwork of incompatible designs. An empowered architect who holds and enforces the vision helps ensure success.

**4. What You Produce, Others Will Consume** — Always design, code, and document knowing someone else will have to understand and maintain your work. Making their job easier adds value to the system.

**5. Be Open to the Future** — Never design yourself into a corner. Build systems that solve the general problem, not just the specific one. Prepare for changing specifications and evolving platforms.

**6. Plan Ahead for Reuse** — Reuse saves time and effort. Planning for reuse reduces cost and increases the value of both the reusable components and the systems that incorporate them.

**7. Think!** — Clear, complete thought before action almost always produces better results. Thinking helps you recognize when you don't know something and need to research the answer. Applying the first six principles requires intense thought.

---

## 1.S The Software Process (Overview from Chapter 1)

A **process** is a collection of activities, actions, and tasks performed when a work product is to be created. It is not rigid but adaptable to the problem, project, team, and organizational culture.

### Process Framework

A generic process framework encompasses **five framework activities**:

- **Communication** — understand stakeholders' objectives and gather requirements.
- **Planning** — create a software project plan describing tasks, risks, resources, work products, and schedule.
- **Modeling** — create models (sketches, UML diagrams) to understand requirements and design the solution.
- **Construction** — code generation (manual or automated) combined with testing to uncover errors.
- **Deployment** — deliver software to the customer, who evaluates it and provides feedback.

These activities are applied **iteratively**: each iteration produces an **increment** that adds features and functionality until the software is complete.

### Umbrella Activities

Applied throughout the software process to manage and control progress, quality, change, and risk:

- **Software project tracking and control** — assess progress against the plan.
- **Risk management** — assess risks affecting outcome or quality.
- **Software quality assurance** — activities to ensure software quality.
- **Technical reviews** — uncover and remove errors before propagation.
- **Measurement** — collect process, project, and product measures.
- **Software configuration management** — manage effects of change.
- **Reusability management** — define reuse criteria and mechanisms.
- **Work product preparation and production** — create models, documents, logs, forms.

### Process Adaptation

The process adopted for one project may differ significantly from another. Differences include: overall flow of activities, degree of detail, quality assurance rigor, customer involvement, team autonomy, and role prescription.

---
