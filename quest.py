import random
import tkinter as tk
from tkinter import ttk


class AdventureApp:
    def __init__(self, root):
        self.root = root
        root.title("Apple Quest")
        root.geometry("860x620")
        root.resizable(False, False)
        root.configure(bg="#121B28")

        self.style = ttk.Style(root)
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#121B28")
        self.style.configure("Card.TFrame", background="#1F2F43", relief="flat")
        self.style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"), foreground="#F8D36B", background="#121B28")
        self.style.configure("Sub.TLabel", font=("Segoe UI", 12), foreground="#DDE7F0", background="#121B28")
        self.style.configure("Body.TLabel", font=("Segoe UI", 11), foreground="#EFF4FA", background="#1F2F43")
        self.style.configure("Small.TLabel", font=("Segoe UI", 10), foreground="#A6B7CE", background="#1F2F43")
        self.style.configure("TButton", font=("Segoe UI", 11, "bold"), foreground="#1F2F7F", background="#F8D36B")
        self.style.map("TButton", background=[("active", "#F4E29E")])

        self.name = "John"
        self.strength = 20
        self.health = 20
        self.apples = 0
        self.bonus_item = random.choice(["a magical sword", "15 gold coins", "a treasure map"])

        self.main_frame = ttk.Frame(root, style="TFrame", padding=18)
        self.main_frame.pack(fill="both", expand=True)

        self.header = ttk.Frame(self.main_frame, style="TFrame")
        self.header.pack(fill="x", pady=(0, 12))

        self.title_label = ttk.Label(self.header, text="Apple Quest", style="Title.TLabel")
        self.title_label.pack(anchor="w")

        self.subtitle_label = ttk.Label(
            self.header,
            text="A cozy forest adventure where every choice makes a difference.",
            style="Sub.TLabel",
        )
        self.subtitle_label.pack(anchor="w", pady=(4, 0))

        self.status_card = ttk.Frame(self.main_frame, style="Card.TFrame", padding=12)
        self.status_card.pack(fill="x", pady=(0, 12))

        self.strength_label = ttk.Label(self.status_card, text="Strength: 20", style="Small.TLabel")
        self.health_label = ttk.Label(self.status_card, text="Health: 20", style="Small.TLabel")
        self.apples_label = ttk.Label(self.status_card, text="Apples: 0", style="Small.TLabel")

        self.strength_label.grid(row=0, column=0, padx=10, pady=4, sticky="w")
        self.health_label.grid(row=0, column=1, padx=10, pady=4, sticky="w")
        self.apples_label.grid(row=0, column=2, padx=10, pady=4, sticky="w")

        self.story_card = ttk.Frame(self.main_frame, style="Card.TFrame", padding=14)
        self.story_card.pack(fill="both", expand=True)

        self.story_label = ttk.Label(
            self.story_card,
            text="",
            style="Body.TLabel",
            wraplength=800,
            justify="left",
        )
        self.story_label.pack(fill="both", expand=True)

        self.buttons_card = ttk.Frame(self.main_frame, style="Card.TFrame", padding=12)
        self.buttons_card.pack(fill="x", pady=(12, 0))

        self.choice_buttons = [ttk.Button(self.buttons_card) for _ in range(4)]
        for index, button in enumerate(self.choice_buttons):
            button.grid(row=index // 2, column=index % 2, padx=8, pady=8, sticky="ew")
        self.buttons_card.columnconfigure(0, weight=1)
        self.buttons_card.columnconfigure(1, weight=1)

        self.input_card = ttk.Frame(self.main_frame, style="Card.TFrame", padding=12)
        self.input_card.pack(fill="x", pady=(12, 0))

        self.name_prompt = ttk.Label(self.input_card, text="Your name:", style="Small.TLabel")
        self.name_entry = ttk.Entry(self.input_card, font=("Segoe UI", 11))
        self.start_button = ttk.Button(self.input_card, text="Begin Adventure", command=self.start_adventure)

        self.name_prompt.grid(row=0, column=0, padx=(0, 8), pady=4, sticky="w")
        self.name_entry.grid(row=0, column=1, padx=(0, 8), pady=4, sticky="ew")
        self.start_button.grid(row=0, column=2, pady=4)
        self.input_card.columnconfigure(1, weight=1)

        self.name_entry.insert(0, "John")
        self.show_intro()

    def update_status(self):
        self.strength_label.config(text=f"Strength: {self.strength}")
        self.health_label.config(text=f"Health: {self.health}")
        self.apples_label.config(text=f"Apples: {self.apples}")

    def set_story(self, text, options):
        self.story_label.config(text=text)
        for button in self.choice_buttons:
            button.grid_remove()

        for index, (label, callback) in enumerate(options):
            if index < len(self.choice_buttons):
                button = self.choice_buttons[index]
                button.config(text=label, command=callback)
                button.grid()

    def show_intro(self):
        self.set_story(
            "Welcome to Apple Quest!\n\nThe forest is alive with whispers, and your journey begins with a brave heart. Type your name and join the adventure as John, the young hero who must gather apples before winter arrives.",
            [("Begin", self.start_adventure)],
        )

    def start_adventure(self):
        name_text = self.name_entry.get().strip()
        if name_text:
            self.name = name_text
        self.name_entry.config(state="disabled")
        self.start_button.config(state="disabled")
        self.update_status()
        self.show_potions()

    def show_potions(self):
        self.set_story(
            f"Lovely to meet you, {self.name}! The winter is coming, and your family needs apple harvests. Choose a potion to start your journey.",
            [
                ("Warrior (+5 str, -5 hp)", lambda: self.choose_potion(5, -5, "Warrior Potion")),
                ("Woodcutter (+5 hp, -5 str)", lambda: self.choose_potion(-5, 5, "Woodcutter Potion")),
                ("Quiet Walker (-3 str, +3 hp)", lambda: self.choose_potion(-3, 3, "Quiet Walker Potion")),
            ],
        )

    def choose_potion(self, str_change, hp_change, potion_name):
        self.strength += str_change
        self.health += hp_change
        self.update_status()
        self.set_story(
            f"You drink the {potion_name}. A warm glow rushes through you, and the path ahead looks clearer.\n\nStrength: {self.strength} | Health: {self.health}\n\nYou step into the forest. Birds sing overhead, and suddenly a wild boar bursts from the underbrush!",
            [
                ("Fight", lambda: self.boar_scene("fight")),
                ("Run", lambda: self.boar_scene("run")),
                ("Hide", lambda: self.boar_scene("hide")),
            ],
        )

    def boar_scene(self, action):
        if action == "fight":
            if self.strength > 15:
                self.health -= 5
                result = "You stand your ground and the boar retreats deeper into the forest."
            else:
                self.health -= 10
                result = "The boar charges you hard — you escape, but you feel the sting of its tusks."
        elif action == "run":
            self.health -= 2
            result = "You dash away through fallen leaves and keep your apples safe."
        else:
            self.health -= 1
            result = "You melt into the shadows, and the boar passes by without seeing you."

        self.update_status()
        self.set_story(
            f"{result}\n\nThe forest light dims. Ahead, a tall apple tree waits with glowing fruit high above.",
            [
                ("Climb", lambda: self.tree_scene("climb")),
                ("Shake", lambda: self.tree_scene("shake")),
                ("Use the sword", lambda: self.tree_scene("sword")),
            ],
        )

    def tree_scene(self, choice):
        if choice == "climb":
            if self.strength > 15:
                self.health -= 2
                self.apples += 5
                result = "You climb carefully and gather ripe apples from the top."
            else:
                self.health -= 10
                result = "The branch breaks and you tumble down."
        elif choice == "shake":
            self.health -= 1
            self.apples += 3
            result = "The tree shakes free a nice bundle of apples."
        else:
            self.health -= 3
            self.apples += 4
            result = "A smart cut drops apples safely into your arms."

        self.update_status()
        self.set_story(
            f"{result}\n\nThrough the mist, you see a playful monkey perched on a branch, guarding a second cluster of apples.",
            [
                ("Approach", lambda: self.monkey_scene("talk")),
                ("Brave", lambda: self.monkey_scene("fight")),
                ("Avoid", lambda: self.monkey_scene("move")),
            ],
        )

    def monkey_scene(self, action):
        if action == "fight":
            if self.strength > 10:
                self.health -= 5
                self.apples += 5
                result = "You outwit the monkey and gain extra apples."
            else:
                self.health -= 10
                result = "The monkey proves too strong and you retreat."
        elif action == "talk":
            self.health -= 1
            self.apples += 3
            result = "The monkey shares fruit after you speak kindly."
        else:
            self.health -= 2
            result = "You slip by quietly and continue onward."

        self.update_status()
        self.set_story(
            f"{result}\n\nThe forest darkens, and a wise dweller blocks your path.",
            [
                ("Challenge", lambda: self.dweller_scene("fight")),
                ("Retreat", lambda: self.dweller_scene("run")),
                ("Speak", lambda: self.dweller_scene("talk")),
            ],
        )

    def dweller_scene(self, action):
        if action == "fight":
            if self.strength > 10:
                self.health -= 5
                result = "You meet the dweller bravely and earn his respect."
            else:
                self.health -= 10
                self.apples = max(0, self.apples - 3)
                result = "The dweller proves too strong and you lose some apples."
        elif action == "run":
            self.health -= 2
            self.apples = max(0, self.apples - 2)
            result = "You slip away safely, but some apples fall."
        else:
            self.health -= 1
            self.apples += 3
            result = "The dweller understands you and gives you apples."

        self.update_status()
        self.set_story(
            f"{result}\n\nA hidden path opens up — do you continue deeper or head home?",
            [
                ("Deeper", self.bird_choice),
                ("Home", self.conclude_game),
            ],
        )

    def bird_choice(self):
        self.set_story(
            "You reach a hidden grove where a mother bird protects a nest filled with sparkling apples. Choose your next step carefully.",
            [
                ("Fight", lambda: self.bird_scene("fight")),
                ("Run", lambda: self.bird_scene("run")),
                ("Speak gently", lambda: self.bird_scene("talk")),
            ],
        )

    def bird_scene(self, action):
        if action == "fight":
            if self.strength > 10:
                self.health -= 5
                self.apples += 5
                result = "You bravely fight and earn a handful of apples."
            else:
                self.health -= 10
                result = "The bird proves too strong and you retreat."
        elif action == "run":
            self.health -= 2
            self.apples = max(0, self.apples - 2)
            result = "You run away and keep most of your apples."
        else:
            self.health -= 1
            self.apples += 6
            result = "The bird warms to your kindness and gives you fruit."

        self.update_status()
        self.conclude_game(result)

    def conclude_game(self, final_result=""):
        if self.apples >= 10:
            ending = "Your family will survive winter — your adventure was a triumph!"
            title = "Hero of the Orchard"
        else:
            ending = "You return home safely, and your family still feels proud of your journey."
            title = "Journey Complete"

        self.title_label.config(text=title)
        self.set_story(
            f"{final_result}\n\nFinal apples: {self.apples}\nHealth: {self.health}\n\n{ending}",
            [("Play Again", self.reset_game)],
        )

    def reset_game(self):
        self.strength = 20
        self.health = 20
        self.apples = 0
        self.bonus_item = random.choice(["a magical sword", "15 gold coins", "a treasure map"])
        self.title_label.config(text="Apple Quest")
        self.name_entry.config(state="normal")
        self.start_button.config(state="normal")
        self.update_status()
        self.show_intro()


if __name__ == "__main__":
    root = tk.Tk()
    AdventureApp(root)
    root.mainloop()

