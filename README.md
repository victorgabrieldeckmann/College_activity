# PokeWeather Fight

This project is being developed as a university assignment focused on Object-Oriented Programming concepts such as classes, inheritance, polymorphism, and class relationships.

The application uses external APIs to retrieve Pokémon and weather data and simulates turn-based Pokémon battles. The project is currently under development, and new features are being implemented continuously.

---

## Project Status

✅ First playable version completed.

Implemented features:

- Turn-based battle system
- Move inheritance (DamageMove and StatusMove)
- Type effectiveness system
- Weather battle modifiers
- Stat buffs and debuffs
- Healing system
- Player vs CPU battles
- Input validation for Pokémon, city, and moves

🚧 Planned features:

- Improved CPU decision-making
- Web interface integration
- Multiple Pokémon teams
- Additional battle mechanics

## Battle System

The current version of the project includes a fully functional turn-based battle system.

### Battle Flow

1. The player chooses two Pokémon using data retrieved from the PokéAPI.
2. A city is selected, and the current weather is obtained through the WeatherAPI.
3. The Pokémon with the highest Speed stat attacks first.
4. Players take turns selecting actions until one Pokémon faints.
5. The winner is declared when the opponent's HP reaches zero.

### Available Actions

Each Pokémon can:

* Use one of its available moves
* Use a healing potion

Healing potions restore health points but cannot be used when the Pokémon is already at full health.

### Move System

Moves are divided into two categories:

#### Damage Moves

Damage moves calculate the amount of damage dealt based on:

* Move power
* Attacker Attack stat
* Defender Defense stat
* Type effectiveness
* Weather modifiers

#### Status Moves

Status moves can modify battle statistics such as:

* Attack
* Defense
* Speed

Buffs and debuffs are applied according to the move target:

* `user`: affects the Pokémon that used the move
* `opponent`: affects the enemy Pokémon

### Type Effectiveness

The simulator uses Pokémon type relations obtained from the PokéAPI.

Examples:

* Fire is super effective against Grass
* Water is super effective against Fire
* Electric is super effective against Water

Effectiveness multipliers:

* 2.0× → Super effective
* 0.5× → Not very effective
* 0× → No effect
* 1.0× → Normal damage

### Weather Effects

The current weather affects move effectiveness during battle.

Examples:

| Weather | Buffed Types | Weakened Types |
| ------- | ------------ | -------------- |
| Sun     | Fire         | Water          |
| Rain    | Water        | Fire           |
| Storm   | Electric     | Flying         |
| Snow    | Ice          | Grass          |
| Fog     | Ghost, Dark  | Normal         |
| Cloud   | Flying       | Fire           |

Weather modifiers:

* Buffed types: 1.2× damage
* Weakened types: 0.8× damage

### CPU Opponent

The project currently includes a CPU-controlled trainer.

The CPU selects actions automatically by choosing randomly between:

* Available moves
* Healing (when potions are available)

More advanced battle AI is planned for future versions.


## Requirements

Install the project dependencies using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
Flask
requests
python-dotenv
```

---

## Project Setup

### Linux / Ubuntu

#### Navigate to the project folder

```bash
cd YOUR_REPOSITORY
```

#### Install Python virtual environment support

```bash
sudo apt update
sudo apt install python3.14-venv -y
```

#### Create a virtual environment

```bash
python3 -m venv venv
```

#### Activate the virtual environment

```bash
source venv/bin/activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Run the application

```bash
python app.py
```

---

### Windows (PowerShell)

#### Navigate to the project folder

```powershell
cd PROJECT_PATH
```

#### Create a virtual environment

```powershell
python -m venv venv
```

#### Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

> If you receive a permission error when running scripts:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

#### Install dependencies

```powershell
pip install -r requirements.txt
```

#### Run the application

```powershell
python app.py
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
WEATHER_API_KEY=your_weather_api_key
```

---

## Verify that the Virtual Environment is Active

If everything is configured correctly, your terminal should display something similar to:

```text
(venv) PS C:\project>
```

or

```text
(venv) user@ubuntu:~/project$
```
