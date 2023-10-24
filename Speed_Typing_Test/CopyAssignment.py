import tkinter as tk
import ctypes
import random

ctypes.windll.shcore.SetProcessDpiAwareness(1)

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.setup_gui()
        self.handle_labels()

    def setup_gui(self):
        self.root.title('CopyAssignment - Typing Speed Test')
        self.root.geometry('1400x700')
        self.root.option_add("*Label.Font", "consolas 30")
        self.root.option_add("*Button.Font", "consolas 30")

    def handle_labels(self):
        # Text List
        random_selection = [
            'A random statement can inspire authors and help them start writing. It challenges the author to use their imagination because the sentences subject is utterly ambiguous. The random sentence may be creatively used in a variety of ways by writers. The statement is most frequently used to start a tale. Another choice is to include it into the narrative. The issue of using it to conclude a tale is far more challenging. In all of these scenarios, the writer is compelled to use their imagination because they have no idea what words will come out of the tool.',
            'Python Code aims to teach beginning and intermediate programmers Python through tutorials, recipes, articles, and problem-solving techniques while also disseminating information globally. Everyone in the globe will be able to learn how to code for free thanks to Python Code. Python is a general-purpose, high-level, interpreted programming language. Code readability is prioritised in its design philosophy, which makes heavy use of indentation. Python uses garbage collection and has dynamic typing. It supports a variety of programming paradigms, including procedural, object-oriented, and functional programming as well as structured programming (especially this). Due to its extensive standard library, it is frequently referred to as a "batteries included" language.',
            'We begin with the imports as usual. We must import tkinter since we utilise it to create the user interface. In order to subsequently modify the typefaces on our components, we additionally import the font module from tkinter. The partial function is obtained from functools and is a brilliant function that accepts another function as a first argument, along with certain args and kwargs, and returns a reference to this function with those arguments. When we wish to add one of our functions to a command argument of a button or key binding, this is extremely helpful.',
            'A computer programmer is a person who writes computer programmes, frequently for bigger pieces of software. They are also known as software developers, software engineers, programmers, or coders. A programmer is a person who uses a particular programming language to construct or write computer software or applications. The majority of programmers have substantial computer and coding expertise across a wide range of platforms and programming languages, including SQL, Perl, XML, PHP, HTML, C, C++, and Java. The terms "programmer" and "software engineer" may be used to describe the same position at various businesses because there is no industry-wide vocabulary standard. Usually, a "programmer" or "software developer" will concentrate on translating a precise specification into computer code.',
            'Understanding quantum physics requires a deep dive into the complexities of subatomic particles and their behavior. The enigmatic nature of quantum phenomena challenges our traditional understanding of reality and pushes the boundaries of scientific comprehension. Exploring this realm opens up a world of possibilities and prompts researchers to question fundamental principles, ultimately propelling us towards innovative breakthroughs and technologies.',
            'The art of brewing a perfect cup of coffee is a delicate dance between the right beans, water temperature, and brewing time. Achieving that ideal balance in flavors and aromas is a pursuit that both amateur baristas and seasoned coffee enthusiasts constantly strive for. From the origin of the coffee beans to the grind size and brewing method, every detail matters in this aromatic journey. And with each sip, one can savor the dedication and passion of coffee lovers around the world.',
            'In the quiet corners of a forgotten library, ancient tomes whisper the secrets of civilizations long past. Dusty pages, yellowed with age, hold tales of empires risen and fallen, of heroes and villains, and of wisdom handed down through generations. The fragrance of old books and the hushed ambiance transport readers to worlds beyond, where imagination takes flight and knowledge reigns supreme. These literary relics connect us to our history and remind us that every word written is a glimpse into the soul of humanity.',
        ]
        # Choosing one of the texts randomly with the choice function
        text = random.choice(random_selection).lower()

        split_point = 0

        self.name_label_left = tk.Label(self.root, text=text[0:split_point], fg='green')
        self.name_label_left.place(relx=0.5, rely=0.5, anchor=tk.E)

        self.name_label_right = tk.Label(self.root, text=text[split_point:])
        self.name_label_right.place(relx=0.5, rely=0.5, anchor=tk.W)

        self.current_alphabet_label = tk.Label(self.root, text=text[split_point], fg='grey')
        self.current_alphabet_label.place(relx=0.5, rely=0.6, anchor=tk.N)

        self.seconds_left = tk.Label(self.root, text=f'0 Seconds', fg='red')
        self.seconds_left.place(relx=0.5, rely=0.4, anchor=tk.S)

        self.write_able = True
        self.root.bind('<Key>', self.handle_key_press)

        self.seconds_passed = 0

        self.root.after(60000, self.stop_game)
        self.root.after(1000, self.time_addition)

    def stop_game(self):
        self.write_able = False

        # Calculating the amount of words
        amount_words = len(self.name_label_left.cget('text').split(' '))

        self.seconds_left.destroy()
        self.current_alphabet_label.destroy()
        self.name_label_right.destroy()
        self.name_label_left.destroy()

        self.label_of_result = tk.Label(self.root, text=f'Words per Minute (WPM): {amount_words}', fg='black')
        self.label_of_result.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Display a button to restart_game the game
        self.showcase_results = tk.Button(self.root, text=f'Retry', command=self.restart_game)
        self.showcase_results.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def restart_game(self):
        # Destroy result widgets
        self.label_of_result.destroy()
        self.showcase_results.destroy()
        self.handle_labels()

    def time_addition(self):
        self.seconds_passed += 1
        self.seconds_left.configure(text=f'{self.seconds_passed} Seconds')

        if self.write_able:
            self.root.after(1000, self.time_addition)

    def handle_key_press(self, event=None):
        try:
            if event.char.lower() == self.name_label_right.cget('text')[0].lower():
                self.name_label_right.configure(text=self.name_label_right.cget('text')[1:])
                self.name_label_left.configure(text=self.name_label_left.cget('text') + event.char.lower())
                self.current_alphabet_label.configure(text=self.name_label_right.cget('text')[0])
        except tk.TclError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
