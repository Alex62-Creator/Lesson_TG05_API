from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Клавиатура для выбора конференции
async def conf_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="East", callback_data='east'))
    keyboard.add(InlineKeyboardButton(text="West", callback_data='west'))
    return keyboard.as_markup()

# Добавляем ID для каждой команды
TEAM_IDS = {
    # Восточная конференция (East)
    "Atlanta Hawks": 1,
    "Boston Celtics": 2,
    "Brooklyn Nets": 4,
    "Charlotte Hornets": 5,
    "Chicago Bulls": 6,
    "Cleveland Cavaliers": 7,
    "Detroit Pistons": 10,
    "Indiana Pacers": 15,
    "Miami Heat": 20,
    "Milwaukee Bucks": 21,
    "New York Knicks": 24,
    "Orlando Magic": 26,
    "Philadelphia 76ers": 27,
    "Toronto Raptors": 38,
    "Washington Wizards": 41,
    # Западная конференция (West)
    "Dallas Mavericks": 8,
    "Denver Nuggets": 9,
    "Golden State Warriors": 11,
    "Houston Rockets": 14,
    "LA Clippers": 16,
    "Los Angeles Lakers": 17,
    "Memphis Grizzlies": 19,
    "Minnesota Timberwolves": 22,
    "New Orleans Pelicans": 23,
    "Oklahoma City Thunder": 25,
    "Phoenix Suns": 28,
    "Portland Trail Blazers": 29,
    "Sacramento Kings": 30,
    "San Antonio Spurs": 31,
    "Utah Jazz": 40,
}
# Клавиатура для команд восточной конференции
async def east_keyboard():
    east = [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets",
        "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
        "Detroit Pistons", "Indiana Pacers", "Miami Heat",
        "Milwaukee Bucks", "New York Knicks", "Orlando Magic",
        "Philadelphia 76ers", "Toronto Raptors", "Washington Wizards"
    ]
    keyboard = InlineKeyboardBuilder()
    for team in east:
        team_id = TEAM_IDS[team]  # Получаем ID команды
        keyboard.add(InlineKeyboardButton(text=team, callback_data=f"team_{team_id}"))  # Формат: team_1, team_2...
    return keyboard.adjust(3).as_markup()

# Клавиатура для команд западной конференции
async def west_keyboard():
    west = [
        "Dallas Mavericks", "Denver Nuggets", "Golden State Warriors",
        "Houston Rockets", "LA Clippers", "Los Angeles Lakers",
        "Memphis Grizzlies", "Minnesota Timberwolves", "New Orleans Pelicans",
        "Oklahoma City Thunder", "Phoenix Suns", "Portland Trail Blazers",
        "Sacramento Kings", "San Antonio Spurs", "Utah Jazz"
    ]
    keyboard = InlineKeyboardBuilder()
    for team in west:
        team_id = TEAM_IDS[team]
        keyboard.add(InlineKeyboardButton(text=team, callback_data=f"team_{team_id}"))
    return keyboard.adjust(3).as_markup()