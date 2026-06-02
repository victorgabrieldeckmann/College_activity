# Pokémon Battle Simulator

This project is being developed as a university assignment focused on Object-Oriented Programming concepts such as classes, inheritance, polymorphism, and class relationships.

The application uses external APIs to retrieve Pokémon and weather data and simulates turn-based Pokémon battles. The project is currently under development, and new features are being implemented continuously.

---

## Project Status

🚧 This project is currently under development. Features, architecture, and game mechanics may change as development progresses.


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
