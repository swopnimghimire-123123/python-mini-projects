import random
import time

TURN_COUNT = 10
POINTS_CORRECT = 10
POINTS_WRONG = -10
SCORE_MIN = 0
SCORE_MAX = 100
DELAY_SECONDS = 1


MOVIES = {
    "Titanic": "🚢 🧊 💔 🌊",
    "It": "🎈 🤡 😱 👦",
    "Pinocchio": "🤥 🪵 👃",
    "Annabelle": "🪆 👻 😱 🔒",
    "3 Idiots": "🎓 👨‍🎓 👨‍🎓 👨‍🎓 💡",
    "The Lion King": "🦁 👑 👶 ➡️ 🦁",
    "Boss Baby": "👶 💼 🍼 👔",
    "Shrek": "👹 🧅 🏰",
    "Robot": "🤖 ❤️ 💔 ⚡ 💌",
    "Taare Zameen Par": "🎨 🧒 ⭐ 👀",
    "Spider-Man": "🕷️ 🕸️ 🦸",
    "Iron Man": "🪨 🧔🏻",
    "Up": "🎈 🏠 👴 👦",
    "Ratatouille": "🐭 🍝 👨‍🍳",
    "Cars 2": "🚗 🚗 ",
    "Frozen": "❄️ 👭 👸🏻 🎶",
    "TMKOC": "☕ 🏘️ 😂 👨‍👩‍👧‍👦 ⎚-⎚ 🔁",
    "Jurassic Park": "🦖 🌴 🛝",
    "Jumanji": " 🪨 🎲 🌴 🦓 🐍",
    "Hotel Transylvania": "🏨 🧛‍♂️ 😂",
    "Zootopia": "🦊 🐰 🚓",
    "Harry Potter": "🧙‍♂️ ⚡ 🏰 📚",
    "Makkhi": "🪰 😡 🎯",
    "Sooryavansham": "👪 🍚 📺 👨🏼‍🦳 🩸 🤬",
    "Train to Busan": "🚆 🧟‍♂️ 😢",
    "Chhakka Panja": " 6️⃣ 😂 💍 👰 🤵",
    "Jhola": "🎒 🔥 🖤",
    "Unko Sweater": "🧶 🧥 💔 🥶",
    "Prem Geet": "🎵 ❤️ 🎬",
    "Jerry on Top": "🐭 🏆 ⛰️",
    "Breaking Bad": "🧪 💊 💰 😈",
    "Stranger Things": "🚲 🧇 👾 🔦 👨‍❤️‍💋‍👨",
    "Friends": "☕ 🛋️ 👭 👬",
    "Munna Bhai MBBS": "😎 💉 ❤️ ⛓️ 👩‍🦽",
    "Interstellar": "🚀 🌌 ⏳ 🌍 🕳️",
    "Dhamaal": "😂 🚗 💰",
    "Baahubali": "👑 💪 ⚔️",
    "The Dark Knight": "🦇 ♞ 🃏 🔥",
    "The Mask": "🟢 😷 🎭 😜",
    "Tangled": "👸 🪢 🌞 🏰",
    "Chandramukhi": "💃 👻 🎭",
    "Final Destination": "✈️ ⏳ ☠️ ",
    "The Princess Diaries": "👑 📓 👸 ✨",
    "Money Heist": "🎭 🏦 🕵🏻‍♀️ 💰",
    "Legally Blonde": "👱‍♀️ 💄 ⚖️",
    "Moon Knight": "🌙 🪞 🦸 🧠 ♞",
    "How to Lose a Guy in 10 Days": "📅 💔 🎯 😂 🔟"
}

def normalize_text(text):
    text = text.strip().lower()
    cleaned = []
    for ch in text:
        if ch.isalnum():
            cleaned.append(ch)
        else:
            cleaned.append(" ")
    return " ".join("".join(cleaned).split())


def letters_only(text):
    letters = []
    for ch in text.lower():
        if ch.isalpha():
            letters.append(ch)
    return "".join(letters)


def is_correct_guess(guess, answer):
    if not guess:
        return False

    g = normalize_text(guess)
    a = normalize_text(answer)

    if g == a:
        return True

    if g.replace(" ", "") == a.replace(" ", ""):
        return True

    return letters_only(g) == letters_only(a)


def clamp_score(score):
    return max(SCORE_MIN, min(SCORE_MAX, score))


def pick_movies(movie_titles, count):
    count = min(count, len(movie_titles))
    return random.sample(list(movie_titles), count)


def maybe_delay():
    if DELAY_SECONDS > 0:
        time.sleep(DELAY_SECONDS)


def show_welcome():
    print("🎉 Welcome to Emoji Dumb Charades! 🎉")
    print("Guess the movie from the emoji clues!")
    print(f"You have {TURN_COUNT} turns. Let's play!\n")
    maybe_delay()


def prompt_guess():
    return input("Your guess: ").strip()


def show_turn_result(turn_number, guess, answer, points, total_score):
    print("\n--- Scoreboard ---")
    print(f"Turn: {turn_number}")
    print(f"Your Guess: {guess.strip().title()}")
    print(f"Correct Answer: {answer}")
    print(f"Points Gained/Lost: {points}")
    print(f"Current Total Score: {total_score}")
    print("-" * 20)


def show_final_results(total_score, correct_guesses, incorrect_guesses):
    print("\n🎊 Game Over! 🎊")
    print(f"Final Score: {total_score}")
    print(f"Correct Guesses: {correct_guesses}")
    print(f"Incorrect Guesses: {incorrect_guesses}")

    if total_score >= 80:
        message = "You're the GOAT! 🐐"
    elif total_score >= 50:
        message = "Good job! Keep practicing! 👍"
    elif total_score >= 20:
        message = "Try again! You'll get better! 💪"
    else:
        message = "Tough round—try again! 🙂"

    print(message)


def prompt_replay():
    while True:
        choice = input("\nWant to play again? (y/n): ").strip().lower()
        if choice == "y":
            return True
        if choice == "n":
            return choice == "y"
        print("Please enter 'y' or 'n'.")


def play_turn(movie, turn_number, score):
    print(f"\nTurn {turn_number}:")
    print(f"Clues: {MOVIES[movie]}")
    maybe_delay()

    guess = prompt_guess()
    is_correct = is_correct_guess(guess, movie)
    points = POINTS_CORRECT if is_correct else POINTS_WRONG
    new_score = clamp_score(score + points)

    show_turn_result(turn_number, guess, movie, points, new_score)
    return new_score, is_correct


def play_game():
    while True:
        show_welcome()
        selected_movies = pick_movies(MOVIES.keys(), TURN_COUNT)
        score = 0
        correct_count = 0
        incorrect_count = 0

        for turn_number, movie in enumerate(selected_movies, start=1):
            score, is_correct = play_turn(movie, turn_number, score)
            if is_correct:
                correct_count += 1
            else:
                incorrect_count += 1

        show_final_results(score, correct_count, incorrect_count)

        if not prompt_replay():
            print("Thanks for playing! Goodbye! 👋")
            break


def main():
    play_game()


if __name__ == "__main__":
    main()