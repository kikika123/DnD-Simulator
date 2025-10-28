-- ===== CORE CHARACTERS =====
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    level INTEGER DEFAULT 1,
    race TEXT,
    char_class TEXT,
    str INTEGER, dex INTEGER, con INTEGER,
    int INTEGER, wis INTEGER, cha INTEGER,
    hp INTEGER, max_hp INTEGER,
    mana INTEGER DEFAULT 0,
    ac INTEGER DEFAULT 10,
    exp INTEGER DEFAULT 0,
    gold INTEGER DEFAULT 0,
    spell_slots TEXT  -- JSON {"1":2,"2":0}
);

CREATE TABLE IF NOT EXISTS enemies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hp INTEGER, max_hp INTEGER,
    atk_min INTEGER, atk_max INTEGER,
    exp_value INTEGER DEFAULT 0
);

-- ===== INVENTORY =====
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    effect TEXT,
    quantity INTEGER DEFAULT 1,
    owner_id INTEGER REFERENCES players(id)
);

-- ===== WEAPONS =====
CREATE TABLE IF NOT EXISTS weapons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dmg_dice TEXT,
    dmg_bonus INTEGER DEFAULT 0,
    type TEXT
);

CREATE TABLE IF NOT EXISTS player_weapons (
    player_id INTEGER REFERENCES players(id),
    weapon_id INTEGER REFERENCES weapons(id)
);

-- ===== SPELLS =====
CREATE TABLE IF NOT EXISTS spells (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    level INTEGER,
    dmg_dice TEXT,
    cost INTEGER,
    description TEXT
);

CREATE TABLE IF NOT EXISTS player_spells (
    player_id INTEGER REFERENCES players(id),
    spell_id INTEGER REFERENCES spells(id)
);

-- ===== BATTLES LOG =====
CREATE TABLE IF NOT EXISTS battles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER REFERENCES players(id),
    enemy_id INTEGER REFERENCES enemies(id),
    outcome TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
