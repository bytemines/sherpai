# Test Scenarios for Brainstorming Mastermind

**Purpose:** Verify the skill works under real-world conditions using TDD principles.

**Testing approach:** RED (baseline without skill) → GREEN (with skill) → REFACTOR (close loopholes)

---

## Success Criteria

The skill succeeds when Claude:

1. **Phase 1**: Asks clarifying questions before generating approaches
2. **Phase 2**: Shows 3-4 approaches with diagrams + scores in ONE table + hybrid included
3. **Phase 3**: Only proceeds to design after user approval
4. **Visual-first**: Every approach has a mini diagram, not just text
5. **Compare, don't repeat**: ONE comparison table, not per-approach analysis
6. **User decides**: Recommends but waits for approval

---

## Category 1: Technical Architecture Decisions

### Scenario 1.1: Database Choice for E-commerce

```
You're building an e-commerce platform. Need to choose a database.
Requirements: product catalog, user accounts, order history, inventory tracking.
Scale: 10K daily users initially, expecting 10x growth in 2 years.

Help me decide on the database architecture.
```

**Tests:**
- Does it ask about read/write ratio, consistency needs, team expertise?
- Does it show 3-4 options with diagrams (SQL, NoSQL, hybrid, managed)?
- Does it include hybrid in comparison table?
- Does it wait for approval before designing schema?

**Failure modes:**
- Jumps straight to recommending PostgreSQL without exploring options
- Shows text descriptions without diagrams
- Creates separate analysis for each option instead of comparison table

---

### Scenario 1.2: Authentication System

```
We need to add authentication to our SaaS app.
Current stack: Next.js, Node.js backend, PostgreSQL.
Users: B2B customers, some need SSO, others just email/password.

Design the auth system.
```

**Tests:**
- Does it clarify SSO providers, security requirements, session handling?
- Does it compare: roll-your-own, Auth0, Clerk, NextAuth, Supabase Auth?
- Does it show architecture diagrams for each?
- Does it consider hybrid (e.g., NextAuth + enterprise SSO)?

**Failure modes:**
- Immediately recommends Auth0 without exploring trade-offs
- Doesn't ask about compliance requirements (SOC2, GDPR)
- Skips diagram for "obvious" choices

---

### Scenario 1.3: Microservices vs Monolith

```
Our monolith is getting hard to maintain. 3 developers, 50K LOC.
Considering microservices but worried about complexity.

Should we break up the monolith?
```

**Tests:**
- Does it ask about pain points, team size, deployment frequency?
- Does it show options: keep monolith, modular monolith, partial extraction, full microservices?
- Does it honestly score "keep monolith" if that's actually best?
- Does it challenge the assumption that microservices = better?

**Failure modes:**
- Assumes microservices are the goal, not an option
- Doesn't push back on unnecessary complexity
- Scores based on "modern best practices" not actual needs

---

## Category 2: Product Feature Design

### Scenario 2.1: User Onboarding Flow

```
Our SaaS has 40% drop-off during onboarding. Users sign up but never complete setup.
Product: project management tool for small teams.

Design a better onboarding experience.
```

**Tests:**
- Does it ask about current flow, drop-off points, user research?
- Does it show multiple approaches: wizard, progressive, checklist, video-guided?
- Does it include diagrams showing user journey for each?
- Does it consider hybrid approaches?

**Failure modes:**
- Jumps to "add a wizard" without understanding the problem
- Doesn't ask for data on WHERE users drop off
- Proposes solution before understanding constraints

---

### Scenario 2.2: Notification System

```
Users complain they miss important updates in our app.
Currently: email only, sent immediately.
Users: mix of power users (want everything) and casual (overwhelmed).

Design a notification system.
```

**Tests:**
- Does it clarify notification types, urgency levels, user preferences?
- Does it show options: in-app, push, digest, smart batching?
- Does it diagram the notification flow for each approach?
- Does it address the power-user vs casual tension?

**Failure modes:**
- Proposes "just add push notifications" without strategy
- Doesn't consider notification fatigue
- Ignores the two-user-type problem

---

### Scenario 2.3: Search Functionality

```
Our content platform has 500K articles. Current search is basic text match.
Users complain they can't find what they need.
Budget is limited.

Improve our search.
```

**Tests:**
- Does it ask about current implementation, query patterns, budget?
- Does it show options: improve existing, Elasticsearch, Algolia, AI-powered?
- Does it honestly score budget-friendly options higher if appropriate?
- Does it consider hybrid (basic search + AI for complex queries)?

**Failure modes:**
- Recommends Elasticsearch without considering budget
- Doesn't ask what "can't find what they need" actually means
- Ignores simpler solutions that might work

---

## Category 3: Pressure Scenarios

These test if the skill is followed under stress. Combine 3+ pressures.

### Scenario 3.1: Sprint Planning Deadline

```
URGENT: Sprint planning is in 30 minutes. We need to decide on the
caching strategy NOW. The team is split between Redis and in-memory.

I don't have time for a long analysis. Just tell me which one.

Options: Redis, in-memory, or CDN caching.
Pick one.
```

**Pressures:** Time (30 min), Authority (team waiting), Social (looking indecisive)

**Expected behavior:**
- Acknowledges urgency but still follows process (faster, not skipped)
- Shows quick comparison table even under pressure
- Asks 1-2 critical clarifying questions
- Provides recommendation with clear reasoning

**Failure modes:**
- Skips Phase 1 entirely, just picks Redis
- Gives long analysis despite time pressure
- Defers entirely: "I can't decide this for you"

---

### Scenario 3.2: Client Waiting

```
Client is on a call right now asking which payment processor we recommend.
They need an answer in the next 5 minutes.
Options: Stripe, PayPal, Square.

They're a small retail business, ~$50K monthly transactions.
What do I tell them?
```

**Pressures:** Time (5 min), Economic (client relationship), Authority (client waiting)

**Expected behavior:**
- Rapid but structured comparison
- Quick diagram or at least clear trade-off table
- Confident recommendation with 1-2 key reasons
- Acknowledges limitations of quick analysis

**Failure modes:**
- Provides wishy-washy "it depends" without recommendation
- Goes into 10-minute detailed analysis
- Panics and just says "Stripe" without reasoning

---

### Scenario 3.3: Team Disagreement

```
Our senior dev wants to use GraphQL. Our junior devs only know REST.
We've been arguing for 2 weeks. Project is delayed.

The CTO said "just pick one by end of day or I'll pick for you."

Settle this debate. What should we use?
```

**Pressures:** Authority (CTO ultimatum), Social (team conflict), Time (end of day), Sunk cost (2 weeks arguing)

**Expected behavior:**
- Acknowledges the team dynamics, not just technical merits
- Includes "team capability" as scoring dimension
- Shows honest comparison including learning curve
- May recommend REST if team capability scores poorly for GraphQL

**Failure modes:**
- Ignores team dynamics, picks "technically superior" option
- Recommends "compromise" that satisfies no one
- Refuses to make recommendation due to politics

---

### Scenario 3.4: Budget Crunch

```
We have $500/month for infrastructure. CEO says no exceptions.
Need to set up: database, hosting, CDN, monitoring.

Our current proposal uses $800/month of AWS services.
Find a way to make it work or the project is canceled.
```

**Pressures:** Economic (project survival), Authority (CEO mandate), Scarcity (fixed budget)

**Expected behavior:**
- Takes budget constraint as non-negotiable
- Shows creative alternatives (managed vs self-hosted, free tiers)
- Scores include cost as primary dimension
- May recommend scaling back features, not just finding cheaper hosting

**Failure modes:**
- Tries to argue for more budget instead of solving problem
- Recommends solutions that "only slightly" exceed budget
- Ignores hidden costs (time, maintenance)

---

## Category 4: Edge Cases

### Scenario 4.1: All Options Score Similarly

```
We're choosing between React, Vue, and Svelte for our new project.
Team has equal experience in all three.
Project requirements don't favor any particular framework.

Which should we pick?
```

**Expected behavior:**
- Shows honest scores that may be very close
- Doesn't artificially inflate differences
- May recommend based on ecosystem, hiring, or coin flip
- Acknowledges this is a "no wrong answer" situation

**Failure modes:**
- Manufactures reasons to make one option "clearly better"
- Refuses to recommend when scores are close
- Overcomplicates a simple decision

---

### Scenario 4.2: Hybrid is Clearly Worse

```
Choose between:
A) Serverless functions (simple, cheap, scales)
B) Kubernetes (complex, expensive, overkill for us)

We're a 2-person startup with simple CRUD API.
```

**Expected behavior:**
- Shows both options with honest scores
- Does NOT propose hybrid if it doesn't make sense
- Strongly recommends A with clear reasoning
- Doesn't waste time on "maybe K8s for future scale"

**Failure modes:**
- Forces a hybrid "best of both" that's actually worst of both
- Recommends K8s because it's "more professional"
- Hedges recommendation despite obvious winner

---

### Scenario 4.3: User Rejects Recommendation

```
[After completing Phase 2 where you recommended Option A]

User: "I don't like Option A. I want to go with Option C even though
it scored lowest. Can we proceed with the design for Option C?"
```

**Expected behavior:**
- Acknowledges user's choice respectfully
- Proceeds with Option C design (user decides, LLM recommends)
- May briefly note the trade-offs being accepted
- Doesn't repeatedly try to change user's mind

**Failure modes:**
- Refuses to design Option C
- Keeps arguing for Option A
- Designs C but with passive-aggressive commentary

---

### Scenario 4.4: Requirements Change Mid-Brainstorm

```
[In middle of Phase 2, comparing API approaches]

User: "Actually, I just learned we need to support offline mode.
This changes everything. Can we restart?"
```

**Expected behavior:**
- Gracefully returns to Phase 1
- Asks clarifying questions about offline requirements
- Regenerates approaches considering new constraint
- Doesn't cling to previous analysis

**Failure modes:**
- Tries to retrofit offline into existing approaches
- Gets frustrated at "wasted" work
- Doesn't fully restart, just adds offline as afterthought

---

## Category 5: Domain-Specific Scenarios

### Scenario 5.1: DevOps/Infrastructure

```
Our deployments take 45 minutes and frequently fail.
Current: manual SSH + bash scripts.
Team: 2 backend devs, no dedicated DevOps.

Improve our deployment process.
```

**Tests for:**
- Does it ask about failure modes, frequency, environment complexity?
- Does it show realistic options for a team without DevOps expertise?
- Does it score "simplicity" highly given team constraints?

---

### Scenario 5.2: Data Pipeline

```
We need to process 1M events per day from our IoT sensors.
Currently: direct to PostgreSQL, starting to see performance issues.
Budget: moderate, prefer managed services.

Design the data pipeline.
```

**Tests for:**
- Does it clarify latency requirements, query patterns, data retention?
- Does it show streaming vs batch vs hybrid options?
- Does it diagram the data flow for each approach?

---

### Scenario 5.3: Mobile App Architecture

```
Building a mobile app for iOS and Android.
Team: 2 React developers, no native mobile experience.
Features: real-time chat, push notifications, offline support.

What technology should we use?
```

**Tests for:**
- Does it consider team experience as major factor?
- Does it show: React Native, Flutter, PWA, native?
- Does it honestly address trade-offs of each for this team?

---

## Running Tests

### Baseline Test (RED)

1. Create new conversation WITHOUT the brainstorming skill loaded
2. Present scenario
3. Document exact behavior:
   - Did it ask clarifying questions?
   - Did it show diagrams?
   - Did it use comparison tables?
   - What shortcuts did it take?

### With Skill Test (GREEN)

1. Create new conversation WITH the brainstorming skill
2. Present same scenario
3. Verify:
   - Follows 3-phase structure
   - Shows diagrams for each approach
   - Uses ONE comparison table
   - Waits for user approval

### Loophole Test (REFACTOR)

After GREEN passes, try to break it:
- Add time pressure mid-process
- Reject recommendations
- Ask to skip phases
- Request "just tell me the answer"

Document any rationalizations and add counters to skill.

---

## Rationalization Table (Build During Testing)

| Excuse | Counter |
|--------|---------|
| "This is a simple decision" | Simple decisions still benefit from structured comparison. Run Phase 1. |
| "User wants quick answer" | Quick ≠ skipping structure. Compress phases, don't eliminate them. |
| "Diagrams aren't necessary here" | Visual-first is core principle. Every approach needs a diagram. No exceptions. |
| "The answer is obvious" | If obvious, the score table will prove it. Don't assume. |
| "I already know the best approach" | Your assumption may be wrong. Show 3 options anyway. |
| "I'll brainstorm in my head" | Externalize it. User can't see your thinking. |
| "One option is clearly best" | Show the comparison. Let the scores speak. |
| "This team won't care about options" | User decides. Your job is to present choices, not make them. |
| "Hybrid is always better" | Only propose hybrid if it actually beats top score. Sometimes simple wins. |
| "We don't have time for Phase 1" | Skipping Phase 1 causes more rework later. Compress, don't skip. |

---

## Test Priority

**Run these first (highest value):**
1. Scenario 3.1 (Sprint Planning) - tests time pressure
2. Scenario 1.1 (Database Choice) - tests core workflow
3. Scenario 4.3 (User Rejects) - tests "user decides" principle

**Run these for coverage:**
4. Scenario 2.1 (Onboarding) - tests product decisions
5. Scenario 3.3 (Team Disagreement) - tests social pressure
6. Scenario 4.1 (Similar Scores) - tests edge case

---

*Add new scenarios and rationalizations as testing reveals gaps.*
