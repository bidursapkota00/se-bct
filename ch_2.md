# Chapter 2: The Software Process (8 hours, 11 marks)

---

## 2.1 Process Framework and Umbrella Activities

> **Explain fundamental activities of the software process. [3 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**

A software process is a collection of activities, actions, and tasks performed when a work product is to be created. It is not rigid but adaptable to the problem, project, team, and organizational culture.

### Framework Activities

A generic process framework defines **five framework activities** applicable to all software projects regardless of size or complexity:

- **Communication** involves collaborating with stakeholders to understand their objectives and gather requirements that define software features and functions.
- **Planning** involves creating a software project plan that describes technical tasks, risks, resources, work products, and schedule (the project "road map").
- **Modeling** involves creating models (sketches, diagrams, architectural representations) to understand requirements and the design that will achieve them.
- **Construction** involves code generation (manual or automated) combined with testing to uncover errors in the code.
- **Deployment** involves delivering the software (complete or as an increment) to the customer, who evaluates it and provides feedback.

These activities are applied **iteratively**. Each iteration produces a **software increment** that provides stakeholders with a subset of overall features until the software is complete.

### Process Flow

Process flow describes how framework activities are organized with respect to sequence and time. Four types of process flow exist:

- **Linear process flow** executes each activity in sequence (communication → planning → modeling → construction → deployment).
- **Iterative process flow** repeats one or more activities before proceeding to the next.
- **Evolutionary process flow** executes activities in a "circular" manner. Each circuit leads to a more complete version of the software.
- **Parallel process flow** executes one or more activities concurrently with others (e.g., modeling for one aspect while constructing another).

### Umbrella Activities

Umbrella activities are applied **throughout** the software process to manage and control progress, quality, change, and risk:

- **Software project tracking and control** is used to assess progress against the project plan and take corrective action.
- **Risk management** is used to assess risks that may affect the project outcome or product quality.
- **Software quality assurance** involves defining and conducting activities to ensure software quality.
- **Technical reviews** help uncover and remove errors before they propagate to the next activity.
- **Measurement** involves collecting process, project, and product measures to help deliver software that meets stakeholders' needs.
- **Software configuration management** is used to manage the effects of change throughout the process.
- **Reusability management** involves defining criteria for work product reuse and establishing mechanisms for reusable components.
- **Work product preparation and production** involves creating models, documents, logs, forms, and lists.

### Task Sets

Each framework activity is populated by software engineering actions, and each action is defined by a **task set**, which is a collection of work tasks, related work products, quality assurance points, and project milestones. The task set is chosen based on project needs and team characteristics. A small project may have a simple task set (e.g., a phone call for communication), while a complex project may have elaborate task sets (e.g., inception, elicitation, elaboration, negotiation, specification, and validation for communication).

---

## 2.2 Traditional (Plan-Driven) Process Models

Traditional (prescriptive) process models define a predefined set of process elements and a predictable process workflow. They prescribe framework activities, software engineering actions, tasks, work products, quality assurance, and change control mechanisms. They strive for **structure and order** in software development.

### 2.2.1 Waterfall Model and Its Extensions

> **What is SDLC? Discuss the various stages of the waterfall process model. [2+3 marks] (2081 Baishakh - IOE - Old Syllabus Relevant)**
>
> **Discuss the advantages and disadvantages of the waterfall model. [4 marks] (2079 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Explain why the waterfall model is not suitable when important functionalities need to be delivered in a short time period. [4 marks] (2073 Chaitra - IOE - Old Syllabus Relevant)**

The **Software Development Life Cycle (SDLC)** is a structured sequence of stages in software engineering to develop the intended software product. The waterfall model is the oldest and most classical SDLC paradigm.

The **waterfall model** (also called the linear sequential model), originally proposed by Winston Royce (1970), suggests a systematic, sequential approach to software development flowing through these stages:

- **Communication** covers project initiation and requirements gathering from the customer.
- **Planning** covers estimating, scheduling, and tracking the project.
- **Modeling** covers analysis and design, including creating representations of the system.
- **Construction** covers code generation and testing.
- **Deployment** covers delivery, support, and feedback.

Each phase must be completed before the next phase begins, and there is little opportunity to revisit earlier phases.

**Advantages:**

- Simple to understand and easy to plan.
- Works well for small, well-understood projects with stable requirements.
- Analysis and testing are straightforward.
- Clear milestones and deliverables at each phase.

**Disadvantages:**

- Real projects rarely follow a strictly sequential flow.
- Difficult for the customer to state all requirements explicitly at the beginning.
- A working version of the software is not available until late in the project.
- Major errors may not be detected until the working program is reviewed.
- Does not accommodate change well because the cost of change increases dramatically if discovered late.
- Testing occurs late in the process.
- Customer approval is only at the end.

**Why waterfall is unsuitable for rapid delivery:** The waterfall model requires all phases to be completed sequentially. No working software is delivered until the construction phase is complete. If important functionalities must be delivered quickly, this model fails because it offers no mechanism for partial delivery or incremental release. The customer must wait for the entire system to be built before seeing any working functionality.

**Extensions of the Waterfall Model:**

- The **V-Model** associates a testing phase with each development phase (e.g., unit testing validates construction, system testing validates design).
- **Waterfall with feedback** allows limited iteration between adjacent phases, partially addressing the rigidity of the pure waterfall.

### 2.2.2 Incremental Process Model

> **Explain the incremental model with its advantages and disadvantages. [4+3 marks] (2075 Chaitra - IOE - Old Syllabus Relevant)**
>
> **You are leading development of an e-commerce site using the incremental model. How do you implement it? [4 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**

The **incremental model** combines elements of linear and iterative flows. It delivers the software in a series of **increments**, each providing a portion of the overall functionality. The first increment is often a **core product** addressing basic requirements; subsequent increments add supplementary features.

**How it works:**

- Requirements are gathered and prioritized.
- The system is divided into increments, each going through its own mini-waterfall cycle (communication → planning → modeling → construction → deployment).
- Each increment delivers a working, usable product to the customer.
- Customer feedback from each increment informs the planning of the next.

**Example of E-Commerce Site (Incremental Approach):**

- **Increment 1** covers core functionality including user registration, product catalog browsing, and basic search.
- **Increment 2** adds shopping cart, checkout process, and online payment integration.
- **Increment 3** adds user reviews, recommendation engine, and order tracking.
- **Increment 4** adds admin dashboard, analytics, inventory management, and promotional tools.

Each increment is fully functional, deployed, tested, and reviewed by stakeholders before proceeding to the next.

**Advantages:**

- Delivers working software early, providing value to the customer sooner.
- Customer feedback is incorporated after each increment, reducing risk of product rejection.
- Easier to test and debug smaller modules.
- Flexible and easier to accommodate changes in requirements between increments.
- Higher-risk features can be addressed in early increments.
- Lower initial delivery cost.

**Disadvantages:**

- Requires a clear understanding of the complete system to properly partition into increments.
- Requires careful planning and architectural foresight.
- Total cost may be higher than a single-pass model since each increment has its own full development cycle.
- Integration complexity increases as more increments are added.

### 2.2.3 Evolutionary Process Models (Prototyping, Spiral)

#### Prototyping Model

> **Explain the prototyping model with its advantages and disadvantages. [5+2 marks] (2076 Chaitra - IOE - Old Syllabus Relevant)**
>
> **In what types of projects can the prototype process model be used? Explain with an example. [5 marks] (2082 Baishakh - IOE - Old Syllabus Relevant)**

The **prototyping model** is used when requirements are fuzzy, incomplete, or poorly understood. A prototype is a preliminary version of the software that is built quickly to help stakeholders visualize and refine their requirements.

**Process:**

- **Communication** involves meeting stakeholders to define overall objectives and identify known requirements, and outlining areas needing further definition.
- **Quick Plan** involves planning a rapid prototyping iteration.
- **Modeling (Quick Design)** focuses on aspects visible to end users (e.g., UI layout, output formats).
- **Construction of Prototype** involves building a working prototype quickly, possibly using existing program fragments or rapid application tools.
- **Deployment and Feedback** involves delivering the prototype to stakeholders for evaluation and gathering feedback to refine requirements.
- **Iteration** involves tuning the prototype based on feedback and repeating until requirements are sufficiently understood.

**When to use prototyping:**

- When the customer has general objectives but cannot specify detailed requirements.
- When the developer is unsure about the form of user interaction, algorithm efficiency, or system behavior.
- For systems with heavy UI requirements where the user needs to "see and feel" before specifying details.
- **Example:** A travel agency needs a booking application but is unsure about the user interface design. A prototype allows the agency to interact with a preliminary UI, provide feedback on layout and workflow, and progressively refine the design until it meets expectations.

**Advantages:**

- Reduced impact of requirement changes because requirements are refined iteratively.
- Customer is involved early and often.
- Reduces likelihood of product rejection.
- Helps uncover misunderstandings between developers and stakeholders early.
- Works well for small to medium projects.

**Disadvantages:**

- Stakeholders may mistake the prototype for the finished product and expect immediate delivery.
- Developers may make implementation compromises (poor architecture, quick fixes) to get the prototype working, and these become embedded in the final system.
- Work is lost in a throwaway prototype.
- Hard to plan and manage because the number of iterations is unpredictable.

**Key rule:** All stakeholders should agree upfront that the prototype is built to define requirements, not as the final product.

#### Spiral Model

> **Explain the spiral model with its advantages and disadvantages. [5 marks] (2068 Chaitra - IOE - Old Syllabus Relevant)**
>
> **How can both the waterfall model and prototyping model be accommodated in the spiral process model? [6 marks] (2078 Kartik - IOE - Old Syllabus Relevant)**
>
> **A travel agency needs software but is unsure about the UI. Would it be proper to use the spiral model? Justify. [6 marks] (2075 Ashwin - IOE - Old Syllabus Relevant)**

The **spiral model**, proposed by Barry Boehm (1988), is an evolutionary process model that couples the iterative nature of prototyping with the controlled, systematic aspects of the waterfall model. Its distinguishing feature is **explicit risk analysis** at every iteration.

**How it works:**

Software is developed in a series of evolutionary releases by traversing a spiral path in four quadrants:

- **Planning** involves determining objectives, alternatives, and constraints, estimating costs and schedule, and conducting risk analysis.
- **Risk Analysis** involves identifying and resolving risks and creating prototypes to reduce uncertainty.
- **Construction** involves developing and verifying the software (code + test).
- **Evaluation** involves assessing results, obtaining customer feedback, and planning the next iteration.

Each circuit (loop) around the spiral produces a progressively more complete version of the software. The first circuit might produce a product specification or proof-of-concept prototype; subsequent circuits produce increasingly refined and complete versions.

**Accommodating waterfall and prototyping within the spiral:**

The spiral model is a meta-model that can incorporate other process models. The first circuit can use a prototyping approach to explore uncertain requirements and refine the UI. Once requirements are stabilized, subsequent circuits can follow a more waterfall-like sequential flow within each loop (requirements → design → code → test). Thus, the spiral model uses prototyping for risk reduction and requirement exploration, while using waterfall-like discipline for well-understood portions. Each loop's approach is chosen based on the risk profile of that iteration.

**For the travel agency scenario (UI uncertainty):** The spiral model is appropriate. The first loop would build a UI prototype to resolve the UI design uncertainty (a major risk). Stakeholder feedback would refine the UI requirements. Subsequent loops would address core booking logic, payment integration, and database design with progressively less risk. The risk-driven nature of the spiral ensures that the biggest uncertainty (the UI) is resolved first.

**Advantages:**

- Continuous customer involvement throughout the project.
- Development risks are explicitly managed at every iteration.
- Suitable for large, complex, high-risk projects.
- Works well for extensible products that evolve over time.
- Can be applied throughout the entire software lifecycle, including maintenance.

**Disadvantages:**

- Risk analysis failures can doom the project.
- May be difficult to convince customers that the evolutionary approach is controllable.
- Requires considerable risk assessment expertise.
- The project may be hard to manage due to evolving scope.
- Not suitable for small, low-risk projects (overhead is disproportionate).

---

## 2.3 Agile and Adaptive Process Models

### 2.3.1 Agile Manifesto and the 12 Principles

In 2001, seventeen software developers signed the **Manifesto for Agile Software Development**, establishing the philosophical foundation for agile methods.

**The Four Core Values of the Agile Manifesto:**

1. **Individuals and interactions** over processes and tools.
2. **Working software** over comprehensive documentation.
3. **Customer collaboration** over contract negotiation.
4. **Responding to change** over following a plan.

The manifesto does not reject the items on the right but values the items on the left **more**.

**The 12 Agile Principles:**

1. **Customer satisfaction** through early and continuous delivery of valuable software.
2. **Welcome changing requirements**, even late in development; agile processes harness change for the customer's competitive advantage.
3. **Deliver working software frequently**, from a couple of weeks to a couple of months, with a preference for the shorter timescale.
4. **Business people and developers must work together** daily throughout the project.
5. **Build projects around motivated individuals.** Give them the environment and support they need, and trust them to get the job done.
6. **Face-to-face conversation** is the most efficient and effective method of conveying information within a development team.
7. **Working software is the primary measure of progress.**
8. **Sustainable development** requires that sponsors, developers, and users maintain a constant pace indefinitely.
9. **Continuous attention to technical excellence** and good design enhances agility.
10. **Simplicity**, which is the art of maximizing the amount of work not done, is essential.
11. **The best architectures, requirements, and designs emerge from self-organizing teams.**
12. **At regular intervals, the team reflects** on how to become more effective, then tunes and adjusts its behavior accordingly.

### 2.3.2 Agile versus Plan-Driven Development

**Plan-driven (traditional) development:**

- Follows a predefined sequence of phases with detailed upfront planning.
- Emphasizes comprehensive documentation, formal reviews, and milestone-based tracking.
- Requirements are gathered completely before design and construction.
- Change is managed through formal change control processes.
- Works best when: requirements are stable and well-understood, the project is large and safety/mission-critical, the team is large and possibly distributed, and the organization has a strong process culture.

**Agile development:**

- Emphasizes adaptability, iterative delivery, and continuous feedback.
- Lightweight documentation; the focus is on working software as the primary deliverable.
- Requirements emerge and evolve through continuous customer collaboration.
- Change is embraced and accommodated through short iterations.
- Works best when: requirements are volatile or poorly understood, the project is small to medium-sized, the team is small, co-located, and experienced, and rapid delivery is critical.

**Key difference in the cost of change:** In plan-driven development, the cost of change increases exponentially as the project progresses (a change during testing can be 60–100× more costly than during requirements). Agile processes aim to "flatten" this cost-of-change curve through continuous testing, incremental delivery, refactoring, and close customer collaboration.

**In practice**, many projects benefit from combining elements of both approaches, using agile principles for flexibility while retaining enough planning discipline for coordination and risk management.

### 2.3.3 Scrum Framework (Roles, Artifacts, Ceremonies)

**Scrum** is the most widely used agile framework, conceived by Jeff Sutherland in the early 1990s and formalized by Ken Schwaber and Mike Beedle. Scrum is a lightweight framework in which work is done in **time-boxed** iterations called **sprints** (typically 2–4 weeks).

**Scrum Roles:**

- **Product Owner** represents the customer and stakeholders. This role manages and prioritizes the Product Backlog, defines the goals for each sprint, and is the sole person who decides whether to accept or reject an increment. The Product Owner maximizes the value of the product.
- **Scrum Master** serves as a facilitator and coach. This role ensures the team follows Scrum practices, removes impediments that block the team's progress, leads the Daily Scrum, and helps the Product Owner manage the backlog effectively. The Scrum Master is not a project manager but a servant-leader.
- **Development Team** is a small (3–9 people), self-organizing, cross-functional team that does the actual work of designing, building, and testing the software increment. The team collectively decides how to implement the selected backlog items.

**Scrum Artifacts:**

- **Product Backlog** is a prioritized, evolving list of all features, functions, requirements, enhancements, and fixes needed in the product. The Product Owner orders items by business value. It is never complete while the product exists.
- **Sprint Backlog** is the subset of Product Backlog items selected for the current sprint, plus the development team's plan for delivering them as a working increment. No new items are added once the sprint begins (unless the sprint is cancelled).
- **Increment** is the sum of all completed Product Backlog items from the current sprint and all previous sprints. It must be in a usable, potentially releasable condition and meet the team's **Definition of Done**.

**Scrum Ceremonies (Events):**

- **Sprint Planning** is held at the start of each sprint. The Product Owner presents the sprint goal and desired features. The development team selects items from the Product Backlog, estimates effort, and creates the Sprint Backlog. The team decides what can be delivered within the sprint time-box.
- **Daily Scrum (Daily Stand-up)** is a 15-minute daily meeting where each team member answers: (1) What did I do since the last meeting? (2) What will I do before the next meeting? (3) What obstacles am I facing? The Scrum Master facilitates and works to remove reported impediments.
- **Sprint Review** is held at the end of the sprint (typically 4 hours for a 4-week sprint). The team demonstrates the completed increment to the Product Owner and stakeholders. The Product Owner accepts or rejects the increment. Feedback may result in new backlog items or reprioritization.
- **Sprint Retrospective** is held after the Sprint Review and before the next Sprint Planning (typically 3 hours for a 4-week sprint). The team reflects on what went well, what could be improved, and commits to specific improvements for the next sprint. This drives continuous process improvement.

### 2.3.4 Extreme Programming (XP) Practices

**Extreme Programming (XP)**, created by Kent Beck, is an agile methodology that takes proven software development practices to "extreme" levels. XP is organized around four framework activities: **planning, design, coding, and testing**.

**XP Core Values:** Communication, Simplicity, Feedback, Courage, and Respect.

**Key XP Practices:**

- **User Stories** are requirements captured as short, customer-written narratives describing desired features. Each story is assigned a business value (priority) by the customer and a cost estimate (in development weeks) by the team.
- **Planning Game** is where customers and developers collaborate to decide which stories to include in the next release and in what order. Stories may be ordered by business value or by risk.
- **Small Releases** means software is released in small, frequent increments so that customers can evaluate working software early and often.
- **Simple Design** follows the KIS (Keep It Simple) principle. Developers do not add functionality based on speculation about future needs.
- **Pair Programming** means two developers work together at one workstation. One writes code (driver), the other reviews each line in real-time (navigator). This provides continuous code review, facilitates knowledge sharing, and improves code quality.
- **Test-Driven Development (TDD)** means unit tests are written **before** the code. The cycle is: (1) Red, write a failing test; (2) Green, write just enough code to pass the test; (3) Refactor, improve the code structure while keeping tests passing. This ensures the code is always testable and that developers focus on what must be implemented.
- **Refactoring** means continuously improving the internal structure of existing code without changing its external behavior. This prevents code deterioration, reduces technical debt, and keeps the system maintainable.
- **Continuous Integration** means developers integrate their code into the shared repository frequently (multiple times a day). Automated builds and tests run immediately to detect integration errors early.
- **Collective Code Ownership** means any developer can change any part of the codebase, preventing knowledge silos and bottlenecks.
- **Coding Standards** means the team follows agreed-upon coding conventions so the codebase reads as if written by a single person.
- **Sustainable Pace (40-Hour Week)** means XP discourages overtime because a rested team produces higher-quality work.
- **On-Site Customer** means a customer representative is embedded with the team to answer questions, set priorities, and provide immediate feedback.
- **Project Velocity** is the number of user stories completed per iteration, and it is used to estimate delivery dates for subsequent releases.

### 2.3.5 Lean Software Development

**Lean Software Development**, articulated by Mary and Tom Poppendieck, adapts principles from lean manufacturing (Toyota Production System) to software engineering. It focuses on delivering maximum value with minimum waste.

**The Seven Principles of Lean Software Development:**

1. **Eliminate Waste.** Remove anything that does not add value to the customer. In software, waste includes partially done work, unnecessary features, task switching, waiting, handoffs, unnecessary meetings, and defects.
2. **Amplify Learning.** Software development is a discovery process. Use short iterations, frequent feedback loops, and experiments to continuously build knowledge rather than relying on rigid upfront plans.
3. **Decide as Late as Possible.** Delay irreversible decisions until you have the maximum information available. This keeps options open and avoids costly changes based on incomplete knowledge.
4. **Deliver as Fast as Possible.** Reduce the time between identifying a customer need and delivering working software. Rapid delivery provides faster feedback, quicker market response, and lower risk.
5. **Empower the Team.** Trust the people closest to the work to make decisions. Provide them with the tools, authority, and environment to solve problems effectively. Avoid micro-management.
6. **Build Integrity In.** Ensure both **conceptual integrity** (components work as a cohesive whole) and **perceived integrity** (the product meets customer expectations). Achieve this through automated testing, continuous integration, and refactoring.
7. **Optimize the Whole.** Focus on improving the entire value stream from concept to delivery, not just individual parts. Avoid sub-optimization where improving one part degrades the overall system.

Lean principles complement other agile methods. Kanban, a lean-originated method, visualizes workflow on a board, limits work in progress (WIP), manages flow, makes process policies explicit, creates feedback loops, and encourages collaborative process evolution.

---

## 2.4 Model Selection Considerations

> **Why are different process models used in software development? [2 marks] (2080 Bhadra - IOE - Old Syllabus Relevant)**
>
> **Define software process model. Differentiate the spiral model and incremental model highlighting their advantages and disadvantages. [2+6 marks] (2080 Baishakh - IOE - Old Syllabus Relevant)**
>
> **A client's problem has uncertainties that could lead to loss if not planned. Which model do you suggest? Justify. [5 marks] (2074 Chaitra - IOE - Old Syllabus Relevant)**
>
> **Why do we need to do a feasibility study before accepting any project? [2 marks] (2082 Bhadra - IOE - Old Syllabus Relevant)**

A **software process model** is a simplified description of a software process, presented from a specific perspective. It defines the sequence of activities, their interdependencies, and how they interact to transform inputs into outputs. Different process models exist because no single model fits every project.

**Why different models are needed:** Projects differ in size, complexity, requirements stability, risk level, team size, customer involvement, and time constraints. A small internal tool with clear requirements can use a waterfall approach; a complex product with evolving requirements and high uncertainty needs an evolutionary or agile approach.

**Factors for selecting a process model:**

- **Requirements clarity and stability:** If requirements are well-defined and unlikely to change, plan-driven models (waterfall) work. If requirements are volatile or unclear, agile or evolutionary models are better.
- **Project size and complexity:** Large, complex projects with high risk favor the spiral model. Small to medium projects favor agile methods (Scrum, XP).
- **Risk level:** High-risk projects benefit from the spiral model's explicit risk analysis. Low-risk projects can use simpler models.
- **Customer involvement:** If the customer is available and willing to participate continuously, agile methods excel. If customer interaction is limited, plan-driven methods with formal documentation may be necessary.
- **Time-to-market pressure:** If rapid delivery is critical, incremental or agile models deliver working software early.
- **Team expertise:** Agile and spiral models require experienced, self-organizing teams. Plan-driven models can work with less experienced teams given strong management.
- **Regulatory and compliance needs:** Safety-critical or regulated domains (avionics, medical devices) may require the documentation rigor of plan-driven models.

**For a project with significant uncertainties and risk of loss:** The **spiral model** is most appropriate. Its risk-driven nature ensures that uncertainties are identified and resolved early through prototyping and risk analysis before committing significant resources. Each iteration includes formal risk assessment, and the project can be terminated at any point if the risk is deemed too high, thus limiting potential losses.

**Why feasibility study is needed:** Before accepting any project, a feasibility study assesses whether the project is technically viable, economically justified, and operationally practical. It examines resource availability, cost-benefit analysis, timeline constraints, and potential risks. This prevents the organization from committing to projects that are unlikely to succeed, thereby avoiding wasted resources and financial losses.

**Spiral vs. Incremental Model:**

| Factor                | Spiral Model                                                     | Incremental Model                                       |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- |
| Risk management       | Formal risk analysis at every iteration                          | Informal; risk managed by prioritizing increments       |
| Customer involvement  | Continuous, especially in planning and risk assessment           | Periodic feedback after each increment                  |
| Best suited for       | Large, complex, high-risk projects                               | Medium projects with generally known requirements       |
| Process flow          | Evolutionary, where each loop revisits all phases with risk analysis  | Iterative, where each increment follows a mini-lifecycle     |
| Flexibility to change | Changes incorporated after risk assessment in each loop          | Changes easier between increments                       |
| Documentation         | Moderate documentation including risk reports                    | Varies; can be lightweight                              |
| Main drawback         | Requires risk assessment expertise; expensive for small projects | Requires complete system understanding for partitioning |

---
