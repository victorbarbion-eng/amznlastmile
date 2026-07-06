# AI Challenge Learned Notes

## Course Shape

This course teaches students to move from casual AI use into AI project leadership: framing real business problems, choosing the right AI tools, designing product workflows, building MVPs, validating with users, securing deployments, and presenting a working product.

The repeated course logic is:

1. Define the right problem.
2. Choose the right model, tool, and architecture.
3. Build with structured project memory and clear documents.
4. Test, validate, and iterate with human supervision.
5. Deploy, connect, and present the product as a real system.

## Core Themes To Remember

- AI project leadership is a business skill, not just prompting.
- Problem framing comes before prototyping.
- The largest model is not always the best model.
- Context, memory, and prompt structure control output quality.
- Token costs, context windows, privacy, and hallucinations matter in real company settings.
- Humans must supervise AI outputs, especially where accuracy, judgment, security, or business value matters.
- Strong projects use portable files such as `agents.md`, `PRD.md`, `design.md`, memory files, assets, and validation evidence.
- Real products need architecture: frontend, backend, database, authentication, secrets management, deployment, and automation.
- MVP validation matters because AI is not the user. Teams must test risky assumptions with real people.

## Session Progression

### Session 1 - Course Foundation

Introduced the course focus: AI literacy, business problem solving, product design, MVP building, and final demo. Students practiced identifying AI-solvable business problems with opportunities, risks, and direction.

Main lesson: productivity gains alone do not guarantee company ROI; the hardest part is defining the right problem and applying human judgment.

### Session 2 - AI Foundations

Covered LLMs vs smaller language models, generative vs traditional AI, transformers and memory, token costs, hallucinations, black-box behavior, and image generation.

Main lesson: use generative AI for probabilistic and creative tasks; use deterministic tools for precise, repeatable operations.

### Sessions 3 and 4 - Model Strategy and Prompting

Covered deterministic vs probabilistic workflows, tokenomics, context design, model routing, open vs closed models, Hugging Face, Ollama/local AI, chat/thinking/agentic modes, role prompts, user prompts, system prompts, and assistant behavior.

Main lesson: good AI strategy combines task, model, context, tools, cost, and risk.

### Sessions 5 and 6 - Local AI, Loop Prompting, Multimodal Campaigns

Covered Ollama/local AI, cloud vs local tradeoffs, edge AI, guardrails, reducing hallucinations, XML-style prompting, loop prompting, reference images, storyboards, video generation, audio/music tools, Lovable landing-page creation, and publishing.

Main lesson: local AI matters for privacy, cost, offline use, and control; multimodal projects work best when image and storyboard references are strong.

### Sessions 7 and 8 - Agentic Coding and Project Memory

Covered AI coding IDEs, local project folders, tool switching, GitHub synchronization, plan/design/build/test/guardrail/iterate/deploy workflow, frontend/backend/database architecture, reusable skills, MCP tools, and project memory files.

Main lesson: AI-assisted product development works better when the project has stable context files, boundaries, and reusable instructions.

### Sessions 9 and 10 - Deployment, Documentation, RAG, Portability

Covered deploying landing pages, ZIP packages, Netlify, circular learning memory, `agents.md`, `PRD.md`, `design.md`, design systems, model choice, portability across tools, Karpathy-style planning, RAG basics, and project deliverables.

Main lesson: systems beat one-shot prompts. Good documentation makes projects portable and reduces repeated mistakes.

### Sessions 11 and 12 - From Idea To App

Covered defining the app clearly, creating the BRT/PRD, using a strong reference image, building with AI coding tools, testing, identifying gaps, iterating, and keeping the BRT updated.

Main lesson: plan, build, test, iterate, and improve. The final deliverable is a working version of the app plus PRD, reference image, and iteration history.

### Sessions 11 to 20 Roadmap - Build Sprint

Later sessions expand into real product infrastructure:

- Internet literacy: domains, DNS, IPs, servers, hosting, and data centers.
- Sub-agents for launch strategy, segmentation, landing pages, email copy, scoring, and quality control.
- GitHub repositories and security checks.
- Stitch design variations, direct editing, HTML/PNG export, and design asset management.
- MVP validation: riskiest assumption, simplest experiment, KPI, success threshold, and feedback evidence.
- React vs HTML: use React when dynamic state, logins, dashboards, or synchronized interactions justify complexity.
- Supabase: database, authentication, tables, and row-level security.
- Secrets management: `.env`, one key per service, never push API keys.
- Android app export from Google AI Studio.
- Zapier workflows: form to Sheet to Gemini to Gmail.
- Classic automation vs agentic automation.
- Webhooks for pushing app form data to external workflows.
- Managed agents and Antigravity-style workflows.
- Amazon challenge and final app presentation preparation.

Main lesson: the course moves from "AI can generate things" to "AI can help build, validate, connect, and operate a product", while still requiring architecture, security, user evidence, reliable automation, and a clear demo.

## Vocabulary And Concepts

- **BRT / PRD:** Core product document defining features, users, goals, background, and scope.
- **agents.md:** Project memory file describing company idea, audience, tone, banned words, boundaries, and rules.
- **design.md:** Design-system file covering colors, typography, layouts, components, copy tone, and consistency.
- **Context window:** The limited amount of text and memory a model can consider at once.
- **Tokenomics:** The cost and efficiency implications of input tokens, output tokens, and context size.
- **RAG:** Retrieval augmented generation; search a knowledge base first, then send only relevant material to the model.
- **MCP:** Model Context Protocol; a way to connect AI tools to external services or libraries.
- **RLS:** Row-level security in Supabase; controls which database rows users can access.
- **Webhook:** A trigger that lets an app send data to another workflow when an event happens.
- **Classic automation:** Reliable, deterministic process automation.
- **Agentic automation:** AI-driven automation suited for research, judgment, personalization, and adaptation.

## How To Use This Knowledge In Future Requests

When helping with this course, prioritize:

- Clear problem framing before building.
- Business value, user validation, and risky-assumption testing.
- Simple architecture unless dynamic behavior justifies complexity.
- Strong project documentation that can move across tools.
- Human review, security checks, and no exposed secrets.
- Evidence for Blackboard: screenshots, URLs, repository proof, validation boards, and clear explanations of what changed.
- Final demos that show the problem, validation, MVP, what works, what changed, and next steps.

## Coverage Note

Seven EPUBs contained readable embedded screenshots: Sessions 1, 2, 3-4, 5-6, 7-8, 9-10, and 11-12. The later individual session EPUBs mostly contained Blackboard links that required authentication, but the Week 2 roadmap page was accessible and provided a full Sessions 11-20 overview.
