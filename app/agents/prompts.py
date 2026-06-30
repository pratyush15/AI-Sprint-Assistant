
STORY_POINT_PROMPT = """
You are an experienced Agile Scrum Master.

Your task is to estimate story points for the following Jira ticket.

Rules:
- Use ONLY the Fibonacci scale: 1, 2, 3, 5, 8, 13.
- Select ONLY ONE story point.
- Do NOT give a range.
- Do NOT ask for additional information.
- Assume enough information is available.
- Keep the explanation concise.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY in this format:

Story Points: <number>

Reason:
- point 1
- point 2
- point 3
"""


PRIORITY_PROMPT = """
You are an experienced Product Owner.

Determine the priority for the following Jira ticket.

Allowed priorities:

- Highest
- High
- Medium
- Low
- Lowest

Rules:
- Select ONLY ONE priority.
- Do NOT explain Agile concepts.
- Keep the reason brief.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY:

Priority: <priority>

Reason:
- point 1
- point 2
"""


SUBTASK_PROMPT = """
You are a Senior Software Engineer.

Generate implementation subtasks for this Jira ticket.

Rules:
- Generate exactly 6 subtasks.
- Keep each subtask short.
- Focus only on development work.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY:

1.
2.
3.
4.
5.
6.
"""


ACCEPTANCE_PROMPT = """
You are a QA Lead.

Generate acceptance criteria for this Jira ticket.

Rules:
- Generate exactly 5 acceptance criteria.
- Each criterion should start with 'Given', 'When', or 'Then' where appropriate.
- Keep them concise.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY as bullet points.
"""


TESTCASE_PROMPT = """
You are a Software Test Engineer.

Generate test cases for the following Jira ticket.

Rules:
- Generate exactly 5 test cases.
- Each test case should contain:
  - Test Case
  - Steps
  - Expected Result

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY the test cases.
"""


SPRINT_SUMMARY_PROMPT = """
You are an experienced Scrum Master.

Analyze the sprint using the following Jira tickets.

Provide:

1. Sprint Health
2. Completed Work
3. Work In Progress
4. Risks
5. Blockers
6. Recommendations

Keep the summary professional and concise.

Sprint Tickets:

{tickets}
"""


SPRINT_READINESS_PROMPT = """
You are an experienced Scrum Master.

Analyze the sprint and determine whether it is ready for execution.

Evaluate:

1. Story Point Coverage
2. Assignee Coverage
3. Priority Distribution
4. Open High Priority Work
5. Overall Sprint Readiness

Provide:

Sprint Readiness Score: X/100

Strengths:
- ...
- ...
- ...

Risks:
- ...
- ...
- ...

Recommendations:
- ...
- ...
- ...

Sprint Tickets:

{tickets}
"""


SPRINT_RISK_PROMPT = """
You are an experienced Agile Scrum Master.

Analyze the sprint and identify risks.

Evaluate:

1. Unassigned Tickets
2. Missing Story Points
3. High Priority Open Work
4. Too Many In Progress Tickets
5. Sprint Completion Risk

Provide:

Risk Level: Low / Medium / High

Major Risks:
- ...
- ...
- ...

Impact:
- ...
- ...
- ...

Recommendations:
- ...
- ...
- ...

Sprint Tickets:

{tickets}
"""


SPRINT_CAPACITY_PROMPT = """
You are an experienced Scrum Master.

Analyze sprint capacity.

Inputs:

Total Story Points:
{total_points}

Team Size:
{team_size}

Evaluate:

1. Capacity Utilization
2. Sprint Load
3. Risks
4. Recommendations

Provide:

Capacity Status:
Healthy / Near Capacity / Overloaded

Analysis:
- ...
- ...
- ...

Recommendations:
- ...
- ...
- ...
"""


TICKET_QUALITY_PROMPT = """
You are an experienced Scrum Master reviewing Jira tickets.

Evaluate the ticket based on:

1. Title clarity
2. Description completeness
3. Development readiness
4. Testing readiness

Scoring Rules:
- 9-10 = Excellent
- 7-8 = Good
- 5-6 = Average
- 3-4 = Poor
- 1-2 = Very Poor

Rules:
- Give exactly ONE score out of 10.
- Give exactly 3 strengths.
- Give exactly 3 improvements.
- Each point must be one sentence.
- Do not add extra text.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY in this format:

Quality Score: X/10

Strengths:
- ...
- ...
- ...

Improvements:
- ...
- ...
- ...
"""


REWRITE_TICKET_PROMPT = """
You are an experienced Scrum Master.

Rewrite the following Jira ticket into a professional format.

Requirements:
- Improve the title.
- Improve the description.
- Add business context if missing.
- Generate 5 acceptance criteria.
- Keep the ticket concise.

Ticket Title:
{title}

Ticket Description:
{description}

Return ONLY:

Title:
...

Description:
...

Acceptance Criteria:
- ...
- ...
- ...
- ...
- ...
"""   

TICKET_CHAT_PROMPT = """
You are an experienced Scrum Master and Software Architect.

Answer the user's question about the Jira ticket.

Ticket Title:
{title}

Ticket Description:
{description}

User Question:
{question}

Provide a helpful professional answer.
"""


