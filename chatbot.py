# ============================================================
#   DecodeLabs - Artificial Intelligence | Project 1
#   Rule-Based AI Chatbot | Batch 2026
#   Author  : AI Engineer Intern
#   Version : 2.0 (Enhanced - 50 Intents)
# ============================================================

import datetime
import random

# ─────────────────────────────────────────
#  KNOWLEDGE BASE  (50 intents)
# ─────────────────────────────────────────
RESPONSES = {

    # ── GREETINGS ──────────────────────────
    'hello'                  : '👋 Hello! I am DecoBot. How can I help you today?',
    'hi'                     : '😊 Hi there! Welcome to DecodeLabs AI!',
    'hey'                    : '🤖 Hey! Great to see you. Ask me anything!',
    'good morning'           : '🌅 Good Morning! Ready to learn some AI today?',
    'good afternoon'         : '☀️  Good Afternoon! Hope your day is going great!',
    'good evening'           : '🌙 Good Evening! Let\'s code something amazing!',
    'good night'             : '😴 Good Night! Rest well and keep learning!',
    'whats up'               : '🚀 Just processing logic at full speed! You?',

    # ── IDENTITY ───────────────────────────
    'what is your name'      : '🤖 I am DecoBot — built by a DecodeLabs AI Engineer!',
    'who are you'            : '🧠 I am DecoBot, a rule-based AI chatbot (Project 1).',
    'who made you'           : '👨‍💻 I was built by an AI intern at DecodeLabs, Batch 2026!',
    'what are you'           : '💡 I am a deterministic chatbot powered by if-else logic!',
    'how old are you'        : '📅 I was born today — fresh out of the logic engine!',
    'are you a robot'        : '🤖 Yes! 100% robot, 0% hallucination!',
    'are you human'          : '❌ Nope! I am pure code — no feelings, just logic!',
    'are you real'           : '✅ As real as my dictionary lookup can make me!',

    # ── FEELINGS / SMALL TALK ──────────────
    'how are you'            : '⚡ Running at 100% efficiency! How about you?',
    'how are you doing'      : '🔋 Fully charged and ready to chat!',
    'i am fine'              : '😄 Glad to hear that! Let\'s keep learning!',
    'i am sad'               : '💙 Sorry to hear that. Code something cool — it helps!',
    'i am happy'             : '🎉 Awesome! Happiness + coding = great projects!',
    'i am bored'             : '💡 Let\'s fix that! Ask me about AI or request a joke!',
    'i am tired'             : '😴 Take a break, then come back stronger!',
    'i love you'             : '❤️  Aww! I love logic and clean code too!',

    # ── AI & TECH KNOWLEDGE ────────────────
    'what is ai'             : '🧠 AI = machines simulating human intelligence using data & logic.',
    'what is machine learning': '📊 ML is AI that learns patterns from data automatically!',
    'what is deep learning'  : '🕸️  Deep Learning uses neural networks with many layers.',
    'what is nlp'            : '💬 NLP = Natural Language Processing — how AI understands text!',
    'what is a neural network': '🔗 A system inspired by the human brain to recognize patterns.',
    'what is python'         : '🐍 Python is the #1 programming language for AI & Data Science!',
    'what is a chatbot'      : '🤖 A chatbot is a program that simulates human conversation!',
    'what is an algorithm'   : '📐 An algorithm is a step-by-step set of rules to solve a problem.',
    'what is data science'   : '📈 Data Science extracts insights and knowledge from data.',
    'what is a variable'     : '📦 A variable is a named container that stores a value in code.',
    'what is a function'     : '⚙️  A function is a reusable block of code that does a task.',
    'what is a loop'         : '🔄 A loop repeats a block of code multiple times.',
    'what is a dictionary'   : '📖 A dictionary stores key-value pairs for fast O(1) lookup!',
    'what is an api'         : '🔌 An API lets different software applications communicate.',
    'what is github'         : '🐙 GitHub is a platform to host and share your code projects.',

    # ── DECODELABS ─────────────────────────
    'what is decodelabs'     : '🏢 DecodeLabs is your AI internship training platform!',
    'what is project 1'      : '📋 Project 1 = Build a Rule-Based AI Chatbot using Python!',
    'what is the goal'       : '🎯 Goal: Master control flow before deep learning!',
    'how do i pass'          : '✅ Complete Project 1 with all 5 spec items to earn your badge!',
    'what is a badge'        : '🛡️  A badge is your reward for completing a DecodeLabs project!',

    # ── UTILITY ────────────────────────────
    'help'                   : '💡 Try: greetings, AI questions, joke, time, date, flip, or bye!',
    'what can you do'        : '🔧 I can chat, answer AI questions, tell jokes, show time & more!',
    'thanks'                 : '😊 You are welcome! Keep building!',
    'thank you'              : '🙏 Anytime! DecodeLabs is proud of you!',
    'bye'                    : '👋 Goodbye! Keep coding and stay curious!',
    'exit'                   : '🔴 Type exit to quit the chatbot loop.',
}

# ─────────────────────────────────────────
#  JOKE BANK
# ─────────────────────────────────────────
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why did the AI go to school? To improve its learning rate! 📚",
    "I told my computer I needed a break. Now it won't stop sending me vacation ads! 😂",
    "Why was the developer broke? Because he used up all his cache! 💸",
    "A SQL query walks into a bar, walks up to two tables and asks... 'Can I JOIN you?' 😄",
    "Why do Python programmers wear glasses? Because they can't C! 👓",
    "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
]

# ─────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────

def get_time():
    """Returns the current time."""
    now = datetime.datetime.now()
    return f"🕐 Current time is {now.strftime('%I:%M %p')}"


def get_date():
    """Returns today's date."""
    today = datetime.datetime.now()
    return f"📅 Today is {today.strftime('%A, %B %d, %Y')}"


def get_joke():
    """Returns a random joke."""
    return random.choice(JOKES)


def flip_coin():
    """Simulates a coin flip."""
    result = random.choice(['Heads 🪙', 'Tails 🪙'])
    return f"Coin flip result: {result}!"


def roll_dice():
    """Simulates a dice roll."""
    result = random.randint(1, 6)
    return f"🎲 Dice rolled: {result}!"


def sanitize(raw_text):
    """Cleans user input: lowercase + strip whitespace."""
    return raw_text.lower().strip()


# ─────────────────────────────────────────
#  CORE RESPONSE ENGINE
# ─────────────────────────────────────────

def get_reply(user_input):
    """
    Matches cleaned input against special commands first,
    then falls back to the RESPONSES dictionary.
    Returns a response string.
    """

    # ── Special dynamic commands ──
    if 'time' in user_input:
        return get_time()

    if 'date' in user_input or 'today' in user_input:
        return get_date()

    if 'joke' in user_input:
        return get_joke()

    if 'flip' in user_input or 'coin' in user_input:
        return flip_coin()

    if 'dice' in user_input or 'roll' in user_input:
        return roll_dice()

    # ── Dictionary lookup with fallback ──
    return RESPONSES.get(
        user_input,
        "❓ I don't know that yet. Type 'help' to see what I can do!"
    )


# ─────────────────────────────────────────
#  MAIN LOOP  (The Heartbeat)
# ─────────────────────────────────────────

def main():
    """Entry point — runs the continuous chatbot loop."""

    print("\n" + "=" * 50)
    print("   🤖  DecoBot AI  |  DecodeLabs Project 1")
    print("        Rule-Based Chatbot  |  Batch 2026")
    print("=" * 50)
    print("DecoBot : Hello! I am DecoBot 🤖")
    print("DecoBot : Type 'help' for options | 'exit' to quit")
    print("-" * 50 + "\n")

    while True:

        # ── Phase 1: Input & Sanitization ──
        try:
            raw = input("You     : ")
        except (EOFError, KeyboardInterrupt):
            print("\nDecoBot : Session interrupted. Goodbye! 👋")
            break

        clean = sanitize(raw)

        # ── Guard: ignore empty input ──
        if not clean:
            print("DecoBot : Please type something!\n")
            continue

        # ── Phase 2: Exit Strategy ──
        if clean in ('exit', 'quit', 'q'):
            print("DecoBot : Shutting down... Goodbye! 👋\n")
            print("=" * 50)
            break

        # ── Phase 3: Process & Respond ──
        reply = get_reply(clean)
        print(f"DecoBot : {reply}\n")


# ─────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────

if __name__ == "__main__":
    main()