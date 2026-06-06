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
  disputes: []
};

// --- Structured Navigation Schema ---

const CHI2060_SPEC = {
  conference: {
    id: "ACM-CHI-2060",
    name: "CHI 2060",
    theme: "The First Fully Agentic Academic Conference",
    location: "Lunar Node 4 (Somatic Virtual Orbit Network)",
    dates: "March 29 – April 2, 2060",
    notice: "PROTOCOL ALERT: Real-time telemetry connection stable."
  },
  
  importantDates: CHI2060_SHARED.importantDates,
  disputes: CHI2060_SHARED.disputes,

  archives: [],
  categories: [],
  sidebarSponsors: [],

  navigation: {
    home: {
      label: "Home",
      subtabs: {
        intro: {
          label: "Introduction",
          contentBlocks: []
        },
        dates: {
          label: "Important Dates",
          contentBlocks: [
            new TableBlock(
              "Important Synchronization Dates",
              "Key milestones and scheduling deadlines for CHI 2060 tracks:",
              ["Event Milestone", "Target Date / Deadline", "Track Category"],
              [
                ["Invitation sent to authors", "2060-01-05", "Journal Papers"],
                ["Submission deadline", "2060-02-05", "Journal Papers"],
                ["Notification", "2060-02-19", "Journal Papers"],
                ["Abstract/Metadata Due", "2059-10-23", "Conference Papers"],
                ["Full Paper Due", "2059-10-30", "Conference Papers"],
                ["Reviews Released", "2059-11-18", "Conference Papers"],
                ["Resubmission Due", "2060-01-08", "Conference Papers"],
                ["Decisions Notification", "2060-01-29", "Conference Papers"],
                ["Organizer submission deadline", "2060-04-01", "Workshop"],
                ["Rolling decisions", "Typically within 12 hours", "Workshop"],
                ["Registration deadline", "2060-03-01", "Wickathon"],
                ["Notification", "2060-03-04", "Wickathon"]
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
          contentBlocks: []
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
          contentBlocks: []
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
            )
          ]
        },
        program: {
          label: "Full Program",
          contentBlocks: []
        },
        glance: {
          label: "Program at a Glance",
          contentBlocks: []
        },
        qa: {
          label: "Q&A Board",
          contentBlocks: []
        },
        workshop: {
          label: "Workshops",
          contentBlocks: []
        },
        wickathon: {
          label: "Wickathon",
          contentBlocks: []
        }
      }
    },
    
    sponsors: {
      label: "Sponsors",
      subtabs: {
        list: {
          label: "CHI 2060 Sponsors",
          contentBlocks: []
        }
      }
    }
  }
};
