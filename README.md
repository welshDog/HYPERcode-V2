# 🌈 HyperCode

**A neurodivergent‑first programming language and IDE built for how our brains actually think.**

HyperCode is an experimental programming language and tooling ecosystem designed for ADHD, autistic, dyslexic, and otherwise neurodivergent minds — and for AI systems that will write and read code alongside us.

Instead of forcing people to bend to traditional language design, HyperCode flips it:
- **Minimal visual noise**
- **Plain-language flow**
- **Highly visual architecture and docs**
- **Future‑proof AI integration**

---

## ✨ Why HyperCode Exists

Programming languages are more than syntax — they’re an expression of *how minds think*.

Most mainstream languages were designed around neurotypical assumptions. HyperCode is different:

- 🧠 **Neurodivergent‑first design**  
  Built to reduce overwhelm: clear structure, fewer symbols, explicit intent.

- 🤝 **AI-native**  
  Designed from day one to collaborate with GPT‑4, Claude, Mistral, Ollama and future models — not bolted on later.

- 🧬 **Future-facing**  
  A research playground for where code meets quantum, molecular, and AI-native computing.

- 🌍 **Open, collaborative, and serious**  
  Proper CI/CD, tests, security policies, and docs — this is a real project, not just an experiment.

---

## 🧪 What HyperCode Can Do (Today)

HyperCode is early, but already supports:

- ✅ **Basic output**
print "Hello, World!";

text

- ✅ **Variables & arithmetic**
let x = 10 + 5 * 2; # 20
print x;

text

- ✅ **Single-line conditionals**
let age = 20;
if age >= 18 print "Adult";

text

### ⚠️ Experimental / In Progress

We’re actively improving:

- Multi‑line `if / else` blocks and `end`
- String concatenation and `str()` conversions
- More descriptive error messages with line info
- A small, friendly standard library

You can see a living snapshot of the language and roadmap in:

- `GETTING_STARTED.md`
- `ARCHITECTURE_VISUAL.md`
- `IMPLEMENTATION_PLAN.md`

---

## 🧱 Project Architecture (High-Level)

HyperCode is split into clear layers:

- **Core language (`hypercode_organized_v2/hypercode/`)**
- `Lexer` → turns source into tokens  
- `Parser` → builds an AST  
- `Interpreter` → executes the AST

- **CLI Interpreter (`hypercode_interpreter.py`)**
- Run `.hc` files from the command line  
- Debug and experimentation mode

- **Web IDE (`hypercode_web_ide.py` + `ide.html`)**
- Browser-based editor
- Sends code to the server, runs through the same interpreter, returns output

- **Tests & Docs**
- `tests/` — unit + integration tests
- `docs/` — architecture, getting started, API, and more

For a visual walkthrough, see `docs/ARCHITECTURE_VISUAL.md`.

---

## 🚀 Running HyperCode

### 1. Command-Line Interpreter

Run a `.hc` file:

python hypercode_interpreter.py test_hello.hc

text

Example `test_hello.hc`:

print "Hello from HyperCode!";

text

### 2. Web IDE

Start the web IDE:

python hypercode_web_ide.py

text

Then open:

http://localhost:8000

text

You’ll get a browser-based editor where you can write HyperCode and run it instantly.

---

## 🔐 Production-Grade Foundations

We’re not just hacking: we’re building this with serious engineering practices.

- ✅ **Security**
  - `SECURITY.md` – formal security policy and responsible disclosure
  - Dependabot configuration
  - Automated security scanning workflows

- ✅ **Testing**
  - Unit + integration tests
  - Coverage reporting via CI (`test-coverage.yml`)
  - 30‑day plan to reach 85%+ coverage

- ✅ **Documentation**
  - Visual architecture diagrams (`ARCHITECTURE_VISUAL.md`)
  - Neurodivergent‑friendly getting started guide (`GETTING_STARTED.md`)
  - Implementation roadmap (`IMPLEMENTATION_PLAN.md`)

---

## 🧭 Roadmap (Short Version)

**Phase 1 – Stabilize Core (Now)**  
- Document the *working subset* of the language  
- Improve error messages (line numbers, clearer messages)  
- Fix multi‑line control flow and string handling

**Phase 2 – Developer Experience (Next)**  
- Richer Web IDE experience  
- Inline error display and explanations  
- More examples and templates

**Phase 3 – AI & Advanced Features**  
- AI‑assisted coding patterns  
- Prompt + code testing harness  
- More backends / targets over time

Details live in `IMPLEMENTATION_PLAN.md`.

---

## 🤝 How to Get Involved

We’d love contributors — especially neurodivergent developers, educators, and tool builders.

### 1. Try the Language

- Clone the repo  
- Run the CLI or Web IDE  
- Write small programs, break things, take notes

### 2. File Issues

- 🐛 Bugs, confusing behavior
- 💡 Language/design suggestions
- 📚 Documentation gaps
- 🧠 Accessibility feedback

### 3. Contribute Code

Check:

- `CONTRIBUTING.md` – workflow and expectations  
- `IMPLEMENTATION_PLAN.md` – what we’re working on now  
- Good first issues (coming as the project opens up)

---

## 💬 How to Talk About HyperCode

> “HyperCode is a neurodivergent‑first programming language and IDE — minimal noise, highly visual, and built to collaborate with modern AI models. It’s resurrecting forgotten language ideas, aligning code with how our brains actually think, and shipping with real CI, tests, and security from day one.”

---

## ❤️ Credits & Community

HyperCode is an open, evolving project — a **living digital research paper** about what programming could look like when we design it for *all* minds and for AI collaboration.

If any of this resonates, you’re invited:

- Use it.
- Break it.
- Question it.
- Help shape what comes next.

---

## 📄 License

[Add your chosen license here – e.g. MIT, Apache 2.0, etc.]
