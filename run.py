from kahoot_bot import KahootBot


def run():
    bot = KahootBot(debug=True)
    # username, game_pin, game_id = bot.get_game_data()
    username, game_pin, game_id = "My Bot", "1690542", "66b9ce8a-fbbd-43b3-81e2-a5265af2a1db"
    bot.play_game(username, game_pin, game_id)


if __name__ == "__main__":
    run()
