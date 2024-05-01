
# This program implements a circular linked list and tkinter to create a counting-out game.
# Author: Ishaan Reddy

import tkinter as tk
from tkinter import messagebox # For custom error messages
import math # For calculating positions of players

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Appends a new node with the given data to the end of the circular linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head

    # Removes the given node from the circular linked list
    def eliminate_player(self, k):
        if not self.head:
            return

        current = self.head
        while current.next != current:
            for _ in range(k - 1):
                previous_node = current
                current = current.next
            next_player = current.next
            yield current.data
            if current == self.head:
                self.head = next_player
            previous_node.next = next_player  # Remove current player from the list
            current = next_player

        yield current.data
        self.head = None  # Clear the head since there's only one player left

class GameGUI:
    def __init__(self):

        # Creating the main window
        self.window = tk.Tk()
        self.window.title('Counting-Out Game')
        self.window.geometry('800x750')
        self.window.configure(bg='gray10')

        # Creating the widgets
        self.label = tk.Label(self.window, text='Counting-Out Game', bg='gray10', fg='lightgray', font=('Arial', 24))
        self.label.pack(side = tk.TOP, pady = 50)

        self.label_n = tk.Label(self.window, text="Enter N value:", bg='gray10', fg='lightgray')
        self.label_n.pack(padx=10, pady=10)
        self.entry_n = tk.Entry(self.window, bg='gray20', fg='lightgray')
        self.entry_n.pack()

        self.label_k = tk.Label(self.window, text="Enter K value:", bg='gray10', fg='lightgray')
        self.label_k.pack(padx=10, pady=10)
        self.entry_k = tk.Entry(self.window, bg='gray20', fg='lightgray')
        self.entry_k.pack()

        self.start_button = tk.Button(self.window, text='Start Game', command=self.start_game)
        self.start_button.configure(bg='gray20', fg='lightgray', height=2, width=20)
        self.start_button.pack(pady=30)
        
        self.text = tk.Text(self.window, height=300, bg='gray20', fg='lightgray')

        self.eliminate_button = tk.Button(self.window, text='Eliminate', command=self.eliminate_player)

        # Dictionary to store player labels
        self.players = CircularLinkedList()
        self.player_icons = []
        self.elimination_generator = None

        self.window.mainloop()

    def display_text(self, text):
        self.text.insert(tk.END, text + "\n")
        self.text.see(tk.END)

    def clear_text(self):
        self.text.delete(1.0, tk.END)

    # Validates N and K input values
    def validate_input(self, n, k):
        if not (1 < n < 12):
            messagebox.showinfo("Invalid Input", "N should be between 1 and 11.")
            return False
        elif k < 1:
            messagebox.showinfo("Invalid Input", "K should be greater than or equal to 1.")
            return False
        else:
            return True

    # Starts the game with the given N and K values
    def start_game(self):
        self.n = int(self.entry_n.get())
        self.k = int(self.entry_k.get())
        if self.validate_input(self.n, self.k):
            self.clear_text()
            self.players = CircularLinkedList()
            for i in range(self.n):
                self.players.append("Player " + str(i))

        self.start_button.pack_forget()
        self.label.pack_forget()
        self.label_n.pack_forget()
        self.entry_n.pack_forget()
        self.label_k.pack_forget()
        self.entry_k.pack_forget()

        self.eliminate_button.pack(pady=300)
        self.eliminate_button.configure(bg='gray20', fg='lightgray', height=2, width=20)

        self.text.pack(side = tk.BOTTOM)

        self.text.delete('1.0', tk.END)
        self.text.insert(tk.END, f'The Game Started With N={self.n} Players K={self.k} Steps\n')

        positions = circle_positions(self.n, 200)
        for i, (x, y) in enumerate(positions):
            player_label = tk.Label(self.window, text=('[', str(i), ']'), bg='gray20', fg='lightgray')
            player_label.place(x=400 + x, y=300 + y)
            self.player_icons.append(player_label)

        self.elimination_generator = self.players.eliminate_player(self.k)

    # Eliminates a player from the game
    def eliminate_player(self):
        if self.players.head is None:
            messagebox.showinfo("Game Over", "No players to eliminate.")
            return
        if self.players.head.next == self.players.head:
            winner = self.players.head.data
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
            
            # Reset the widgets
            self.clear_text()
            # self.window.delete("all")

            self.eliminate_button.pack_forget()
            self.text.pack_forget()

            # Forget the player icons
            for player_icon in self.player_icons:
                player_icon.place_forget()  

            self.label.pack(side = tk.TOP, pady = 50)
            self.label_n.pack( pady = 10)
            self.entry_n.pack( pady = 10)
            self.label_k.pack( pady = 10)
            self.entry_k.pack( pady = 10)
            self.start_button.pack( pady = 30)

            self.players = CircularLinkedList()
            self.player_icons = []
            
            self.elimination_generator = None  # Reset the generator for the next game
            return

        if self.elimination_generator is None:
            return  # No active game

        try:
            eliminated_player = next(self.elimination_generator)
            self.display_text("Eliminated player: " + str(eliminated_player))
            
            # Find the player icon to remove
            x = eliminated_player.split(" ")[1]
            player_icon = self.player_icons[int(x)]
            player_icon.place_forget()

            
        except StopIteration:
            pass

# Displays linked list of players in a circle
def circle_positions(n, radius):
    positions = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        positions.append((x, y))
    return positions

if __name__ == '__main__':
    GameGUI()