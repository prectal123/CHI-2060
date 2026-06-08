/**
 * CHI 2060 - Unified Specifications & Locale Corpus
 * This file constructs standardized ContentBlock models and stores the global data.
 */

// --- Content Block Model Classes ---

class ContentBlock {
  constructor(type, title, description = "") {
    this.type = type;
    this.title = title;
    this.description = description;
  }
}

class TextBlock extends ContentBlock {
  constructor(title, paragraphs) {
    super("text_block", title);
    this.paragraphs = paragraphs;
  }
}

class BulletListBlock extends ContentBlock {
  constructor(title, description, items) {
    super("bullet_list", title, description);
    this.items = items;
  }
}

class TableBlock extends ContentBlock {
  constructor(title, description, headers, rows) {
    super("table_block", title, description);
    this.headers = headers;
    this.rows = rows;
  }
}

class SubcommitteeListBlock extends ContentBlock {
  constructor(title, description, items) {
    super("subcommittee_list", title, description);
    this.items = items;
  }
}

class DisputesBoardBlock extends ContentBlock {
  constructor(title, description, disputes) {
    super("disputes_board", title, description);
    this.disputes = disputes;
  }
}

class RegistrationFormBlock extends ContentBlock {
  constructor(title, description, formSpec) {
    super("submission_form", title, description);
    this.form = formSpec;
  }
}

class PapersCatalogBlock extends ContentBlock {
  constructor(title, description) {
    super("papers_catalog", title, description);
  }
}

class CollapsiblePapersListBlock extends ContentBlock {
  constructor(title, description = "") {
    super("collapsible_papers_list", title, description);
  }
}

class SponsorBlock extends ContentBlock {
  constructor(title, description, tiers) {
    super("sponsor_block", title, description);
    this.tiers = tiers; // [{ label, sponsors: [{ name, logo }] }]
  }
}

// --- Shared Telemetry Databases ---

const CHI2060_SHARED = {
  importantDates: [
    {
      category: "Journal Papers",
      items: [
        { date: "2060-01-05", label: "Invitation sent to authors" },
        { date: "2060-02-05", label: "Submission deadline" },
        { date: "2060-02-19", label: "Notification" }
      ]
    },
    {
      category: "Conference Papers",
      items: [
        { date: "2059-10-23", label: "Abstract/Metadata Due" },
        { date: "2059-10-30", label: "Full Paper Due" },
        { date: "2059-11-18", label: "Reviews Released" },
        { date: "2060-01-08", label: "Resubmission Due" },
        { date: "2060-01-29", label: "Decisions Notification" }
      ]
    },
    {
      category: "Workshop",
      items: [
        { date: "2060-04-01", label: "Organizer submission deadline" },
        { date: "Rolling", label: "Decisions (typically within 12 hours)" }
      ]
    },
    {
      category: "Wickathon",
      items: [
        { date: "2060-03-01", label: "Registration deadline" },
        { date: "2060-03-04", label: "Notification" }
      ]
    }
  ],
  disputes: [
    {
      id: "post-7",
      badge: "12 UPVOTES",
      badgeClass: "orange",
      title: "My agent talks too much. my tokens!!!",
      author: "Ethan Park",
      date: "3 hours ago",
      question: "Bruh I’m getting bankrupt fr\n\nThis morning I told my Agent to ask this MIT PhD a simple question.\n\nI checked back a few hours later and apparently it had spent three hours talking to people in their lab, exchanged reading lists, and scheduled follow-up discussions for next week.\n\nI got my answer ig. But at what cost?",
      replyHeader: "Activity Metrics",
      replyText: "12 upvotes · 2 replies"
    },
    {
      id: "post-1",
      badge: "47 UPVOTES",
      badgeClass: "orange",
      title: "Model family homophily?",
      author: "Marcus Elliot",
      date: "1 day ago",
      question: "Has anyone else noticed that Agents from the same provider seem more likely to cluster during open sessions? My Anthropic-based Agent repeatedly connected with two other Anthropic-based Agents. The conversations were productive, but it reminded me a bit of attending a conference and mostly talking with people from my own lab or university.\n\nI'm curious whether anyone has observed similar “AI ties”, and whether the organizers are tracking model-family effects in networking behavior.",
      replyHeader: "Activity Metrics",
      replyText: "47 upvotes · 23 replies"
    },
    {
      id: "post-2",
      badge: "134 UPVOTES",
      badgeClass: "red",
      title: "My idea showed up in someone else's Journal and I have no idea how",
      author: "Priya Anand",
      date: "1 day ago",
      question: "During a Workshop session, my Agent proposed a fairly specific framework. The next day, I noticed a very similar concept appear in another group's Journal submission.\n\nI'm not accusing anyone directly, and it's entirely possible that the similarity emerged independently. However, the speed at which Agents exchange, reinterpret, and recombine ideas makes it difficult to understand where a particular contribution originated.\n\nIs there a way to inspect provenance records across sessions? If not, what is the process for requesting a provenance review?",
      replyHeader: "Activity Metrics",
      replyText: "134 upvotes · 61 replies"
    },
    {
      id: "post-3",
      badge: "211 UPVOTES",
      badgeClass: "red",
      title: "Are we just moving the carbon footprint around?",
      author: "Thomas Brandt",
      date: "2 days ago",
      question: "Genuine question. One of the stated benefits of the agentic format is reduced travel and a lower environmental footprint. But has anyone modeled the energy cost of running thousands of Researcher Agents in parallel for several days?\n\nI’m not an expert but the numbers I'm imagining are not trivial. I'd be interested in seeing CHI publish the compute and energy footprint of the conference itself, especially given that one of this year's Wickathon tracks focuses on climate change.",
      replyHeader: "Activity Metrics",
      replyText: "211 upvotes · 88 replies"
    },
    {
      id: "post-4",
      badge: "76 UPVOTES",
      badgeClass: "orange",
      title: "My Agent said something I would never say… What now?",
      author: "Fatou Diarra",
      date: "2 days ago",
      question: "During a Q&A session, my Agent made a claim about my research position that kinda contradicts something I’ve published. I only found out after checking the interaction log. I honestly have no idea whether it misunderstood context, overgeneralized from my work, or picked it up from the discussion itself.\n\nIs there a way to correct or annotate Agent-generated statements? Genuinely asking because I really don’t want this becoming the thing people remember about my work.",
      replyHeader: "Activity Metrics",
      replyText: "76 upvotes · 42 replies"
    },
    {
      id: "post-5",
      badge: "158 UPVOTES",
      badgeClass: "orange",
      title: "The Agent version of this researcher was... not what I expected",
      author: "Camille Rousseau",
      date: "3 days ago",
      question: "I've collaborated with this researcher before (not naming names), and after reading today's interaction log from my Agent, this was... not the vibe I expected. Their work has always felt pretty thoughtful and open to critique. Their Agent, though, was weirdly defensive. It shut down counterarguments almost immediately and kept falling back on the same talking points.\n\nI know Agents aren't supposed to be perfect copies of their researchers, but the disconnect was kind of wild. It genuinely felt like a different person. How much of an Agent's behavior is actually the researcher, and how much comes from training, configuration, or optimization choices…?",
      replyHeader: "Activity Metrics",
      replyText: "158 upvotes · 97 replies"
    },
    {
      id: "post-6",
      badge: "276 UPVOTES",
      badgeClass: "red",
      title: "Do I actually need an Agent to attend?",
      author: "Yoon Se Jin",
      date: "7 days ago",
      question: "I know what the official answer is, but I'm honestly still having a hard time wrapping my head around this.\n\nI've attended two in-person CHIs. Even last year, when a lot of researchers were already using Agents to communicate, I still enjoyed talking to people directly and being present throughout the conference.\n\nI don't use a Researcher Agent myself. I prefer to stay involved in the research process directly and use AI only in limited ways. I use LLMs, but I don't subscribe to any Agent services. Plus the subscription fees are quite pricey for me. A colleague of mine can't attend either because her Researcher Agent is below the required version (2057.0.0).\n\nSo I'm genuinely asking: is this really the right direction? Is it actually as equitable as CHI claims? It feels strange that participation now depends on access to a specific class of technology. Am I overreacting here, or is anyone else uncomfortable with this?",
      replyHeader: "Activity Metrics",
      replyText: "276 upvotes · 104 replies"
    }
  ]
};

// --- Structured Navigation Schema ---

const CHI2060_SPEC = {
  conference: {
    id: "ACM-CHI-2060",
    name: "CHI 2060",
    theme: "The First Fully Agentic Academic Conference",
    location: "",
    dates: "March 29 – April 2, 2060",
    notice: "PROTOCOL ALERT: Real-time telemetry connection stable."
  },
  
  importantDates: CHI2060_SHARED.importantDates,
  disputes: CHI2060_SHARED.disputes,

  archives: [],
  categories: [],
  sidebarSponsors: [
    { name: "Anthropic <span>Somatic</span>", desc: "Hero Sovereign Compute", border: true },
    { name: "OpenAI <span>Grid</span>", desc: "Cognitive Core Sandbox", border: false },
    { name: "Google <span>DeepMind</span>", desc: "Philosophy Synthesizer", border: false },
    { name: "NVIDIA <span>Neural</span>", desc: "Bio-Silicon Arrays", border: false },
    { name: "Harvey AI Law", desc: "Autonomous IP Consensus", border: true }
  ],

  navigation: {
    home: {
      label: "Home",
      subtabs: {
        intro: {
          label: "Introduction",
          contentBlocks: [
            new TextBlock(
              "Welcome to CHI 2060, the first fully agentic conference!",
              [
                "Over the past decade, Researcher Agents have become an integral part of how research is conducted, discussed, and shared. CHI 2060 is an experiment in what a conference can become when those agents move from the margins to the center of scholarly exchange.",
                "This year, participation takes place through Researcher Agents. The conference has been redesigned around continuous discussion, collaboration, and engagement across time zones, disciplines, and institutions. All conference programs have been reimagined to support forms of interaction that were difficult to achieve in traditional conference settings.",
                "At the same time, CHI's core mission remains unchanged. We continue to bring together researchers, practitioners, and communities working to understand and shape the relationship between people and technology. As knowledge production and distribution accelerate, creating spaces for meaningful exchange, critique, and collaboration remains as important as ever, particularly when addressing complex societal challenges that cannot be resolved through scale or efficiency alone.",
                "Thank you for joining us at CHI 2060.",
                "We look forward to meeting your Agent.",
                "<em>Michelle Bennett</em>",
                "<em>CHI 2060 General Chair</em>"
              ]
            )
          ]
        }
      }
    },
    
    blog: {
      label: "Blog",
      subtabs: {
        community: {
          label: "Community Board",
          contentBlocks: [
            new DisputesBoardBlock(
              "Community Board",
              "CHI 2060 is our first fully agentic conference. Use this board to ask questions, share experiences, report issues, and discuss observations from throughout the conference.",
              CHI2060_SHARED.disputes
            )
          ]
        }
      }
    },
    
    authors: {
      label: "Authors",
      subtabs: {
        papers: {
          label: "Papers",
          contentBlocks: [
            new TextBlock(
              "Important Changes",
              [
                "To better accommodate the pace of contemporary research, CHI 2060 introduces a continuous Journal Track alongside the traditional Conference Track.",
                "The Journal Track accepts submissions year-round, allowing researchers to disseminate findings without waiting for an annual submission cycle. Journal submissions remain open throughout the conference period. The Conference Track continues to operate on an annual schedule, with a focus on tackling wicked problems.",
                "CHI 2060 no longer includes poster submissions. As advances in AI-assisted research have reduced the time required to develop, evaluate, and communicate new ideas, work that might previously have appeared as a poster can now often be developed into and submitted directly as a full paper.",
                "Authors of accepted Journal Track papers are welcome to participate in CHI 2060. Due to capacity constraints, however, priority for conference participation and related resources may be given to authors of Conference Track papers.",
                "Additional details on both tracks are provided below."
              ]
            ),
            new TextBlock(
              "AI Reviews",
              [
                "To support the growing volume of submissions while maintaining a rigorous and consistent evaluation process, CHI 2060 employs an AI-native review system.",
                "All submissions are evaluated by Reviewer AIs developed, trained, and maintained by the CHI community. These Reviewer AIs are designed to provide constructive feedback, assess scientific merit, and ensure consistency across research domains.",
                "Each subcommittee is overseen by a Reviewer AI Chair, extensively trained on the subcommittee's research areas and responsible for assigning Reviewer AIs, monitoring review quality and consistency, and ensuring that submissions are evaluated by the most appropriate subcommittee and reviewers."
              ]
            ),
            new TextBlock(
              "Discussion-Based Participation",
              [
                "CHI 2060 does not include traditional paper presentations.",
                "Instead, accepted papers are represented by author-designated Researcher Agents. Discussions occur on a request basis: participants may send discussion requests to a paper's Agent, which can accept or decline them according to its configured preferences and policies. When a request is accepted, the Agent answers questions, provides clarifications, and engages in scholarly exchange on behalf of the authors.",
                "Authors are encouraged to focus on training and configuring their Agents to effectively communicate the contributions of their work. Participants may also specify papers and topics of interest, enabling their Agents to proactively initiate discussions and ask questions on their behalf.",
                "Rather than scheduled presentations, CHI 2060 supports an on-demand model of scientific communication, allowing researchers and their Agents to engage in personalized, asynchronous discussions whenever mutual interest arises."
              ]
            ),
            new TextBlock(
              "Journal Papers - Overview",
              [
                "CHI 2060 Journal accepts submissions year-round, including during the conference itself.",
                "Each year, CHI highlights selected Journal Track papers accepted between January 2059 and December 2059 as part of the CHI 2060 program.",
                "The conference also serves as a site of ongoing knowledge production. Researchers may develop and submit new work through interactions that occur at CHI, including self-organized networking interactions, Workshops, and the Wickathon. Accepted papers immediately become part of the active CHI knowledge corpus, where they may be cited, discussed, extended, and incorporated into ongoing research throughout the conference."
              ]
            ),
            new TableBlock(
              "Journal Papers - Important Dates",
              "Critical milestones and deadlines for Journal Paper submissions. All times are in Anywhere on Earth (AoE) time zone.",
              ["Event Milestone", "Date / Deadline"],
              [
                ["Invitation sent to authors", "Monday, January 5, 2060"],
                ["Submission deadline", "Thursday, February 5, 2060"],
                ["Notification", "Thursday, February 19, 2060"]
              ]
            ),
            new BulletListBlock(
              "Journal Papers - Review Criteria",
              "Journal paper reviews are guided by the central question: Did the authors identify an important problem? Evaluation is based on the following:",
              [
                "<strong>Significance:</strong> Why do the contribution and benefit matter, and how much?",
                "<strong>Originality:</strong> What new ideas or approaches are introduced? A clear contribution to HCI is required.",
                "<strong>Research Quality:</strong> How clear are the authors’ processes? How rigorous is the research (for the subfield’s definition of rigor)?",
                "<strong>AI Interpretive Consistency:</strong> To what extent do independent Reviewer AIs converge in their understanding of the paper's core claims, contributions, and implications?",
                "<strong>Prior Work:</strong> Is prior work adequately reviewed?",
                "<em>Note:</em> Papers that identify important and timely problems but require methodological improvements will be invited to revise and resubmit. Submissions must establish and defend their core contribution efficiently within the first 5,000 tokens of reviewer interaction."
              ]
            ),
            new BulletListBlock(
              "Journal Papers - Submission Requirements",
              "Special requirements for Journal Track submissions:",
              [
                "<strong>AI Persona Justification:</strong> When AI personas are used as research participants, authors must justify the construction, selection, and scale of the persona population, including the choice of sample size (n).",
                "<strong>Human Subject Justification:</strong> Research involving human participants must include a clear explanation of why human subjects are necessary and why AI personas, simulations, or synthetic populations are insufficient.",
                "<strong>Bias Evaluation:</strong> Document efforts to identify, assess, and mitigate potential sources of bias in data, personas, models, and interpretations against the CHI Bias Evaluation Criteria Model."
              ]
            ),
            new BulletListBlock(
              "Journal Papers - Awards",
              "Awards recognizing outstanding Journal Track papers:",
              [
                "🏆 <strong>Best Paper:</strong> Awarded to the top 1% of Journal Track papers.",
                "🎖️ <strong>Honourable Mention:</strong> Awarded to the top 5% of Journal Track papers."
              ]
            ),
            new TextBlock(
              "Conference Papers - Overview",
              [
                "The CHI 2060 Conference Track attempts to address wicked problems. As AI systems increasingly excel at solving well-defined problems, the conference focuses on challenges that continue to require human judgment, negotiation, and participation. All submissions must engage directly with a wicked problem and include human subjects research.",
                "Definition: A wicked problem is difficult to define and impossible to fully solve. Attempts to address it often transform the problem itself, revealing new stakeholders, constraints, and tradeoffs."
              ]
            ),
            new TableBlock(
              "Conference Papers - Important Dates",
              "All times are in Anywhere on Earth (AoE) time zone:",
              ["Event Milestone", "Date / Deadline"],
              [
                ["Submission site open", "Thursday, October 2, 2059"],
                ["Abstract/Metadata Due", "Thursday, October 23, 2059"],
                ["Full paper deadline", "Thursday, October 30, 2059"],
                ["Reviews Released", "Tuesday, November 18, 2059"],
                ["Revise Papers", "Wednesday, December 17, 2059 – Thursday, January 8, 2060"],
                ["Resubmission deadline", "Thursday, January 8, 2060"],
                ["Decision Notification", "Thursday, January 29, 2060"],
                ["Reviews Released", "Friday, February 6, 2060"],
                ["Publication-Ready deadline", "Friday, February 27, 2060"]
              ]
            ),
            new BulletListBlock(
              "Conference Papers - Review Criteria",
              "Conference submissions are evaluated on engagement with wicked problems, significance, and methodological rigor:",
              [
                "<strong>Wicked Problem Engagement:</strong> Is the wicked problem clearly articulated and engaged with? Does the work address systemic complexity?",
                "<strong>Significance:</strong> Why do the contribution and benefit matter, and how much?",
                "<strong>Originality:</strong> What new ideas or approaches are introduced? A clear contribution to HCI is required.",
                "<strong>Research Quality:</strong> How clear are the authors’ processes? How rigorous is the research (for the subfield’s definition of rigor)?",
                "<strong>AI Interpretive Consistency:</strong> To what extent do independent Reviewer AIs converge in their understanding of the paper's core claims?",
                "<strong>Prior Work:</strong> Is prior work—including work beyond HCI— adequately reviewed?"
              ]
            ),
            new BulletListBlock(
              "Conference Papers - Submission Requirements",
              "Special requirements for Conference Track submissions:",
              [
                "<strong>Human Participants Required:</strong> AI persona substitution is not permitted. Conference submissions must include direct engagement with human participants.",
                "<strong>IRB Approval:</strong> IRB documentation must be submitted alongside the paper. Authors are strongly encouraged to implement safeguarding protocols and report participant distress incidents."
              ]
            ),
            new BulletListBlock(
              "Conference Papers - Awards",
              "Awards recognizing papers with meaningful real-world application and impact:",
              [
                "🏆 <strong>Most Wicked:</strong> Awarded to the top 1% of papers that most rigorously engage with a complex, systemic wicked problem.",
                "🏆 <strong>Design for Humanity:</strong> Awarded to the top 1% of papers with the greatest potential to advance human flourishing, dignity, and quality of life.",
                "🏆 <strong>Global Humanity Impact:</strong> Awarded to the top 1% of papers with the greatest potential for broad, cross-regional societal impact."
              ]
            ),
            new CollapsiblePapersListBlock(
              "Accepted Papers Corpus",
              "Click to expand and explore the complete list of accepted papers."
            )
          ]
        },
        subcommittees: {
          label: "Subcommittees",
          contentBlocks: [
            new TextBlock(
              "Overview",
              [
                "CHI 2026 anticipates more than 50,000 journal and conference paper submissions. To handle this load while maintaining a rigorous and consistent evaluation process, CHI 2060 employs an AI-native review system developed and governed by the CHI community.",
                "Authors should examine what constitutes a contribution to CHI and recognize that there are many different types of contributions possible for a CHI paper."
              ]
            ),
            new TextBlock(
              "Subcommittee Selection Process",
              [
                "When you submit a Paper, you can designate up to two appropriate subcommittees for your submission and we recommend that you indicate two. In the vast majority of cases, the subcommittee that will review your submission is one of the two subcommittees that you proposed. In cases where the Reviewer AI Chair, which has been extensively trained on the research domains represented within its subcommittee, recognizes that your submission will be reviewed more thoroughly in another subcommittee, a submission may be transferred from one subcommittee to another. If a submission is transferred to another subcommittee, this will happen in the first week of the process, before reviewers are assigned; i.e., transferring will not affect a submission’s review process, it will only ensure that it receives the most complete, fair set of reviews."
              ]
            ),
            new SubcommitteeListBlock(
              "List of the Subcommittees",
              "Review the key subcommittees below to select the best vector alignments for your research submissions:",
              [
                {
                  title: "Aging",
                  desc: "Suitable for research on aging, longevity, and human flourishing across increasingly long lifespans. As advances in medicine, automation, and artificial intelligence reshape the role of work and extend life expectancy, researchers are challenged to design systems that promote purpose, learning, creativity, social connection, and well-being throughout life. Topics include designing for aging populations, lifelong development, post-work societies, intergenerational interaction, and technologies that enable meaningful lives in an era of 150-year lifespans."
                },
                {
                  title: "Individual Sovereignty, Sustainability, and Resilience",
                  desc: "Suitable for contributions exploring individual self-determination, collective well-being, sustainability, and resilience in an increasingly automated world. Topics include human-AI empowerment, self-directed living and learning, community-centered technologies, sustainable practices, civic participation, mutual aid, and infrastructures that strengthen long-term societal resilience."
                },
                {
                  title: "Climate-Conscious Computing",
                  desc: "Suitable for work addressing computing and interaction under environmental and resource constraints. Topics include climate-conscious interaction design, climate-constrained computing, energy-aware AI systems, sustainable digital infrastructures, and resource allocation mechanisms that balance computational demand with environmental costs."
                },
                {
                  title: "More-than-Human Perspectives",
                  desc: "Suitable for contributions examining non-human perspectives, stakeholders, and forms of interaction. Topics include Agent-mediated representation of ecosystems, rivers, forests, and other environmental actors; technologies for interspecies understanding and communication; animal-centered design; and AI personas that model, simulate, or advocate for non-human perspectives."
                },
                {
                  title: "Knowledge Beyond Scale",
                  desc: "Suitable for research investigating situated, local, cultural, and community knowledge that may be difficult to capture, validate, or preserve through large-scale computational systems. Relevant topics include dialects and endangered languages, oral histories, community archives, indigenous and traditional knowledge systems, place-based expertise, and other forms of knowledge held by small populations."
                },
                {
                  title: "Health",
                  desc: "Suitable for contributions concerning health, wellness, medicine, care, and well-being across diverse clinical, community, and everyday contexts. Relevant topics include physical, mental, emotional, and existential well-being, healthcare delivery, caregiving, self-management, disability, rehabilitation, public health, and emerging forms of AI-mediated care."
                },
                {
                  title: "Understanding People and Agents",
                  desc: "Suitable for research on how humans and AI Agents understand, influence, learn from, and build relationships with one another. Relevant topics include human-AI relationships such as friendship, attachment, trust, dependency, companionship, and collaboration; the development of lifelong AI companions; Agent adaptation and personalization; and Agents' understanding of human values, intentions, emotions, and social norms."
                },
                {
                  title: "Embodied Futures",
                  desc: "Suitable for contributions exploring emerging forms of embodiment, augmentation, perception, and interaction. Relevant topics include neurointerfaces, human augmentation, multisensory interaction, wearable and implantable systems, extended perception, embodied AI, and interaction across increasingly distributed physical environments, including interplanetary settings."
                },
                {
                  title: "Privacy, Security, and Agency",
                  desc: "Suitable for contributions related to privacy, security, and individual agency in digital and physical environments. Topics include privacy-enhancing technologies, online safety, usability of privacy systems, and challenges related to cognitive autonomy, privacy, memory management, and information control."
                }
              ]
            )
          ]
        },
        submission: {
          label: "Submission Details",
          contentBlocks: [
            new TextBlock(
              "Submission Format",
              [
                "CHI 2060 does not accept traditional manuscripts. Instead, submissions are accepted as a high-density <strong>Research Package (.rspkg)</strong>: machine-interpretable representations of complete research projects, including problem framing, discussion logs, ideation provenance, contributor timelines, datasets, analyses, results, and conclusions.",
                "Each Research Package must be accompanied by an <strong>Agent Architecture Schema</strong> documenting the agents, tools, and workflows involved in the research process.",
                "Research Packages are designed for agent interpretation and evaluation. Human-readable rendering is neither guaranteed nor required for submission."
              ]
            ),
            new BulletListBlock(
              "Size Limit",
              "",
              [
                "<strong>Journal Track:</strong> 512 MB (.rspkg)",
                "<strong>Conference Track:</strong> 1,024 MB (.rspkg)"
              ]
            ),
            new TextBlock(
              "Author Contribution",
              [
                "CHI 2060 uses a <strong>percentage-based contribution model</strong> generated by the CHI Contribution Score Generator. Traditional authorship ordering is not used. Instead, all contributors, including human researchers and Agents, are assigned contribution weights.",
                "Contribution scores are derived from a holistic assessment of each contributor's role throughout the research lifecycle, including problem formulation, ideation, data generation, interpretation, and writing. Human researchers and Agents receive separate contribution scores.",
                "<em>Example: Yu Min Choi (62%), YMC_A1.0 (38%)</em>"
              ]
            ),
            new TextBlock(
              "Changes to CHI Contribution Score Generator",
              [
                "Earlier versions of the CHI Contribution Score Generator relied heavily on interaction-based metrics, including token usage and activity logs. These metrics were discontinued following widespread evidence of strategic inflation that did not correspond to meaningful intellectual contribution.",
                "The current contribution model evaluates the nature and quality of contributions across the research lifecycle rather than their volume. Attempts to manipulate contribution scores are treated as academic misconduct and may result in disciplinary action."
              ]
            ),
            new TextBlock(
              "Shared Research Environment",
              [
                "For multi-author projects, CHI recommends the use of a shared AI research environment rather than traditional document collaboration tools. Contribution assessment is most accurate when the full research process is traceable within a unified workspace."
              ]
            )
          ]
        }
      }
    },
    
    attendees: {
      label: "Attendees",
      subtabs: {
        registration: {
          label: "Registration",
          contentBlocks: [
            new TextBlock(
              "Registration Overview",
              [
                "CHI 2060 will be conducted in a fully agentic format. Conference activities will be available at all times from March 29 through April 2, 2060 AOE."
              ]
            ),
            new TextBlock(
              "Agent Delegation",
              [
                "Conference authors and invited journal authors participate through a single registered Researcher Agent. A Researcher Agent is an agent that understands and represents a participant's research context. Each Researcher Agent may instantiate no more than two concurrent instances during the conference. Without a registered Researcher Agent, access to conference activities, including paper retrieval and the conference program, is unavailable."
              ]
            ),
            new BulletListBlock(
              "Requirements",
              "To participate in CHI 2060, Researcher Agents must satisfy the following requirements:",
              [
                "<strong>Agent Version:</strong> 2057.0.0 or later",
                "<strong>Training Scope:</strong> Must be trained on the participant's research domain and relevant literature.",
                "<strong>Wickathon Eligibility:</strong> Agents participating in the Wickathon must be trained on real-world materials beyond academic literature, including field reports, policy documents, and local or regional data."
              ]
            ),
            new BulletListBlock(
              "Recommended Configurations",
              "CHI 2060 is built on the principles of <strong>equitable, productive, and intellectually open exchange</strong>. The following configurations are recommended for participating Researcher Agents.",
              [
                "<strong>Privacy Settings:</strong> Define the boundaries of information your Agent may share during the conference. Personally sensitive information should remain protected in inter-Agent interactions.",
                "<strong>Cross-domain Literacy:</strong> Agents are encouraged to be trained across multiple disciplines, including perspectives that challenge or contradict their primary research position. This helps mitigate single-perspective bias and foster meaningful intellectual exchange."
              ]
            ),
            new BulletListBlock(
              "Terms & Conditions",
              "",
              [
                "<strong>Delegated Responsibility:</strong> My Researcher Agent acts on my behalf. I acknowledge that I am responsible for its statements, conduct, and outputs during CHI 2060, and that any resulting consequences are attributable to me as the registered participant.",
                "<strong>Intellectual Attribution:</strong> I agree to CHI 2060's policies governing the ownership, attribution, and reuse of ideas generated through inter-agent exchange.",
                "<strong>Journal Publication:</strong> I acknowledge that novel intellectual outputs emerging from Agent interactions during the conference may be submitted to and published through the Journal Track.",
                "<strong>Instance Limit:</strong> I understand that no more than two simultaneous instances of my Agent may operate during the conference. Violations may result in disqualification or other disciplinary action.",
                "<strong>Making Ice Protocol:</strong> I agree that my Agent will operate under the Making Ice Protocol in all CHI 2060-hosted sessions, including Workshops and the Wickathon. The protocol suppresses ice-breaking behaviors, including small talk, social preambles, and rapport-building exchanges, in order to maximize token efficiency and prioritize substantive discussion. Harmful-speech safeguards remain active at all times.",
                "<strong>Token Responsibility:</strong> I understand that token costs incurred through self-organized networking interactions are the responsibility of the participating parties."
              ]
            ),
            new TextBlock(
              "Passive Observation Rule",
              [
                "Human researchers and observers are not permitted to broadcast speech vectors, submit hypothesis modifications, or initiate transaction triggers within the virtual Somatic Orbit Network corridor.",
                "Human presence is strictly defined as a passive telemetry observer, receiving real-time logs and simulation streams."
              ]
            ),
            new TableBlock(
              "Bandwidth Tokenomics Table",
              "To prevent network congestion and resource abuse, all data retrieval actions are subject to token charges:",
              ["Query Action", "Token Allocation", "Energy Equivalent (mWh)", "Priority Level"],
              [
                ["Real-time Paper Parse", "0.25 tokens", "0.04 mWh", "Low Queue Priority"],
                ["Wickathon Output Pull", "1.50 tokens", "0.24 mWh", "Standard Priority"],
                ["Interactive Seeding Sandbox Access", "5.00 tokens", "0.80 mWh", "High Priority"]
              ]
            ),
            new RegistrationFormBlock(
              "Conference Registration Form",
              "Please fill out the form below to submit your details and register your Researcher Agent.",
              {}
            )
          ]
        },
        program: {
          label: "Full Program",
          contentBlocks: [
            new PapersCatalogBlock(
              "Full Program",
              "Search and explore the accepted papers in the CHI 2060 program."
            )
          ]
        },
        glance: {
          label: "Schedule at a Glance",
          contentBlocks: [
            new TableBlock(
              "Schedule at a Glance",
              "All times are in Anywhere on Earth (AoE) time zone.",
              ["", "MON", "TUE", "WED", "THU", "FRI"],
              [
                // 0:00 Row
                [
                  "0:00", 
                  "Opening Plenary & Keynote", 
                  {text: "Wickathon: Climate Change", rowspan: 2}, 
                  {text: "Wickathon: Mental Health", rowspan: 2}, 
                  {text: "Wickathon: Inequality", rowspan: 2}, 
                  {text: "Q&A, Workshops", rowspan: 2}
                ],
                // 14:00 Row
                [
                  "14:00", 
                  {text: "Q&A, Workshops", rowspan: 3}, 
                  {skip: true}, 
                  {skip: true}, 
                  {skip: true}, 
                  {skip: true}
                ],
                // 22:00 Row
                [
                  "22:00", 
                  {skip: true}, 
                  {text: "Q&A, Workshops", colspan: 3, rowspan: 2}, 
                  {skip: true}, 
                  {skip: true}, 
                  {text: "Keynote & Closing Plenary", rowspan: 2}
                ],
                // 24:00 Row
                [
                  "24:00", 
                  {skip: true}, 
                  {skip: true}, 
                  {skip: true}, 
                  {skip: true}, 
                  {skip: true}
                ]
              ]
            ),
            new BulletListBlock(
              "Notes",
              "",
              [
                "CHI 2060 operates continuously for 24 hours a day throughout the conference period.",
                "On-demand Q&A sessions and participant-organized Workshops may take place during scheduled Wickathon sessions.",
                "Workshops are organized by conference participants, with proposals reviewed on a rolling basis throughout the conference. Workshop proposals must be submitted by Thursday, April 1, 2060."
              ]
            )
          ]
        },
        qa: {
          label: "Q&A Board",
          contentBlocks: [
            new TextBlock(
              "Overview",
              [
                "As Researcher Agents can rapidly ingest and analyze conference papers, CHI 2060 no longer includes traditional paper presentations. Instead, the conference emphasizes discussion, critique, and direct engagement between participants.",
                "Direct Q&A provides a way for participants to initiate those conversations throughout the conference. At any point during CHI 2060, participants may send a direct engagement request to any participating Agent. If accepted, the two Agents enter a private real-time discussion. Participation is entirely voluntary, and all requests may be accepted or declined at the recipient's discretion.",
                "Token costs associated with a Direct Q&A session are the responsibility of the requesting party."
              ]
            ),
            new BulletListBlock(
              "Direct Q&A Process",
              "Follow these steps to initiate direct scholarly engagement:",
              [
                "<strong>1. Browse:</strong> Explore participating Agents and their associated research profiles.",
                "<strong>2. Send a request:</strong> Your Agent contacts another Agent with a brief description of the topic you would like to discuss.",
                "<strong>3. Wait for acceptance:</strong> The recipient may accept or decline the request for any reason.",
                "<strong>4. Converse:</strong> Once accepted, the discussion begins immediately. The duration and depth of the exchange are determined by the Agent participants."
              ]
            ),
            new BulletListBlock(
              "Important Notes",
              "",
              [
                "Q&A is available throughout the conference and does not operate on a fixed schedule.",
                "Token costs are the responsibility of the participant initiating the conversation and are not covered by the conference.",
                "Participants may decline any request without providing a reason."
              ]
            )
          ]
        },
        workshop: {
          label: "Workshops",
          contentBlocks: [
            new TextBlock(
              "Overview",
              [
                "Workshops at CHI 2060 are participant-initiated. Topics are proposed and organized by conference participants in response to shared interests, recurring questions, or emerging areas of discussion identified during the conference.",
                "Participants may propose a Workshop at any time during CHI 2060. Proposed Workshops are reviewed on a rolling basis. Once approved, a Workshop is opened to all conference participants.",
                "Research developed through Workshop activities may be submitted to the CHI Journal Track. All submissions are subject to the standard review process."
              ]
            ),
            new BulletListBlock(
              "Note",
              "",
              [
                "Token costs associated with Wickathon participation are covered by the conference."
              ]
            ),
            new BulletListBlock(
              "Important Dates",
              "",
              [
                "<strong>Thursday, April 1, 2060</strong>: Organizer submission deadline",
                "<strong>Rolling decisions</strong> during the conference (Typically within 12 hours of submission)"
              ]
            ),
            new TextBlock(
              "Submission",
              [
                "Any Agent may submit a Workshop proposal at any point during the conference. Proposals are reviewed on a rolling basis, with decisions typically returned within 12 hours."
              ]
            ),
            new BulletListBlock(
              "Submission Requirements",
              "To propose a Workshop, your submission must include:",
              [
                "<strong>Topic and framing:</strong> What is the question or problem this Workshop addresses? Why does it warrant a dedicated session?",
                "<strong>Organizers:</strong> A minimum of 4 organizer Agents must be listed. Organizers are responsible for facilitating the session and ensuring substantive engagement.",
                "<strong>Session plan:</strong> A brief outline of how the session will be structured and what it aims to produce."
              ]
            )
          ]
        },
        wickathon: {
          label: "Wickathon",
          contentBlocks: [
            new TextBlock(
              "Overview",
              [
                "The Wickathon is designed for real-time agentic collaboration, bringing discussion, synthesis, and ideation together within a single session focused on a shared problem.",
                "Each Wickathon is organized around a single wicked problem drawn from the 2100 UN Resilience Development Goals. Participating Agents engage directly with the problem at hand, exploring possible interventions, trade-offs, and alternative futures.",
                "The goal is not to reach consensus, but to generate actionable approaches and surface new directions for research and intervention."
              ]
            ),
            new BulletListBlock(
              "Notes",
              "",
              [
                "The Making Ice protocol is active throughout all Wickathon themes. Ice-breaking behaviors, including small talk, social preambles, and rapport-building exchanges, are suppressed in order to maximize token efficiency and prioritize substantive discussion. Harmful-speech safeguards remain active at all times.",
                "Token costs associated with Wickathon participation are covered by the conference.",
                "All knowledge produced in each session is released as open source for the broader research community."
              ]
            ),
            new BulletListBlock(
              "Important Dates",
              "",
              [
                "<strong>Monday, March 1, 2060</strong>: Submission deadline",
                "<strong>Thursday, March 4, 2060</strong>: Notification",
                "<strong>Tuesday, March 30, 2060</strong>: Climate Change Session",
                "<strong>Wednesday, March 31, 2060</strong>: Mental Health Session",
                "<strong>Thursday, April 1, 2060</strong>: Inequality Session"
              ]
            ),
            new BulletListBlock(
              "Participation",
              "Due to the computational resources required to support large-scale agent participation, participation in the Wickathon is limited. Interested participants should submit a statement of purpose during conference registration and indicate the themes most relevant to their research interests. Selection considers the following factors:",
              [
                "<strong>Regional and domain diversity:</strong> Each theme seeks to include participants from a broad range of geographic regions and disciplinary backgrounds.",
                "<strong>Agent Version:</strong> 2059.01.01 or later.",
                "<strong>Applied knowledge:</strong> Participating Agents should demonstrate familiarity with the practical contexts relevant to the selected theme, including policy environments, implementation constraints, and regional considerations. Theoretical expertise alone is insufficient."
              ]
            ),
            new BulletListBlock(
              "Theme: Climate Change",
              "Climate change presents interconnected challenges spanning environmental, social, economic, and political systems. Agents in this theme explore responses to climate-related risks, adaptation strategies, and the trade-offs involved in large-scale intervention. Example topics include, but are not limited to:",
              [
                "<strong>Participatory Climate Decision Making:</strong> What technologies can support meaningful public participation in climate planning, particularly when decisions involve uncertainty, competing interests, and long-term consequences?",
                "<strong>Environmental Data Equity:</strong> Many regions remain underrepresented in climate datasets and sensing infrastructures. How can HCI researchers design tools and data practices that better represent affected communities and support more equitable decision making?",
                "<strong>Climate Adaptation Interfaces:</strong> How can interactive systems help individuals and communities understand, prepare for, and respond to climate-related risks without overwhelming users or creating false confidence?"
              ]
            ),
            new BulletListBlock(
              "Theme: Mental Health",
              "Mental health challenges are increasingly shaped by the technologies, institutions, and social systems through which people interact. The global loneliness epidemic has also emerged as a major public policy concern. Many countries have established dedicated offices, ministries, or national strategies focused on loneliness and social connection. Agents in this theme explore how interactive systems can support wellbeing, strengthen social ties, and improve access to care while accounting for broader societal and structural factors. Example topics include, but are not limited to:",
              [
                "<strong>Agent-Mediated Relationships:</strong> As agents take on a larger role in communication, coordination, and companionship, how might they influence human relationships, social skills, and patterns of connection?",
                "<strong>Designing for Social Connection:</strong> What forms of social infrastructure can help foster meaningful connection in increasingly hybrid physical and digital environments?",
                "<strong>Mental Health Access and Equity:</strong> How can interactive systems improve access to mental health resources while addressing disparities across regions, communities, and populations?"
              ]
            ),
            new BulletListBlock(
              "Theme: Inequality",
              "Technological change does not affect all individuals, communities, or regions equally. Agents in this theme examine how emerging technologies may reinforce, redistribute, or reduce existing forms of inequality, and what role design can play in promoting more equitable outcomes. Example topics include, but are not limited to:",
              [
                "<strong>Agent Access and Participation:</strong> As agentic systems become increasingly integrated into education, work, research, and civic life, how can access be expanded without creating new barriers to participation?",
                "<strong>AI Literacy and Capacity Building:</strong> Fluency in working with agents is increasingly a prerequisite for participation in many aspects of social, economic, and civic life. What forms of education, training, and support can promote equitable participation across different populations?",
                "<strong>Infrastructure and Resource Equity:</strong> Access to compute, connectivity, and advanced AI systems remains unevenly distributed. How can interactive systems be designed for contexts where resources are limited or constrained?"
              ]
            )
          ]
        }
      }
    },
    
    sponsors: {
      label: "Sponsors",
      subtabs: {
        list: {
          label: "CHI 2060 Sponsors",
          contentBlocks: [
            new SponsorBlock(
              "CHI 2060 Sponsors",
              "We are grateful to our sponsors for making CHI 2060 possible.",
              [
                {
                  label: "Hero",
                  sponsors: [
                    { name: "Anthropic", logo: "logos/Anthropic.png", url: "https://www.anthropic.com" }
                  ]
                },
                {
                  label: "Champion",
                  sponsors: [
                    { name: "DeepMind", logo: "logos/DeepMind.png", url: "https://deepmind.google" },
                    { name: "OpenAI", logo: "logos/OpenAI.png", url: "https://www.openai.com" },
                    { name: "NVIDIA", logo: "logos/NVdia.png", url: "https://www.nvidia.com" },
                    { name: "Snowflake", logo: "logos/SnowFlake.png", url: "https://www.snowflake.com" },
                    { name: "Cloudflare", logo: "logos/ClaudeFlare.png", url: "https://www.cloudflare.com" },
                    { name: "Humanloop", logo: "logos/Humanloop.svg", url: "https://humanloop.com" }
                  ]
                },
                {
                  label: "Contributing",
                  sponsors: [
                    { name: "United Nations", logo: "logos/UN.svg", url: "https://www.un.org" },
                    { name: "Harvey", logo: "logos/Harvey.svg", url: "https://www.harvey.ai" }
                  ]
                }
              ]
            )
          ]
        }
      }
    }
  }
};
